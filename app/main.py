import sys
import os
import subprocess
import shlex

def find_executable(command):
    """Find if the command exists in PATH and return full path."""
    for path in os.getenv("PATH", "").split(":"):
        full_path = os.path.join(path, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path  
    return None

def run_executable(user_input):
    """Run the command if it exists in PATH, supporting output redirection."""
    
    # Step 1: Handle output redirection (`> file`)
    if " > " in user_input or " 1> " in user_input:
        parts = shlex.split(user_input)
        
        # Find the redirection symbol `>` or `1>`
        try:
            redirect_index = parts.index(">")
        except ValueError:
            redirect_index = parts.index("1>")  # Handle explicit `1>` case
        
        command_parts = parts[:redirect_index]  # Everything before `>` is the command
        output_file = parts[redirect_index + 1]  # File after `>` is where output goes

        if not command_parts:
            print("Error: No command before redirection")
            return

        command = command_parts[0]  # First part is the actual command
        args = command_parts[1:]  # Rest are command arguments
        
        executable_path = find_executable(command)

        if executable_path:
            try:
                # Open file in write mode and run command
                with open(output_file, "w") as f:
                    result = subprocess.run([command] + args, stdout=f, stderr=subprocess.PIPE, text=True)

                # Print errors to stderr normally (they should still appear on screen)
                if result.stderr:
                    print(result.stderr, end="")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"{command}: command not found")

    else:
        # Step 2: Normal command execution (without redirection)
        parts = shlex.split(user_input)
        if not parts:
            return  # If input is empty, do nothing

        command = parts[0]
        args = parts[1:]

        executable_path = find_executable(command)

        if executable_path:
            try:
                result = subprocess.run([command] + args, capture_output=True, text=True)
                print(result.stdout, end="")  # Print normal output
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"{command}: command not found")


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input().strip()

        if user_input == "exit 0":
            sys.exit(0)

        elif user_input.startswith("echo "):
            args = shlex.split(user_input[5:])
            print(" ".join(args))

        elif user_input == "pwd":
            print(os.getcwd())  

        elif user_input.startswith("cd ~"):
            path = os.getenv("HOME")
            os.chdir(path)

        elif user_input.startswith("cd "):
            path = user_input[3:]
            try:
                os.chdir(path)  # Changes the directory (handles all types of operations like ., ./, etc.)
            except FileNotFoundError:
                print(f"cd: {path}: No such file or directory") 

        elif user_input.startswith("type "):
            command = user_input[5:]
            if command in {"echo", "exit", "type", "pwd"}:
                print(f"{command} is a shell builtin")
            else:
                path = find_executable(command)
                if path:
                    print(f"{command} is {path}")  # ✅ Print full path
                else:
                    print(f"{command}: not found")

        else:
            run_executable(user_input)

if __name__ == "__main__":
    main()
