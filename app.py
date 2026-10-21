
import streamlit as st
import pandas as pd
import joblib

# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="ChurnIQ | Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

THRESHOLD = 0.20


# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
    .stApp {
        background-color: #0b1120;
        color: #e5e7eb;
    }

    [data-testid="stSidebar"] {
        background-color: #111a2e;
    }

    h1, h2, h3 {
        color: #f1f5f9 !important;
    }

    p, label {
        color: #bac7dc;
    }

    [data-testid="stMetric"] {
        background: #151f33;
        border: 1px solid #2a3853;
        padding: 20px;
        border-radius: 14px;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #6d5dfc, #4387f5);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 13px;
        font-weight: 600;
        width: 100%;
    }

    div.stButton > button:hover {
        border: 1px solid #9b91ff;
        color: white;
    }

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #151f33;
        border-color: #35435d;
        border-radius: 8px;
    }

    .hero {
        padding: 30px;
        background: linear-gradient(120deg, #182447, #17213a);
        border: 1px solid #2b3a5b;
        border-radius: 18px;
        margin-bottom: 25px;
    }

    .hero-label {
        color: #a69cff;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
    }

    .hero-subtitle {
        color: #bac7dc;
        font-size: 15px;
        line-height: 1.7;
    }

    .section-card {
        background: #111a2e;
        border: 1px solid #263550;
        border-radius: 14px;
        padding: 18px;
    }

    .footer {
        text-align: center;
        color: #8190a9;
        font-size: 12px;
        padding: 25px 0 10px 0;
    }

    hr {
        border-color: #263550;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD TRAINED MODEL
# =====================================================
@st.cache_resource
def load_model():
    return joblib.load("churn_model.pkl")


try:
    model = load_model()
except Exception as e:
    st.error(
        "Could not load the trained model. "
        "Ensure churn_model.pkl is in the same folder as app.py."
    )
    st.stop()


# =====================================================
# SIDEBAR BRANDING
# =====================================================
with st.sidebar:
    st.markdown("# 📊 ChurnIQ")
    st.caption("TELECOM CUSTOMER ANALYTICS")
    st.divider()

    st.markdown("### Customer Retention")
    st.write(
        "Identify customers who may leave your telecom service "
        "and help prioritize retention efforts."
    )

# =====================================================
# MAIN HEADER
# =====================================================
st.markdown("""
<div class="hero">
    <div class="hero-label">CUSTOMER RETENTION INTELLIGENCE</div>
    <h1 style="margin: 12px 0;">
        Telecom Customer Churn Prediction
    </h1>
    <div class="hero-subtitle">
        Enter customer information to estimate churn probability
        and identify customers who may need retention attention.
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# CUSTOMER PROFILE
# =====================================================
st.markdown("## 👤 Customer Profile")
st.caption("Enter personal details, subscription information, and billing data.")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    partner = st.selectbox("Has Partner?", ["Yes", "No"])
    dependents = st.selectbox("Has Dependents?", ["Yes", "No"])

with col2:
    tenure = st.slider("Tenure (months)", 0, 72, 12)

    phone_service = st.selectbox("Phone Service", ["Yes", "No"])

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

with col3:
    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


# =====================================================
# INTERNET AND SERVICES
# =====================================================
st.divider()
st.markdown("## 🌐 Internet & Services")
st.caption("Select the services included in the customer's plan.")

col1, col2, col3 = st.columns(3)

with col1:
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

with col2:
    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

with col3:
    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )


# =====================================================
# BILLING INFORMATION
# =====================================================
st.divider()
st.markdown("## 💳 Billing Information")

col1, col2 = st.columns(2)

with col1:
    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0,
        max_value=10000.0,
        value=70.0,
        step=1.0
    )

with col2:
    total_charges = st.number_input(
        "Total Charges ($)",
        min_value=0.0,
        max_value=100000.0,
        value=float(monthly_charges * tenure),
        step=10.0
    )


# =====================================================
# PREDICTION
# =====================================================
st.markdown("")
predict_button = st.button(
    "✨ Analyze Customer Churn Risk",
    use_container_width=True
)

if predict_button:

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    probability = float(model.predict_proba(customer)[0, 1])
    at_risk = probability >= THRESHOLD

    st.divider()
    st.markdown("## 🔍 Prediction Results")

    result_col1, result_col2 = st.columns([1, 1])

    with result_col1:
        st.metric(
            label="Estimated Churn Probability",
            value=f"{probability:.1%}"
        )

        st.progress(probability)

        st.caption(
            "Estimated probability that the customer will churn."
        )

    with result_col2:
        if at_risk:
            st.error("⚠️ Customer flagged as potentially at risk")

            st.write(
                "The predicted probability meets or exceeds the "
                "selected threshold. Consider reviewing this customer "
                "for an appropriate retention offer."
            )
        else:
            st.success("✅ Customer not flagged as at risk")

            st.write(
                "The predicted probability is below the selected "
                "threshold. This does not guarantee that the customer "
                "will remain with the company."
            )

    st.markdown(
        f"""
        <div class="section-card">
            <b>How to interpret this result</b>
            <p>
                The model flags customers when their estimated churn
                probability is at least {THRESHOLD:.0%}.
                This lower threshold is intended to catch more potential
                churners, but it will also generate more false alarms.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<div class="footer">
    ChurnIQ · Machine Learning Customer Analytics<br>
    Predictions are estimates and should support, not replace,
    business judgment.
</div>
""", unsafe_allow_html=True)
