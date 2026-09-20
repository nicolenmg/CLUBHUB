print("Welcome, dear student, to CLUBHUB")
print("I am Clubby, Your Guide to the world of Clubs and activities. I will help you find the perfect club for your interests.")
name = input("Let me know your name: ")
if not name:
    print("You didn't enter your name. Please try again.")
elif name[0].lower() in "bcdfghjklmnpqrstvwxyz":
    print(f"You have a beautiful name, {name}!")
else:
    print(f"That's a unique name, {name}!")
