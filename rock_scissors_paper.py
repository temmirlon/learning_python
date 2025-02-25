import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

if my_choice > 2 or my_choice < 0:
    print("You type invalid number. You lose!")
else:
    print(f"My choice: {game_images[my_choice]}")
    print(f"Computer choice: {game_images[computer_choice]}")

    if my_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and my_choice == 2:
        print("You lose!")
    elif computer_choice > my_choice:
        print("You lose!")
    elif my_choice > computer_choice:
        print("You win!")
    elif computer_choice == my_choice:
        print("It's a draw!")
