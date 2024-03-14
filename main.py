import tkinter as tk
from dashboard import Dashboard
from menu import Menu

def open_dashboard():
    dashboard.show()
    dashboard_label.config(text="Dashboard Page Opened")
    print("Dashboard page opened")

def open_nutrition():
    dashboard.hide()
    dashboard_label.config(text="Nutrition Page Opened")
    print("Nutrition page opened")

def open_workout():
    dashboard.hide()
    dashboard_label.config(text="Workout Page Opened")
    print("Workout page opened")

def logout():
    dashboard.hide()
    dashboard_label.config(text="Logged Out")
    print("Logout")

def toggle_menu():
    if menu_visible.get():
        menu.hide()
        menu_visible.set(False)
    else:
        menu.show()
        menu_visible.set(True)

root = tk.Tk()
root.geometry('300x500')
root.title('Arogya Zenn')
root.configure(bg='#333333')

menu_visible = tk.BooleanVar()
menu_visible.set(False)

head_frame = tk.Frame(root, bg='#555555', highlightbackground='white', highlightthickness=1)
head_frame.pack(side=tk.TOP, fill=tk.X)

toggle_btn = tk.Button(head_frame, text='☰', bg='#555555', fg='white', font=('Arial', 20), bd=0, command=toggle_menu)
toggle_btn.pack(side=tk.LEFT, padx=10)

title_label = tk.Label(head_frame, text='Arogya Zenn', bg='#555555', fg='white', font=('Arial', 20))
title_label.pack(side=tk.LEFT, padx=(0, 10))

dashboard = Dashboard(root)
dashboard.pack(pady=10)

dashboard_label = tk.Label(root, text="Welcome to Your Dashboard", bg='#333333', fg='white', font=('Arial', 16))
dashboard_label.pack(pady=10)

menu = Menu(root, commands=[('Dashboard', open_dashboard), ('Nutrition', open_nutrition), ('Workout', open_workout), ('Logout', logout)])
root.mainloop()
