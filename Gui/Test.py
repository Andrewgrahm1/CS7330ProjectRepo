
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Database Application",
    page_icon="🗄️",
    layout="centered"
)

# Application title
st.title("Database Application")

# Welcome message
st.write("Welcome to our database application!")

# Section heading
st.header("User Input")

# Text input
name = st.text_input("Enter your name")

# Button
if st.button("Submit"):
    if name:
        st.success(f"Welcome, {name}!")
    else:
        st.warning("Please enter your name.")
