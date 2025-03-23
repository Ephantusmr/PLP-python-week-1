# Define a function to perform the operation
def calculate(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        return f"{num1} {operation} {num2} = {result}"
    elif operation == '-':
        result = num1 - num2
        return f"{num1} {operation} {num2} = {result}"
    elif operation == '*':
        result = num1 * num2
        return f"{num1} {operation} {num2} = {result}"
    elif operation == '/':
        # Ensure the second number is not zero to avoid division by zero
        if num2 != 0:
            result = num1 / num2
            return f"{num1} {operation} {num2} = {result}"
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."


# Main program
try:
    # Get inputs from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the operation and print the result
    result = calculate(num1, num2, operation)
    print(result)

except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print("An error occurred: ", str(e))