import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set page title
st.set_page_config(page_title="Matplotlib Graph in Streamlit", page_icon="📈")

# App title
st.title("📈 Line Graph with Matplotlib")

# Generate random dataset
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # Sin wave

# Create Matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)", color="blue")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Sine Wave Plot")
ax.legend()

# Display the Matplotlib figure in Streamlit
st.pyplot(fig)
