
# type of calculation in a function
def get_calculation_selection():
    print("What would you like to calculate; 'area' or 'perimeter' or 'both'.")

    answer = input("Plaease enter the available options : ")
    if answer.lower() == "area":
        print("You chose to calculate Area.")
    elif answer.lower() == "perimeter":
        print("You chose to calculate Perimeter.")
    elif answer.lower() == "both":
        print("You chose to calculate Area and Perimeter.")
    else:
        print("Invalid input. Please input a valid option.")



