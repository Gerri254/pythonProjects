import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]

1
user_choice =  int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice >= 3 or user_choice <0 :
    print ("You chose an invalid number, you lose")
else:
    print (game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_images[computer_choice])

 
if user_choice >= 3 or user_choice <0 :
    print ("You chose an invalid number, you lose")

if user_choice == 0 and computer_choice == 2:
    print("You win")

elif computer_choice == 0 and user_choice == 2:
     print("You win")

elif computer_choice > user_choice:
    print("You Lose")

elif computer_choice < user_choice:
    print("You Win")

elif user_choice == computer_choice:
    print ("Its a draw")

