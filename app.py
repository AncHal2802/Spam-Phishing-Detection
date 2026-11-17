import streamlit as st
from src.pipeline import analyze_message

# Page configuration
st.set_page_config(
    page_title="CyberSieve | Spam & Phishing Detector",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for a modern UI
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTextArea textarea {
        background-color: #1f2937;
        color: #f3f4f6;
        border-radius: 8px;
        border: 1px solid #374151;
    }
    .metric-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #374151;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar information
with st.sidebar:
    st.image("https://img.icons8.com/color/96/security-checked.png", width=80)
    st.title("CyberSieve AI")
    st.write("A robust two-stage machine learning framework designed to protect users from SMS spam and malicious phishing links.")
    st.markdown("---")
    st.markdown("### 🧠 Under the Hood")
    st.markdown("- **Stage 1:** Detect SPAM SMS")
    st.markdown("- **Stage 2:** Detect Phishing Links in Text")
    st.markdown("- **Accuracy:** ~94% (Spam) | ~97% (Phishing)")
    st.markdown("---")
    st.info("Tip: You can paste any suspicious SMS, promotional text, or email body.")

# Main Header
st.title("🛡️ Spam & Phishing Threat Detector")
st.markdown("Paste your suspicious text message or email content below to run a real-time AI security scan.")

# Input text area
msg = st.text_area("Message Content:", height=160, placeholder="Example: Congratulations! You have won a free iPhone. Click here to claim: http://bit.ly/fake-offer...")

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    analyze_btn = st.button("🔍 Scan Message", type="primary", use_container_width=True)

if analyze_btn:
    if msg.strip():
        with st.spinner("Analyzing text patterns and scanning web links..."):
            r = analyze_message(msg)
        
        st.markdown("---")
        st.subheader("📊 Threat Analysis Breakdown")
        
        # Metrics display
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.metric(label="Spam Probability", value=f"{r['spam_prob']:.1%}")
        with m_col2:
            max_url_prob = max((u['phishing_prob'] for u in r['urls']), default=0.0)
            st.metric(label="Max Phishing Link Risk", value=f"{max_url_prob:.1%}")
        
        # Link breakdown
        if r["urls"]:
            st.markdown("#### 🔗 Extracted URLs & Safety Scores:")
            for u in r["urls"]:
                risk_color = "🔴" if u['phishing_prob'] >= 0.5 else "🟢"
                st.markdown(f"- {risk_color} `{u['url']}` → Phishing Risk: **{u['phishing_prob']:.1%}**")
        else:
            st.info("ℹ️ No web URLs or domains detected in this message text.")
            
        # Final Verdict Box
        st.markdown("### 🛑 Security Verdict")
        verdict = r["verdict"]
        if "HIGH" in verdict:
            st.error(f"**{verdict}** — Do not click links or reply to this message!")
        elif "MEDIUM" in verdict:
            st.warning(f"**{verdict}** — Proceed with caution and verify the sender.")
        else:
            st.success(f"**{verdict}** — This message appears safe and legitimate.")
    else:
        st.warning("⚠️ Please enter some text content into the box before scanning.")