#!/usr/bin/env python3
#
# Problem: Final Project
# Files:
#     QuinnD_Eidolon_class.py
#     QuinnD_Eidolon_roshambo.py
# 
# Author: Devin Quinn
# Date: 27/04/2026
#
# provide comments for each section of code
#Import random since it is used in the Eidolon class and the roshambo function
import random
#Import the Eidolon class and associated functions from the maker file
from QuinnD_Eidolon_class import Eidolon
from QuinnD_Eidolon_roshambo import roshambo
#Import tkinter and messagebox to create the GUI
import tkinter as tk
from tkinter import messagebox
#Import ttk for styling the GUI
from tkinter import ttk

#Define padding options since they will be used multiple times
OPTIONS = {"padx": 5, "pady": 5}

#Define function to create the Eidolon
def create_eidolon():
    eidolon = Eidolon()
    eidolon.assign_name_and_tier()
    eidolon.assign_locations()
    return eidolon

#Define function to create the button dictionary, which will keep track of which grid buttons have been clicked
def create_button_dict():
    global button_dict
    button_dict = {
        "A1": False,
        "A2": False,
        "A3": False,
        "B1": False,
        "B2": False,
        "B3": False,
        "C1": False,
        "C2": False,
        "C3": False
    }

#Define function to check for the correct amount of grid buttons pressed, then if the guess is correct
def resolve():
    guess = [key for key, value in button_dict.items() if value]
    if len(guess) != 2:
        messagebox.showerror("Invalid Guess", "Please select exactly 2 locations for your guess.")
        reset_buttons()
        return
    if set(guess) == set([eidolon.loc1, eidolon.loc2]):
        messagebox.showinfo("Correct Guess", f'You have correctly guessed both locations, and may proceed to {eidolon.name}\'s next layer.')
        #root.destroy()
    elif set(guess) & set([eidolon.loc1, eidolon.loc2]):
        messagebox.showinfo("Partially Correct Guess", f'You have correctly guessed one location, but not both. You take {eidolon.tier + 2} heat and are knocked back 4 spaces.')
        reset_buttons()
    else:
        messagebox.showinfo("Incorrect Guess", f'You have incorrectly guessed both locations. You take {eidolon.tier + 2} heat and are knocked back 4 spaces.')
        reset_buttons()

#Define function to disable a grid button when it is clicked and update the button dictionary
def grid_button_click(button):
    button.config(state="disabled")
    button_dict[button.cget("text")] = True
    print(f"Button {button.cget('text')} clicked. Current value is {button_dict[button.cget('text')]}.")

#Define function to reset the grid buttons
def reset_buttons():
    for button in root.winfo_children():
        if isinstance(button, ttk.Button) and button.cget("text") in button_dict:
            button.config(state="normal")
    create_button_dict()
    print("Buttons reset.")

#Define function for the TEST button
def test_button():
    """Create the secondary window"""
    rps = tk.Tk()
    rps.title("Roshambo")
    rps.geometry("300x100")
    """Use the roshambo function to dermine who wins, who loses, or if there's a tie. Destroys the window afterward."""
    """Probably a better way to do it than by nesting a function within a function, but it works and I don't want to refactor it."""
    def p_choice(choice):
        result = roshambo(choice)
        if result == "Win":
            messagebox.showinfo("Result", f"You win and may immediately guess.")
            rps.destroy()
        elif result == "Tie":
            messagebox.showinfo("Result", f"It's a tie, you must undergo the TEST again.")
            rps.destroy()
        else:
            messagebox.showinfo("Result", f"You lose and are STUNNED until the end of your next turn.")
            rps.destroy()
    """Create buttons for rock, paper, and scissors, which will call the roshambo function when clicked"""
    rock_button = ttk.Button(rps, text="Rock", command= lambda: p_choice("Rock"))
    paper_button = ttk.Button(rps, text="Paper", command= lambda: p_choice("Paper"))
    scissors_button = ttk.Button(rps, text="Scissors", command= lambda: p_choice("Scissors"))
    rock_button.grid(row=0, column=0, **OPTIONS)
    paper_button.grid(row=0, column=1, **OPTIONS)
    scissors_button.grid(row=0, column=2, **OPTIONS)

#Create main window
root = tk.Tk()
root.title("LAYER//LABYRINTHINE")
root.geometry("300x200")

#Attempt to create buttons for each grid location and assign them to the grid_button_click function, except using a for loop instead.
for row in range(1, 4):
    for col in range(3):
        button_text = f"{chr(64 + row)}{col + 1}"
        button = ttk.Button(root, text=button_text)
        button.config(command=lambda b=button: grid_button_click(b))
        button.grid(row=row, column=col, **OPTIONS)
"""
#Create buttons for each grid location and assign them to the grid_button_click function, refactored out in favor of a for loop but kept just in case.
A1button = ttk.Button(root, text="A1", command=lambda: grid_button_click(A1button))
A1button.grid(row=1, column=0, **OPTIONS)
A2button = ttk.Button(root, text="A2", command=lambda: grid_button_click(A2button))
A2button.grid(row=1, column=1, **OPTIONS)
A3button = ttk.Button(root, text="A3", command=lambda: grid_button_click(A3button))
A3button.grid(row=1, column=2, **OPTIONS)
B1button = ttk.Button(root, text="B1", command=lambda: grid_button_click(B1button))
B1button.grid(row=2, column=0, **OPTIONS)
B2button = ttk.Button(root, text="B2", command=lambda: grid_button_click(B2button))
B2button.grid(row=2, column=1, **OPTIONS)
B3button = ttk.Button(root, text="B3", command=lambda: grid_button_click(B3button))
B3button.grid(row=2, column=2, **OPTIONS)
C1button = ttk.Button(root, text="C1", command=lambda: grid_button_click(C1button))
C1button.grid(row=3, column=0, **OPTIONS)
C2button = ttk.Button(root, text="C2", command=lambda: grid_button_click(C2button))
C2button.grid(row=3, column=1, **OPTIONS)
C3button = ttk.Button(root, text="C3", command=lambda: grid_button_click(C3button))
C3button.grid(row=3, column=2, **OPTIONS)
"""
#Create button to submit guesses
Submitbutton = ttk.Button(root, text="RESOLVE", command= lambda: resolve())
Submitbutton.grid(row=4, column=0, columnspan=2, **OPTIONS)

#Create button to reset the grid buttons for the next round of guesses
Resetbutton = ttk.Button(root, text="RESET", command=reset_buttons)
Resetbutton.grid(row=4, column=2, columnspan=2, **OPTIONS)

#Create button to use the TEST action
Testbutton = ttk.Button(root, text="TEST", command= lambda: test_button())
Testbutton.grid(row=5, column=0, columnspan=2, **OPTIONS)

#Create the Eidolon, and the button dictionary
eidolon = create_eidolon()
create_button_dict()
#Create label to display the name of the Eidolon and its tier
eidolon_label = ttk.Label(root, text=f"{eidolon.name} (Tier {eidolon.tier})")
eidolon_label.grid(row=0, column=0, columnspan=3, **OPTIONS)
root.mainloop()