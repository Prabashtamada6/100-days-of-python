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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('You\'re at a cross road. Where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
   choice2= input('you\'ve come to lake. there is an island in the middle of the lake.'
          ' type "wait" to wait for a boat. type "swim" to swim across. ').lower()
   if choice2 == "wait":
      choice3= input("you arrived at the island unharmed."
                  " there is houses with 3 doors. one red,"
                  " one yellow and one blue. ").lower()
      if choice3== "red":
              print("it's all over fire. GAME OVER.")
      elif choice3== "yellow":
              print("you found the treasure. $ YOU WIN $")
      elif choice3== "blue":
              print("it's full of snakes. GAME OVER.")
      else:
              print("you chose a door that doesn't exists. GAME OVER.")

   else:
        print("you died. you get attacked by lake monster.")
else:
    print("you fell into hole. GAME OVER.")

