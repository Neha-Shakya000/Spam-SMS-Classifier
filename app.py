
import streamlit as st
import joblib
from pathlib import Path

# Load saved model
BASE_DIR = Path(__file__).parent
model = joblib.load(BASE_DIR / "spam_model.pkl")
vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")

st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="💬",
    layout="centered"
)

# CSS styling
st.markdown("""
<style>
/* Page background and default text */
.stApp {
    background: linear-gradient(135deg, #f5f7ff, #fdf2f8);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 720px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Make text readable */
.stApp, .stApp p, .stApp label,
.stApp [data-testid="stCaptionContainer"] {
    color: #334155;
}

/* Heading */
.title {
    text-align: center;
    color: #312e81 !important;
    font-size: 36px;
    font-weight: 750;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    color: #64748b !important;
    font-size: 16px;
    margin-bottom: 30px;
}

/* Input label */
[data-testid="stTextArea"] label {
    color: #334155 !important;
    font-weight: 600;
    font-size: 16px;
}

/* Text area */
[data-testid="stTextArea"] textarea {
    background-color: #ffffff !important;
    color: #1e293b !important;
    -webkit-text-fill-color: #1e293b !important;
    border: 1px solid #c7d2fe !important;
    border-radius: 14px !important;
    padding: 14px !important;
    font-size: 16px !important;
}

[data-testid="stTextArea"] textarea:focus {
    border: 2px solid #6366f1 !important;
    box-shadow: 0 0 0 3px #6366f122 !important;
}

/* Buttons */
.stButton > button {
    min-height: 48px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    border-color: #6366f1;
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: #4f46e5 !important;
    color: white !important;
    border: 1px solid #4f46e5 !important;
}

/* Result cards */
.result {
    margin-top: 22px;
    padding: 22px 16px;
    border-radius: 14px;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
}

.spam {
    background: #fff1f2;
    color: #be123c !important;
    border: 1px solid #fda4af;
}

.ham {
    background: #ecfdf5;
    color: #047857 !important;
    border: 1px solid #6ee7b7;
}

.note {
    color: #64748b !important;
    text-align: center;
    font-size: 13px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)


# Heading
st.markdown(
    '<div class="title">💬 SMS Spam Detector</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">'
    'Check whether your message looks like spam.'
    '</div>',
    unsafe_allow_html=True
)


# Clear callback
def clear_message():
    st.session_state.sms_text = ""
    st.session_state.prediction = None


if "sms_text" not in st.session_state:
    st.session_state.sms_text = ""

if "prediction" not in st.session_state:
    st.session_state.prediction = None


# Message input
st.text_area(
    "Enter your message",
    key="sms_text",
    height=150,
    max_chars=5000,
    placeholder="Type or paste your message here..."
)

# Character counter
current_message = st.session_state.sms_text
st.caption(f"{len(current_message)} / 5000 characters")


# Action buttons
col1, col2 = st.columns(2)

with col1:
    check = st.button(
        "🔍 Check Message",
        type="primary",
        use_container_width=True
    )

with col2:
    st.button(
        "✕ Clear",
        on_click=clear_message,
        use_container_width=True
    )


# Prediction
if check:
    current_message = st.session_state.sms_text.strip()

    if not current_message:
        st.session_state.prediction = None
        st.warning("Please enter a message first.")
    else:
        transformed = vectorizer.transform([current_message])
        result = str(model.predict(transformed)[0]).strip().lower()
        st.session_state.prediction = result


# Display result
if st.session_state.prediction == "spam":
    st.markdown(
        '<div class="result spam">'
        '🚨 Spam Message Detected!'
        '</div>',
        unsafe_allow_html=True
    )

elif st.session_state.prediction == "ham":
    st.markdown(
        '<div class="result ham">'
        '✅ This looks like a normal message.'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="note">'
    'Predictions may not always be correct. Be careful with suspicious links.'
    '</div>',
    unsafe_allow_html=True
)



