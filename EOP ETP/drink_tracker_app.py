from flask import Flask, request, render_template_string, redirect, url_for, flash, send_file
import pandas as pd
import os
import webbrowser
from threading import Timer

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Initialize an empty dictionary to store the number of drinks for each badge number
drink_tracker = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            badge_number = int(request.form['badge_number'])
            if not (1 <= badge_number <= 9999):
                flash("Invalid badge number. Please enter a number between 1 and 9999.", "error")
            else:
                current_drinks = drink_tracker.get(badge_number, 0)
                if current_drinks >= 2:
                    flash(f"Badge number {badge_number} has already reached the drink limit of 2.", "info")
                else:
                    drink_tracker[badge_number] = current_drinks + 1
                    flash(f"Drink {current_drinks + 1} recorded for badge number {badge_number}.", "success")
        except ValueError:
            flash("Invalid input. Please enter a numeric badge number.", "error")
        return redirect(url_for('index'))

    tracker_info = drink_tracker.items()
    return render_template_string(template, tracker_info=tracker_info)

@app.route('/export')
def export():
    # Convert the drink tracker dictionary to a DataFrame
    df = pd.DataFrame(list(drink_tracker.items()), columns=['Badge Number', 'Drinks'])
    
    # Define the filename and path
    file_path = os.path.join(os.getcwd(), 'drink_tracker.xlsx')
    
    # Save the DataFrame to an Excel file
    df.to_excel(file_path, index=False)
    
    # Send the file to the user
    return send_file(file_path, as_attachment=True)

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Drink Tracker for ETP Night at EOP</title>
</head>
<body>
    <h1>Drink Tracker</h1>
    <h2>for ETP Night at EOP</h2>
    <form method="post">
        <label for="badge_number">Please enter the badge number (1-9999):</label>
        <input type="text" id="badge_number" name="badge_number">
        <input type="submit" value="Record Drink">
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
          {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <h2>Drink Tracker:</h2>
    <ul>
    {% for badge, drinks in tracker_info %}
        <li>Badge {{ badge }}: {{ drinks }} drinks</li>
    {% endfor %}
    </ul>
    <br>
    <a href="{{ url_for('export') }}">Export to Excel</a>
</body>
</html>
'''

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)
