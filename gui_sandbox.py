#!/usr/bin/env python
import tkinter as tk
import subprocess

def start_tetris():
    subprocess.run(["python", "tetris_game.py"])  # Replace with the actual Tetris game script

def main():
    window = tk.Tk()
    window.title("GUI with Tetris Launcher")

    label = tk.Label(window, text="Click the button to start Tetris:")
    label.pack(pady=10)

    button = tk.Button(window, text="Click Me", command=start_tetris)
    button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
