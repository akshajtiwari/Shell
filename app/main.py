import sys
import os
import subprocess
import shlex
import readline

def find_executable(command):
    """Find if the command exists in PATH and return full path."""
    for path in os.getenv("PATH", "").split(":"):
        full_path = os.path.join(path, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path  
    return None

def run_executable(user_input):
    """Run the command if it exists in PATH."""
    parts = shlex.split(user_input)  # Correctly split input while handling quotes
    if not parts:
        return  # If the command is empty, do nothing

    command = parts[0]
    args = parts[1:]

    executable_path = find_executable(command)

    if executable_path:
        try:
            result = subprocess.run([command] + args, capture_output=True, text=True)
            print(result.stdout, end="")  # Print output exactly as expected
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"{command}: command not found")

BUILTIN_COMMANDS = ["echo", "exit"]
def complete_builtin(text, state):
    matches = [cmd for cmd in BUILTIN_COMMANDS if cmd.startswith(text)]
    return matches[state] + " " if state < len(matches) else None

readline.set_completer(complete_builtin)
readline.parse_and_bind("tab: complete")

while True:
    try:
        command = input("$ ")  # Prompt for input
        if command.strip() == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])  # Mimic echo behavior
        else:
            print(f"Command not found: {command}")
    except EOFError:
        break


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
