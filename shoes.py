import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
df = pd.read_csv("SHOES.csv")

# Clean and convert columns to numeric
for col in ['Sales', 'Returns', 'Inventory']:
    df[col] = df[col].replace('[$,]', '', regex=True).astype('int64')

# App title
st.title("Region Sales Estimator ")

# Region selection
regions = df['Region'].unique()
selected_region = st.selectbox("Select a Region", regions)

# Filter data for the selected region
filtered_data = df[df['Region'] == selected_region]

# Create bar plot
fig, ax = plt.subplots()
sb.barplot(x='Subsidiary', y='Sales', data=filtered_data, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
