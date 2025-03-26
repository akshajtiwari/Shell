import sys


def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
    while True:
     sys.stdout.write("$ ")
     sys.stdout.flush
     user_input = input()
     if user_input.lower()=="exit 0":
        sys.exit(0)
        break
     elif user_input.startswith("echo "):
        print(user_input[5:])
     else:
        print(f"{user_input}: command not found")
     if user_input == 'type echo':
        print('echo is a shell bulletin')
     if user_input == 'exit':
        print('exit is a shell bulletin')
     if user_input == 'invalid_command':
        print('invalid_command: not found')
    # Wait for user input
    input()


if __name__ == "__main__":
    main()

    
