import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# Load dataset
df = pd.read_csv("SHOES.csv")

# Clean and convert numeric columns safely
for col in ['Sales', 'Returns', 'Inventory']:
    if col in df.columns:
        df[col] = df[col].replace('[$,]', '', regex=True).astype('int64')

# App title
st.title("Shoes Sales Analysis Dashboard")

# --- Theme Toggle ---
theme = st.radio("Select Theme", ["Light Mode", "Dark Mode"])

# Set plot style
if theme == "Dark Mode":
    plt.style.use("dark_background")
else:
    plt.style.use("default")

# --- Region Selection ---
if "Region" in df.columns:
    regions = df['Region'].dropna().unique()
    selected_region = st.selectbox("Select a Region", regions)
else:
    selected_region = None

# --- Area Selection ---
if "Area" in df.columns:
    if selected_region:
        areas = df[df['Region'] == selected_region]['Area'].dropna().unique()
    else:
        areas = df['Area'].dropna().unique()
    selected_area = st.selectbox("Select an Area", areas)
else:
    selected_area = None

# --- Brand Selection ---
if "Brand" in df.columns:
    if selected_region and selected_area:
        brands = df[(df['Region'] == selected_region) & (df['Area'] == selected_area)]['Brand'].dropna().unique()
    elif selected_region:
        brands = df[df['Region'] == selected_region]['Brand'].dropna().unique()
    else:
        brands = df['Brand'].dropna().unique()
    selected_brand = st.selectbox("Select a Brand", brands)
else:
    selected_brand = None

# --- Filter Data ---
filtered_data = df.copy()
if selected_region:
    filtered_data = filtered_data[filtered_data['Region'] == selected_region]
if selected_area:
    filtered_data = filtered_data[filtered_data['Area'] == selected_area]
if selected_brand:
    filtered_data = filtered_data[filtered_data['Brand'] == selected_brand]

# --- Visualization ---
if not filtered_data.empty:
    fig, ax = plt.subplots()
    sb.barplot(x='Subsidiary', y='Sales', data=filtered_data, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)
else:
    st.warning("No data available for this selection.")
