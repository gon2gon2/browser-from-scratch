from tkinter import font
import tkinter as tk

SIZE = 400

window = tk.Tk()
canvas = tk.Canvas(window, width=SIZE, height=SIZE)
bi_times = font.Font(family="Times", size=16, weight="bold", slant="italic")


TEXT = "Hello!"
canvas.create_text(200, 100, text=TEXT, font=bi_times)
tk.mainloop()
