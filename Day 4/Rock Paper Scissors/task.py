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

computer_choice = random.choice(game_images)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n Choose an option:"))
user_choice_img = game_images[user_choice]

print(computer_choice)
print(f"Computer choise ")
print(user_choice_img)
print(f"user choice ")


if user_choice_img == computer_choice:
    print("Draw")
elif user_choice_img == rock and computer_choice == paper:
    print("you loose")
elif user_choice_img == paper and computer_choice == scissors:
    print("You loose")
elif user_choice_img == scissors and computer_choice == rock:
    print("you loose")

else:
    print("You win")



