import streamlit as st
from datetime import datetime

# 1. Configurare Pagină Full-Screen
st.set_page_config(
    page_title="PariuriGO • Portal",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# Injectăm stilurile profesionale OLED și Glassmorphism direct aici
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #030305 !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    h1, h2, h3, h4, p, span, label {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #ffffff !important;
    }

    /* TELEFON MOBIL CENTRAT STIL IPHONE */
    .phone-wrapper-container {
        max-width: 410px;
        margin: 40px auto;
        background: rgba(18, 18, 24, 0.8) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 40px;
        padding: 24px;
        box-shadow: 0 25px 50px -12px rgba(157, 0, 255, 0.2);
    }
    
    .phone-notch {
        width: 110px;
        height: 25px;
        background: #000000;
        margin: -12px auto 25px auto;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .stTextInput div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .stTextInput div[data-baseweb="input"]:focus-within {
        border-color: #a855f7 !important;
        box-shadow: 0 0 12px rgba(168, 85, 247, 0.2) !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
    }
    
    .stTextInput input {
        color: #ffffff !important;
        font-size: 15px !important;
        font-weight: 500 !important;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #a855f7 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        letter-spacing: 0.3px !important;
        border: none !important;
        width: 100% !important;
        border-radius: 14px !important;
        padding: 12px !important;
        box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4) !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 12px 25px -5px rgba(168, 85, 247, 0.5) !important;
    }

    .premium-sport-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .sport-left-section { display: flex; align-items: center; gap: 14px; }
    .sport-icon-box { background: rgba(255, 255, 255, 0.04); width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 20px; border: 1px solid rgba(255, 255, 255, 0.05); }
    .card-main-title { font-size: 16px; font-weight: 700; margin: 0; }
    .card-sub-desc { font-size: 12px; color: #8e8e93; margin: 2px 0 0 0; }
    .tag-active { background: rgba(52, 211, 153, 0.1); color: #34d399 !important; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
    .tag-upcoming { background: rgba(255, 255, 255, 0.03); color: #8e8e93 !important; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

if "utilizator_logat" not in st.session_state:
    st.session_state.utilizator_logat = False

# CONSTRUIM DESIGN-UL DE TELEFON
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

# ---- ECRANUL DE LOGIN PROFESIONAL ----
if not st.session_state.utilizator_logat:
    st.markdown("<h1 style='text-align:center; font-size:28px; font-weight:800; background: linear-gradient(135deg, #ffffff 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>PariuriGO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:25px; font-weight:500;'>Sign in to access the VIP prediction engine</p>", unsafe_allow_html=True)
    
    username = st.text_input("USER IDENTITY", placeholder="Enter your membership username...", key="input_user")
    password = st.text_input("SECURE KEY", type="password", placeholder="Enter your password...", key="input_pass")
    
    st.write("")
    
    if st.button("SIGN IN TO PREMIUM ACCOUNT", use_container_width=True):
        if username == "admin" and password == "pariurigo":
            st.session_state.utilizator_logat = True
            st.success("Access Granted!")
            st.rerun()
        else:
            st.error("Access Denied! Check your credentials.")
            
    st.markdown('</div>', unsafe_allow_html=True)
