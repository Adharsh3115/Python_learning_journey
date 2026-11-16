username = input("Enter your username: ")

if len(username)>12:
    print("Your username should have less than 12 characters")

elif not username.find(" ")==-1:
    print("your username cannot contain space")

elif not username.isalpha():
    print("your username cannot contain digits")

else:
    print(f"Hello {username}!")
