# T R Hoshino
# Baic calculator

# On-screen instruction with options
print("Select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

# set the input function
operation = input()

if operation == "1":
    # code for add
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)) + ".")

elif operation == "2":
    # code for subtract
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) - int(num2)) + ".")

elif operation == "3":
    # code for multiply
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) * int(num2)) + ".")

elif operation == "4":
    # code for divide
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) / int(num2)) + ".")