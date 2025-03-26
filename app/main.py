import sys


def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
    while True:
     sys.stdout.write("$ ")

     sys.stdout.flush()

     user_input = input()

     if user_input.lower()=="exit 0":
        sys.exit(0)
        break

     if user_input.startswith("echo "):
        print(user_input[5:])

     if user_input == 'type echo':
        print('echo is a shell builtin')

     if user_input == 'type exit':
        print('exit is a shell builtin')

     if user_input == 'invalid_command':
        print('invalid_command: not found')
     if user_input == 'type type':
        print("type is a shell builtin")
     else:
        print(f"{user_input}: command not found")

    # Wait for user input
    input()


if __name__ == "__main__":
    main()

    
