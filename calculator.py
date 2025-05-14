# Basic Calculator Program

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:  # Prevent division by zero
        result = num1 / num2
    else:
        result = "Error! Division by zero is not allowed."
else:
    result = "Invalid operation entered."

# Display result
print(f"{num1} {operation} {num2} = {result}")
