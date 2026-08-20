import streamlit as st

st.set_page_config(
    page_title="Crop Analysis",
    page_icon="🌾"
)

st.title("🌾 Crop Analysis")

st.write(
    "Select a crop to view its recommended "
    "nutrient requirements."
)

crop_data = {
    "Rice": {
        "N": 100,
        "P": 50,
        "K": 80
    },
    "Wheat": {
        "N": 120,
        "P": 60,
        "K": 70
    },
    "Maize": {
        "N": 150,
        "P": 60,
        "K": 80
    },
    "Cotton": {
        "N": 120,
        "P": 50,
        "K": 70
    },
    "Tomato": {
        "N": 110,
        "P": 50,
        "K": 90
    }
}

crop = st.selectbox(
    "🌾 Select Crop",
    list(crop_data.keys())
)

values = crop_data[crop]

st.success(f"Selected crop: {crop}")

st.subheader("Recommended Nutrient Requirements")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Nitrogen (N)",
        f"{values['N']} kg/ha"
    )

with col2:
    st.metric(
        "Phosphorus (P)",
        f"{values['P']} kg/ha"
    )

with col3:
    st.metric(
        "Potassium (K)",
        f"{values['K']} kg/ha"
    )

st.info(
    "These values are simplified project values "
    "for demonstration."
)