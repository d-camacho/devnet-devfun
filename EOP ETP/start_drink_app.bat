@echo off
:: Navigate to the directory containing your Flask app
cd /d "C:\Users\dwayn\Documents\Git\devnet-devfun\EOP ETP"

:: Activate the virtual environment
call venv\Scripts\activate

:: Set the FLASK_APP environment variable
set FLASK_APP=drink_tracker_app.py

:: Run the Flask application
start "" python -m flask run

:: Wait for a few seconds to allow the Flask server to start
timeout /t 5 /nobreak

:: Open the default web browser and navigate to the Flask app
start "" "http://127.0.0.1:5000/"

:: End of the script