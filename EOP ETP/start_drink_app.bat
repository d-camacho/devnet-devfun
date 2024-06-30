@echo off
:: Navigate to the directory containing your Flask app
cd /d "C:\Users\dwayn\Documents\Git\devnet-devfun\EOP ETP"
if %errorlevel% neq 0 (
    echo Failed to navigate to Flask app directory
    pause
    exit /b 1
)

:: Set the FLASK_APP environment variable
set FLASK_APP=drink_tracker_app.py

:: Run the Flask application
python -m flask run
if %errorlevel% neq 0 (
    echo Failed to start Flask application
    pause
    exit /b 1
)

:: Open the default web browser and navigate to the Flask app
start "" "http://127.0.0.1:5000/"
if %errorlevel% neq 0 (
    echo Failed to open web browser
    pause
    exit /b 1
)

echo Flask application started successfully
pause
