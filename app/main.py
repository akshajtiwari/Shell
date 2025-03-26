import sys


def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
    sys.stdout.write("$ ")

    # Wait for user input
    input()


if __name__ == "__main__":
    main()

    command=input()
    print(f"{command}:command not found")
