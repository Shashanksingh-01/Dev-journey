def get_even_number(n):
    evens=[]
    for i in range(n+1):
        if i%2==0:
            evens.append(i)
            return evens
        
result=get_even_number(10)
print(result)
