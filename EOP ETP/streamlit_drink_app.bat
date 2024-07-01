@echo off
REM Change to the directory where the Streamlit app is located
cd /d "C:\Users\CIS_User\Documents\git\devnet-devfun\EOP ETP"

REM Activate the virtual environment if you are using one
REM If not using a virtual environment, you can remove or comment out the following line
REM call C:\Users\CIS_User\Documents\git\devnet-devfun\EOP ETP\Scripts\activate
call venv\Scripts\activate

REM Launch the Streamlit app
start "" streamlit run drinktracker_app.py

REM Keep the command prompt open after the script finishes
pause
