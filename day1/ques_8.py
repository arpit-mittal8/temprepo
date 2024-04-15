# 8) accept a character and display whether it is upper case or lower case or not an alphabet.
while True:
    char = input("Enter the character :")
    if char.isupper():
        print("Upper case")
    elif char.islower():
        print("Lower case")
    else:
        print("Not an Alphabet")