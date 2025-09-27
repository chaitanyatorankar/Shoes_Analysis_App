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
st.title("Region & Sector Sales Estimator")

# --- Region selection ---
regions = df['Region'].unique()
selected_region = st.selectbox("Select a Region", regions)

# --- Sector selection (dependent on region) ---
sectors = df[df['Region'] == selected_region]['Sector'].unique()
selected_sector = st.selectbox("Select a Sector", sectors)

# --- Filter data ---
filtered_data = df[(df['Region'] == selected_region) & (df['Sector'] == selected_sector)]

# --- Create bar plot ---
fig, ax = plt.subplots()
sb.barplot(x='Subsidiary', y='Sales', data=filtered_data, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
