    
# rectangle calculation in a function
def func_rectangle():
    print("What are dimensions of this rectangle?")
    rec_height = int(input("Height : "))
    rec_width = int(input("Width : "))
    print("Rectangle height is {} and width is {}".format(rec_height, rec_width))

    rec_area = rec_height * rec_width
    rec_p = (2*rec_height) + (2*rec_width)
    print("Area of this rectangle is {}. Perimeter of this rectangle is {}"
          .format(rec_area, rec_p))

# square calculation in a function
def func_square():
    print("What are dimensions of this square?")
    square_height = int(input("Height : "))
    square_width = int(input("Width : "))
    print("Square height is {} and width is {}".format(square_height, square_width))

    square_area = square_height * square_width
    square_p = (2*rec_height) + (2*rec_width)
    print("Area of this square is {}. Perimeter of this square is {}"
          .format(square_area, square_p))    

# triangle calculation in a function
def func_triangle():
    print("What are dimensions of the triangle?")
    tri_height = int(input("Height : "))
    tri_base = int(input("Base : "))
    tri_side_left = int(input("Left side : "))
    tri_side_right = int(input("Right side : "))
    print("Rectangle height is {} and base is {}".format(rec_height, rec_width))

    tri_area = 0.5 * tri_height * tri_base
    tri_p = tri_base + tri_side_left + tri_side_right
    print("Area of the rectangle is {}. Perimeter of the rectangle is {}"
          .format(rec_area, rec_p))

# circle calculation in a function
def func_circle():
    print("What is the radius of the circle?")
    cir_radius = int(input("Radius : "))
    print("Circle radius is {}.".format(cir_radius))

    cir_area = 3.14 * cir_radius ** 2
    cir_p = 2 * 3.14 * cir_radius
    print("Area of the circle is {} Perimeter of the circle is {}"
          .format(cir_area, cir_p))

# parallelogram calculation in a function
def func_parallelogram():
    print("What is the dimension of the parallelogram?")
    paralle_base = int(input("Base : "))
    paralle_height = int(input("Height : "))
    paralle_side = int(input("Side : "))
    print("Parallelogram base is {}, height is {} and side is {}"
          .format(paralle_base, paralle_height, paralle_side))

    paralle_area = paralle_base * paralle_height
    paralle_p = 2 * (paralle_base + paralle_side)
    print("Area of the parallelogram is {}."
          " Perimeter of the parallelogram is {}"
          .format(paralle_area, paralle_p))
