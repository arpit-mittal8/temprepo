# 2)	using switch ….case   display whether accepted character is vowel or not.

def is_vowel(char):
    char = char.lower()
    switcher = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True,
    }
    return switcher.get(char, False)

# Test the function
char = input("Enter a character: ")
if is_vowel(char):
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")
