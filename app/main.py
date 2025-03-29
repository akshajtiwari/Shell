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
def run_executable(user_input):
    path_dirs = os.getenv("PATH", "").split(":")  
    parts = user_input.split()  # Split input into command and arguments
    command = parts[0]  # Extract command
    args = parts[1:]  # Extract arguments

    for path in path_dirs:
        full_path = os.path.join(path, command)  # Construct full path
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):  # Check if executable
    
            result = subprocess.run( args)  # Run executable
            return result

    print(f"DEBUG: {command} not found in PATH directories")  # Debugging info
    return None  # If executable not found





def main():
    while True:
        sys.stdout.flush()
        sys.stdout.write("$ ")  # Display shell prompt
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
                continue  
            
            path = find_executable(command)
            if not path:
                print(f"{command}: command not found")

        else:
            result = run_executable(user_input)  # Try executing it
            if result is None:
                print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
