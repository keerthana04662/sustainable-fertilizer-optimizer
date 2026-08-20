import streamlit as st

st.set_page_config(
    page_title="Soil Analysis",
    page_icon="🧪"
)

st.title("🧪 Soil Analysis")

st.write(
    "Enter your soil nutrient values to analyze "
    "Nitrogen, Phosphorus and Potassium levels."
)

st.subheader("🌱 Enter Soil Values")

nitrogen = st.number_input(
    "Soil Nitrogen (N)",
    min_value=0.0,
    value=40.0
)

phosphorus = st.number_input(
    "Soil Phosphorus (P)",
    min_value=0.0,
    value=25.0
)

potassium = st.number_input(
    "Soil Potassium (K)",
    min_value=0.0,
    value=35.0
)

if st.button(
    "🧪 Analyze Soil",
    type="primary"
):
    st.success("Soil analysis completed!")

    st.subheader("📊 Soil Analysis Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Nitrogen (N)",
            f"{nitrogen}"
        )

    with col2:
        st.metric(
            "Phosphorus (P)",
            f"{phosphorus}"
        )

    with col3:
        st.metric(
            "Potassium (K)",
            f"{potassium}"
        )

    st.write("### 🌱 Nutrient Status")

    if nitrogen < 50:
        st.warning("Nitrogen level: Low")
    else:
        st.success("Nitrogen level: Good")

    if phosphorus < 30:
        st.warning("Phosphorus level: Low")
    else:
        st.success("Phosphorus level: Good")

    if potassium < 40:
        st.warning("Potassium level: Low")
    else:
        st.success("Potassium level: Good")