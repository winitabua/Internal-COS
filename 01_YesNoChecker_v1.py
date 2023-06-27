
# yes no checker function
def yes_no_checker():
    answer = input("Please enter 'yes' or 'no': ")
    if answer.lower() == "yes":
        print("You entered 'yes'.")
    elif answer.lower() == "no":
        print("You entered 'no'.")
    else:
        print("Invalid input. Please try again.")
        yes_no_checker()




