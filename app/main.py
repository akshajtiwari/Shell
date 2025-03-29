import sys
import os
import subprocess

def find_executable(command):
    """Find if the command exists in PATH and return full path."""
    for path in os.getenv("PATH", "").split(":"):
        full_path = os.path.join(path, command)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path  
    return None

def run_executable(user_input):
    """Run the command if it exists in PATH."""
    parts = user_input.split()
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

def main():
   
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input().strip()

        if user_input == "exit 0":
            sys.exit(0)
        elif user_input.startswith("echo "):
            print(user_input[5:]) 
        elif user_input == "pwd":
            print(os.getcwd())  
        elif user_input.startswith("cd ~"):
            path = os.getenv("HOME")
            os.chdir(path)
        elif user_input.startswith("cd "):
         path = user_input[3:]
         try:
            os.chdir(path)  # changes the directory (handles all types of operations like . , ./ etc)
         except FileNotFoundError:
            print(f"cd: {path}: No such file or directory") 

        elif user_input.startswith("type "):
            command = user_input[5:]
            if command in {"echo", "exit", "type" , "pwd"}:
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
