import sys
import os
import subprocess

def find_executable(command):
    """Search for an executable in directories listed in PATH."""
    path_dirs = os.getenv("PATH", "").split(":")  # Get directories from PATH

    for path in path_dirs:
        full_path = os.path.join(path, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):  # Check if executable
            return full_path  # Return the full path if found

    return None  # Return None if not found

def run_executable(user_input):
    """Execute an external command if found in PATH."""
    parts = user_input.split()  # Split input into command and arguments
    command = parts[0]  # Extract command
    args = parts[1:]  # Extract arguments

    executable_path = find_executable(command)  # Find the full path

    if executable_path:
        try:
            result = subprocess.run([executable_path] + args, capture_output=True, text=True)
            print(result.stdout, end="")  # Print the output of the command
        except Exception as e:
            print(f"Error: {e}")  # Print error if execution fails
    else:
        print(f"{command}: command not found")  # Command not found

def main():
    while True:
        sys.stdout.flush()
        sys.stdout.write("$ ")  # Display shell prompt
        sys.stdout.flush()
        user_input = input().strip()  # Read input and remove extra spaces

        if user_input.lower() == "exit 0":
            sys.exit(0)

        elif user_input.startswith("echo "):
            print(user_input[5:])

        elif user_input.startswith("type "):  
            command = user_input[5:]  
            builtins = {"echo", "exit", "type"}
            if command in builtins:
                print(f"{command} is a shell builtin")
            else:
                path = find_executable(command)
                if path:
                    print(f"{command} is {path}")
                else:
                    print(f"{command}: command not found")

        else:
            run_executable(user_input)  # Run external command

if __name__ == "__main__":
    main()
