import random

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5
num_to_guess = random.randint(1, 100)

# Utility Functions

def checkGuess(user_guess):
    if user_guess > num_to_guess:
        return 1
    elif user_guess == num_to_guess:
        return 0
    elif user_guess < num_to_guess:
        return -1

# Main Function

print(r"""
  _   _                 _                  _____                     _             
 | \ | |               | |                / ____|                   (_)            
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                                                              __/ |
                                                                             |___/ 
""")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
num_chances = EASY_DIFFICULTY if difficulty_choice == "easy" else HARD_DIFFICULTY 
while num_chances > 0:
    user_guess = int(input("Make a guess: "))
    result = checkGuess(user_guess)
    if result == 1:
        print("Too high.\nGuess again.")
    elif result == 0:
        print(f"You got it! The answer was {num_to_guess}.")
        quit()
    elif result == -1:
        print("Too low.\nGuess again.")
    num_chances-=1
    print(f"You have {num_chances} attempts remaining to guess the number.")
print(f"You lost! The answer was {num_to_guess}.")