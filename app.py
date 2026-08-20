import streamlit as st

st.set_page_config(
    page_title="Sustainable Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
.main-title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    margin-top: 20px;
}

.subtitle {
    font-size: 20px;
    text-align: center;
    color: #666;
    margin-bottom: 40px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    background-color: #f5f9f3;
    border: 1px solid #dcebd8;
    margin-bottom: 20px;
}

.section-title {
    font-size: 30px;
    font-weight: 600;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #777;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown(
    '<div class="main-title">🌱 Sustainable Fertilizer Optimizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart fertilizer recommendations for efficient, economical, and sustainable farming.</div>',
    unsafe_allow_html=True
)


# ---------- HOME INFORMATION ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🌾 Crop Based</h3>
        <p>Choose your crop and receive fertilizer recommendations based on nutrient requirements.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🧪 Soil Analysis</h3>
        <p>Enter Nitrogen, Phosphorus and Potassium values to estimate nutrient requirements.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🌍 Sustainable</h3>
        <p>Use fertilizer more efficiently and avoid unnecessary nutrient application.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown(
    '<div class="section-title">🚀 Fertilizer Recommendation</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter your soil nutrient values below to calculate the recommended "
    "amount of Urea, DAP and MOP."
)


# ---------- INPUTS ----------
col1, col2 = st.columns(2)

with col1:
    crop = st.selectbox(
        "🌾 Select Crop",
        ["Rice", "Wheat", "Maize", "Cotton", "Tomato"]
    )

with col2:
    st.info(f"Selected crop: **{crop}**")


col1, col2, col3 = st.columns(3)

with col1:
    soil_n = st.number_input(
        "Soil Nitrogen (N)",
        min_value=0.0,
        value=40.0
    )

with col2:
    soil_p = st.number_input(
        "Soil Phosphorus (P)",
        min_value=0.0,
        value=25.0
    )

with col3:
    soil_k = st.number_input(
        "Soil Potassium (K)",
        min_value=0.0,
        value=35.0
    )


# ---------- CALCULATION ----------
if st.button("🌱 Optimize Fertilizer", use_container_width=True):

    n_required = max(100 - soil_n, 0)
    p_required = max(50 - soil_p, 0)
    k_required = max(80 - soil_k, 0)

    urea = round(n_required / 0.46, 2)
    dap = round(p_required / 0.46, 2)
    mop = round(k_required / 0.60, 2)

    st.success("Fertilizer recommendation generated successfully!")

    st.markdown("### 📊 Recommended Fertilizer")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Urea", f"{urea} kg")

    with col2:
        st.metric("DAP", f"{dap} kg")

    with col3:
        st.metric("MOP", f"{mop} kg")


# ---------- FOOTER ----------
st.markdown(
    '<div class="footer">🌱 Sustainable Fertilizer Optimizer | Smart Farming Solution</div>',
    unsafe_allow_html=True
)
