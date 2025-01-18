# Fibonacci series using without recursion (add the numbers).




# n=int(input("Enter a number: "))
# a=0
# b=1
# if n==1:
#     print(0)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)





#       Function:- Block of reusable code to perform a specific action.

#       Recursion:- A function calling itself is called a Recursion.


#  Fibonacci series using recursion.

# def fib(n): # 0 1 1 2 3 5
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1)+fib(n-2)
# n=int(input("Enter number: "))
# result=fib(n)
# print(result)
    

from tkinter import *

# Create the main window
root = Tk()
root.title("Calculator App")

# Create a variable to store the current expression
expression = ""

# Function to update the expression variable
def update_expression(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def evaluate_expression():
    global expression
    try:
        result = eval(expression)
        equation.set(result)
        expression = str(result)
    except Exception as e:
        equation.set("Error")
        expression = ""

# Function to clear the expression
def clear_expression():
    global expression
    expression = ""
    equation.set("")

# Create a variable to store the current equation
equation = StringVar()

# Create the input field
input_field = Entry(root, textvariable=equation, width=20)
input_field.grid(row=0, column=0, columnspan=4)

# Create the number buttons
button_1 = Button(root, text="1", width=5, command=lambda: update_expression(1))
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", width=5, command=lambda: update_expression(2))
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", width=5, command=lambda: update_expression(3))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", width=5, command=lambda: update_expression(4))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", width=5, command=lambda: update_expression(5))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", width=5, command=lambda: update_expression(6))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", width=5, command=lambda: update_expression(7))
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", width=5, command=lambda: update_expression(8))
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", width=5, command=lambda: update_expression(9))
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0", width=5, command=lambda: update_expression(0))
button_0.grid(row=4, column=0)

# Create the operator buttons
button_add = Button(root, text="+", width=5, command=lambda: update_expression("+"))
button_add.grid(row=1, column=3)

button_subtract = Button(root, text="-", width=5, command=lambda: update_expression("-"))
button_subtract.grid(row=2, column=3)

button_multiply = Button(root, text="*", width=5, command=lambda: update_expression("*"))
button_multiply.grid(row=3, column=3)

button_divide = Button(root, text="/", width=5, command=lambda: update_expression("/"))
button_divide.grid(row=4, column=3)

button_equals = Button(root, text="=", width=5, command=evaluate_expression)
button_equals.grid(row=4, column=2)

button_clear = Button(root, text="Clear", width=20, command=clear_expression)
button_clear.grid(row=5, column=0, columnspan=4)

# Start the main loop
root.mainloop()
