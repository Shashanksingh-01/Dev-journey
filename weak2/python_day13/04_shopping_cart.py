cart = []

while True:
    item = input("Add item to cart (or type 'done' to finish):")
    if item=="done":
        break
    cart.append(item)

print("/n your shopping cart:")
for i in cart:
    print("-",i)