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

game_image = [rock, paper, scissors]
User_choice = int(input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print(f"You choose  {game_image[User_choice]}")


Computer_Choice = random.randint(0,2)
print(f"Computer choose  {game_image[Computer_Choice]}")


if User_choice >= 3 and User_choice < 0:
  print("You have typed invalid number")
elif User_choice == 0 and Computer_Choice == 2:
  print("You win!")
elif Computer_Choice == 0 and User_choice == 2:
  print("You loose")
elif Computer_Choice > User_choice:
  print("You loose")
elif User_choice > Computer_Choice:
  print("You win")
elif Computer_Choice == User_choice:
  print("Draw")