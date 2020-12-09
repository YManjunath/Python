from replit import clear
from art import logo
print(logo)

bid_dict ={}
bidding_finished = False

def highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"Highest bidder is {winner} with bid price of {highest_bid}")



while not bidding_finished:
  name = input("what's your name? ")
  bid_price = int(input("what's your bid? $"))
  bid_dict[name] = bid_price 
  any_bidders = input("are there any other bidders?? type 'yes' or 'no'").lower()
  if any_bidders == 'no':
    bidding_finished = True
    highest_bidder(bid_dict)
  else:
    clear()
    bidding_finished = False


