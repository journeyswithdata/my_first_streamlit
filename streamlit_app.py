import streamlit as st
import pandas as pd

# Load your cross-reference dataset (filter or full version)
@st.cache_data
def load_data():
    df = pd.read_csv("toid_uprn_address.csv")  # Full dataset path
    return df

data = load_data()

st.title("TOID to Address Lookup Tool")

# Single TOID search
toid_input = st.text_input("Enter TOID to search:")

if toid_input:
    result = data[data['TOID'] == toid_input]
    if not result.empty:
        st.write(result)
    else:
        st.warning("TOID not found.")

# Optional: Batch Lookup
st.write("---")
st.subheader("Batch TOID Lookup")

uploaded_file = st.file_uploader("Upload CSV with TOIDs", type="csv")

if uploaded_file:
    toid_list = pd.read_csv(uploaded_file)
    if 'TOID' in toid_list.columns:
        merged = toid_list.merge(data, on='TOID', how='left')
        st.write(merged)
        st.download_button("Download Results as CSV", merged.to_csv(index=False), "results.csv")
    else:
        st.error("CSV must have a 'TOID' column.")