import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Plotly in Streamlit", page_icon="📊")

# App title
st.title("📊 Interactive Scatter Plot with Plotly")

# Generate random dataset
np.random.seed(42)  # For reproducibility
df = pd.DataFrame({
    "X": np.random.randint(1, 100, 50),
    "Y": np.random.randint(1, 100, 50),
    "Category": np.random.choice(["A", "B", "C"], 50)  # Random categories
})

# Create scatter plot using Plotly
fig = px.scatter(df, x="X", y="Y", color="Category",
                 title="Interactive Scatter Plot",
                 labels={"X": "X Values", "Y": "Y Values"},
                 template="plotly_dark")

# Display the Plotly figure in Streamlit
st.plotly_chart(fig, use_container_width=True)
