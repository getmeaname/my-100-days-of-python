from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bid_dict = {}

bidding_over = False

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bid_dict:
    bid_amt = bid_dict[bidder]  
    if bid_amt > highest_bid:
      highest_bid = bid_amt
      winner = bidder
  print(f"the winner is {winner} with bid of {highest_bid}")
    

while not bidding_over:
  name = input("what is your name : ")
  price = int(input("How much would you like to bid?: "))
  bid_dict[name] = price
  should_continue = input("Is there anyone left. y or n \n")
  if should_continue == "n":
    bidding_over = True
    highest_bidder(bid_dict)
  elif should_continue == "y":
    clear()


    
  
