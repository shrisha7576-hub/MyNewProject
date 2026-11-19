import streamlit as st

# ---------------------------------------------------------------------------
# Retail Business Dashboard
# ---------------------------------------------------------------------------
# A retail manager enters a monthly sales target, selects a region, then
# clicks Submit to see a summary.
# Replace each ______ with the missing code. Do not pre-write answers in
# functions — keep everything at top level.

# Blank A: page title (match the screenshot).
st.title("Retail Business Dashboard")  # hint: st.title("...")

# Blank B: section header (match the screenshot).
st.header("Manager Input Section")  # hint: st.header("...")

# Blank C: short instruction under the header (match the screenshot).
st.write("Please enter the monthly sales target and select the region.")  # hint: st.write("...")

# Blank D: monthly sales target (USD). Default 50000. Minimum 0. (match the screenshot)
# Do not set a maximum (the Challenge uses a target above 50000).
sales_target = st.number_input(" Enter Monthly Sales Target(in USD):",
                               min_value=0,
                               value=50000,
                               )  # hint: st.number_input("...")

# Blank E: region dropdown (match the options shown in the document).
region = st.selectbox("Select Region:",
                      ["North","South"," East","West"]
                      )  # hint: st.selectbox("...")

# Blank F: Submit button, then show the entered values and a success message (match the screenshot).

if st.button("Submit"):
    st.write(f"Sales Target: ${sales_target}")
    st.write(f"Region Selected: {region}")
    st.error("Dashboard updated successfully!")
    if sales_target > 100000:
        st.write("Great! You have set an ambitious target!")
