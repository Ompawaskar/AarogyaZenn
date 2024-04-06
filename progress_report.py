import tkinter as tk
import customtkinter as ctk
from customtkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


water_intake = [1, 3, 45, 56, 56, 96]
calorie_intake = [155, 355, 455, 565, 56, 96]
sleep = [10, 3, 4, 56, 560, 396]
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

fig1, ax1= plt.subplots(figsize=(10, 6))
fig1.suptitle('Calorie Intake per Week', fontsize=12)


ax1.bar(days_of_week, calorie_intake, color='skyblue', edgecolor='black')




for i, value in enumerate(calorie_intake):
    ax1.text(i, value + 2, str(value), ha='center', va='bottom')

ax1.grid(axis='y', linestyle='--', alpha=0.6)





fig2, ax2 = plt.subplots(figsize=(10, 6))  # Adjust figure size as needed
fig2.suptitle('Water Intake per Week', fontsize=12)  # Add main title for the figure

# Create a bar chart within the subplot
ax2.bar(days_of_week, water_intake, color='skyblue', edgecolor='black')


# Add data labels above bars (optional)
for i, value in enumerate(water_intake):
    ax2.text(i, value + 2, str(value), ha='center', va='bottom')

# Customize grid and axes
ax2.grid(axis='y', linestyle='--', alpha=0.6)

fig3, ax3 = plt.subplots(figsize=(10, 6))  # Adjust figure size as needed
fig3.suptitle('Sleep hours per Week', fontsize=12)  # Add main title for the figure

# Create a bar chart within the subplot
ax3.bar(days_of_week, sleep, color='skyblue', edgecolor='black')


# Add data labels above bars (optional)
for i, value in enumerate(sleep):
    ax3.text(i, value + 2, str(value), ha='center', va='bottom')

# Customize grid and axes
ax3.grid(axis='y', linestyle='--', alpha=0.6)

class Progress(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame = ctk.CTkScrollableFrame(master=self, fg_color='white', width=1200, height=700)
        self.frame.pack()

        self.waterframe = ctk.CTkFrame(master=self.frame,fg_color='red', width=1000, height=600)
        self.waterframe.pack(padx = 100,pady = 50)
        self.canvas1 = FigureCanvasTkAgg(fig2, master=self.waterframe)  
        self.canvas1.draw()  # Render the plot onto the canvas
        self.canvas1.get_tk_widget().pack()
        
        self.calframe = ctk.CTkFrame(master=self.frame, fg_color='red', width=1000, height=600)
        self.calframe.pack(padx = 100,pady = 50)
        self.canvas2 = FigureCanvasTkAgg(fig1, master=self.calframe)  
        self.canvas2.draw()  # Render the plot onto the canvas
        self.canvas2.get_tk_widget().pack()

        self.sleepframe = ctk.CTkFrame(master=self.frame,fg_color='red', width=1000, height=600)
        self.sleepframe.pack(padx = 100,pady = 50)
        self.canvas3 = FigureCanvasTkAgg(fig3, master=self.sleepframe)  
        self.canvas3.draw()  # Render the plot onto the canvas
        self.canvas3.get_tk_widget().pack()

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("1200x700")
#         self.grid_rowconfigure(0, weight=1)  # configure grid system
#         self.grid_columnconfigure(0, weight=1)

#         self.my_frame = Progress(master=self)
#         self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


# app = App()
# app.mainloop()
