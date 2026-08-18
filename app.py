import streamlit as st
import base64
from datetime import datetime
from baza import aplica_stiluri_champions, preia_baza_date

# 1. Configurare Pagina principala
st.set_page_config(page_title="PariuriGO World Live Center", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")
data_azi = datetime.now().strftime("%d.%m.%Y")

def incarc_logo_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

logo_base64 = incarc_logo_local("logo.png")

# Aplicare stiluri mov si incarcare date din baza.py
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
        parola = st.text_input("🔑 Parola", type="password", key="login_pass")
        if st.button("CONECTARE CONT VIP"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                if utilizator == "admin": st.session_state.admin = True
                st.success("Conectat!")
                st.rerun()
            else: st.error("Date incorecte!")
    else:
        st.markdown(f"<div style='text-align:center; background:rgba(0,255,102,0.1); border:1px solid #00ff66; padding:10px; border-radius:8px; margin-bottom:15px;'>🟢 Profil VIP Activ!</div>", unsafe_allow_html=True)
        if st.button("DECONECTARE PROFIL"):
            st.session_state.vip = False
            st.session_state.admin = False
            st.rerun()

if st.session_state.admin:
    st.write("---")
    st.header("🛠 ADMIN PANEL")
    nume = st.text_input("Nume membru nou")
    passw = st.text_input("Parola membru nou")
    if st.button("➕ Adauga membru"):
        if nume:
            st.session_state.lista_membri[nume] = passw
            st.success("Adaugat!")
            st.rerun()

col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

with col_meciuri:
    st.markdown('<p style="font-size: 22px; color: #b042ff; font-weight:800; margin-bottom: 10px;">📱 APLICAȚIA INTERACTIVĂ PARIURIGO</p>', unsafe_allow_html=True)
    pas_aplicatie = st.radio("🧭 Navigare Pasi Aplicatie:", ["🔥 Oferta Zilei (3 Zile Moca)", "📊 Algoritm & Statistici Live", "🌍 Toate Meciurile Live"], horizontal=True)
    st.write("---")
    
    if pas_aplicatie == "🔥 Oferta Zilei (3 Zile Moca)":
        st.markdown("""
        <div class="glass-box-container" style="border-color: #ff9900 !important; background: rgba(255,153,0,0.03) !important;">
            <h2 style="color:#ff9900; text-align:center; font-size:32px;">🎁 CADOU: 3 ZILE DE PROBĂ GRATUITE!</h2>
            <p style="font-size:18px; text-align:center; margin:15px 0; color:#cbd5e1;">Vrei sa testezi algoritmul PariuriGO fara sa platesti nimic? Iti oferim acces complet timp de 72 de ore pe canalul nostru VIP!</p>
            <p style="text-align:center; font-size:15px; color:#a0aec0;">• Bilete zilnice incluse • Notificari instant • Fara obligatii</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("💥 RECLAMĂ CELE 3 ZILE GRATUITE PE TELEGRAM", "https://t.me", use_container_width=True)
    elif pas_aplicatie == "📊 Algoritm & Statistici Live":
        meci_ales = st.selectbox("🎯 Schimba meciul:", list(meciuri_date.keys()))
        m = meciuri_date[meci_ales]
        st.markdown('<div class="glass-box-container">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center; color:#b042ff; margin: 5px 0; font-size:32px; font-weight:800;'>"+meci_ales+"</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#cbd5e1; font-size:14px; font-weight:700;'>🏆 "+m['liga']+" &bull; "+data_azi+"</p>", unsafe_allow_html=True)
        st.markdown('<hr style="border-color: #221545;">', unsafe_allow_html=True)
        st.markdown('<div class="stat-container">', unsafe_allow_html=True)
        st.markdown('<div class="stat-row"><div class="stat-left-val">'+m["g_gz"]+'</div><div class="stat-center-label">Total goluri marcate</div><div class="stat-right-val">'+m["g_os"]+'</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-row"><div class="stat-left-val">'+m["med_gz"]+'</div><div class="stat-center-label">Medie goluri</div><div class="stat-right-val">'+m["med_os"]+'</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-row"><div class="stat-left-val">'+m["gp_gz"]+'</div><div class="stat-center-label">Goluri primite</div><div class="stat-right-val">'+m["gp_os"]+'</div></div>', unsafe_allow_html=True)
        st.markdown('<hr style="border-color: #221545;">', unsafe_allow_html=True)
        st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="mov-badge-tiktok">'+m["ht_gz"]+'</span></div><div class="stat-center-label">Peste 0.5 HT</div><div class="stat-right-val"><span class="mov-badge-tiktok">'+m["ht_os"]+'</span></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="mov-badge-tiktok">'+m["st_gz"]+'</span></div><div class="stat-center-label">Peste 0.5 ST</div><div class="stat-right-val"><span class="mov-badge-tiktok">'+m["st_os"]+'</span></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="mov-badge-tiktok">'+m["p15_gz"] + '</span></div><div class="stat-center-label">Peste 1.5 goluri</div><div class="stat-right-val"><span class="mov-badge-tiktok">'+m["p15_os"]+'</span></div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<hr style="border-color: #221545; margin: 20px 0;">', unsafe_allow_html=True)
        st.markdown('<div class="bar-wrapper"><div class="bar-title-flex"><span>Peste 1.5:</span></div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: '+m["w_p15"]+';"></div></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="bar-wrapper"><div class="bar-label">Peste 2.5:</div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: '+m["w_p25"]+';"></div></div></div>', unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

    elif pas_aplicatie == "🌍 Toate Meciurile Live":
        st.markdown('<div style="width:100%; height:420px; overflow:auto; background:rgba(0,0,0,0.8); border-radius:12px; border:1px solid #1a0f30; padding:10px; margin-bottom: 25px;"><iframe src="https://scorebat.com" frameborder="0" width="100%" height="390px" allowfullscreen allow="autoplay; fullscreen"></iframe></div>', unsafe_allow_html=True)
