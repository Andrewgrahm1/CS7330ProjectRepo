
import streamlit as st
from database import connect_db

# Page configuration
st.set_page_config(
    page_title="Database Application",
    page_icon="🗄️",
    layout="wide"
)

# Main title
st.title("Database Application")

st.write("Welcome to our database management application.")

st.divider()

# Introduction
st.header("Home")

st.write("""
This application allows users to interact with our database
without needing to access the database directly.

Use the navigation menu on the left to:
- Enter new information
- Search existing records
- Run database queries
""")

# Status section
st.subheader("Application Status")

col1, col2 = st.columns(2)

with col1:
    st.info("Database: Not Connected")

with col2:
    st.success("Application: Running")

st.subheader("Database Connection")

if st.button("Test Database Connection"):

    try:
        connection = connect_db()

        if connection.is_connected():
            st.success("Successfully connected to MySQL!")

        connection.close()

    except Exception as e:
        st.error(f"Database connection failed: {e}")
