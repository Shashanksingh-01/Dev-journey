try:
    a= int(input("Enter first numbr:"))
    b = int(input("Enter second number:"))
    result = a / b
except ZeroDivisionError:
    print("Division by zero is not allowed!")
except ValueError:
    print("Please eneter valid numbers!")
else:
    print("Result:", result)
finally:
    print("Thank you for using the safe calculator!")
    