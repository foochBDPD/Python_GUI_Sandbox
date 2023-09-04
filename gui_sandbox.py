#!/usr/bin/env python
import tkinter as tk

def main():
    window = tk.Tk()
    label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=50,
    height=50
)
    label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()