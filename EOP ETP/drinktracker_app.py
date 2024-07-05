import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Initialize Streamlit settings
st.set_page_config(page_title='Drink Tracker', layout='wide')

# Declare variables
current_date = datetime.now().strftime("%Y-%m-%d")
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", f"drink_tracker_{current_date}.xlsx")

# Checks and load data based on date/time in the downloads_path to handle data preservation of data in case app crashes or refreshes
def load_data():
    if os.path.exists(downloads_path):
        df = pd.read_excel(downloads_path)
        df['Badge Number'] = df['Badge Number'].astype(int)
        st.session_state.drink_tracker = dict(zip(df['Badge Number'], df['Drinks']))
    else:
        st.session_state.drink_tracker = {}

# Initialize the drink tracker in session state if it doesn't exist
if 'drink_tracker' not in st.session_state:
    load_data()

# Define a callback function to record drinks
def record_drink(badge_number):
    try:
        badge_number = int(badge_number)
        if not (1 <= badge_number <= 9999):
            st.error("Invalid badge number. Please enter a number between 1 and 9999.")
        else:
            current_drinks = st.session_state.drink_tracker.get(badge_number, 0)
            if current_drinks >= 2:
                st.warning(f"Badge number {badge_number} has already reached the drink limit of 2.", icon="⚠️")
            else:
                st.session_state.drink_tracker[badge_number] = current_drinks + 1
                st.success(f"Drink {current_drinks + 1} recorded for badge number {badge_number}.")
                export_to_excel()
    except ValueError:
        st.error("Invalid input. Please enter a numeric badge number.")

# Function to display drink tracker
def display_drink_tracker():
    st.header('Drink Tracker:')
    if not st.session_state.drink_tracker:
        st.write('No drinks recorded yet.')
    else:
        df = pd.DataFrame(list(st.session_state.drink_tracker.items()), columns=['Badge Number', 'Drinks'])
        df['Badge Number'] = df['Badge Number'].astype(str)  # Ensure badge numbers are treated as strings
        st.dataframe(df)

# Function to export drink tracker to Excel
def export_to_excel():
    if not st.session_state.drink_tracker:
        st.warning('No data to export.')
    else:
        df = pd.DataFrame(list(st.session_state.drink_tracker.items()), columns=['Badge Number', 'Drinks'])
        df['Badge Number'] = df['Badge Number'].astype(str)  # Ensure badge numbers are treated as strings
        df.to_excel(downloads_path, index=False)
        

# Main function to run the app
def main():
    st.title('Just be :blue[cool] :sunglasses:')
    st.title('ETP Night at EOP')
    st. text('V1.4')  
    st.header('Drink Tracker', divider='violet')  
    

    badge_number = st.text_input('Please enter the badge number (1-9999):', key='badge_number')
    record_button = st.button('Record Drink')    

    if record_button and badge_number:
        record_drink(badge_number)

    display_drink_tracker()

    export_button = st.button('Export to Excel')
    if export_button:
        export_to_excel()
        st.success(f'Data exported to {downloads_path}')

if __name__ == '__main__':
    main()
