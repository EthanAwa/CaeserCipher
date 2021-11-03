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


message = string_input("What is your message: ")
print(split_message(message))

