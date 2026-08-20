import streamlit as st
from datetime import datetime
from baza import aplica_stiluri_elita_login, aplica_stiluri_aplicatie_elita

# 1. Configurare Pagină Full-Screen
st.set_page_config(
    page_title="PariuriGO • Portal",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# Activăm stilurile din baza.py
aplica_stiluri_aplicatie_elita()

# Memoria nativă a contului (Fără cookies nesigure)
if "utilizator_logat" not in st.session_state:
    st.session_state.utilizator_logat = False
if "ecran_activ" not in st.session_state:
    st.session_state.ecran_activ = "meniu_sporturi"

# CONSTRUIM DESIGN-UL DE TELEFON PE ECRAN
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
            
    st.markdown('</div>', unsafe_allow_html=True) # Închide caseta de login în modul securizat
# ---- ECRANUL DEBLOCAT (MENIUL PRINCIPAL DE SPORTURI DIN APLICAȚIE) ----
else:
    st.markdown('<p style="color:#a855f7; font-size:13px; font-weight:800; margin-bottom:15px; text-transform:uppercase; letter-spacing:0.5px; text-align:center;">🔥 PREDICTION ENGINES ACTIVATED</p>', unsafe_allow_html=True)
    
    # Meniul de control discret integrat în interfață
    optiune = st.selectbox(
        "⚡ SELECTEAZĂ PORTALUL:", 
        ["Alege un sport activ...", "⚽ FOTBAL", "🎮 COUNTER-STRIKE 2 (CS2)"],
        key="sel_sport_premium_v3"
    )
    
    if optiune == "⚽ FOTBAL":
        st.session_state.ecran_activ = "modul_fotbal"
    elif optiune == "🎮 COUNTER-STRIKE 2 (CS2)":
        st.session_state.ecran_activ = "modul_cs2"

    st.write("")
    
    # 1. FOTBAL AVAILABLE
    st.markdown("""
    <div class="premium-sport-card">
        <div class="sport-left-section">
            <div class="sport-icon-box">⚽</div>
            <div>
                <div class="card-main-title">Fotbal</div>
                <div class="card-sub-desc">Goals Predictor & Half-Time Analytics</div>
            </div>
        </div>
        <span class="tag-active">AVAILABLE</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. CS2 AVAILABLE
    st.markdown("""
    <div class="premium-sport-card" style="border-color: rgba(168, 85, 247, 0.25);">
        <div class="sport-left-section">
            <div class="sport-icon-box" style="color:#a855f7;">🎮</div>
            <div>
                <div class="card-main-title" style="color:#a855f7;">CS2 Esports</div>
                <div class="card-sub-desc">Pistol Rounds & Map Performance Data</div>
            </div>
        </div>
        <span class="tag-active" style="background:rgba(168,85,247,0.1); color:#a855f7 !important; border:1px solid #a855f7;">AVAILABLE</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 3. BASCHET SOON
    st.markdown("""
    <div class="premium-sport-card" style="opacity:0.4;">
        <div class="sport-left-section">
            <div class="sport-icon-box">🏀</div>
            <div>
                <div class="card-main-title">Baschet</div>
                <div class="card-sub-desc">NBA Lineups & Player Performance</div>
            </div>
        </div>
        <span class="tag-upcoming">SOON</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 4. HOCHEY SOON
    st.markdown("""
    <div class="premium-sport-card" style="opacity:0.4;">
        <div class="sport-left-section">
            <div class="sport-icon-box">🏒</div>
            <div>
                <div class="card-main-title">Hockey</div>
                <div class="card-sub-desc">NHL System Predictions</div>
            </div>
        </div>
        <span class="tag-upcoming">SOON</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 5. TENIS SOON
    st.markdown("""
    <div class="premium-sport-card" style="opacity:0.4;">
        <div class="sport-left-section">
            <div class="sport-icon-box">🎾</div>
            <div>
                <div class="card-main-title">Tenis</div>
                <div class="card-sub-desc">Live Court Analytics</div>
            </div>
        </div>
        <span class="tag-upcoming">SOON</span>
    </div>
    """, unsafe_allow_html=True)

    # Buton mic și elegant în sidebar în caz că vrei să dai Log Out pe viitor
    with st.sidebar:
        if st.button("🔒 Sign Out / Lock Device", use_container_width=True):
            st.session_state.utilizator_logat = False
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Închide corect phone-wrapper-container
