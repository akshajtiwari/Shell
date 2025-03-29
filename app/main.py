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
    """Autocomplete built-in commands."""
    matches = [cmd for cmd in BUILTIN_COMMANDS if cmd.startswith(text)]
    return matches[state] + " " if state < len(matches) else None

def main():
    """Main shell loop."""
    readline.set_completer(complete_builtin)
    readline.parse_and_bind("tab: complete")

    while True:
        try:
            command = input("$ ").strip()  # Prompt for input
            if command == "exit":
                break
            elif command.startswith("echo "):
                print(command[5:])  # Mimic echo behavior
            elif command.startswith("pwd"):
                print(os.getcwd())
            elif command.startswith("cd ~"):
                os.chdir(os.getenv("HOME"))
            elif command.startswith("cd "):
                path = command[3:]
                try:
                    os.chdir(path)  # Changes directory
                except FileNotFoundError:
                    print(f"cd: {path}: No such file or directory")
            elif command.startswith("type "):
                cmd = command[5:]
                if cmd in BUILTIN_COMMANDS or cmd in ["type", "pwd"]:
                    print(f"{cmd} is a shell builtin")
                else:
                    path = find_executable(cmd)
                    if path:
                        print(f"{cmd} is {path}")  # ✅ Print full path
                    else:
                        print(f"{cmd}: not found")
            else:
                run_executable(command)

        except EOFError:
            break

if __name__ == "__main__":
    main()
