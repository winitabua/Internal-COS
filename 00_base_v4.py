
"""
base component for my area and perimeter calculation program

v0 - skeleton setup
v1 - user yes no checker and instructions
v2 - shape + type of calculation selection, calculation of area +perimeter and create a loop
v3 - display the history

by Winita Buaban
"""

# All functions below this line

# yes no checker function
def yes_no_checker(question):
    while True:
        try:
            answer = input(question)
            if answer.lower() == "yes":
                answer = "continue program"
                return answer
    
            elif answer.lower() == "no":
                answer = "show instruction"
                return answer
    
            else:
                print("Invalid input. Please answer yes or no.")
        
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")
        

# Instruction in a function, basic explanation
def instructions():
    print()
    print("***** How to use area and perimeter calculation tool *****")
    print("This is a program for students to check their maths homework "
          "specifically about Area and Perimeter.\n"
          "To use, please follow through each step; select shape & select type of calculation\n"
          "Then program will display the answer.\n"
          "You can do as many calculation as you want until you select finished.\n"
          "The program will display your calculation history at the end of the session.")
    print("Let's begin!")

# Shape selection in function
def shape_selection():
    print("Here are type of shape avalaible;\n"
            "1) Rectangle\n"
            "2) Square\n"
            "3) Circle\n"
            "4) Triangle\n"
            "5) Parallelogram")
    shape_type = input("Please choose a number from above : ")
    if shape_type == "1":
        print("\nYou chose Rectangle.")
        func_rectangle()
        
    elif shape_type == "2":
        print("\nYou chose Square.")
        func_square()
        
    elif shape_type == "3":
        print("\nYou chose Circle.")
        func_circle()
        
    elif shape_type == "4":
        print("\nYou chose Triangle.")
        func_triangle()
        
    elif shape_type == "5":
        print("\nYou chose Parallelogram.")
        func_parallelogram()
        
    else:
        print("Invalid input.\n"
            "Please input a number from 1-5 to select a shape.")
        shape_selection()
            
        
# function of area and perimeter calculation for each shape below this line

# type of calculation in a function
def get_calculation_type():
    print()
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

# validate input in a function 
def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# history stored in lists
calculation_history_A =[]
calculation_history_P =[]

# rectangle calculation in a function
def func_rectangle():
    print("What are the dimensions of this rectangle?")

    rec_height = validate_input("Height: ")
    rec_width = validate_input("Width: ")

    print("Rectangle height is {} and width is {}".format(rec_height, rec_width))

    rec_area = rec_height * rec_width
    rec_p = (2 * rec_height) + (2 * rec_width)

    calc_type = get_calculation_type()
    if calc_type == "1":
        print("Area of this rectangle is {}".format(rec_area))
    elif calc_type == "2":
        print("Perimeter of this rectangle is {}".format(rec_p))
    elif calc_type == "3":
        print("Area of this rectangle is {}. Perimeter of this rectangle is {}"
              .format(rec_area, rec_p))

    calculation_history_A.append((rec_area))
    calculation_history_P.append((rec_p))

# square calculation in a function
def func_square():
    print("What are dimensions of this square?")

    square_height = validate_input("Height : ")
    square_width = validate_input("Width : ")
    
    print("Square height is {} and width is {}".format(square_height, square_width))

    square_area = square_height * square_width
    square_p = (2*square_height) + (2*square_width)

    calc_type = get_calculation_type()
    if calc_type == "1":
        print("Area of this square is {}".format(square_area))
    elif calc_type == "2":
        print("Perimeter of this square is {}".format(square_p))
    elif calc_type == "3":
        print("Area of this square is {}. Perimeter of this square is {}"
              .format(square_area, square_p))

    calculation_history_A.append((square_area))
    calculation_history_P.append((square_p))

# triangle calculation in a function
def func_triangle():
    print("What are dimensions of the triangle?")
    
    tri_height = validate_input("Height : ")
    tri_base = validate_input("Base : ")
    tri_side_left = validate_input("Left side : ")
    tri_side_right = validate_input("Right side : ")
    
    print("Rectangle height is {} and base is {}".format(rec_height, rec_width))

    tri_area = 0.5 * tri_height * tri_base
    tri_p = tri_base + tri_side_left + tri_side_right

    calc_type = get_calculation_type()
    if calc_type == "1":
        print("Area of the triangle is {}".format(tri_area))
    elif calc_type == "2":
        print("Perimeter of this triangle is {}".format(tri_p))
    elif calc_type == "3":
        print("Area of this triangle is {}. Perimeter of this triangle is {}"
              .format(tri_area, tri_p))

    calculation_history_A.append((tri_area))
    calculation_history_P.append((tri_p))

# circle calculation in a function
def func_circle():
    print("What is the radius of the circle?")
    
    cir_radius = validate_input("Radius : ")
    
    print("Circle radius is {}.".format(cir_radius))

    cir_area = 3.14 * cir_radius ** 2
    cir_p = 2 * 3.14 * cir_radius
    
    calc_type = get_calculation_type()
    if calc_type == "1":
        print("Area of the circle is {}".format(cir_area))
    elif calc_type == "2":
        print("Perimeter of this circle is {}".format(cir_p))
    elif calc_type == "3":
        print("Area of this circle is {}. Perimeter of this circle is {}"
              .format(cir_area, cir_p))

    calculation_history_A.append((cir_area))
    calculation_history_P.append((cir_p))

# parallelogram calculation in a function
def func_parallelogram():
    print("What is the dimension of the parallelogram?")

    paralle_base = validate_input("Base : ")
    paralle_height = validate_input("Height : ")
    paralle_side = validate_input("Side : ")
    
    print("Parallelogram base is {}, height is {} and side is {}"
          .format(paralle_base, paralle_height, paralle_side))

    paralle_area = paralle_base * paralle_height
    paralle_p = 2 * (paralle_base + paralle_side)
    
    calc_type = get_calculation_type()
    if calc_type == "1":
        print("Area of the Parallelogram is {}".format(paralle_area))
    elif calc_type == "2":
        print("Perimeter of this Parallelogram is {}".format(paralle_p))
    elif calc_type == "3":
        print("Area of this Parallelogram is {}. Perimeter of this Parallelogram is {}"
              .format(paralle_area, paralle_p))

    calculation_history_A.append((paralle_area))
    calculation_history_P.append((paralle_p))

# main routine goes below here...
print("***** Welcome to the Area and Perimeter checker tool! *****")

used_before = yes_no_checker("Have you used this program before? ('yes' or 'no'): ")

if used_before == "continue program":
    shape_selection()

if used_before == "show instruction":
    instructions()
    shape_selection()
    
# loop, ask user whether they have more calculation to do
while True:
    print()
    continue_calculation = input("Do you want to do more calculations? (yes/no): ")
    if continue_calculation.lower() == "yes":
        shape_selection()
    elif continue_calculation.lower() == "no":
        print("\nCalculation History:")
        for i in range(1, len(calculation_history_A) + 1):
            print("Calculation {}".format(i))
            print("Area: {:.2f}".format(calculation_history_A[i - 1]))
            print("Perimeter: {:.2f}".format(calculation_history_P[i - 1]))
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("Hope you find this program helpful. Thank you for visiting this site :)")

