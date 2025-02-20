import streamlit as st

# Set page title
st.set_page_config(page_title="Counter App", page_icon="🔢")

# Initialize session state for counter if not already present
if "count" not in st.session_state:
    st.session_state.count = 0

# Display the counter
st.title("🔢 Counter App")
st.write(f"Current count: **{st.session_state.count}**")

# Button to increment the counter
if st.button("Increment"):
    st.session_state.count += 1
    st.experimental_rerun()  # Refresh the app to update the count
