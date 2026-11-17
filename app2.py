import streamlit as st

# Title and Header

st.title("Retail Business Dashboard")
st.write("Manager input selection")
st.number_input("enter number",n)
option = st.selectbox(
    "Enter the region ",
    ["north","south","east","west"]
)

st.write("You selected:", option)


# Instruction




# Number input for sales target



# Dropdown for region selection



# Submit button
if st.button("Submit"):
    # Display entered values



    # Success message



    # Extra message for ambitious target

