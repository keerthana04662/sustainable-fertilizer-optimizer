import streamlit as st

st.set_page_config(
    page_title="Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Fertilizer Optimizer")

crop_requirements = {
    "Rice": {"N": 100, "P": 50, "K": 80},
    "Wheat": {"N": 120, "P": 60, "K": 70},
    "Maize": {"N": 150, "P": 60, "K": 80},
    "Cotton": {"N": 120, "P": 50, "K": 70},
    "Tomato": {"N": 110, "P": 50, "K": 90}
}

crop = st.selectbox(
    "🌾 Select Crop",
    list(crop_requirements.keys())
)

st.subheader("🧪 Enter Soil Nutrient Values")

col1, col2, col3 = st.columns(3)

with col1:
    soil_n = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        value=40.0
    )

with col2:
    soil_p = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        value=25.0
    )

with col3:
    soil_k = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        value=35.0
    )

if st.button(
    "🌱 Generate Fertilizer Recommendation",
    type="primary",
    use_container_width=True
):

    requirement = crop_requirements[crop]

    n_required = max(requirement["N"] - soil_n, 0)
    p_required = max(requirement["P"] - soil_p, 0)
    k_required = max(requirement["K"] - soil_k, 0)

    urea = round(n_required / 0.46, 2)
    dap = round(p_required / 0.46, 2)
    mop = round(k_required / 0.60, 2)

    st.success(
        f"Fertilizer recommendation generated for {crop}!"
    )

    st.subheader("📊 Recommended Fertilizer")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("UREA", f"{urea} kg/ha")

    with col2:
        st.metric("DAP", f"{dap} kg/ha")

    with col3:
        st.metric("MOP", f"{mop} kg/ha")

    st.info(
        "This is a simplified project calculation. "
        "Real fertilizer recommendations should use validated "
        "soil tests and agricultural guidelines."
    )

if st.button("🏠 Back to Home"):
    st.switch_page("app.py")