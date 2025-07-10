try:
    result = 10 / 0 
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("This will run no matter what.")