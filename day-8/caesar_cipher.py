# encode: shift all characters in text to right by a shift value
import caesar_logo as cl

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    return (text, shift, direction)


def caesar(text, shift, direction):
    result = ""
    for letter in text:
        if letter in alphabet:
            idx_alphabet = alphabet.index(letter)

        if direction == 'encode' and (letter in alphabet):
            if idx_alphabet + shift <= 25:
                result += alphabet[idx_alphabet + shift]
            else:
                result += alphabet[(idx_alphabet + shift) % 26]

        elif direction == 'encode' and (letter in alphabet):
            if idx_alphabet - shift < 0:
                result += alphabet[26 - abs(idx_alphabet - shift)]
            else:
                result += alphabet[idx_alphabet - shift]
        else:
            result += letter
    print(f"Here's the {direction}d result: {result}")


to_cont = True
print(cl.logo)
while to_cont:
    (text, shift, direction) = get_input()
    caesar(text, shift, direction)

    get_to_cont = input("Do you wish to continue? (y/n) ").lower()
    if get_to_cont == "n":
        to_cont = False