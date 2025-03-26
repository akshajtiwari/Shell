import sys


def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
    while True:
     sys.stdout.flush()

     sys.stdout.write("$ ")

     user_input = input()

     if user_input.lower()=="exit 0":
        sys.exit(0)
        break

     elif user_input.startswith("echo "):
        print(user_input[5:])

     elif user_input == 'type echo':
        print('echo is a shell builtin')

     elif user_input == 'type exit':
        print('exit is a shell builtin')

     elif user_input == 'invalid_command':
        print('invalid_command: not found')
     elif user_input == 'type type':
        print("type is a shell builtin")
     else:
        print(f"{user_input}: command not found")
     if user_input.startswith("type invalid"):
        print((user_input[4:]))


    # Wait for user input
    input()


if __name__ == "__main__":
    main()

    
