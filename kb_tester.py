################################################
##
## Author:  Mike Palladino's Keyboard Tester
##
## Purpose: This is just a learning 
##          project for python. This
##          python script opens a keyboard
##          tester that turns green when a 
##          button is pressed. 
## Date:    9/4/2023
##
################################################

#!/usr/bin/env python
import tkinter as tk

def key_pressed(event):
    key = event.keysym
    if key in key_buttons:
        key_buttons[key].config(bg='green')
    
def key_released(event):
    key = event.keysym
    if key in key_buttons:
        key_buttons[key].config(bg='red')

def main():
    global key_buttons  # Define key_buttons as a global variable
    window = tk.Tk()
    window.title("Keyboard Tester")

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
