# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize an empty dictionary to store the number of drinks for each badge number
drink_tracker = {}

def get_drink(badge_number):
    # Check if the badge number is valid
    if not (1 <= badge_number <= 9999):
        return "Invalid badge number. Please enter a number between 1 and 9999."

    # Get the current drink count for the badge number, defaulting to 0 if not present
    else:
        current_drinks = drink_tracker.get(badge_number, 0)

        # Check if the user has already reached the drink limit
        if current_drinks >= 2:
            return f"Badge number {badge_number} has already reached the drink limit of 2."
        else:
            # Increment the drink count
            drink_tracker[badge_number] = current_drinks + 1
            return f"Drink {current_drinks + 1} recorded for badge number {badge_number}."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_drink', methods=['POST'])
def record_drink():
    badge_number = int(request.form['badge_number'])
    message = get_drink(badge_number)
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
