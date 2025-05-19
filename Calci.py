#Simple Calculator for basic arithmetic operations 
 
def add(x, y):
    return x + y
 
def subtract(x, y):
    return x - y
 
def multiply(x, y):
    return x * y
 
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    else:
        return x / y
 
def calci():
    print("What operation do you wish to do?:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
 
    choice = input("Enter choice [1/2/3/4]: ")
 
    if choice in ['1', '2', '3', '4']:

#try and except for error handling if the user inputs any other inputs than numerical values.
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
 
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError:
            print("Only numerical values are allowed!")
    else:
        print("Invalid choice. only above given selections are possible.")

#calling the function for execution
calci()
 
