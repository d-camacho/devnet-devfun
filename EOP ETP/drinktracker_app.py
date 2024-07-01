import streamlit as st
import pandas as pd
import os

# Initialize Streamlit settings
st.set_page_config(page_title='Drink Tracker', layout='wide')

# Initialize the drink tracker in session state if it doesn't exist
if 'drink_tracker' not in st.session_state:
    st.session_state.drink_tracker = {}

# Define a callback function to record drinks
def record_drink(badge_number):
    try:
        badge_number = int(badge_number)
        if not (1 <= badge_number <= 9999):
            st.error("Invalid badge number. Please enter a number between 1 and 9999.")
        else:
            current_drinks = st.session_state.drink_tracker.get(badge_number, 0)
            if current_drinks >= 2:
                st.warning(f"Badge number {badge_number} has already reached the drink limit of 2.")
            else:
                st.session_state.drink_tracker[badge_number] = current_drinks + 1
                st.success(f"Drink {current_drinks + 1} recorded for badge number {badge_number}.")
    except ValueError:
        st.error("Invalid input. Please enter a numeric badge number.")

# Define the main function to handle the Streamlit app
def main():
    st.title('Drink Tracker for ETP Night at EOP')

    badge_number = st.text_input('Please enter the badge number (1-9999):', key='badge_number')
    record_button = st.button('Record Drink')

    if record_button and badge_number:
        record_drink(badge_number)

    display_drink_tracker()

    export_button = st.button('Export to Excel', on_click=export_to_excel)

    
# Function to display drink tracker
def display_drink_tracker():
    st.header('Drink Tracker:')
    if not st.session_state.drink_tracker:
        st.write('No drinks recorded yet.')
    else:
        df = pd.DataFrame(list(st.session_state.drink_tracker.items()), columns=['Badge Number', 'Drinks'])
        st.dataframe(df)

# Function to export drink tracker to Excel
def export_to_excel():
    if not st.session_state.drink_tracker:
        st.warning('No data to export.')
    else:
        df = pd.DataFrame(list(st.session_state.drink_tracker.items()), columns=['Badge Number', 'Drinks'])
        file_path = os.path.join(os.getcwd(), 'drink_tracker.xlsx')
        df.to_excel(file_path, index=False)
        st.success(f'Data exported to {file_path}')

if __name__ == '__main__':
    main()
