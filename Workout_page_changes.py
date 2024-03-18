import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io

def search():
    query = search_entry.get().lower()  
    body_part = body_part_var.get()
    target = target_var.get()
    secondary_muscle = secondary_muscle_var.get()
    equipment = equipment_var.get()

    
    filtered_exercises = [exercise for exercise in exercises if
                          (query in exercise['name'].lower()) and
                          (body_part == "All" or body_part.lower() == exercise['bodyPart'].lower()) and
                          (target == "All" or target.lower() == exercise['target'].lower()) and
                          (secondary_muscle == "All" or secondary_muscle.lower() in map(str.lower, exercise['secondaryMuscles'])) and
                          (equipment == "All" or equipment.lower() == exercise['equipment'].lower())]

    display_exercises(filtered_exercises)  

def fetch_exercises():
    url = "https://exercisedb.p.rapidapi.com/exercises"
    querystring = {"limit": "1324"}  
    headers = {
        "X-RapidAPI-Key": "e1388555aamsh715a82d5d0acf9ap12e4d8jsna244a61e64aa",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def on_configure(event):
    
    canvas.configure(scrollregion=canvas.bbox("all"))

def show_exercise_details(exercise):
    
    exercise_window = tk.Toplevel(window)
    exercise_window.title("Exercise Details")
    exercise_window.configure(bg="#E0E0E0")

    
    detailed_info = f"Exercise Name: {exercise.get('name')}\n" \
                    f"Body Part: {exercise.get('bodyPart')}\n" \
                    f"Equipment: {exercise.get('equipment')}\n" \
                    f"Target: {exercise.get('target')}\n" \
                    f"Secondary Muscles: {', '.join(exercise.get('secondaryMuscles'))}\n" \
                    f"Instructions:\n" \
                    f"{'; '.join(exercise.get('instructions'))}"

    
    details_label = tk.Label(exercise_window, text=detailed_info, bg="#E0E0E0", fg="#333333", font=("Helvetica", 12), wraplength=400)
    details_label.pack(pady=10, padx=10)

    
    gif_url = exercise.get('gifUrl')
    if gif_url:
        response = requests.get(gif_url)
        if response.status_code == 200:
            
            img_data = response.content
            img = Image.open(io.BytesIO(img_data))

            
            gif_label = tk.Label(exercise_window, bg="#E0E0E0")
            gif_label.pack(pady=10)

           
            def update_gif(frame_num=0):
                frame = img.seek(frame_num)
                frame = img.copy().convert('RGBA')
                photo = ImageTk.PhotoImage(frame)
                gif_label.config(image=photo)
                gif_label.image = photo  
                exercise_window.after(200, update_gif, (frame_num + 1) % img.n_frames)

            
            update_gif()
        else:
            
            messagebox.showerror("Error", "Failed to fetch GIF image.")
    else:
        
        messagebox.showinfo("Info", "No GIF image available for this exercise.")

def display_exercises(exercises_to_display):
    
    for widget in inner_frame.winfo_children():
        widget.destroy()

    
    for i, exercise in enumerate(exercises_to_display):
        card_frame = tk.Frame(inner_frame, bg="black", width=200, height=100, padx=10, pady=10)
        card_frame.grid(row=i // num_columns, column=i % num_columns, padx=10, pady=10)
        label = tk.Label(card_frame, text=exercise["name"], bg="black", fg="white")
        label.pack()

        
        label.bind("<Button-1>", lambda event, ex=exercise: show_exercise_details(ex))


window = tk.Tk()
window.title("Search Window")
window.configure(bg="black")  


exercises = fetch_exercises()


search_frame = tk.Frame(window, pady=20, bg="black")  
search_frame.pack(fill="x")

search_label = tk.Label(search_frame, text="Search:", bg="black", fg="white")   
search_label.pack(side=tk.LEFT)


search_entry = tk.Entry(search_frame, width=50, bg="black", fg="white")  
search_entry.pack(side=tk.LEFT, padx=5)


body_part_var = tk.StringVar(window)
body_part_var.set("All")
body_part_menu = tk.OptionMenu(search_frame, body_part_var, "All", *sorted(set(exercise['bodyPart'] for exercise in exercises)))
body_part_menu.config(bg="black", fg="white")  
body_part_menu.pack(side=tk.LEFT, padx=5)


target_var = tk.StringVar(window)
target_var.set("All")
target_menu = tk.OptionMenu(search_frame, target_var, "All", *sorted(set(exercise['target'] for exercise in exercises)))
target_menu.config(bg="black", fg="white")  
target_menu.pack(side=tk.LEFT, padx=5)

secondary_muscle_var = tk.StringVar(window)
secondary_muscle_var.set("All")
secondary_muscle_menu = tk.OptionMenu(search_frame, secondary_muscle_var, "All", *sorted(set(muscle for exercise in exercises for muscle in exercise['secondaryMuscles'])))
secondary_muscle_menu.config(bg="black", fg="white")  
secondary_muscle_menu.pack(side=tk.LEFT, padx=5)

equipment_var = tk.StringVar(window)
equipment_var.set("All")
equipment_menu = tk.OptionMenu(search_frame, equipment_var, "All", *sorted(set(exercise['equipment'] for exercise in exercises)))
equipment_menu.config(bg="black", fg="white")  
equipment_menu.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", command=search, bg="black", fg="white")
search_button.pack(side=tk.LEFT)

canvas = tk.Canvas(window, bg="black")
canvas.pack(side=tk.LEFT, fill="both", expand=True)

scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)


inner_frame = tk.Frame(canvas, bg="black")
inner_frame.bind("<Configure>", on_configure)  

canvas.create_window((0, 0), window=inner_frame, anchor="nw")


num_exercises = len(exercises)
num_columns = 5  # Number of columns per row
num_rows = -(-num_exercises // num_columns) 

display_exercises(exercises)

window.mainloop()
