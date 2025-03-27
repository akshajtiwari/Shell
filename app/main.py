import sys
import os

def find_executable(command):
    """Search for an executable in directories listed in PATH."""
    path_dirs = os.environ.get("PATH", "").split(":")  # Get directories from PATH
    
    for directory in path_dirs:
        full_path = os.path.join(directory, command)  # Construct full path
        
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):  # Check if it's executable
            return full_path  # Return first match found

    return None  # Return None if no match is found



def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
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
            if path:
                print(f"{command} is {path}")
            else:
                print(f"{command}: not found")

        else:
            print(f"{user_input}: command not found")


    # Wait for user input
    input()

if __name__ == "__main__":
    main()
