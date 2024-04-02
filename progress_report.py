import tkinter as tk
import customtkinter

class Progress(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = customtkinter.CTkFrame(self, bg_color='red',fg_color='red', width=600, height=700)
        self.container.pack(fill=customtkinter.BOTH, expand=True)  # Pack the container frame

        self.label = customtkinter.CTkLabel(master=self.container, text="Hello")
        self.label.pack()  # Pack the label within the container

        # You can add more widgets here as needed
