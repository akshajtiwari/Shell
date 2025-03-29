import sys
import os
import subprocess
import shlex

def run_executable(user_input):
    """Run a command with support for output redirection (> and 1>)."""

    # ✅ Detect if the command contains redirection (`>`, `1>`)
    if " > " in user_input or " 1> " in user_input:
        parts = shlex.split(user_input)  # ✅ Split properly, preserving quotes

        # ✅ Find redirection operator (`>` or `1>`)
        try:
            redirect_index = parts.index(">")
        except ValueError:
            redirect_index = parts.index("1>")  # If `1>` is used instead
        
        # ✅ Extract command and output file
        command_parts = parts[:redirect_index]  # Everything before `>` is the command
        output_file = parts[redirect_index + 1]  # The file after `>` is the output file

        # ✅ Handle `echo` separately
        if command_parts[0] == "echo":
            output_text = " ".join(command_parts[1:])  # Extract message
            with open(output_file, "w") as f:
                f.write(output_text + "\n")  # ✅ Write to file
        else:
            # ✅ Run external commands and redirect output
            with open(output_file, "w") as f:
                subprocess.run(command_parts, stdout=f, stderr=subprocess.PIPE, text=True)
        return  # ✅ Prevent extra output

    else:
        # Normal execution (no redirection)
        parts = shlex.split(user_input)
        result = subprocess.run(parts, capture_output=True, text=True)
        print(result.stdout, end="")

def main():
    while True:
        sys.stdout.write("$ ")  # Show shell prompt
        sys.stdout.flush()
        user_input = input().strip()

        if user_input == "exit 0":
            sys.exit(0)
        elif user_input.startswith("echo "):
            args = shlex.split(user_input[5:])
            print(" ".join(args))
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
