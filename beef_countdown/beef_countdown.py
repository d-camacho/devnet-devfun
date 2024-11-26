#!/usr/bin/python/env
# Countdown for the big beef party

import streamlit as st
from datetime import datetime
import time
import base64
from pathlib import Path

# utilize the entirity of the screen
st.set_page_config(layout="wide")

# Set your target date and time
target_date = datetime(2024, 12, 14, 15, 59, 59)

# Get the directory of the current Python script
current_dir = Path(__file__).parent

# Construct the path to the background image
background_image_path = current_dir / "brisket.png"

# Check if the image exists
if not background_image_path.exists():
    st.error("Background image not found. Check the file path!")
    st.stop()

# Load and encode the background image to base64
with open(background_image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Apply the background image without affecting the text
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("data:image/png;base64,{encoded_string}") no-repeat center center fixed;
    background-size: cover;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and Header
st.markdown("<h1 style='text-align: center; font-size: 90px; -webkit-text-fill-color: yellow; -webkit-text-stroke: 3px black;'>🎊🥩THE BIG BEEF PARTY 🥩🎊</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 60px; -webkit-text-fill-color: yellow; -webkit-text-stroke: 2px black;'>COUNTDOWN</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 30px; font-family: Lucida Handwriting, cursive; color: yellow;'>Dec. 14, 2024 at 4PM </h1>", unsafe_allow_html=True)

# Create a container for the countdown text
countdown_placeholder = st.empty()

# Countdown logic
while True:
    now = datetime.now()
    time_diff = target_date - now

    # If the countdown is over, display a message
    if time_diff.total_seconds() <= 0:
        countdown_placeholder.markdown(
            "<h1 style='text-align: center; color: white;'>🎉 Bring out the Beef! 🎉</h1>",
            unsafe_allow_html=True,
        )
        break

    # Calculate days, hours, minutes, and seconds remaining
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Display the countdown with a full-width gray background
    countdown_html = f"""
    <div style="
        text-align: center; 
        font-weight: bold; 
        font-size: 100px; 
        color: white; 
        background-color: rgba(50, 50, 50, 0.7); 
        padding: 20px 0; 
        width: 100%;
        margin: 0;
    ">
        {days}:{hours:02}:{minutes:02}:{seconds:02}
    </div>
    """
    countdown_placeholder.markdown(countdown_html, unsafe_allow_html=True)

    # Sleep for 1 second before updating
    time.sleep(1)
