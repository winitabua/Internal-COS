
# Shape selection in function
def shape_selection():
    print("Here are type of shape avalaible;\n"
          "Rectangle, Square, Circle, Triangle & Parallelogram")
    shape_type.lower = input("Please choose one option from above : ")
    if shape_type == "Rectangle":
        print("You chose Rectangle.") 
    elif shape_type == "Square":
        print("You chose Square.")
    elif shape_type == "Circle":
        print("You chose Circle.")
    elif shape_type == "Triangle":
        print("You chose Triangle.") 
    elif shape_type == "Parallelogram":
        print("You chose Parallelogram.")
    else:
        print("Invalid input. Please input a valid choice.")

