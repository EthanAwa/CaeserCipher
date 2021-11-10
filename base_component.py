# Functions

# Make sure that input has no numbers
def string_input(question):
    valid = False

    while not valid:
        answer = input(question).lower()

        # If the input contains a number, print error
        if not answer.isalpha():
            print("Please enter letters only, numbers are not allowed.")
            valid = False

        # If the input has no numbers, return input
        if answer.isalpha():
            valid = True

    return answer


# Make sure that input is integer only
def int_check(question):
    error = "Please enter a whole number that is more than 0 (1, 2, 3...)\n"

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print("Please enter a whole number only, not a decimal (e.g 3.0) "
                  "or a word (e.g Three)\n")


# Encryption function
def encrypt(text, s):
    result = ""

    # Loop through text
    for i in range(len(text)):
        char = text[i]

        result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# Decryption function
def decrypt(text, s):
    result = ""
    v = 26 - s

    # Loop through text
    for i in range(len(text)):
        char = text[i]

        result += chr((ord(char) + v - 97) % 26 + 97)

    return result


# Main Loop
loop = False
while not loop:

    # Ask user for message
    message = string_input("What is your message (type \"quit\" if you want to stop using the cipher: ")

    # Check for exit code
    if message == "quit":
        loop = True
        print("Thanks for using the cipher")
        break

    # Ask user for key/shift value
    keycheck = False
    while not keycheck:
        key = int_check("What is your encryption/decryption key (1 - 25 only): ")

        # Check if its between 1 - 25
        if key < 0 or key > 25:
            print("Please enter a whole number between 1 - 25")
        else:
            keycheck = True

    # Ask the user if they want to encrypt/decrypt their message
    edcheck = False
    while not edcheck:
        choice = string_input("Do you want to encrypt or decrypt? ")

        if choice == "encrypt":
            final = encrypt(message, key)
            edcheck = True

        elif choice == "decrypt":
            final = decrypt(message, key)
            edcheck = True

        else:
            print("Please enter only \"encrypt\" or \"decrypt\"")

    # Print original message, key, and new message
    print(f"Original message: {message}")
    print(f"Shift value: {key}")
    print(f"New message: {final}")
    print()
