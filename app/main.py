import sys


def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
    while True:
     sys.stdout.write("$ ")
     sys.stdout.flush
     user_input = input()
     if user_input.lower()=="exit ":
        sys.exit(0)
        break
     elif user_input.startswith("echo "):
        print(user_input[5:])
     else:
        print(f"{user_input}: command not found")
    # Wait for user input
    input()


if __name__ == "__main__":
    main()

    
