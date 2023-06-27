def calculator():
    print("Welcome to the Python Calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    o = input("Enter the operation number (1-4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if o == '1':
        result = num1 + num2
        print("The result of addition is: " + str(result))
    elif o == '2':
        result = num1 - num2
        print("The result of subtraction is: " + str(result))
    elif o == '3':
        result = num1 * num2
        print("The result of multiplication is: " + str(result))
    elif o == '4':
        if num2 != 0:
            result = num1 / num2
            print("The result of division is: " + str(result))
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation number. Please try again.")

calculator()
