
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
def shape_select():

# function of area and perimeter calculation
def func_rectangle():

def func_circle():

def func_triangle():

def func_parallelogram():


# loop, ask user whether they have more calculation to do


# Display the history


# main routine goes below here...
print("Welcome to...")



