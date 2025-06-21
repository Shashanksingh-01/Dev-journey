def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid Operator"

# User input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+ - * /): ")

print("Result =", calculator(a, b, op))
