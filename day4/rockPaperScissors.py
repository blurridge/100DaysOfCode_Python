import random

ascii_art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if user_choice < 0 or user_choice > 2:
    print("You entered an invalid choice. You lose!")
else:
    print(ascii_art[user_choice])
    cpu_choice = random.randint(0, 2)
    print(f"Computer chose: \n\n{ascii_art[cpu_choice]}")
    if user_choice == cpu_choice:
        print("It's a draw!")
    elif (user_choice == 0 and cpu_choice == 1) or (user_choice == 1 and cpu_choice == 2) or (user_choice == 2 and cpu_choice == 0):
        print("You lose!")
    elif (user_choice == 0 and cpu_choice == 2) or (user_choice == 1 and cpu_choice == 0) or (user_choice == 2 and cpu_choice == 1):
        print("You win!")