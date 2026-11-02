import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Global Demographic Analyzer", page_icon="🌍", layout="wide")

st.title("🌍 Global State & Province Demographic Analyzer")
st.markdown("An analytical web application to explore, filter, and visualize state/province-level demographic indicators worldwide.")

# Simulated/Structured Global Demographic Dataset across key regions
@st.cache_data
def load_data():
    data = {
        "Country": ["USA", "USA", "USA", "Canada", "Canada", "India", "India", "Germany", "Germany", "Japan", "Japan", "Brazil", "Brazil"],
        "State_Province": ["California", "Texas", "New York", "Ontario", "Quebec", "Maharashtra", "Uttar Pradesh", "Bavaria", "North Rhine-Westphalia", "Tokyo", "Osaka", "São Paulo", "Rio de Janeiro"],
        "Population": [38940000, 30500000, 19570000, 15800000, 8500000, 126000000, 235000000, 13100000, 17900000, 14000000, 8800000, 45000000, 17200000],
        "Area_sq_km": [423970, 695662, 141300, 1076395, 1542056, 307713, 240928, 70550, 34110, 2191, 1905, 248222, 43750],
        "Urban_Population_Percent": [85.2, 84.7, 87.9, 86.0, 87.1, 45.2, 22.3, 77.5, 90.1, 91.5, 92.8, 96.0, 97.3],
        "Growth_Rate_Percent": [0.4, 1.3, -0.2, 0.9, 0.6, 1.1, 1.5, 0.3, 0.2, -0.5, -0.3, 0.8, 0.5]
    }
    df = pd.DataFrame(data)
    df["Population_Density"] = df["Population"] / df["Area_sq_km"]
    return df

df = load_data()

# Sidebar Controls
st.sidebar.header("🔍 Filter Options")
selected_countries = st.sidebar.multiselect("Select Countries", options=df["Country"].unique(), default=df["Country"].unique())

filtered_df = df[df["Country"].isin(selected_countries)]

# Main Dashboard layout
col1, col2, col3 = st.columns(3)
col1.metric("Total Population Analyzed", f"{filtered_df['Population'].sum():,}")
col2.metric("Average Growth Rate", f"{filtered_df['Growth_Rate_Percent'].mean():.2f}%")
col3.metric("Regions Tracked", len(filtered_df))

st.markdown("---")

# Data Table View
st.subheader("📋 Regional Demographic Breakdown")
st.dataframe(filtered_df, use_container_width=True)

# Visualizations
st.markdown("---")
st.subheader("📊 Comparative Visualizations")

tab1, tab2, tab3 = st.tabs(["Population by Region", "Population Density", "Urbanization Rate"])

with tab1:
    st.bar_chart(filtered_df.set_index("State_Province")["Population"])

with tab2:
    st.bar_chart(filtered_df.set_index("State_Province")["Population_Density"])

with tab3:
    st.bar_chart(filtered_df.set_index("State_Province")["Urban_Population_Percent"])
