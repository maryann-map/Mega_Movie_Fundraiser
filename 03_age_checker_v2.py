# function goes here


# Checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number between 12 and 130"

    valid = False
    while not valid:

        # ask user for number and check if it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        #if an integer is not entered, display error message
        except ValueError:
            print(error)

# main routine goes here
age = int_check("Age: ")