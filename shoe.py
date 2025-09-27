import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("your_file.csv")

# Clean numeric columns
for col in ["Sales", "Inventory", "Returns"]:
    df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

# Sidebar filters
region = st.sidebar.selectbox("Select Region", ["All"] + df["Region"].unique().tolist())
product = st.sidebar.selectbox("Select Product", ["All"] + df["Product"].unique().tolist())

filtered_df = df.copy()
if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]
if product != "All":
    filtered_df = filtered_df[filtered_df["Product"] == product]

st.title("📊 Retail Sales Dashboard")

# Sales by Region
fig_region = px.bar(filtered_df, x="Region", y="Sales", color="Region", title="Sales by Region")
st.plotly_chart(fig_region)

# Sales vs Inventory
fig_inventory = px.scatter(filtered_df, x="Inventory", y="Sales", size="Stores", color="Product",
                           hover_name="Subsidiary", title="Sales vs Inventory")
st.plotly_chart(fig_inventory)

# Returns by Product
fig_returns = px.bar(filtered_df, x="Product", y="Returns", color="Product", title="Returns by Product")
st.plotly_chart(fig_returns)

# Show table
st.subheader("📋 Data Preview")
st.dataframe(filtered_df)
