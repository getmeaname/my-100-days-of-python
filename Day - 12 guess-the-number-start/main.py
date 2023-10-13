#Number Guessing Game Objectives:
from art import logo
import random
print(logo)
# Include an ASCII art logo.
easy_lvl = 10
hard_lvl = 5



# game_level = input("choose the difficulty 'easy' or 'hard': ").lower()
def set_difficulty():
  difficulty = input("Choose a difficulty Easy or Hard: ").lower()
  if difficulty == 'easy':
    return easy_lvl
  else:
    return hard_lvl
  
  
# Allow the player to submit a guess for a number between 1 and 100.

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_answer(guess, com, attempt):
  if guess > com:
    print("Too high")
    return attempt - 1
  elif guess < com:
    print("Too low")
    return attempt - 1
  elif guess == com:
    print(f"You Won. the answer is {com}")
# If they got the answer correct, show the actual answer to the player.

def game():
  print("Welcome to the number guessing game!")
  print("I am thinking of a num between 1 to 100")
  com = random.randint(1, 100)
  # print(f"{com}")
  attempt = set_difficulty()
  guess = 0
  while guess != com:
    print(f"You have {attempt} attempt left.")
    guess = int(input("Make a guess "))
    attempt = check_answer(guess, com, attempt)
    if attempt == 0:
      print("You Lose")
      return
    elif guess != com:
      print("Guess again")

game()
# Track the number of turns remaining.

# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# def easy_level():
  # global end_of_game
  # while end_of_game == False:
  #   lives = 10
  #   if guess != com:
  #     lives -= 1
  #     print(f"You have only {lives} left. ")
  #     if lives == 0:
  #       end_of_game = True
  #       print("You run out of guesses, you lose")
# if game_level == "easy":
#   easy_level()
# elif game_level == "hard":
#   hard_level()
