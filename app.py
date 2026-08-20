import streamlit as st

st.set_page_config(
    page_title="Sustainable Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.stApp {
    background-color: #F7FBF5;
}

.hero {
    background-color: #E8F5E9;
    padding: 45px 30px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 30px;
    border: 1px solid #C8E6C9;
}

.hero h1 {
    color: #1B5E20;
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    color: #455A64;
    font-size: 19px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #DDE8DC;
    min-height: 180px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
}

.card h3 {
    color: #2E7D32;
    font-size: 22px;
}

.card p {
    color: #455A64;
    font-size: 16px;
    line-height: 1.5;
}

.section {
    color: #1B5E20;
    font-size: 30px;
    font-weight: 700;
    margin-top: 35px;
}

.footer {
    text-align: center;
    color: #607D8B;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown("""
<div class="hero">

<h1>🌱 Sustainable Fertilizer Optimizer</h1>

<p>
Smart fertilizer recommendations for efficient,
economical, and sustainable farming.
</p>

</div>
""", unsafe_allow_html=True)


# ---------- FEATURES ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🌾 Crop Based</h3>
        <p>
        Select your crop and receive fertilizer recommendations
        based on its nutrient requirements.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🧪 Soil Analysis</h3>
        <p>
        Enter soil Nitrogen, Phosphorus and Potassium values
        to estimate the nutrient requirements.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🌍 Sustainable</h3>
        <p>
        Optimize fertilizer usage and reduce unnecessary
        fertilizer application.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------- CALCULATOR ----------
st.markdown(
    '<div class="section">🌱 Fertilizer Recommendation</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter your soil nutrient values below to calculate "
    "the recommended fertilizer quantity."
)


# ---------- INPUTS ----------
col1, col2 = st.columns(2)

with col1:
    crop = st.selectbox(
        "🌾 Select Crop",
        ["Rice", "Wheat", "Maize", "Cotton", "Tomato"]
    )

with col2:
    st.info(f"Selected crop: {crop}")


col1, col2, col3 = st.columns(3)

with col1:
    soil_n = st.number_input(
        "Soil Nitrogen (N)",
        min_value=0.0,
        value=40.0,
        step=1.0
    )

with col2:
    soil_p = st.number_input(
        "Soil Phosphorus (P)",
        min_value=0.0,
        value=25.0,
        step=1.0
    )

with col3:
    soil_k = st.number_input(
        "Soil Potassium (K)",
        min_value=0.0,
        value=35.0,
        step=1.0
    )


# ---------- BUTTON ----------
if st.button(
    "🌱 Optimize Fertilizer",
    use_container_width=True,
    type="primary"
):

    n_required = max(100 - soil_n, 0)
    p_required = max(50 - soil_p, 0)
    k_required = max(80 - soil_k, 0)

    urea = round(n_required / 0.46, 2)
    dap = round(p_required / 0.46, 2)
    mop = round(k_required / 0.60, 2)

    st.success(
        "Fertilizer recommendation generated successfully!"
    )

    st.markdown(
        '<div class="section">📊 Recommended Fertilizer</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Urea", f"{urea} kg")

    with col2:
        st.metric("DAP", f"{dap} kg")

    with col3:
        st.metric("MOP", f"{mop} kg")


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
🌱 Sustainable Fertilizer Optimizer
<br>
Smart Farming • Efficient Fertilization • Sustainable Agriculture
</div>
""", unsafe_allow_html=True)