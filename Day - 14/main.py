from game_data import data
from replit import clear
import random
from art import logo,vs

print(logo)

def account_format(compare):
  format_name = compare['name']
  format_desc = compare['description']
  format_country = compare['country']
  return (f"{format_name}, a {format_desc}, from {format_country}")

def check_answer(guess, a_follower_count, b_follower_count):
  if a_follower_count > b_follower_count :
    return guess == 'a'
  else:
    return guess == 'b'

score = 0
game_should_continue = True
compare_b = random.choice(data)

while game_should_continue:
  
  compare_a = compare_b
  compare_b = random.choice(data)
  
  if compare_a == compare_b:
    compare_b = random.choice(data)
  
  print(f"Compare A: {account_format(compare_a)}")
  print(vs)
  print(f"With B: {account_format(compare_b)}")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count = compare_a['follower_count']
  b_follower_count = compare_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You are right!, Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry game over, Final score: {score}")