try:
    num= int(input("Enter a positive number:"))
except ValueError:
    print("That`s not a valide number!")
else:
    print("Good Job! You entered a vaide number:", num)