print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
firstChoice = input("You are at a crossroads. Where do you want to go? Left or right?\n").lower()
if firstChoice == "left":
    secondChoice = input("You come to a lake. There is an island in the middle of the lake. Do you wait for a boat or swim across?\n").lower()
    if secondChoice == "wait":
        thirdChoice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, yellow and blue. Which color do you choose?\n").lower()
        if thirdChoice == "red":
            print("Burned by fire. Game over.")
        elif thirdChoice == "blue":
            print("Eaten by beasts. Game over.")
        elif thirdChoice == "yellow":
            print("You win!")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("You fell into a hole. Game over.")