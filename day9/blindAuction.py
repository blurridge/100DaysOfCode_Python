import os

# Initialization of empty dictionary

bids = {}

# Utility Functions

def find_highest_bid():
    highest_bid_key = ""
    current_highest_bid = 0
    for name in bids:
        current_highest_bid = bids[name] if bids[name] > current_highest_bid else current_highest_bid
        if bids[name] == current_highest_bid:
            highest_bid_key = name
    return highest_bid_key   

# Main Function

print(r"""
                ___________
                \         /
                )_______(
                |"""""""|_.-._,.---------.,_.-._
                |       | | |               | | ''-.
                |       |_| |_             _| |_..-'
                |_______| '-' `'---------'` '-'
                )"""""""(
                /_________\
                `'-------'`
            .-------------.
            /_______________\
""")
print("Welcome to the Secret Auction Program.")
continue_choice = "yes"
while continue_choice == "yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bids[name] = bid
    continue_choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls||clear')
winner = find_highest_bid()
winning_bid = "{:.2f}".format(bids[winner])
print(f"The winner is {winner} with a bid of ${winning_bid}")