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

# Injectăm stilurile profesionale OLED, Telefon Centrat și Glassmorphism direct aici
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

# Inițializăm stările de memorie
if "utilizator_logat" not in st.session_state:
    st.session_state.utilizator_logat = False
if "baza_date_utilizatori" not in st.session_state:
    st.session_state.baza_date_utilizatori = {"admin": "pariurigo", "andreiwizz": "Parola123parola"}
if "mod_ecran_autentificare" not in st.session_state:
    st.session_state.mod_ecran_autentificare = "login"

# CONSTRUIM CORPUL TELEFONULUI MOBIL CENTRAT PENTRU TOT SITE-UL
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

# ---- CAZUL A: UTILIZATORUL NU ESTE LOGAT ÎNCĂ ----
if not st.session_state.utilizator_logat:
    
    # ECRANUL DE LOGIN
    if st.session_state.mod_ecran_autentificare == "login":
        st.markdown("<h1 style='text-align:center; font-size:28px; font-weight:800; background: linear-gradient(135deg, #ffffff 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>PariuriGO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:25px; font-weight:500;'>Sign in to access your VIP prediction portal</p>", unsafe_allow_html=True)
        
        username = st.text_input("USER IDENTITY", placeholder="Enter username...", key="input_user_real")
        password = st.text_input("SECURE KEY", type="password", placeholder="Enter password...", key="input_pass_real")
        
        st.write("")
        
        if st.button("SIGN IN TO APP", use_container_width=True):
            if username in st.session_state.baza_date_utilizatori and st.session_state.baza_date_utilizatori[username] == password:
                st.session_state.utilizator_logat = True
                st.success("Access Granted!")
                st.rerun()
            else:
                st.error("Invalid Username or Password!")
                
        st.write("---")
        st.markdown("<p style='text-align:center; font-size:14px; color:#8e8e93; margin-bottom: 5px;'>New to PariuriGO?</p>", unsafe_allow_html=True)
        if st.button("CREATE NEW ACCOUNT 🚀", use_container_width=True):
            st.session_state.mod_ecran_autentificare = "register"
            st.rerun()

    # ECRANUL DE REGISTER (CREARE CONT)
    elif st.session_state.mod_ecran_autentificare == "register":
        st.markdown("<h1 style='text-align:center; font-size:26px; font-weight:800; color:#a855f7;'>Sign Up Center</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:25px;'>Create a permanent membership profile</p>", unsafe_allow_html=True)
        
        new_user = st.text_input("CHOOSE USERNAME", placeholder="Pick a unique profile name...", key="reg_user")
        new_pass = st.text_input("CHOOSE SECURE KEY", type="password", placeholder="Create a strong password...", key="reg_pass")
        confirm_pass = st.text_input("CONFIRM SECURE KEY", type="password", placeholder="Repeat your password...", key="reg_pass_conf")
        
        st.write("")
        
        if st.button("REGISTER PROFILE NOW", use_container_width=True):
            if not new_user or not new_pass:
                st.error("All input areas must be completed!")
            elif new_user in st.session_state.baza_date_utilizatori:
                st.error("This username identity is already taken!")
            elif new_pass != confirm_pass:
                st.error("Passwords do not match!")
            else:
                st.session_state.baza_date_utilizatori[new_user] = new_pass
                st.success("Account successfully created!")
                st.session_state.mod_ecran_autentificare = "login"
                st.rerun()
                
        st.write("---")
        if st.button("⬅️ BACK TO SIGN IN", use_container_width=True):
            st.session_state.mod_ecran_autentificare = "login"
            st.rerun()

# ---- CAZUL B: UTILIZATORUL ESTE LOGAT CU SUCCES (ECRANUL INTERIOR) ----
else:
    st.markdown('<p style="color:#a855f7; font-size:13px; font-weight:800; margin-bottom:15px; text-transform:uppercase; letter-spacing:0.5px; text-align:center;">🔥 PREDICTION ENGINES ACTIVATED</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="premium-sport-card">
        <div class="sport-left-section">
            <div class="sport-icon-box">⚽</div>
            <div>
                <div class="card-main-title">Fotbal Module</div>
                <div class="card-sub-desc">Live Predictions Engine</div>
            </div>
        </div>
        <span class="tag-active">AVAILABLE</span>
    </div>
    <div class="premium-sport-card" style="border-color: rgba(168, 85, 247, 0.25);">
        <div class="sport-left-section">
            <div class="sport-icon-box" style="color:#a855f7;">🎮</div>
            <div>
                <div class="card-main-title" style="color:#a855f7;">CS2 Esports</div>
                <div class="card-sub-desc">Map Analytics Data</div>
            </div>
        </div>
        <span class="tag-active" style="background:rgba(168,85,247,0.1); color:#a855f7 !important; border:1px solid #a855f7;">AVAILABLE</span>
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        if st.button("🔒 Lock Application / Sign Out", use_container_width=True):
            st.session_state.utilizator_logat = False
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Închide corect phone-wrapper-container
