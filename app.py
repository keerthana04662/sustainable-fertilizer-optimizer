import streamlit as st

st.set_page_config(
    page_title="Sustainable Fertilizer Optimizer",
    page_icon="🌱"
)

st.title("🌱 Sustainable Fertilizer Optimizer")

st.write("Enter your soil nutrient values to get a fertilizer recommendation.")

crop = st.selectbox(
    "Select Crop",
    ["Rice", "Wheat", "Maize", "Cotton", "Tomato"]
)

soil_n = st.number_input("Soil Nitrogen (N)", min_value=0.0, value=40.0)
soil_p = st.number_input("Soil Phosphorus (P)", min_value=0.0, value=25.0)
soil_k = st.number_input("Soil Potassium (K)", min_value=0.0, value=35.0)

if st.button("🌱 Optimize Fertilizer"):

    n_required = max(100 - soil_n, 0)
    p_required = max(50 - soil_p, 0)
    k_required = max(80 - soil_k, 0)

    urea = round(n_required / 0.46, 2)
    dap = round(p_required / 0.46, 2)
    mop = round(k_required / 0.60, 2)

    st.success("Fertilizer recommendation generated!")

    st.write("### Recommended Fertilizer")

    st.metric("Urea", f"{urea} kg")
    st.metric("DAP", f"{dap} kg")
    st.metric("MOP", f"{mop} kg")