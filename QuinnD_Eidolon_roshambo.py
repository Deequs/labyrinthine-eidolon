#!/usr/bin/env python3
#
# Problem: Final Project
# Files:
#     None
# 
# Author: Devin Quinn
# Date: 27/04/2026
#
# provide comments for each section of code
#Imports random to actually run the rock/paper/scissors game
import random
#Define the roshambo function
def roshambo(choice=""):
    """Function to play roshambo (rock-paper-scissors), for use in the main program's TEST button"""
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    if choice == computer_choice:
        return "Tie"
    elif (choice == "rock" and computer_choice == "scissors") or (choice == "paper" and computer_choice == "rock") or (choice == "scissors" and computer_choice == "paper"):
        return "Win"
    else:
        return "Lose"