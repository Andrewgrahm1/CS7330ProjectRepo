
import streamlit as st

st.title("Data Entry")

st.write("Enter new information into the database.")

st.divider()

# Data entry form
st.header("Add New Record")

with st.form("add_record"):

    name = st.text_input("Name")

    description = st.text_area("Description")

    category = st.selectbox(
        "Category",
        ["Category 1", "Category 2", "Category 3"]
    )

    submit = st.form_submit_button("Add Record")

    if submit:
        if name:
            st.success(f"Record '{name}' submitted!")
        else:
            st.warning("Please enter a name.")
