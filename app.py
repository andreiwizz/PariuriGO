import streamlit as st
import base64
from datetime import datetime
from baza import aplica_stiluri_landing_premium, date_fotbal_real, date_cs2_real

st.set_page_config(
    page_title="PariuriGO • World Sports Community",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")
aplica_stiluri_landing_premium()

# Inițializăm starea paginii din interiorul telefonului
if "pagina_curenta" not in st.session_state:
    st.session_state.pagina_curenta = "meniu_principal"

def incarc_logo_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

logo_base64 = incarc_logo_local("logo.png")

# HERO TITLE SECTION
st.markdown("""
<div class="hero-title-container">
    <h1 style="font-size: 38px; font-weight: 800; letter-spacing: 1px; margin-bottom: 5px; text-align: center;">
        PariuriGO s-a mutat acum în aplicație!
    </h1>
    <p style="font-size: 17px; color: #a0aec0; font-weight: 600; margin-top: 0; text-align: center;">
        Alege sportul preferat pentru statistici și filtre avansate de predictivitate.
    </p>
</div>
""", unsafe_allow_html=True)

# MOCKUP CENTRAL INTERACTIV
st.markdown('<div class="mockup-wrapper">', unsafe_allow_html=True)
col_mock1, col_mock2, col_mock3 = st.columns([1, 1.3, 1])

with col_mock2:
    st.markdown("""
    <div style="background: #09090d; border: 4px solid #1c123c; border-radius: 32px; padding: 20px; box-shadow: 0 0 40px rgba(176,66,255,0.25); min-height: 480px;">
        <div style="width: 60px; height: 16px; background: #1c123c; margin: 0 auto 15px auto; border-radius: 10px;"></div>
    """, unsafe_allow_html=True)
    
    # ---- 1. ECRANUL PRINCIPAL: MENIUL CU TOATE SPORTURILE ----
    if st.session_state.pagina_curenta == "meniu_principal":
        st.markdown('<p style="color:#cbd5e1; font-size:13px; font-weight:700; margin-bottom:15px; opacity:0.8;">Alege sportul pentru statistici:</p>', unsafe_allow_html=True)
        
        # Folosim butoane native stilizate ca și carduri
        if st.button("⚽ FOTBAL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AVAILABLE", key="btn_fotbal"):
            st.session_state.pagina_curenta = "pag_fotbal"
            st.rerun()
            
        if st.button("🎮 COUNTER-STRIKE 2 (CS2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AVAILABLE", key="btn_cs2"):
            st.session_state.pagina_curenta = "pag_cs2"
            st.rerun()
            
        st.write("")
        st.markdown("""
        <div style="opacity: 0.4;">
            <div class="phone-row"><span class="phone-label">🏀 Baschet</span><span class="badge-soon">SOON</span></div>
            <div class="phone-row"><span class="phone-label">🏒 Hockey</span><span class="badge-soon">SOON</span></div>
            <div class="phone-row"><span class="phone-label">🎾 Tenis</span><span class="badge-soon">SOON</span></div>
        </div>
        """, unsafe_allow_html=True)
