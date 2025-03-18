import streamlit as st

# Streamlit UI
st.set_page_config(page_title="Fashion Explorer", layout="wide")
st.title("🛍️ Fashion Product Explorer")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "LocalFileStore", "Vectorstore", "UMAP Plot", "UMAP Plot Query"])


# Sidebar filters
st.sidebar.header("🎛️ Filters")
category = st.sidebar.selectbox("👗 Select Category", ["All", "Dresses", "Shoes", "Bags", "Accessories"])
price_range = st.sidebar.slider("💰 Price Range", 0, 500, (50, 200))
