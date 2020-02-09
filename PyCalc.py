import math
# from tkinter import *
#
# root = Tk()
#
# myLabel = Label(root, text="Hello World!")
# myLabel.pack()
# root.mainloop()


def calc_info():
    print("The 'add' option activates addition.")
    print("The 'subtract' option activates subtraction.")
    print("The 'divide' option activates division.")
    print("The 'multiply' option activates multiplication.")
    print("The 'power' option raises a number to the power of another.")
    print("The 'square' option finds the square root of a number.")
    print("The 'cos' option finds the cosine of a number.\n")


def calculator():
    while True:
        calc_info()
        user_input = input("Enter your command:")

        # Add two numbers together
        if user_input == 'add':
            first_num = float(input("Enter the first number:"))
            second_num = float(input("Enter the second number:"))
            result = str(first_num + second_num)
            print(f"the result is {result}")

        # Subtract two numbers
        elif user_input == 'subtract':
            first_num = float(input("Enter the first number:"))
            second_num = float(input("Enter the second number:"))
            result = str(first_num - second_num)
            print(f"the result is {result}")

        #  Divide two numbers
        elif user_input == 'divide':
            first_num = float(input("Enter the first number:"))
            second_num = float(input("Enter the second number:"))
            result = str(first_num / second_num)
            print(f"the result is {result}")

        #  Multiply two numbers
        elif user_input == 'multiply':
            first_num = float(input("Enter the first number:"))
            second_num = float(input("Enter the second number:"))
            result = str(first_num * second_num)
            print(f"the result is {result}")

        #  Raise to the power of another number
        elif user_input == 'power':
            first_num = float(input("Enter the first number:"))
            second_num = float(input("Enter the second number:"))
            result = str(first_num ** second_num)
            print(f"the result is {result}")

        # find the square root of a number
        elif user_input == 'square':
            first_num = float(input("Enter the number you want to find the square root of:"))
            result = str(math.sqrt(first_num))
            print(f"the result is {result}")

        # find the cosine of a number
        elif user_input == 'cos':
            first_num = float(input("Enter the number you want to find the cosine of:"))
            result = str(math.cos(first_num))
            print(f"the result is {result}")

        # Exit the program
        elif user_input == "exit":
            break


calculator()
