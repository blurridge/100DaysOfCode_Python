import random
import string

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
total_chars = num_letters + num_symbols + num_numbers
final_chars = list()
for i in range (0, total_chars):
    if num_letters != 0:
        final_chars.append(random.choice(letters))
        num_letters-=1
    elif num_symbols != 0:
        final_chars.append(random.choice(symbols))
        num_symbols-=1
    elif num_numbers != 0:
        final_chars.append(random.choice(numbers))
        num_numbers-=1
random.shuffle(final_chars)
final_pass = ''.join(final_chars)
print(final_pass)