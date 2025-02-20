import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Interactive Data Table", page_icon="📊")

# App title
st.title("📊 Interactive Data Table with Pandas")

# Load dataset
@st.cache_data  # Cache the data for better performance
def load_data():
    # Create a sample dataset (or replace with your CSV file)
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 40, 28],
        "Score": [85, 90, 78, 88, 92]
    }
    return pd.DataFrame(data)

df = load_data()

# Display the interactive table
st.dataframe(df, use_container_width=True)

# Optional: Show raw data in an expandable section
with st.expander("📂 View Raw Data"):
    st.write(df)
