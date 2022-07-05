import random

# Rules
# 1. Deck is unlimited in size.
# 2. No jokers.
# 3. J/Q/K is equal to 10.
# 4. Ace can be 11 or 1.
# 5. Cards in the list have equal probability and are not removed.

# Possible results in resultCheck()
# 1. Loss if:
#   a. User scores greater than 21.
#   b. Dealer scores 21.
#   c. Dealer score is greater if user stands.
# 2. Win if:
#   a. User scores 21.
#   b. Dealer scores greater than 21 and user scores less than 21.
#   c. User scores is greater than dealer if user stands.
# 3. Tie only if both score the same even after user stands and dealer takes cards.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Utility functions

def calculateScore(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def resultCheck(user_score, dealer_score, num_turns):
    if user_score > 21 or dealer_score == 21 or (dealer_score < 21 and dealer_score > user_score and num_turns > 2):
        return "You lose!"
    elif user_score == 21 or (dealer_score > 21 and user_score < 21) or (user_score < 21 and user_score > dealer_score and num_turns > 2):
        return "You win!"
    elif user_score == dealer_score and num_turns > 2:
        return "It's a tie!"

def getDealerCards(dealer_cards, num_turns):
    if(num_turns == 1):
        for i in range(0, 2):
            dealer_cards.append(random.choice(cards))
    else:
        dealer_cards.append(random.choice(cards))

def getUserCards(user_cards, num_turns):
    if(num_turns == 1):
        for i in range(0, 2):
            user_cards.append(random.choice(cards))
    else:
        user_cards.append(random.choice(cards))

# Main function

play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play_choice == 'y':
    num_turns = 1
    print(r"""
     _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                           _/ |                
                          |__/                 
    """)
    user_cards = list()
    dealer_cards = list()
    getUserCards(user_cards, num_turns)
    getDealerCards(dealer_cards, num_turns)
    user_score = calculateScore(user_cards)
    dealer_score = dealer_cards[0]
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {dealer_cards[0]}")
    if resultCheck(user_score, dealer_score, num_turns) == None:
        num_turns+=1
        continue_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        while(continue_choice == 'y' and user_score < 21):
            getUserCards(user_cards, num_turns)
            print(f"Your cards: {user_cards}")
            user_score = calculateScore(user_cards)
            continue_choice = input("Type 'y' to get another card, type 'n' to pass: ") if user_score < 21 else "n"
        dealer_score = calculateScore(dealer_cards)
        if resultCheck(user_score, dealer_score, num_turns) == None:
            num_turns+=1
            while dealer_score < 17:
                getDealerCards(dealer_cards, num_turns)
                dealer_score = calculateScore(dealer_cards)
    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: {dealer_cards}")
    print(resultCheck(user_score, dealer_score, num_turns))
    play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")