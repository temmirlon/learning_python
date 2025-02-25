def caesar():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    while True:
        encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        original_text = input("Type your message:\n").lower()
        shift_amount = int(input("Type the shift number:\n"))

        result_text = ""
        digit_number = ""
        if encode_or_decode == "decode":
            shift_amount = shift_amount * -1

        for i in range(0, len(original_text)):
            for y in range(0, len(alphabet)):
                if original_text[i] == alphabet[y]:
                    shift_position = (y + shift_amount) % len(alphabet)
                    result_text += alphabet[shift_position]
            if original_text[i] not in alphabet:
                digit_number += original_text[i]

        print(f"Your result word: {result_text}{digit_number}")

        restart_caesar = input("Would you like to restart? Write 'Yes' or 'No': ").lower()

        if restart_caesar == "no":
            print("Thank you. Bye )")
            break

caesar()