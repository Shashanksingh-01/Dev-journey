# Sum of 'n' number
n = int(input("Enter how many numbers: "))
sum = 0

for i in range(1, n+1):
    sum += i   # i add karo, na ki 1
    print("Step", i, "→ Sum =", sum)

print("Total Sum =", sum)
