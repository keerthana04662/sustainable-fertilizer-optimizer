import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.write(
    "The Sustainable Fertilizer Optimizer is a smart agriculture "
    "application that helps estimate fertilizer requirements using "
    "crop and soil nutrient information."
)

st.header("🎯 Objectives")

st.write("""
- Optimize fertilizer usage
- Analyze soil nutrient levels
- Support crop-specific recommendations
- Reduce unnecessary fertilizer application
- Promote sustainable agriculture
""")

st.header("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🐍 Python")

with col2:
    st.success("🎈 Streamlit")

with col3:
    st.success("📊 Data Analysis")

st.header("🌱 Project Vision")

st.write(
    "To provide a simple, user-friendly and data-driven platform "
    "for efficient and sustainable fertilizer management."
)

if st.button("🏠 Back to Home"):
    st.switch_page("app.py")
