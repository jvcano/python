from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print (logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  #bidding_record = {"angela":123, "james", "321" }
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"the winner is:{winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("what is your name?: ")
  price = int(input("what is your bit: $"))
  bids[name] = price
  should_continue = input("are there any other bidders? type 'yes' or 'no'. \n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  else:
    bidding_finished = False
    clear() 


