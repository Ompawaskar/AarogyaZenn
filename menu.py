import tkinter as tk
import customtkinter as ctk
from customtkinter import *

class Menu(tk.Frame):
    def __init__(self, master=None, commands=[]):
        super().__init__(master, bg='#444444')
        self.pack_propagate(False)
        self.commands = commands
        self.create_menu()

    def create_menu(self):
        for text, command in self.commands:
            menu_button = tk.Button(self, text=text, bg='#444444', fg='white', font=('Arial', 12), bd=0, command=command)
            menu_button.pack(fill=tk.X, padx=10, pady=5)

    def show(self):
        self.place(x=0, y=50, relheight=1, width=400)

    def hide(self):
        self.place_forget()

    def set_width(self, width):
        self.configure(width=width)

    def set_height(self, height):
        self.configure(height=height)
