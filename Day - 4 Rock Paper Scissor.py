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

# Write your code below this line 👇
option = [rock, paper, scissors]
user = int(input('what do you chose. 0 for rock, 1 for paper, 2 for scissors.\n'))
if user >= 3 or user < 0:
    print("Invalid, You loser")
else:
    print(option[user])
    com = random.randint(0, 2)
    print("Computer chose:")
    print(option[com])
    if user == 0 and com == 2:
        print('You Win')
    elif com == 0 and user == 2:
        print('You Lose')
    elif com > user:
        print("You lose.")
    elif user > com:
        print("You win")
    elif com == user:
        print("It is Draw.")
