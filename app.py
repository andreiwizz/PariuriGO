import streamlit as st
import base64
from datetime import datetime
from baza import aplica_stiluri_champions, preia_baza_date

# 1. Configurare Pagină principală
st.set_page_config(page_title="PariuriGO World Live Center", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")
data_azi = datetime.now().strftime("%d.%m.%Y")

def incarc_logo_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

logo_base64 = incarc_logo_local("logo.png")

# Aplicare stiluri mov și încărcare date din baza.py
aplica_stiluri_champions()
meciuri_date = preia_baza_date()

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800; text-shadow: 0 0 15px rgba(157, 0, 255, 0.4);'>🏆 PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")

if "lista_membri" not in st.session_state: st.session_state.lista_membri = {"admin": "pariurigo"}
if "vip" not in st.session_state: st.session_state.vip = False
if "admin" not in st.session_state: st.session_state.admin = False

with st.sidebar:
    st.title("🔐 LOGIN ACCES")
    utilizator = st.text_input("Utilizator")
    parola = st.text_input("Parolă", type="password")
    if st.button("Conectare"):
        if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
            st.session_state.vip = True
            if utilizator == "admin": st.session_state.admin = True
            st.success("Conectat!")
            st.rerun()
        else: st.error("Date incorecte!")

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
