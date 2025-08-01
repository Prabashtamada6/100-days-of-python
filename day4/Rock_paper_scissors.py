import random
rock_paper_scissors = [ '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', ''' 
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

player_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
print(rock_paper_scissors[player_choice])

print("computer chose:")
computer_choice = random.randint(0,2)

print(rock_paper_scissors[computer_choice])

if player_choice == 0 and computer_choice == 2:
    print("YOU WIN!")
elif computer_choice == 0 and player_choice == 2:
    print("YOU LOSE!")
elif computer_choice > player_choice:
    print("YOU LOSE!")
elif player_choice > computer_choice:
    print("YOU WIN!")
elif computer_choice == player_choice:
    print("it's a tie!")

else:
    print("you are choice does not exists")