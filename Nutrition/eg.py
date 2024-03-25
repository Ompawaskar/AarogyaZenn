import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton  # Assuming you have defined these custom classes

root = tk.Tk()

# Define data for each frame
frame_data = [
    {"title": "Breakfast", "calories": "0 of 337 cals", "color": "red", "text": "All you need is some breakfast!"},
    {"title": "Lunch", "calories": "0 of 500 cals", "color": "green", "text": "Lunchtime!"},
    {"title": "Dinner", "calories": "0 of 600 cals", "color": "blue", "text": "Time for a delicious dinner!"},
    {"title": "Snacks", "calories": "0 of 200 cals", "color": "yellow", "text": "Yummy snacks for you!"},
    {"title": "Dessert", "calories": "0 of 300 cals", "color": "orange", "text": "Save room for dessert!"},
]

# Create frames using loop
frames = []
for i, data in enumerate(frame_data):
    frame = CTkFrame(root, fg_color=data["color"])
    frame.grid(row=i, column=0, sticky='ew', padx=10, pady=10)
    frame.columnconfigure(0, weight=1)

    title_label = CTkLabel(frame, text=data["title"])
    title_label.grid(row=0, column=0, sticky='w', padx=10)

    calories_label = CTkLabel(frame, text=data["calories"])
    calories_label.grid(row=0, column=1, padx=10)

    button = CTkButton(frame, text="+")
    button.grid(row=0, column=2)

    meals_frame = CTkFrame(frame, fg_color="white")
    meals_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

    meals_label = CTkLabel(meals_frame, text=data["text"])
    meals_label.pack(padx=20, pady=20)

    frames.append(frame)

root.mainloop()
