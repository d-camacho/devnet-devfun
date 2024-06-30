import tkinter as tk
from tkinter import messagebox

# Initialize an empty dictionary to store the number of drinks for each badge number
drink_tracker = {}

def get_drink():
    try:
        badge_number = int(entry_badge_number.get())
        if not (1 <= badge_number <= 9999):
            messagebox.showerror("Invalid Input", "Invalid badge number. Please enter a number between 1 and 9999.")
            return

        current_drinks = drink_tracker.get(badge_number, 0)
        if current_drinks >= 2:
            messagebox.showinfo("Drink Limit Reached", f"Badge number {badge_number} has already reached the drink limit of 2.")
        else:
            drink_tracker[badge_number] = current_drinks + 1
            messagebox.showinfo("Drink Recorded", f"Drink {current_drinks + 1} recorded for badge number {badge_number}.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric badge number.")

def show_drink_tracker():
    tracker_info = "\n".join([f"Badge {badge}: {drinks} drinks" for badge, drinks in drink_tracker.items()])
    messagebox.showinfo("Drink Tracker", tracker_info if tracker_info else "No drinks recorded yet.")

# Create the main application window
app = tk.Tk()
app.title("Drink Tracker for ETP Night at EOP")

# Create and place the label and entry for badge number input
label_badge_number = tk.Label(app, text="Please enter the badge number (1-9999):")
label_badge_number.pack(pady=5)

entry_badge_number = tk.Entry(app)
entry_badge_number.pack(pady=5)

# Create and place the buttons
button_record_drink = tk.Button(app, text="Record Drink", command=get_drink)
button_record_drink.pack(pady=5)

button_show_tracker = tk.Button(app, text="Show Drink Tracker", command=show_drink_tracker)
button_show_tracker.pack(pady=5)

button_exit = tk.Button(app, text="Exit", command=app.quit)
button_exit.pack(pady=5)

# Run the application
app.mainloop()
