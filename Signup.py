import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from PIL import ImageTk, Image
from DB import connection
# from Database.Calculations import calculate_daily_calories
from DBfuntions import add_user
import bcrypt
from tkinter import messagebox
import os
from globalStore import current_user

def showpass():
    if password_txt.cget("show") == "*":
        password_txt.configure(show="")
    else:
        password_txt.configure(show="*")



def credentials_pass_to_db():
    # Fetch username from the entry widget
    username = username_txt.get()
    print(username)
    current_user['username'] = username
    # Validate username uniqueness before proceeding with account creation
    if not validate_username(username):
        return
    # Proceed with account creation
    email = email_txt.get()
    password = password_txt.get()
    phone_no = phone_txt.get()
    insert_data(username, email, password, phone_no)

def validate_email():
    email = email_txt.get()
    if '@' not in email:
        messagebox.showerror("Error", "Email must contain '@' symbol")
        # Clear the entry widget or take appropriate action
        email_txt.delete(0, tk.END)
        # You may also focus on the entry for the user's convenience
        email_txt.focus_set()  

def validate_password():
    password = password_txt.get()
    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least eight characters long")
        # Clear the entry widget or take appropriate action
        password_txt.delete(0, tk.END)
        # You may also focus on the entry for the user's convenience
        password_txt.focus_set()          

def validate_phone():
    phone = phone_txt.get()
    if len(phone) != 13 or not phone.startswith('+91'):
        messagebox.showerror("Error", "Phone number must be 10 digits long and start with '+91'")
        # Clear the entry widget or take appropriate action
        phone_txt.delete(0, tk.END)
        # Set default value
        phone_txt.insert(0, '+91')
        # You may also focus on the entry for the user's convenience
        phone_txt.focus_set()

def check_username_uniqueness(username):
    try:
        db = connection()
        Users = db["Users"]
        # Query the database to check if the username exists
        existing_user = Users.find_one({"username": username})
        # If the username already exists, return False indicating it's not unique
        if existing_user:
            return False
        # If the username doesn't exist, return True indicating it's unique
        return True
    except Exception as e:
        print("Error occurred while checking username uniqueness:", e)
        return False

def validate_username(username):
    username = username_txt.get()
    if not check_username_uniqueness(username):
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        # Clear the entry widget or take appropriate action
        username_txt.delete(0, tk.END)
        # You may also focus on the entry for the user's convenience
        username_txt.focus_set()
        return False
    return True

def insert_data(username, email, password,phone_no):
   
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        # Connect to MongoDB
          

        # Prepare the document to be inserted
        user_data = {
            "username": username,
            "email": email,
            "phone":phone_no,
            "hashed_password": hashed_password,
            "salt": salt
        }

        add_user(user_data)
        
        signup.destroy()          
        os.system('python test.py')
# print(add_user(user_data))


         


signup = CTk()
signup.title("Signup Page")
signup.geometry("1300x700")
loginbg = ctk.CTkImage(Image.open("image.png"), size=(1300, 700))
bg_label = ctk.CTkLabel(signup, text="", corner_radius=5, image=loginbg)
bg_label.place(x=0, y=0)
signup.resizable(False, False)

email_txt = ctk.CTkEntry(signup, border_width=1.5, border_color="#94a8fe",
                         placeholder_text="Email", width=315, height=48, corner_radius=30,
                         bg_color="#ffffff")
email_txt.place(x=135, y=315)
# Validate email when focus leaves the entry

username_txt = ctk.CTkEntry(signup, border_width=1.5, border_color="#94a8fe",
                            placeholder_text="Username", width=315, height=48, corner_radius=30,
                            bg_color="#ffffff", )
username_txt.place(x=135, y=205)

password_txt = ctk.CTkEntry(signup, border_width=1.5, border_color="#94a8fe",
                            placeholder_text="Password", width=315, height=48, corner_radius=30,
                            bg_color="#ffffff", show='*')
password_txt.place(x=135, y=425)


phone_txt = ctk.CTkEntry(signup, border_width=1.5, border_color="#94a8fe",
                            placeholder_text="Phone Number", width=315, height=48, corner_radius=30,
                            bg_color="#ffffff",)
phone_txt.place(x=135, y=575)
# Set default value
phone_txt.insert(0, '+91')

# Validate phone number when focus leaves the entry


chk_box = ctk.CTkCheckBox(signup, width=16, height=16, text=None, border_width=1.5,
                          border_color="#94a8fe", command=showpass,
                          corner_radius=30, bg_color="#ffffff")
chk_box.place(x=145, y=485)

l2 = ctk.CTkLabel(signup, text="Show password", font=('Century Gothic', 20), text_color="black", bg_color="#ffffff")
l2.place(x=180, y=480)

nextbtn = ctk.CTkButton(signup, border_width=1.5, border_color="#94a8fe", text="Sign-up", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=lambda: (credentials_pass_to_db(),validate_phone(),validate_email(),validate_password()))

nextbtn.place(x=225, y=650)
signup.mainloop()
