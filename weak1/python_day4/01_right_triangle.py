column = int(input("Enter number of Columns: "))
for i in range(1, column + 1):
    print(" " * (column - i) + "*" * i)
