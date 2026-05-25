# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: Vinoshan_RPSGame.py
# Description: Determine the result of a rock, paper, scissors game based on 
# choices of player 1 and player 2.
# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: Vinoshan_RPSGame.py
# Description: Determine the result of a rock, paper, scissors game based on 
#              choices of player 1 and player 2.

#Optional: Uncomment Below. Library
import os

#Optional: Uncomment Below both lines. Clear Screen functions
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Get Input of Players
player1 = input("Player 1, enter rock, paper, or scissors: ").lower()

# Optional: Uncomment Below. Clear screen so Player 2 cannot see Player 1's choice
clear_screen()

player2 = input("Player 2, enter rock, paper, or scissors: ").lower()

# Game Logic of Rock Paper Scissors
# Tie
if player1 == player2:
    print(f"It's a tie! Player 1 and 2 used {player1}!")
# Player 1 Wins
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "paper" and player2 == "rock") or \
     (player1 == "scissors" and player2 == "paper"):
    print(f"Player 1 wins! Player 1 used {player1} against Players 2's {player2}!")
# Player 2 Wins
else:
    print(f"Player 2 wins! Player 2 used {player2} against Player 1's {player1}!")
