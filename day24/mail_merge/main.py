# Main

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    names = [line.rstrip() for line in names]

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter, open("./Input/Letters/starting_letter.txt", mode="r") as template:
        letter = template.read()
        letter = letter.replace("[name]", name)
        new_letter.write(letter)