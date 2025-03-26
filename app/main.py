import sys


def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
    sys.stdout.write("$ ")
    user_input = input()
    while True:
        print(f"{user_input}: command not found")
        continue
    # Wait for user input
    input()


if __name__ == "__main__":
    main()

    
