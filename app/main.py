import sys
import os
import subprocess

def find_executable(command):
    """Search for an executable in directories listed in PATH."""
    path_dirs = os.getenv("PATH", "").split(":")  # Get directories from PATH
    found = False  # Track if the command is found

    for path in path_dirs:
        if os.path.isdir(path):  # Ensure it's a valid directory
            for f in os.listdir(path):  # Iterate over files in the directory
                if f == command:  # Check if the file matches the command
                    print(f"{command} is {path}/{command}")  # Print full path
                    return path + "/" + command  # Return the full path

    return None  # Return None if not found
def run_executable(prompt):
    path_dirs = os.getenv("PATH", "").split(":")  
    for path in path_dirs:
        if os.path.isdir(path):
          for f in os.listdir(path):
            if f==prompt:
                result= subprocess.run(f)
                return result
    return None


def main():
    while True:
        sys.stdout.flush()
        sys.stdout.write("$ ")  # Display shell prompt
        user_input = input().strip()  # Read input and remove extra spaces

        if user_input.lower() == "exit 0":
            sys.exit(0)

        elif user_input.startswith("echo "):
            print(user_input[5:])

        elif user_input.startswith("type "):  # Handling the `type` command
            command = user_input[5:]  # Extract the command name

            # Check if it's a shell builtin
            builtins = {"echo", "exit", "type"}
            if command in builtins:
                print(f"{command} is a shell builtin")
                continue  # Skip further checks

            # Check if it's an executable in PATH
            path = find_executable(command)
            if not path:
                print(f"{command}: command not found")

        else:
            print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
