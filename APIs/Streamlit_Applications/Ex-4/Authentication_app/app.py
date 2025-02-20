import streamlit as st

# Set page title
st.set_page_config(page_title="Secure App", page_icon="🔒")

# Hardcoded username and password (for demo purposes)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login Form
def login():
    st.title("🔒 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Logout Function
def logout():
    st.session_state.authenticated = False
    st.experimental_rerun()

# Authentication Check
if not st.session_state.authenticated:
    login()
else:
    # Main App Content
    st.title("🎉 Welcome to the Secure Streamlit App!")
    st.write("You have successfully logged in.")
    st.button("Logout", on_click=logout)
