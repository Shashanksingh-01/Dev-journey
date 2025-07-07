def calc(a, b):
    add = a + b
    mul = a * b
    sub = a - b
    div = a / b if b !=0 else None
    return add, mul, sub, div

result = calc(25,25)
print("Addition:",result[0])
print("Multiplication:",result[1])
