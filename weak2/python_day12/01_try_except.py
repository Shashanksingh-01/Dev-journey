try:
    num = int(input("Enter a number:"))
    print("Number is :", num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
