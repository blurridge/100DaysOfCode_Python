import string

# Utility Functions

def decode(ciphertext, shift):
    plain_text = list(ciphertext)
    for i in range(0, len(plain_text)):
        if plain_text[i].isspace() == False and plain_text[i].isdigit() == False:
            if plain_text[i].islower() == True:
                ascii_value = ord(plain_text[i]) - shift
                diff = 97 - ascii_value
                plain_text[i] = chr(ascii_value) if diff <= 0 else chr(123 - diff)
            else:
                ascii_value = ord(plain_text[i]) - shift
                diff = 65 - ascii_value
                plain_text[i] = chr(ascii_value) if diff <= 0 else chr(91 - diff)
    return plain_text

def encode(plaintext, shift):
    cipher_text = list(plaintext)
    for i in range(0, len(cipher_text)):
        if cipher_text[i].isspace() == False and cipher_text[i].isdigit() == False:
            if cipher_text[i].islower() == True:
                ascii_value = ord(cipher_text[i]) + shift
                diff = ascii_value - 122
                cipher_text[i] = chr(ascii_value) if diff <= 0 else chr(96 + diff)
            else:
                ascii_value = ord(cipher_text[i]) + shift
                diff = ascii_value - 90
                cipher_text[i] = chr(ascii_value) if diff <= 0 else chr(64 + diff)
    return cipher_text
        

# Main Function

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
continue_choice = "yes"
while continue_choice == "yes":
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n")
    shift_number = int(input("Type your shift number:\n"))
    if choice == "encode":
        message = "".join(encode(message, shift_number))
        print(f"Here's the encoded result: {message}")
    elif choice == "decode":
        message = "".join(decode(message, shift_number))
        print(f"Here's the decoded result: {message}")
    continue_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()