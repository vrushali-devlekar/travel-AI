import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Toplevel, messagebox

class KayakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌍 Kayak 3.0 - Adventure Planner")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Style settings
        style = ttk.Style("flatly")  # Light theme
        style.configure('TLabel', font=('Segoe UI', 12))
        style.configure('TButton', font=('Segoe UI', 11, 'bold'), padding=10)

        # Title
        self.title_label = ttk.Label(
            root,
            text="🌟 Welcome to Kayak 3.0 🌟",
            font=("Segoe UI", 20, "bold"),
            bootstyle=PRIMARY
        )
        self.title_label.pack(pady=25)

        self.subtitle = ttk.Label(
            root,
            text="Let’s plan your next great adventure.",
            font=("Segoe UI", 13),
            bootstyle="info"
        )
        self.subtitle.pack(pady=5)

        # Buttons
        self.start_button = ttk.Button(
            root,
            text="🧭 Start Planning",
            bootstyle="success",
            width=20,
            command=self.plan_adventure
        )
        self.start_button.pack(pady=15)
        self.add_hover_effect(self.start_button)

        self.quit_button = ttk.Button(
            root,
            text="❌ Quit",
            bootstyle="danger",
            width=20,
            command=root.quit
        )
        self.quit_button.pack()
        self.add_hover_effect(self.quit_button)

    def add_hover_effect(self, button):
        def on_enter(e):
            button.configure(bootstyle="warning")
        def on_leave(e):
            if "start" in button["text"].lower():
                button.configure(bootstyle="success")
            else:
                button.configure(bootstyle="danger")
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def popup_input(self, title, prompt):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = int(screen_width * 0.5)
        height = int(screen_height * 0.5)

        popup = Toplevel(self.root)
        popup.geometry(f"{width}x{height}+{int((screen_width - width) / 2)}+{int((screen_height - height) / 2)}")
        popup.title(title)
        popup.grab_set()
        popup.resizable(False, False)

        label = ttk.Label(popup, text=prompt, font=("Segoe UI", 12), bootstyle="info")
        label.pack(pady=30)

        entry = ttk.Entry(popup, font=("Segoe UI", 12), width=40)
        entry.pack(pady=10)

        result = {"answer": None}

        def submit():
            result["answer"] = entry.get().lower()
            popup.destroy()

        submit_btn = ttk.Button(popup, text="Submit", command=submit, bootstyle="primary")
        submit_btn.pack(pady=15)

        popup.wait_window()
        return result["answer"]

    def plan_adventure(self):
        destination = self.popup_input("Destination", "Do you have a destination in mind? (yes/no)")
        if destination == 'yes':
            transport = self.popup_input("Transport", "Choose your transport: Plane / Train / Car")
            if transport == 'plane':
                class_type = self.popup_input("Flight Class", "Which class? (First / Business / Economy)")
                try:
                    luggage = int(self.popup_input("Luggage", "Enter baggage weight in KG:"))
                except:
                    luggage = 0
                if class_type in ['business', 'first']:
                    if luggage >= 21:
                        messagebox.showinfo("Info", "✅ Great! You can carry more luggage.")
                    else:
                        messagebox.showinfo("Info", "💼 You can bring more if you want!")
                else:
                    messagebox.showwarning("Warning", "⚠️ You may have too much luggage.")
            elif transport == 'train':
                seat = self.popup_input("Train", "Seat type: Economy or Business")
                if seat == 'business':
                    messagebox.showinfo("Train", "🛋️ Comfortable travel ahead!")
                elif seat == 'economy':
                    messagebox.showinfo("Train", "💰 Good savings choice!")
                else:
                    messagebox.showerror("Error", "Invalid class selection.")
            elif transport == 'car':
                messagebox.showinfo("Car", "🚗 Road trips are the best!")
                try:
                    num_people = int(self.popup_input("Passengers", "How many people?"))
                except:
                    num_people = 1
                if num_people <= 4:
                    messagebox.showinfo("Car", "👍 You can rent a car!")
                else:
                    messagebox.showinfo("Car", "🚌 You may need a van or minibus.")
            else:
                messagebox.showerror("Transport", "Invalid transport option.")
        else:
            trip_type = self.popup_input("Help", "Choose type: Beach / City / Adventure")
            if trip_type == 'beach':
                messagebox.showinfo("Beach", "🏖️ How about Hawaii?")
                beach_type = self.popup_input("Beach Type", "Popular or Remote beach?")
                if beach_type == 'popular':
                    messagebox.showinfo("Beach", "✨ Visit Waikiki Beach near Honolulu!")
                elif beach_type == 'remote':
                    messagebox.showinfo("Beach", "🌴 Head over to Maui!")
                else:
                    messagebox.showerror("Error", "Invalid beach type.")
            elif trip_type == 'city':
                messagebox.showinfo("City", "🗽 Explore New York City!")
                activity = self.popup_input("Activity", "Indoor or Outdoor?")
                if activity == 'indoor':
                    messagebox.showinfo("Indoor", "🖼️ Visit the Met Museum!")
                elif activity == 'outdoor':
                    messagebox.showinfo("Outdoor", "🌳 Relax in Central Park!")
                else:
                    messagebox.showerror("Error", "Invalid activity type.")
            elif trip_type == 'adventure':
                messagebox.showinfo("Adventure", "🌲 Explore Yosemite National Park!")
                outdoor_activity = self.popup_input("Activity", "Hiking or Camping?")
                if outdoor_activity == 'hiking':
                    messagebox.showinfo("Hiking", "🥾 Try hiking Half Dome!")
                elif outdoor_activity == 'camping':
                    messagebox.showinfo("Camping", "⛺ Camp inside the national park!")
                else:
                    messagebox.showerror("Error", "Invalid adventure activity.")
            else:
                messagebox.showerror("Error", "Invalid trip type.")

        for _ in range(3):
            answer = self.popup_input("Trivia", "🌍 What is the largest desert in the world?")
            if answer == "antarctica":
                messagebox.showinfo("Winner!", "🎉 WOW, you win a FREE trip!")
                break

        again = messagebox.askyesno("Restart", "🔁 Want to plan another trip?")
        if again:
            self.plan_adventure()
        else:
            self.root.quit()


if __name__ == "__main__":
    root = ttk.Window(themename="flatly")  # Light background
    app = KayakApp(root)
    root.mainloop()
