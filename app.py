
import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="NSE Strategy Dashboard", layout="wide")
st.title("📈 First Million Fintech – Options Strategy Dashboard")

# Load data
try:
    df = pd.read_csv("data/sample_mock_data.csv")
except FileNotFoundError:
    st.error("❌ Could not find sample_mock_data.csv in /data folder.")
    st.stop()

# Confirm data is loading
st.success(f"✅ Loaded data with {len(df)} rows.")
st.dataframe(df.head(50), use_container_width=True)
