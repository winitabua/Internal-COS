
# loop, ask user whether they have more calculation to do
while True:
    print()
    continue_calculation = input("Do you want to do more calculations? (yes/no): ")
    if continue_calculation.lower() == "yes":
        shape_selection()
    elif continue_calculation.lower() == "no":
        print("\nCalculation History:") # display the history
        break 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


