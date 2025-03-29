import sys
import os
import subprocess

def find_executable(command):
    """Find if the command exists in PATH and return full path."""
    for path in os.getenv("PATH", "").split(":"):
        full_path = os.path.join(path, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path  # ✅ Return full path
    return None

def run_executable(user_input):
    """Run the command if it exists in PATH."""
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]

    executable_path = find_executable(command)

    if executable_path:
        try:
            # ✅ Run using full path to avoid issues
            result = subprocess.run([executable_path] + args, capture_output=True, text=True)
            print(result.stdout, end="")  # Print output exactly as expected
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"{command}: command not found")

def main():
    """Simple shell loop."""
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input().strip()

        if user_input == "exit 0":
            sys.exit(0)
        elif user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input.startswith("type "):
            command = user_input[5:]
            if command in {"echo", "exit", "type"}:
                print(f"{command} is a shell builtin")
            else:
                path = find_executable(command)
                if path:
                    print(f"{command} is {path}")  # ✅ Print full path
                else:
                    print(f"{command}: command not found")
        else:
            run_executable(user_input)

if __name__ == "__main__":
    main()
