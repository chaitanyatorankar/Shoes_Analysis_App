import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
df = pd.read_csv("SHOES.csv")

# Title of the app
st.title("Sales by Subsidiary - Region-wise View")

# Get unique regions for selection
regions = df['Region'].unique()

# Dropdown for region selection
selected_region = st.selectbox("Select a Region", regions)

# Filter data based on selected region
filtered_data = df[df['Region'] == selected_region]

# Plot using Seaborn
fig, ax = plt.subplots()
sb.barplot(x='Subsidiary', y='Sales', data=filtered_data, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
