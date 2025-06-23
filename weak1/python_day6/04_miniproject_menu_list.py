menu = ["Burger","Pizza","Magie","Samosa","Chowmein","Eggroll"]
print("🍽️Today menu:")
for i in range(len(menu)):
    print(f"(i+1).{menu[i]}")
choice = int(input("Choose an item(1-6):"))
print("Your selected :", menu[choice-1])