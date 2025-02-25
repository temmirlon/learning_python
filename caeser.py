alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for i in range(0, len(original_text)):
        for y in range(0, len(alphabet)):
            if original_text[i] == alphabet[y]:
                shift_position = (y - shift_amount) % len(alphabet)
                decrypted_text += alphabet[shift_position]
    print(f"Your decrypted word: {decrypted_text}")


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for i in range(0, len(original_text)):
        for y in range(0, len(alphabet)):
            if original_text[i] == alphabet[y]:
                shift_position = (y + shift_amount) % len(alphabet)
                encrypted_text += alphabet[shift_position]
    print(f"Your encrypted word: {encrypted_text}")


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print(f"You need to write either 'encode' or 'decode'. Try again!")


caesar()