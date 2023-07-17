
# type of calculation in a function
def get_calculation_type():
    print("Type of calculation:\n"
          "1) Area\n"
          "2) Perimeter\n"
          "3) Both")

    while True:
        calc_type = input("Please choose a number from above: ")
        if calc_type in ("1", "2", "3"):
            return calc_type
        else:
            print("Invalid input. Please enter a number from 1 - 3.")

