from misc.characters import *

import random
import tkinter as tk
from tkinter import ttk


def character_selection_screen(player1_name, player1_character_param, player2_name, player2_character_param):
    """Run a tkinter window to let the user select which character he wants to play with."""

    #Method for the character selection dropdown
    def on_character_select(player, value):
        if player == 1:
            player1_character.set(value)
            
        elif player == 2:
            player2_character.set(value)
            

    def get_names():
        #Get the names and close the screen
        
        global player1_name
        global player2_name
        
        player1_name = player1_name_entry.get()
        player2_name = player2_name_entry.get()
        
        root.destroy()
    
    #Create a list with the characters
    characters = [
        "Random character",
        "Bert: Average person", 
        "Lorc: Heavy tank", 
        "Berrota: Lightweight", 
        "Jordi: Strong yet fragile"
    ]
    
    character_names = {
        "random": characters[0],
        "Bert": characters[1],
        "Lorc": characters[2],
        "Berrota": characters[3], 
        "Jordi": characters[4]
    }

    #Create the window
    root = tk.Tk()
    
    root.title("Character selection")
    root.iconbitmap("assets/images/pengiun.ico")
    root.geometry(f"530x100+700+300")
    root.resizable(False, False)
    
    #Create stringvars to store the selected character later
    player1_character = tk.StringVar()
    player2_character = tk.StringVar()

    #Player 1
    player1_label = tk.Label(root, text="Player 1 Character:")
    player1_label.grid(row=0, column=0, padx=10, pady=5)

    player1_dropdown = ttk.Combobox(root, values=characters)
    player1_dropdown.grid(row=0, column=1, padx=10, pady=5)
    player1_dropdown.bind("<<ComboboxSelected>>", lambda event: on_character_select(1, player1_dropdown.get()))
    player1_dropdown.set(character_names[player1_character_param])

    player1_name_entry = ttk.Entry(root, width=30)
    player1_name_entry.grid(row=0, column=2, padx=10, pady=5)
    player1_name_entry.insert(0, player1_name)

    #Player 2  
    player2_label = tk.Label(root, text="Player 2 Character:")
    player2_label.grid(row=1, column=0, padx=10, pady=5)

    player2_dropdown = ttk.Combobox(root, values=characters)
    player2_dropdown.grid(row=1, column=1, padx=10, pady=5)
    player2_dropdown.bind("<<ComboboxSelected>>", lambda event: on_character_select(2, player2_dropdown.get()))
    player2_dropdown.set(character_names[player2_character_param])

    player2_name_entry = ttk.Entry(root, width=30)
    player2_name_entry.grid(row=1, column=2, padx=10, pady=5)
    player2_name_entry.insert(0, player2_name)

    #Continue button
    ok_button = ttk.Button(root, text="Start Game", command=get_names)
    ok_button.grid(row=2, column=1, padx=10, pady=5)

    root.mainloop()

    #Converting StringVars into the actual character
    if player1_character.get() == characters[1]:
        player1_character = BERT
    elif player1_character.get() == characters[2]:
        player1_character = LORC
    elif player1_character.get() == characters[3]:
        player1_character = BERROTA
    elif player1_character.get() == characters[4]:
        player1_character = JORDI
    else:
        player1_character = random.choice((BERT, BERROTA, LORC, JORDI))

    if player2_character.get() == characters[1]:
        player2_character = BERT
    elif player2_character.get() == characters[2]:
        player2_character = LORC
    elif player2_character.get() == characters[3]:
        player2_character = BERROTA
    elif player2_character.get() == characters[4]:
        player2_character = JORDI
    else:
        player2_character = random.choice((BERT, BERROTA, LORC, JORDI))
    
    #Return the selected characters
    return [player1_character, player2_character, player1_name, player2_name]