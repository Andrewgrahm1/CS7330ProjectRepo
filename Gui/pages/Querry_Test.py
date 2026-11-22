
import streamlit as st
import pandas as pd

st.title("Database Queries")

st.write("Search and retrieve information from the database.")

st.divider()

# Query selection
st.header("Select a Query")

query_type = st.selectbox(
    "Choose a query",
    [
        "View All Records",
        "Search by Name",
        "Filter by Category"
    ]
)

# Query parameters
st.subheader("Query Parameters")

if query_type == "Search by Name":

    search_name = st.text_input("Enter Name")

elif query_type == "Filter by Category":

    category = st.selectbox(
        "Select Category",
        ["Category 1", "Category 2", "Category 3"]
    )

# Run query
if st.button("Run Query"):

    st.info("Query functionality will be connected to MySQL.")

