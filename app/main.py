import sys


def main():
     #Uncomment this block to pass the first stage
     #sys.stdout.write("$ ")
    while True:
     sys.stdout.write("$ ")
     sys.stdout.flush
     user_input = input()
     if user_input.lower()=="exit":
        break
     print(f"{user_input}: command not found")
    # Wait for user input
    input()


if __name__ == "__main__":
    main()

    
