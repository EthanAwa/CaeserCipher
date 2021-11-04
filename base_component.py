# Imports

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


# Split message into individual characters, then return as a list
def split_message(word):

    return list(word)


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


