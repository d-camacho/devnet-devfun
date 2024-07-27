@echo off
:: Change to the directory where the Streamlit app is located
cd /d "C:\Users\CIS_User\Documents\git\devnet-devfun\EOP ETP"

:: Activate the virtual environment
call venv\Scripts\activate

:: Launch the Streamlit app
start "" streamlit run drinktracker_app.py

:: Keep the command prompt open after the script finishes
pause
