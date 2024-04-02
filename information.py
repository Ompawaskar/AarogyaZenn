import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image
import tkinter as tk

# Import your custom widget here
from customtkinter import CTkTabview

information = CTk()
information.title("Login Page")
information.geometry("1300x700")
loginbg = ctk.CTkImage(Image.open("image3.png"), size=(1300, 700))
bg_label = ctk.CTkLabel(information, text="", corner_radius=5, image=loginbg)
bg_label.place(x=0, y=0)
information.resizable(False, False)

l1=ctk.CTkLabel(information, text="Hello there!",font=('Century Gothic',50),text_color="black",bg_color="#ffffff",)
l1.place(x=790, y=125)
l2=ctk.CTkLabel(information, text="We're happy that you've taken the first step towards a healthier you.\n We need a few details to kickstart your journey",font=('Century Gothic',20),text_color="black",bg_color="#ffffff",)
l2.place(x=590, y=200)
l3=ctk.CTkLabel(information, text="What is your name!",font=('Century Gothic',30),text_color="black",bg_color="#ffffff",)
l3.place(x=790, y=300)

email_txt = ctk.CTkEntry(information, border_width=1.5, border_color="#94a8fe",
                             placeholder_text="Name", width=315, height=48, corner_radius=30,
                             bg_color="#ffffff")
email_txt.place(x=773, y=375)




information.mainloop()
