# Simple calculator

math = input("Enter '+' to add, '-' to subtract, '*' to multiply, '/' to divide:\n")
a = int(input("Enter first operand: \n"))
b = int(input("Enter Second operand: \n"))

match math:
    case "+":
        print("The addition is: ", a + b)
    case "-":
        print("The subtraction is: ", a - b)
    case "*":
        print("The multiplication is: ", a * b)
    case "/":
        print("The multiplication is: ", a / b)
    case _:
        print("Invalid operation.")
