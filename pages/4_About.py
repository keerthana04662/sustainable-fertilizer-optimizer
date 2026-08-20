import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.write(
    "Sustainable Fertilizer Optimizer is a smart agriculture "
    "application designed to support efficient fertilizer management "
    "using soil nutrient information."
)

st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.success("🌱 Optimize fertilizer usage")
    st.success("🧪 Analyze soil nutrient levels")
    st.success("🌾 Support crop-specific recommendations")

with col2:
    st.success("🌍 Promote sustainable agriculture")
    st.success("💰 Reduce unnecessary fertilizer usage")
    st.success("📊 Support data-driven farming")

st.header("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🐍 Python")

with col2:
    st.info("🎈 Streamlit")

with col3:
    st.info("📊 Data Analysis")

st.header("🚀 Future Improvements")

st.write("""
- Crop-specific fertilizer recommendations
- Fertilizer cost optimization
- Soil nutrient visualization
- NPK charts
- Sustainability score
- Dataset-based prediction
- Farmer-friendly recommendations
""")

st.header("🌱 Project Vision")

st.write(
    "To develop a simple and intelligent platform that helps "
    "farmers use fertilizers efficiently while supporting "
    "sustainable agricultural practices."
)