# Task_progress_tracker
day = int(input("Enter today’s day (1–30): "))
if day > 30 or day < 1:
    print("Invalid day! Please enter a number between 1 and 30.")

elif day <= 10:
    print("You have completed < 33% of your task.")
elif day <= 20:
    print("You have completed < 66% of your task.")
else:
    print("You're almost done — just a few days left!")

print("Thank you! Keep going 🚀")

