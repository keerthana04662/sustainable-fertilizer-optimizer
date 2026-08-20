import streamlit as st

st.set_page_config(
    page_title="Sustainable Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# GLOBAL CSS
# -----------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    color: #17202A !important;
}

.stApp {
    background-color: #F7F9F5;
}

h1 {
    color: #123524 !important;
    font-weight: 800 !important;
}

h2 {
    color: #174A2C !important;
    font-weight: 700 !important;
}

h3 {
    color: #1B5E20 !important;
    font-weight: 700 !important;
}

p {
    color: #263238 !important;
}

label {
    color: #17202A !important;
    font-weight: 600 !important;
}

.hero {
    background-color: #DCEFD9;
    padding: 50px;
    border-radius: 20px;
    text-align: center;
    border: 2px solid #9CCC9C;
}

.hero-title {
    color: #123524 !important;
    font-size: 45px;
    font-weight: 800;
}

.hero-text {
    color: #263238 !important;
    font-size: 20px;
}

.card {
    background-color: #FFFFFF;
    padding: 25px;
    border-radius: 16px;
    border: 2px solid #C8DCC5;
    min-height: 180px;
}

.card-title {
    color: #145A32 !important;
    font-size: 22px;
    font-weight: 800;
}

.card-text {
    color: #263238 !important;
    font-size: 16px;
}

.footer {
    color: #37474F !important;
    text-align: center;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("🌱 Sustainable Farm")

st.sidebar.markdown(
    "### Navigation"
)

st.sidebar.info(
    "Use the pages on the left to analyze soil "
    "and calculate fertilizer requirements."
)


# -----------------------------
# HOME PAGE
# -----------------------------

st.markdown("""
<div class="hero">

<div class="hero-title">
🌱 Sustainable Fertilizer Optimizer
</div>

<br>

<div class="hero-text">
Smart fertilizer recommendations for efficient,
economical and sustainable farming.
</div>

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

    <div class="card-title">
    🌾 Crop Analysis
    </div>

    <br>

    <div class="card-text">
    Select a crop and understand its fertilizer
    requirements.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/1_Crop_Analysis.py",
        label="Open Crop Analysis →"
    )


with col2:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🧪 Soil Analysis
    </div>

    <br>

    <div class="card-text">
    Analyze Nitrogen, Phosphorus and Potassium
    levels in your soil.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/2_Soil_Analysis.py",
        label="Open Soil Analysis →"
    )


with col3:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🌱 Fertilizer Optimizer
    </div>

    <br>

    <div class="card-text">
    Calculate recommended Urea, DAP and MOP
    quantities.
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/3_Fertilizer_Optimizer.py",
        label="Open Optimizer →"
    )


# -----------------------------
# HOW IT WORKS
# -----------------------------

st.write("")
st.header("⚙️ How It Works")

step1, step2, step3 = st.columns(3)

with step1:
    st.subheader("1️⃣ Enter Soil Data")
    st.write(
        "Provide your Nitrogen, Phosphorus and "
        "Potassium values."
    )

with step2:
    st.subheader("2️⃣ Select Crop")
    st.write(
        "Choose the crop you want to cultivate."
    )

with step3:
    st.subheader("3️⃣ Get Recommendation")
    st.write(
        "Receive an estimated fertilizer recommendation."
    )


# -----------------------------
# FOOTER
# -----------------------------

st.markdown("""
<div class="footer">

🌱 Sustainable Fertilizer Optimizer

<br><br>

Smart Farming • Efficient Fertilization • Sustainable Agriculture

</div>
""", unsafe_allow_html=True)