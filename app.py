import streamlit as st
import base64
from datetime import datetime
from baza_date import setari_stil_mov, dictionar_meciuri
from interfata import randeaza_sectiune_meciuri

st.set_page_config(page_title="PariuriGO World Live Center", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")
data_azi = datetime.now().strftime("%d.%m.%Y")

def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

bg_base64 = incarc_imagine_locala("chleague.avif")
logo_base64 = incarc_imagine_locala("logo.png")
bg_style = f"background: linear-gradient(rgba(10, 5, 28, 0.94), rgba(4, 2, 15, 0.97)), url('data:image/avif;base64,{bg_base64}') !important; background-size: cover !important; background-position: center !important; background-repeat: no-repeat !important; background-attachment: fixed !important;" if bg_base64 else "background-color: #0c081f !important;"

setari_stil_mov(bg_style)
meciuri_date = dictionar_meciuri()

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

with col_meciuri:
    randeaza_sectiune_meciuri(meciuri_date, data_azi)

with col_abonamente:
    st.subheader("🏆 Pachete Acces VIP")
    link_stripe = "https://stripe.com"
    
    st.markdown('<div class="vip-card-box" style="border-color: #b042ff !important;">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#b042ff; margin:0; font-size:24px;'>🟢 PACHET LOW</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin:10px 0; font-size:36px; color:#ffffff;'>40 RON <span style='font-size:16px; color:#a0aec0;'>/ lună</span></h2>", unsafe_allow_html=True)
    st.write("📋 **Beneficii incluse:**")
    st.write("✅ 3 Bilete analizate / săptămână")
    st.write("✅ Acces grup comunitate chat")
    st.write("")
    st.markdown('</div>', unsafe_allow_html=True)
    st.link_button("Abonare LOW 🚀", link_stripe, use_container_width=True)
    
    st.markdown('<div class="vip-card-box" style="border-color: #eab308 !important;">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#eab308; margin:0; font-size:24px;'>🟡 PACHET MEDIUM</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin:10px 0; font-size:36px; color:#ffffff;'>70 RON <span style='font-size:16px; color:#a0aec0;'>/ lună</span></h2>", unsafe_allow_html=True)
    st.write("📋 **Beneficii incluse:**")
    st.write("✅ 1 Bilet Premium în fiecare zi")
    st.write("✅ Notificări instant Telegram")
    st.write("")
    st.markdown('</div>', unsafe_allow_html=True)
    st.link_button("Abonare MEDIUM 🟡", link_stripe, use_container_width=True)
    
    st.markdown('<div class="vip-card-box" style="border-color: #ef4444 !important;">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#ef4444; margin:0; font-size:24px;'>🔥 HIGH VIP ELITE</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin:10px 0; font-size:36px; color:#ffffff;'>120 RON <span style='font-size:14px; color:#a0aec0;'>/ lună</span></h2>", unsafe_allow_html=True)
    st.write("📋 **Beneficii incluse:**")
    st.write("✅ Cota 2 VIP zilnică + Dublare")
    st.write("✅ Consultanță 1-la-1 privată")
    st.write("")
    st.markdown('</div>', unsafe_allow_html=True)
    st.link_button("Deblochează HIGH 🔥", link_stripe, use_container_width=True)
