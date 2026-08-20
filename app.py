import streamlit as st

st.set_page_config(
    page_title="Sustainable Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background-color: #F5F7F2;
}

h1, h2, h3, h4, p, label, span {
    color: #1F2933 !important;
}

.hero {
    background-color: #DDEFD8;
    padding: 45px;
    border-radius: 20px;
    text-align: center;
    border: 2px solid #9BCB95;
}

.hero h1 {
    color: #14532D !important;
}

.hero p {
    color: #1F2933 !important;
    font-size: 20px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #B7D3B3;
    min-height: 180px;
}

.card h3 {
    color: #14532D !important;
}

.card p {
    color: #1F2933 !important;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HOME PAGE
# -----------------------------

st.markdown("""
<div class="hero">
    <h1>🌱 Sustainable Fertilizer Optimizer</h1>
    <p>
        Smart fertilizer recommendations for efficient,
        economical and sustainable farming.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.header("🌾 Smart Agriculture Platform")

st.write(
    "This application helps farmers understand soil nutrient "
    "levels and estimate fertilizer requirements."
)

st.write("")

# -----------------------------
# FEATURE CARDS
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🌾 Crop Analysis</h3>
        <p>
        Select a crop and understand its fertilizer
        requirements.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Crop Analysis",
        use_container_width=True,
        key="crop"
    ):
        st.switch_page("pages/1_Crop_Analysis.py")


with col2:
    st.markdown("""
    <div class="card">
        <h3>🧪 Soil Analysis</h3>
        <p>
        Analyze Nitrogen, Phosphorus and Potassium
        levels in your soil.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Soil Analysis",
        use_container_width=True,
        key="soil"
    ):
        st.switch_page("pages/2_Soil_Analysis.py")


with col3:
    st.markdown("""
    <div class="card">
        <h3>🌱 Fertilizer Optimizer</h3>
        <p>
        Calculate recommended Urea, DAP and MOP
        quantities.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open Fertilizer Optimizer",
        use_container_width=True,
        key="optimizer"
    ):
        st.switch_page("pages/3_Fertilizer_Optimizer.py")


st.write("")
st.header("⚙️ How It Works")

step1, step2, step3 = st.columns(3)

with step1:
    st.subheader("1️⃣ Enter Soil Data")
    st.write("Provide your Nitrogen, Phosphorus and Potassium values.")

with step2:
    st.subheader("2️⃣ Select Crop")
    st.write("Choose the crop you want to cultivate.")

with step3:
    st.subheader("3️⃣ Get Recommendation")
    st.write("Receive an estimated fertilizer recommendation.")

st.divider()

st.markdown(
    "<center><b>🌱 Sustainable Fertilizer Optimizer</b><br>"
    "Smart Farming • Efficient Fertilization • Sustainable Agriculture"
    "</center>",
    unsafe_allow_html=True
)