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
