from random import randint
from art import logo
print(logo)

easy_level = 10
hard_level = 5

# Checking the user guess against the answer
def check_answer(guess,answer,turns):
  """Checks the guess against answer and returns the remaining attempts """
  if guess > answer:
    print("Too high")
    return turns -1
  elif guess < answer:
    print("Too low")
    return turns -1
  else:
    print(f"You got it, the answer was {answer}")


# set the difficulty level
def dif_level():
  dif = input("Choose a dificulty level, Type 'easy' or 'hard': ")
  if dif == 'easy':
    return easy_level
  else:
    return hard_level

def game():
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100")
  # Choosing a number between 1 and 100
  answer = randint(1,101)


  turns = dif_level()


  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess a number")
    # Let the user guess the number
    guess = int(input("Make a guess : "))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You lost your attempts you lose!")
      return
    elif guess != answer:
      print("Guess again")
game()