import streamlit as st

# Set page title
st.set_page_config(page_title="Reactivity with Widgets", page_icon="🎛️")

# App title
st.title("🎛️ Interactive Slider Example")

# Add a slider widget
slider_value = st.slider("Move the slider to update the value:", min_value=0, max_value=100, value=50)

# Display the selected value dynamically
st.write(f"🔢 **Selected Value:** {slider_value}")
