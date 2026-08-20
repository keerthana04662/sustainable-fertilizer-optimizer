import streamlit as st

st.set_page_config(
    page_title="Fertilizer Optimizer",
    page_icon="🌱"
)

st.title("🌱 Fertilizer Optimizer")

st.write(
    "Calculate the estimated Urea, DAP and MOP "
    "requirements based on your soil values."
)

crop_data = {
    "Rice": {"N": 100, "P": 50, "K": 80},
    "Wheat": {"N": 120, "P": 60, "K": 70},
    "Maize": {"N": 150, "P": 60, "K": 80},
    "Cotton": {"N": 120, "P": 50, "K": 70},
    "Tomato": {"N": 110, "P": 50, "K": 90}
}

st.subheader("🌾 Select Crop")

crop = st.selectbox(
    "Crop",
    list(crop_data.keys())
)

st.subheader("🧪 Enter Soil Values")

soil_n = st.number_input(
    "Soil Nitrogen (N)",
    min_value=0.0,
    value=40.0
)

soil_p = st.number_input(
    "Soil Phosphorus (P)",
    min_value=0.0,
    value=25.0
)

soil_k = st.number_input(
    "Soil Potassium (K)",
    min_value=0.0,
    value=35.0
)

if st.button(
    "🌱 Generate Fertilizer Recommendation",
    type="primary"
):

    required_n = crop_data[crop]["N"]
    required_p = crop_data[crop]["P"]
    required_k = crop_data[crop]["K"]

    n_required = max(required_n - soil_n, 0)
    p_required = max(required_p - soil_p, 0)
    k_required = max(required_k - soil_k, 0)

    urea = round(n_required / 0.46, 2)
    dap = round(p_required / 0.46, 2)
    mop = round(k_required / 0.60, 2)

    st.success(
        f"Fertilizer recommendation generated for {crop}!"
    )

    st.subheader("📊 Recommended Fertilizer")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Urea",
            f"{urea} kg/ha"
        )

    with col2:
        st.metric(
            "DAP",
            f"{dap} kg/ha"
        )

    with col3:
        st.metric(
            "MOP",
            f"{mop} kg/ha"
        )

    st.info(
        "This is an estimated project calculation. "
        "Actual fertilizer recommendations should be "
        "based on validated soil testing and agricultural guidelines."
    )