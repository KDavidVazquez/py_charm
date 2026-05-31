print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7.")
    else:
        bill = 12
        print("Adult ticket is $12.")

    want_photo = input("Would you like to take a photo? This cost $3. Type Y for Yes and N for No")
    if want_photo == "y":
        bill += 3

    print(f"Your total Bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
