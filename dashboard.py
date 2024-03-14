import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='#333333')
        self.pack_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.dashboard_label = tk.Label(self, text="Dashboard", bg='#333333', fg='white', font=('Arial', 16))
        self.dashboard_label.pack(pady=20)

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()
