import streamlit as st

st.set_page_config(
    page_title="Soil Analysis",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Soil Analysis")

st.write(
    "Enter your soil nutrient values to determine their current status."
)

# Soil inputs
col1, col2, col3 = st.columns(3)

with col1:
    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        value=40.0,
        step=1.0
    )

with col2:
    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        value=25.0,
        step=1.0
    )

with col3:
    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        value=35.0,
        step=1.0
    )

st.subheader("📊 Soil Nutrient Status")

col1, col2, col3 = st.columns(3)

with col1:
    if nitrogen < 50:
        st.error("Nitrogen: LOW")
    elif nitrogen < 100:
        st.warning("Nitrogen: MODERATE")
    else:
        st.success("Nitrogen: HIGH")

with col2:
    if phosphorus < 30:
        st.error("Phosphorus: LOW")
    elif phosphorus < 50:
        st.warning("Phosphorus: MODERATE")
    else:
        st.success("Phosphorus: HIGH")

with col3:
    if potassium < 40:
        st.error("Potassium: LOW")
    elif potassium < 80:
        st.warning("Potassium: MODERATE")
    else:
        st.success("Potassium: HIGH")

st.info(
    "Note: These thresholds are simplified project values. "
    "For real agricultural decisions, use soil-test interpretation "
    "standards appropriate to the crop and region."
)