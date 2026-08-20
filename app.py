import streamlit as st

st.set_page_config(
    page_title="Sustainable Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# STYLE
# -----------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F7F9F5;
}

h1, h2, h3 {
    color: #123524 !important;
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
    padding: 45px;
    border-radius: 20px;
    text-align: center;
    border: 2px solid #9CCC9C;
}

.hero-title {
    color: #123524 !important;
    font-size: 42px;
    font-weight: 800;
}

.hero-text {
    color: #263238 !important;
    font-size: 19px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    border: 2px solid #C8DCC5;
    min-height: 160px;
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

st.sidebar.write(
    "Use the pages below to analyze crops, "
    "soil and fertilizer requirements."
)


# -----------------------------
# HOME
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
    "This application helps farmers understand soil "
    "nutrient levels and estimate fertilizer requirements."
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