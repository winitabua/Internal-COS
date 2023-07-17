
# validate input in a function 
def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

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

# square calculation in a function
def func_square():
    print("What are dimensions of this square?")

    square_height = validate_input("Height : ")
    square_width = validate_input("Width : ")
    
    print("Square height is {} and width is {}".format(square_height, square_width))

    square_area = square_height * square_width
    square_p = (2*rec_height) + (2*rec_width)

    calc_type = get_calculation_type()
    if calc_type == "1":
        print("Area of this square is {}".format(square_area))
    elif calc_type == "2":
        print("Perimeter of this square is {}".format(square_p))
    elif calc_type == "3":
        print("Area of this square is {}. Perimeter of this square is {}"
              .format(square_area, square_p))

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


