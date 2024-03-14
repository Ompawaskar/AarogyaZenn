import tkinter as tk
from dashboard import Dashboard
from menu import Menu
import customtkinter as ctk
from customtkinter import *

ctk.set_appearance_mode("Dark") 
def open_dashboard():
    dashboard.show()
    dashboard_label.configure(text="Dashboard Page Opened")
    print("Dashboard page opened")

def open_nutrition():
    dashboard.hide()
    dashboard_label.configure(text="Nutrition Page Opened")
    print("Nutrition page opened")

def open_workout():
    dashboard.hide()
    dashboard_label.configure(text="Workout Page Opened")
    print("Workout page opened")

def logout():
    dashboard.hide()
    dashboard_label.configure(text="Logged Out")
    print("Logout")

def toggle_menu():
    if menu_visible.get():
        menu.hide()
        menu_visible.set(False)
    else:
        menu.show()
        menu_visible.set(True)

root = CTk()
root.geometry('300x500')
root.title('Arogya Zenn')
root.configure(bg='#333333')

menu_visible = ctk.BooleanVar()
menu_visible.set(False)

head_frame = ctk.CTkFrame(root)
head_frame.pack(side=ctk.TOP, fill=ctk.X)

toggle_btn = ctk.CTkButton(head_frame, text='☰',command=toggle_menu)
toggle_btn.pack(side=ctk.LEFT, padx=10)

title_label = ctk.CTkLabel(head_frame, text='Arogya Zenn')
title_label.pack(side=ctk.LEFT, padx=(0, 10))

dashboard = Dashboard(root)
dashboard.pack(pady=10)

dashboard_label = ctk.CTkLabel(root, text="Welcome to Your Dashboard")
dashboard_label.pack(pady=10)

menu = Menu(root, commands=[('Dashboard', open_dashboard), ('Nutrition', open_nutrition), ('Workout', open_workout), ('Logout', logout)])
root.mainloop()
