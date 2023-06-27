
# yes no checker function
def yes_no_checker(question):
    answer = input("Please enter 'yes' or 'no': ")
    if answer.lower() == "yes":
        answer = "continue program"
        return answer
    
    elif answer.lower() == "no":
        answer = "show instruction"
        return answer
    
    else:
        print("Invalid input. Please answer yes or no.")

