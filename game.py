import random
import os

os.system('cls')

print("""
      =================================================
      Let's play ROCK PAPER SCISSORS with the computer
      Press 1 for ROCK 🪨
      Press 2 for PAPER 📄
      Press 3 for SCISSORS ✂️
      =================================================
      """)

play_again = True

while True:

        player_choice = int(input("Enter your choice: "))

        computer_choice = random.randint(1, 3)

        if player_choice == 1:
            if computer_choice == 1:
                print("Your choice ROCK\nComputer's choice ROCK.\nIt's a tie!")
            elif computer_choice == 2:
                print("Your choice ROCK\nComputer's choice PAPER.\nComputer wins!")
            else:
                print("Your choice ROCK\nComputer's choice Scissors.\nYou win!")

        elif player_choice == 2:
            if computer_choice == 1:
                print("Your choice PAPER\nComputer's choice ROCK.\nComputer wins!")
            elif computer_choice == 2:
                print("Your choice PAPER\nComputer's choice PAPER.\nIt's a tie!")
            else:
                print("Your choice PAPER\nComputer's choice Scissors.\nComputer wins!")

        else:
            if computer_choice == 1:
                print("Your choice Scissors\nComputer's choice ROCK.\nComputer wins!")
            elif computer_choice == 2:
                print("Your choice Scissors\nComputer's choice PAPER.\nYou win!")
            else:
                print("Your choice Scissors\nComputer's choice Scissors.\nIt's a tie!")

    
decision = input("\nEnter Y to play again or Q to quit\n")
d = decision.upper()

if "d" != "Y":
    play_again = False
    SystemExit("Bye")
else:
    play_again = True
    