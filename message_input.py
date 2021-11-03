# Make sure that input has no numbers
def string_input(question):
    valid = False

    while not valid:
        answer = input(question)

        # If the input contains a number, print error
        if not answer.isalpha():
            print("Please enter letters only, numbers are not allowed.")
            valid = False

        # If the input has no numbers, return input
        if answer.isalpha():
            valid = True

    return answer


message = string_input("What is your message: ")
print(message)
