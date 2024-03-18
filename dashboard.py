import tkinter as tk
import customtkinter as ctk
from customtkinter import *

class Dashboard(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.dashboard_label = ctk.CTkFrame(self, width=800,height=500,border_width=2,bg_color='red')
        self.dashboard_label.pack(pady=20)

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()
    
    def set_width(self, width):
        self.configure(width=width)

    def set_height(self, height):
        self.configure(height=height)
