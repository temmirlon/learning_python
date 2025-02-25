lives_to_try = 6

while True:
    word = input("Write a word to guess (letters only): ")
    if word.isalpha():  
        break
    print("Invalid input! Please enter a word with letters only.")

guess_word = word.lower()
encrypted_word_list = ["_"] * len(guess_word)

while lives_to_try >= 1:
    guess_char = input("Guess a letter: ")

    if len(guess_char) != 1 or not guess_char.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess_char in guess_word:
        for i in range(0, len(guess_word)):
            if guess_char == guess_word[i]:
                encrypted_word_list[i] = guess_char                
        print(f"Word to guess: {"".join(encrypted_word_list)}")
        
        if "_" not in encrypted_word_list:
            print(f"You won the game!!!")
            break
    else:
        lives_to_try -= 1
        print(f"You guessed '{guess_char}', that's not in the word! You lose a life, {lives_to_try}/6.")
        
        if lives_to_try == 0:
            print("YOU LOSE ALL YOUR LIFE. YOU ARE DEAD!")