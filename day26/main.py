# Main

import pandas as pd

user_input = input("Enter a word: ").upper()
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = df.set_index("letter").to_dict()["code"]
nato_form = [nato_dict[letter] for letter in user_input]
print(nato_form)