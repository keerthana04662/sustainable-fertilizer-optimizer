import streamlit as st

st.set_page_config(
    page_title="Sustainable Fertilizer Optimizer",
    page_icon="🌱",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F7F2;
    }

    h1, h2, h3 {
        color: #123524 !important;
    }

    p, label {
        color: #263238 !important;
    }

    .hero {
        background-color: #DDEFD8;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #9BCB95;
    }

    .hero h1 {
        color: #14532D !important;
        font-size: 40px;
    }

    .hero p {
        color: #263238 !important;
        font-size: 19px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #B7D3B3;
        min-height: 150px;
    }

    .card h3 {
        color: #14532D !important;
    }

    .card p {
        color: #263238 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h1>🌱 Sustainable Fertilizer Optimizer</h1>
        <p>
        Smart fertilizer recommendations for efficient,
        economical and sustainable farming.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.header("🌾 Smart Agriculture Platform")

st.write(
    "This application helps farmers understand soil nutrient "
    "levels and estimate fertilizer requirements."
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>🌾 Crop Analysis</h3>
            <p>
            Select a crop and understand its fertilizer
            requirements.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>🧪 Soil Analysis</h3>
            <p>
            Analyze Nitrogen, Phosphorus and Potassium
            levels in your soil.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>🌱 Fertilizer Optimizer</h3>
            <p>
            Calculate recommended Urea, DAP and MOP
            quantities.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

st.header("⚙️ How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1️⃣ Enter Soil Data")
    st.write(
        "Provide your Nitrogen, Phosphorus and Potassium values."
    )

with col2:
    st.subheader("2️⃣ Select Crop")
    st.write(
        "Choose the crop you want to cultivate."
    )

with col3:
    st.subheader("3️⃣ Get Recommendation")
    st.write(
        "Receive an estimated fertilizer recommendation."
    )

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <b>🌱 Sustainable Fertilizer Optimizer</b>
        <br><br>
        Smart Farming • Efficient Fertilization • Sustainable Agriculture
    </div>
    """,
    unsafe_allow_html=True
)