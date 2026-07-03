print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Before Your eyes there are 2 roads, You must choose going to the 'Left', or going to the 'Right'.").lower()

if choice1 == "left":
    choice2 = input("You come across a river, You have 2 options: Wait for a boat to get you to the other side or Swim.").lower()
    if choice2 == "wait":
        choice3 = input("Thanks to a kind fisher and his boat you have safely arrived on the other side, after some time you have reached an abandoned castle, on the inside there are 3 colored doors, a blue one, a yellow one and a red one, you have to choose only 1 door.").lower()
        if choice3 == "blue":
            print("You enter trough the blue door, finding what looks like a beast nest, unfortunately you are ambushed by an unknown beast and become the lunch. GIT GUT MATE.")
        elif choice3 == "red":
            print("You pass trough the red door, at last, you have found a treasure chest, without hesitation you run to the treasure, activating a trap that set ablaze the entire room. GIT GUT MATE.")
        elif choice3 == "yellow":
            print("Barely opening the yellow door you are dazzled by the glitter of countless gold coins, armors and weapons. CONGRATS!!, YOU HAVE FOUND THE TREASURE!!")
    elif choice2 == "swim":
        print("The river flow is very strong, after some time trying to reach the shore you are completely exhausted and get swifted by the river's current. GIT GUT MATE.")
else:
    print("You have fell into a bandit ambush. GIT GUT MATE!!")
