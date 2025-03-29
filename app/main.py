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
    """Run a command, supporting output redirection (> and 1>)."""

    # ✅ Step 1: Detect redirection (`>` or `1>`)
    if " > " in user_input or " 1> " in user_input:
        parts = shlex.split(user_input)  # ✅ Step 2: Split properly

        try:
            redirect_index = parts.index(">")  # Find the position of `>`
        except ValueError:
            redirect_index = parts.index("1>")  # If `1>` is used instead
        
        # ✅ Step 3: Separate the command and output file
        command_parts = parts[:redirect_index]  # Everything before `>` is the command
        output_file = parts[redirect_index + 1]  # The file after `>` is the output file

        # ✅ Step 4: Handle `echo` manually
        if command_parts[0] == "echo":
            echo_output = " ".join(command_parts[1:])  # Get the echo message
            with open(output_file, "w") as f:
                f.write(echo_output + "\n")  # ✅ Write to file instead of printing
        else:
            # ✅ Step 5: Run external commands and redirect output
            with open(output_file, "w") as f:
                subprocess.run(command_parts, stdout=f, stderr=subprocess.PIPE, text=True)
        return  # ✅ Avoid printing anything extra

    else:
        # Normal execution without redirection
        parts = shlex.split(user_input)
        subprocess.run(parts, text=True)

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
