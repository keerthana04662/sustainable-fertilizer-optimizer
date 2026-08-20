import streamlit as st

st.set_page_config(
    page_title="Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Fertilizer Optimizer")

st.write(
    "Enter your soil nutrient values to calculate "
    "the estimated fertilizer quantities."
)

# Crop selection
crop = st.selectbox(
    "🌾 Select Crop",
    ["Rice", "Wheat", "Maize", "Cotton", "Tomato"]
)

st.subheader("🧪 Soil Nutrient Values")

# Soil inputs
col1, col2, col3 = st.columns(3)

with col1:
    soil_n = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        value=40.0,
        step=1.0
    )

with col2:
    soil_p = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        value=25.0,
        step=1.0
    )

with col3:
    soil_k = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        value=35.0,
        step=1.0
    )

st.write("")

# Optimization
if st.button(
    "🌱 Generate Fertilizer Recommendation",
    use_container_width=True,
    type="primary"
):

    # Example nutrient requirements
    n_required = max(100 - soil_n, 0)
    p_required = max(50 - soil_p, 0)
    k_required = max(80 - soil_k, 0)

    # Fertilizer calculations
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
            "UREA",
            f"{urea} kg"
        )

    with col2:
        st.metric(
            "DAP",
            f"{dap} kg"
        )

    with col3:
        st.metric(
            "MOP",
            f"{mop} kg"
        )

    st.info(
        "This is an estimated project recommendation. "
        "Actual fertilizer application should be based on "
        "validated soil-test and crop-specific recommendations."
    )