#!/usr/bin/env python
import tkinter as tk

def key_pressed(event):
    key = event.keysym
    if key in key_colors:
        key_colors[key] = 'green'
        update_key_colors()
    
def key_released(event):
    key = event.keysym
    if key in key_colors:
        key_colors[key] = 'red'
        update_key_colors()

def update_key_colors():
    for key, color in key_colors.items():
        key_buttons[key].config(bg=color)

def main():
    window = tk.Tk()
    window.title("Keyboard Tester")

    key_colors = {key: 'red' for key in 'qwertyuiopasdfghjklzxcvbnm'}
    key_buttons = {}

    row_num = 0
    col_num = 0
    for key in 'qwertyuiopasdfghjklzxcvbnm':
        key_buttons[key] = tk.Button(
            window, text=key, width=4, height=2, bg='red', relief='raised')
        key_buttons[key].grid(row=row_num, column=col_num, padx=5, pady=5)
        col_num += 1
        if col_num > 4:
            col_num = 0
            row_num += 1

    window.bind("<KeyPress>", key_pressed)
    window.bind("<KeyRelease>", key_released)

    window.mainloop()

if __name__ == "__main__":
    main()
