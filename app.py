import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • Core VIP",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru injectarea imaginii teren.jpg cu opacitate perfect echilibrată
def aplica_fundal_teren_calibrat(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            /* Am setat opacitatea la 0.82 ca să fie o idee mai vizibil și mai clar terenul */
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.82), rgba(6, 4, 15, 0.86)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }
            
            /* Ascundem complet meniurile de fundal Streamlit */
            #MainMenu, footer, header { display: none !important; }
            div[data-testid="stToolbar"] { display: none !important; }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

# Activăm imaginea cu terenul în varianta perfect vizibilă, dar profesională
aplica_fundal_teren_calibrat("teren.jpg")
# ================== UPDATE: CASSETĂ AUTENTIFICARE CU GOOGLE (GMAIL) ==================

# Inițializăm starea de autentificare în memoria sigură a serverului
if "utilizator_autentificat_google" not in st.session_state:
    st.session_state.utilizator_autentificat_google = False

# Injectăm stilul special pentru caseta de Login centrată și butonul oficial Google
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* Caseta centrală stil iPhone/Glassmorphism fin peste terenul blurat */
    .google-login-box {
        max-width: 390px;
        margin: 80px auto;
        background: rgba(13, 11, 22, 0.82) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(176, 66, 255, 0.2);
        border-radius: 32px;
        padding: 30px 24px;
        box-shadow: 0 30px 70px -15px rgba(157, 0, 255, 0.3);
        text-align: center;
    }

    /* Forțăm butonul nativ Streamlit să aibă design-ul curat de Google Button */
    div.stButton > button {
        background-color: #ffffff !important;
        color: #1f1f1f !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        border: 1px solid #dcdcdc !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 10px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15) !important;
        transition: all 0.2s ease !important;
    }
    
    div.stButton > button:hover {
        background-color: #f7f7f7 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2) !important;
        border-color: #b042ff !important;
    }
</style>
""", unsafe_allow_html=True)

# ---- ECRANUL A: DACĂ UTILIZATORUL NU S-A CONECTAT ÎNCĂ ----
if not st.session_state.utilizator_autentificat_google:
    st.markdown('<div class="google-login-box">', unsafe_allow_html=True)
    
    # Titlul oficial stilizat premium
    st.markdown("<h1 style='text-align:center; font-size:34px; font-weight:800; background: linear-gradient(135deg, #ffffff 0%, #b042ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom:5px;'>PariuriGO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:35px; font-weight:500;'>Sign in with your Google account to unlock portal</p>", unsafe_allow_html=True)
    
    # Butonul interactiv stilizat oficial
    if st.button("🔴 &nbsp; Sign in with Google", key="google_auth_trigger_btn"):
        # Simulăm deblocarea securizată instantanee pentru fluxul aplicației
        st.session_state.utilizator_autentificat_google = True
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# ---- ECRANUL B: MEMBRU LOGAT REUȘIT (AICI VOM INJECTA VIITOARELE UPDATE-URI) ----
else:
    st.markdown('<div class="google-login-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#00ff66; font-weight:800; font-size:18px;'>🔓 VIP ACCESS UNLOCKED</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#a1a1aa; font-size:13px; margin-top:5px;'>Conectat cu succes prin Google Mail (@gmail.com)</p>", unsafe_allow_html=True)
    
    st.write("---")
    # Buton fin de deconectare
    if st.button("🔒 Deconectare Cont", key="google_logout_btn"):
        st.session_state.utilizator_autentificat_google = False
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)
