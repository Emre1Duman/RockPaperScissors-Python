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



# UserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# #Computers random choice
# Options = ["Rock", "Paper", "Scissors"]
# RandomOption = random.randint(0, 2)
# ComputerChoice = Options[RandomOption]

# if UserChoice == 0 and ComputerChoice == "Scissors":
#     print("Computer chose:")
#     print("You win")
# elif UserChoice == 2 and ComputerChoice == "Paper":
#     print()

Options = [rock, paper, scissors]
UserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#2 beats 1, 1 beats 0, 0 beats 2


if UserChoice >= 3 or UserChoice < 0: #If the user enters an invalid number, the print statement below will kick in and avoid all the other code
    print("Invalid number! You Lose!")
else: #If the user enters a valid number, the else statement will kick in and trigger the rest of the code below
    print(Options[UserChoice])

    ComputerChoice = random.randint(0, 2)
    print(f"Computer chose: {Options[ComputerChoice]}")

    if UserChoice == 0 and ComputerChoice == 2:
        print("You win!")
    elif ComputerChoice > UserChoice:
        print("Compter wins!")
    elif UserChoice == 2 and ComputerChoice == 0:
        print("Computer wins!")
    elif UserChoice > ComputerChoice:
        print("you win!")
    elif  UserChoice == ComputerChoice:
        print("Its a draw")



