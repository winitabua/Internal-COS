
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
        print("You chose Rectangle.")    
    elif shape_type == "2":
        print("You chose Square.")
    elif shape_type == "3":
        print("You chose Circle.")
    elif shape_type == "4":
        print("You chose Triangle.")
    elif shape_type == "5":
        print("You chose Parallelogram.")
    else:
        print("Invalid input. Please input a number from 1 to 5.")
        shape_selection()
        


