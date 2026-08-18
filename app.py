import streamlit as st
import base64
from datetime import datetime
from baza import aplica_stiluri_champions, preia_baza_date

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(page_title="PariuriGO World Live Center", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")
data_azi = datetime.now().strftime("%d.%m.%Y")

def incarc_logo_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

logo_base64 = incarc_logo_local("logo.png")

# Aplicare stiluri de bază din fișierul baza.py
aplica_stiluri_champions()
meciuri_date = preia_baza_date()

# Injectare stil custom pentru noul meniu de login din sidebar (Stil TikTok Mov)
st.markdown("""
<style>
    div[data-testid="stSidebarUserContent"] { padding: 20px 15px !important; }
    .stTextInput div[data-baseweb="input"] {
        background-color: #000000 !important;
        border: 1px solid rgba(176, 66, 255, 0.4) !important;
        border-radius: 8px !important;
    }
    .stTextInput input { color: #ffffff !important; font-size: 16px !important; }
    div[data-testid="stSidebar"] button {
        background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        border: none !important;
        width: 100% !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800; text-shadow: 0 0 15px rgba(157, 0, 255, 0.4);'>🏆 PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")

if "lista_membri" not in st.session_state: st.session_state.lista_membri = {"admin": "pariurigo"}
if "vip" not in st.session_state: st.session_state.vip = False
if "admin" not in st.session_state: st.session_state.admin = False

# SIDEBAR MODERNIZAT COMPLET STIL TIKTOK MOV
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#b042ff; font-size:26px; margin-bottom:20px;'>🔐 LOGIN ACCES</h2>", unsafe_allow_html=True)
    
    if not st.session_state.vip:
        utilizator = st.text_input("👤 Utilizator", key="login_user")
        parola = st.text_input("🔑 Parolă", type="password", key="login_pass")
        if st.button("CONECTARE CONT VIP"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                if utilizator == "admin": st.session_state.admin = True
                st.success("Conectat cu succes!")
                st.rerun()
            else:
                st.error("Date incorecte!")
    else:
        st.markdown(f"<div style='text-align:center; background:rgba(0,255,102,0.1); border:1px solid #00ff66; padding:10px; border-radius:8px; margin-bottom:15px;'>🟢 Ești conectat ca profil VIP!</div>", unsafe_allow_html=True)
        if st.button("DECONECTARE PROFILE"):
            st.session_state.vip = False
            st.session_state.admin = False
            st.rerun()

if st.session_state.admin:
    st.write("---")
    st.header("🛠 ADMIN PANEL")
    nume = st.text_input("Nume membru nou")
    passw = st.text_input("Parolă membru nou")
    if st.button("➕ Adaugă membru"):
        if nume:
            st.session_state.lista_membri[nume] = passw
            st.success("Adăugat!")
            st.rerun()

col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")
