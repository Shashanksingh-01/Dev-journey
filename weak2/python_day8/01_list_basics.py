fruits = ["apple", "banana", "mango"]
print(fruits)              # pura list
print(fruits[0])           # first item
print(fruits[-1])          # last item
print(len(fruits))         # total items

# Add item
fruits.append("orange")
print(fruits)

# Insert at index
fruits.insert(1, "guava")
print(fruits)

# Remove item
fruits.remove("banana")
print(fruits)

# Sort
fruits.sort()
print(fruits)
