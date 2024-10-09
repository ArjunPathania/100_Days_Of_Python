import art
print(art.logo)

print("Welcome to the secret auction program.\n")
bidders = "yes"
auction_dictionary={}
while bidders.lower() !="no":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    auction_dictionary[name] = bid
    bidders = input("Are there any other bidders?Type 'yes' or 'no'.")
    print("\n"*100)

max_bid = 0
max_bidder = ""
for key in auction_dictionary:
    if auction_dictionary[key]>max_bid:
        max_bid = auction_dictionary[key]
        max_bidder = key

print(f"The winner is {max_bidder} with a bid of ${max_bid}")