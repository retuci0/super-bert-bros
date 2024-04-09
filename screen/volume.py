from misc.characters import *

import tkinter as tk
from tkinter import ttk


def change_volume(volume, music_volume):
    """Run a tkinter window to let the user adjust the volume."""

    def set_volume(volume):
        global final_volume
        final_volume = round(float(volume), 1)
        volume_text.config(text=f"Volume: {final_volume}")
    
    def set_music_volume(volume):
        global final_music_volume
        final_music_volume = round(float(volume), 1)
        music_volume_text.config(text=f"Music volume: {final_music_volume}")


    #Create the window
    root = tk.Tk()
    
    root.title("Change volume")
    root.iconbitmap("assets/images/pengiun.ico")
    root.geometry(f"530x200+700+300")
    root.resizable(False, False)

    #Label that displays current volume
    volume_text = tk.Label(root, text="Volume: 1")
    volume_text.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    
    #Slider to let the user adjust the volume
    volume_slider = ttk.Scale(root, from_=0, to=2, orient="horizontal", length=500, command=set_volume)
    volume_slider.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    volume_slider.set(volume)

    #Label that displays current music volume
    music_volume_text = tk.Label(root, text="Music volume: 1")
    music_volume_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    #Slider to let the user adjust the music volume
    music_volume_slider = ttk.Scale(root, from_=0, to=2, orient="horizontal", length=500, command=set_music_volume)
    music_volume_slider.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    music_volume_slider.set(music_volume)

    #OK button
    ok_button = ttk.Button(root, text="OK", command=root.destroy)
    ok_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
    
    return final_volume, final_music_volume