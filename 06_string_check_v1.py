# string checking functions, takes in
# question and list valid responses
def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # check if response is the first letter of
                # an item in the list
                if response == item[0]:
                    # note: return the entire response
                    # rather than just the first letter
                    return item

        print("Sorry that is not a valid response")

# *** Main routine starts here ***
for item in range(0,6):
    want_snacks = string_checker("Do you want "
                                 "snacks? ", ["yes","no"])
    print("Answer OK, you said:", want_snacks)
    print()