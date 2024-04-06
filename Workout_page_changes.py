import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk, ImageDraw
import io
import json
import urllib3
from concurrent.futures import ThreadPoolExecutor

import custom_wkt

class ExerciseImageLoader:
    def __init__(self):
        self.image_cache = {}
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.create_placeholder_image()

    def create_placeholder_image(self):
        size = (100, 100)
        self.placeholder_img = Image.new("RGB", size, "white")
        draw = ImageDraw.Draw(self.placeholder_img)
        draw.rectangle([0, 0, size[0]-1, size[1]-1], outline="black")

    def load_image(self, url, callback):
        if url in self.image_cache:
            callback(self.image_cache[url])
        else:
            future = self.executor.submit(self._fetch_image, url, callback)

    def _fetch_image(self, url, callback):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                img_data = response.content
                img = Image.open(io.BytesIO(img_data))
                photo = ImageTk.PhotoImage(img)
                self.image_cache[url] = photo
                callback(photo)
            else:
                print(f"Failed to fetch image from {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching image from {url}: {e}")
            callback(ImageTk.PhotoImage(self.placeholder_img))

class ExerciseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout")
        self.root.geometry("1300x700")
        self.root.configure(bg="black") 
        self.custom_workout_page = None
        self.exercise_loader = ExerciseImageLoader()
        self.exercises = []
        self.displayed_exercises = []  # Keep track of displayed exercises
        self.setup_ui()

    def setup_ui(self):
        search_frame = tk.Frame(self.root, pady=20, bg="black")
        search_frame.pack(fill="x")
        
        search_label = tk.Label(search_frame, text="Search:", bg="black", fg="white")
        search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(search_frame, width=50, bg="black", fg="white") 
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.fetch_exercises()
        body_parts = set()
        targets = set()
        secondary_muscles = set()
        equipment = set()
        for exercise in self.exercises:
            body_parts.add(exercise['bodyPart'])
            targets.add(exercise['target'])
            secondary_muscles.update(exercise['secondaryMuscles'])
            equipment.add(exercise['equipment'])
        
        body_parts_list = sorted(list(body_parts))
        targets_list = sorted(list(targets))
        secondary_muscles_list = sorted(list(secondary_muscles))
        equipment_list = sorted(list(equipment))

        self.body_part_var = tk.StringVar(self.root)
        self.body_part_var.set("All")
        body_part_menu = tk.OptionMenu(search_frame, self.body_part_var, "All", *body_parts_list)
        body_part_menu.config(bg="black", fg="white")
        body_part_menu.pack(side=tk.LEFT, padx=5)

        self.target_var = tk.StringVar(self.root)
        self.target_var.set("All")
        target_menu = tk.OptionMenu(search_frame, self.target_var, "All", *targets_list)
        target_menu.config(bg="black", fg="white")
        target_menu.pack(side=tk.LEFT, padx=5)

        self.secondary_muscle_var = tk.StringVar(self.root)
        self.secondary_muscle_var.set("All")
        secondary_muscle_menu = tk.OptionMenu(search_frame, self.secondary_muscle_var, "All", *secondary_muscles_list)
        secondary_muscle_menu.config(bg="black", fg="white")
        secondary_muscle_menu.pack(side=tk.LEFT, padx=5)

        self.equipment_var = tk.StringVar(self.root)
        self.equipment_var.set("All")
        equipment_menu = tk.OptionMenu(search_frame, self.equipment_var, "All", *equipment_list)
        equipment_menu.config(bg="black", fg="white")
        equipment_menu.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(search_frame, text="Search", command=self.search, bg="black", fg="white")
        self.search_button.pack(side=tk.LEFT)
        
        

        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(side=tk.LEFT, fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas, bg="black")
        self.inner_frame.bind("<Configure>", self.on_configure)

        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.executor = ThreadPoolExecutor(max_workers=10)
        self.displayed_exercises = self.exercises[:100]
        self.display_exercises(self.displayed_exercises)

        self.setup_scroll_event()

    def fetch_exercises(self):
        url = "https://exercisedb.p.rapidapi.com/exercises"
        headers = {
            "X-RapidAPI-Key": "e1388555aamsh715a82d5d0acf9ap12e4d8jsna244a61e64aa",
            "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
        }
        querystring = {"limit": 1324}  # Limit the response to 1324 exercises
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            self.exercises = response.json()
            with open('exercises.json', 'w') as json_file:
                json.dump(self.exercises, json_file)
        else:
            print(f"Failed to fetch exercises. Status code: {response.status_code}")

    def display_exercises(self, exercises_to_display):
        loader = ExerciseImageLoader()  
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        num_exercises = len(exercises_to_display)
        num_columns = 3
        num_rows = -(-num_exercises // num_columns)  

        for i, exercise in enumerate(exercises_to_display):
            label_references = [] 
            card_frame = tk.Frame(self.inner_frame, bg="black", width=200, height=100, padx=10, pady=10)
            card_frame.grid(row=i // num_columns, column=i % num_columns, padx=10, pady=10)
            label = tk.Label(card_frame, text=exercise["name"], bg="black", fg="white")
            label.pack()

            label.bind("<Button-1>", lambda event, ex=exercise: self.show_exercise_details(ex))

            select_button = tk.Button(card_frame, text="Add to Workout", command=lambda ex=exercise: self.add_to_custom_workout(ex))
            select_button.pack()

            gif_url = exercise.get('gifUrl')
            if gif_url:
                gif_label = tk.Label(card_frame, bg="#E0E0E0")
                gif_label.pack(pady=5)
                loader.load_image(gif_url, lambda img, gl=gif_label: self.update_label_with_image(gl, img))

    def update_label_with_image(self, label, img):
        if img:
            label.config(image=img)
            label.image = img
        else:
            messagebox.showinfo("Info", "Failed to fetch image.")

    def show_exercise_details(self, exercise):
        exercise_window = tk.Toplevel(self.root)
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

    def add_to_custom_workout(self, exercise):
        if self.custom_workout_page is None:
            self.custom_workout_page = custom_wkt.CustomWorkoutPage(self.root)

        self.custom_workout_page.update_exercises_list([exercise])
        messagebox.showinfo("Added", "Exercise added to Custom Workout.")

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def search(self):
        query = self.search_entry.get().lower() 
        body_part = self.body_part_var.get()
        target = self.target_var.get()
        secondary_muscle = self.secondary_muscle_var.get()
        equipment = self.equipment_var.get()

        filtered_exercises = [exercise for exercise in self.exercises if
                              (query in exercise['name'].lower()) and
                              (body_part == "All" or body_part.lower() == exercise['bodyPart'].lower()) and
                              (target == "All" or target.lower() == exercise['target'].lower()) and
                              (secondary_muscle == "All" or secondary_muscle.lower() in map(str.lower, exercise['secondaryMuscles'])) and
                              (equipment == "All" or equipment.lower() == exercise['equipment'].lower())]

        if filtered_exercises:
            self.displayed_exercises = filtered_exercises
            self.display_exercises(self.displayed_exercises)
        else:
            messagebox.showinfo("No Exercises", "No exercises match the selected filters.")

    def setup_scroll_event(self):
        self.canvas.bind("<Configure>", self.on_configure)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        if self.canvas.bbox("all")[3] == self.canvas.winfo_height():
            print("Loading more exercises...")
            self.load_more_exercises()

    def load_more_exercises(self):
        start_index = len(self.displayed_exercises)
        end_index = start_index + 100

        additional_exercises = self.exercises[start_index:end_index]
        self.displayed_exercises.extend(additional_exercises)

        self.display_exercises(additional_exercises)

    def open_custom_workout_page(self):
        if self.custom_workout_page is None:
            self.custom_workout_page = custom_wkt.CustomWorkoutPage(self.root)

        self.custom_workout_page.update_exercises_list([])

if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    root = tk.Tk()
    app = ExerciseApp(root)
    root.mainloop()
