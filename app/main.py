import sys
import os
import subprocess
import shlex

def run_executable(user_input):
    """Run a command, supporting output redirection (> and 1>)."""

    if " > " in user_input or " 1> " in user_input:
        parts = shlex.split(user_input)  # ✅ Properly split input while handling quotes

        # ✅ Find redirection operator (`>` or `1>`)
        for i, part in enumerate(parts):
            if part in [">", "1>"]:
                redirect_index = i
                break
        else:
            redirect_index = -1  # No redirection found (shouldn't happen)

        if redirect_index == -1 or redirect_index + 1 >= len(parts):
            print("Syntax error: No output file specified")
            return

        # ✅ Extract command and output file
        command_parts = parts[:redirect_index]  # Everything before `>` is the command
        output_file = parts[redirect_index + 1]  # The file after `>` is the output file

        # ✅ Run command and redirect both `stdout` and `stderr`
        with open(output_file, "w") as f:
            process = subprocess.run(command_parts, stdout=f, stderr=subprocess.PIPE, text=True)

        # ✅ Print stderr immediately if there's an error
        if process.stderr:
            sys.stdout.write(process.stderr)  # ✅ Show error message

        return  # ✅ Prevent extra output

    else:
        # Normal execution (no redirection)
        parts = shlex.split(user_input)
        result = subprocess.run(parts, capture_output=True, text=True)

        # ✅ Print both `stdout` and `stderr`
        if result.stdout:
            sys.stdout.write(result.stdout)
        if result.stderr:
            sys.stdout.write(result.stderr)

def main():
    while True:
        sys.stdout.write("$ ")  # Show shell prompt
        sys.stdout.flush()
        user_input = input().strip()

        if user_input == "exit 0":
            sys.exit(0)
        elif user_input.startswith("pwd"):
            print(os.getcwd())
        elif user_input.startswith("cd "):
            path = user_input[3:].strip()
            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd: {path}: No such file or directory")
        else:
            run_executable(user_input)  # Run command

if __name__ == "__main__":
    main()
