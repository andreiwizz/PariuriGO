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

with col_meciuri:
    st.subheader("🌍 Toate Meciurile Live din Lume")
    st.markdown('<div style="width:100%; height:420px; overflow:auto; background:rgba(0,0,0,0.8); border-radius:12px; border:1px solid #1a0f30; padding:10px; margin-bottom: 25px;"><iframe src="https://scorebat.com" frameborder="0" width="100%" height="390px" allowfullscreen allow="autoplay; fullscreen"></iframe></div>', unsafe_allow_html=True)
    st.write("---")
    st.subheader("📊 Modul Algoritm & Probabilități")
    
    meci_ales = st.selectbox("🎯 Schimbă meciul:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]
    
    st.markdown('<div class="glass-box-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#b042ff; margin: 5px 0; font-size:32px; font-weight:800; text-shadow: 0 0 10px rgba(176,66,255,0.4);'>" + meci_ales + "</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#cbd5e1; font-size:14px; font-weight:700;'>" + m['liga'] + "</p>", unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #221545;">', unsafe_allow_html=True)
    
    # Rânduri de statistici identice cu aplicația ta din TikTok
    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["g_gz"] + '</div><div class="stat-center-label">Total goluri marcate</div><div class="stat-right-val">' + m["g_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["med_gz"] + '</div><div class="stat-center-label">Medie goluri</div><div class="stat-right-val">' + m["med_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["gp_gz"] + '</div><div class="stat-center-label">Goluri primite</div><div class="stat-right-val">' + m["gp_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #221545;">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="orange-badge">' + m["ht_gz"] + '</span></div><div class="stat-center-label">Peste 0.5 HT</div><div class="stat-right-val"><span class="orange-badge">' + m["ht_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="orange-badge">' + m["st_gz"] + '</span></div><div class="stat-center-label">Peste 0.5 ST</div><div class="stat-right-val"><span class="orange-badge">' + m["st_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="orange-badge">' + m["p15_gz"] + '</span></div><div class="stat-center-label">Peste 1.5 goluri</div><div class="stat-right-val"><span class="orange-badge">' + m["p15_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="color:#b042ff; font-size:20px;">' + m["p25_gz"] + '</div><div class="stat-center-label">Peste 2.5 goluri</div><div class="stat-right-val" style="color:#b042ff; font-size:20px;">' + m["p25_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="color:#b042ff; font-size:20px;">' + m["gg_gz"] + '</div><div class="stat-center-label">Ambele marchează</div><div class="stat-right-val" style="color:#b042ff; font-size:20px;">' + m["gg_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="font-size:14px; color:#a0aec0;">' + m["c_gz"] + '</div><div class="stat-center-label">Peste 3.5 cartonașe</div><div class="stat-right-val" style="font-size:14px; color:#a0aec0;">' + m["c_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="font-size:14px; color:#a0aec0;">' + m["cor_gz"] + '</div><div class="stat-center-label">Peste 9.5 cornere</div><div class="stat-right-val" style="font-size:14px; color:#b042ff;">' + m["cor_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-color: #221545; margin: 20px 0;">', unsafe_allow_html=True)
    st.markdown('<p style="font-weight:800; color:#b042ff;">📈 BARE EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:</p>', unsafe_allow_html=True)
    
    # Barele orizontale din imaginea ta redesenate în nuanțe Mov Premium
    st.markdown('<div class="bar-wrapper"><div class="bar-title-flex"><span>Peste 1.5:</span></div><div class="bar-container-custom"><div class="bar-fill-orange-tiktok" style="width: ' + m["w_p15"] + ';">' + m["w_p15"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Peste 2.5:</div><div class="bar-container-custom"><div class="bar-fill-orange-tiktok" style="width: ' + m["w_p25"] + ';">' + m["w_p25"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Peste 0.5 R1:</div><div class="bar-container-custom"><div class="bar-fill-orange-tiktok" style="width: ' + m["w_p05r1"] + ';">' + m["w_p05r1"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Peste 0.5 R2:</div><div class="bar-container-custom"><div class="bar-fill-orange-tiktok" style="width: ' + m["w_p05r2"] + ';">' + m["w_p05r2"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Ambele marchează:</div><div class="bar-container-custom"><div class="bar-fill-orange-tiktok" style="width: ' + m["w_gg"] + ';">' + m["w_gg"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">+ 3.5 Cartonașe:</div><div class="bar-container-custom"><div class="bar-fill-orange-tiktok" style="width: ' + m["w_c35"] + ';">' + m["w_c35"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">+ 9.5 Cornere:</div><div class="bar-container-custom"><div class="bar-fill-orange-tiktok" style="width: ' + m["w_cor95"] + ';">' + m["w_cor95"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_abonamente:
    st.subheader("🏆 Pachete Acces VIP")
    link_stripe = "https://stripe.com"
    
    for pachet, pret, cul, benf in [
        ("🟢 PACHET LOW", "40 RON", "#b042ff", ["3 Bilete analizate / săptămână", "Acces grup comunitate chat"]), 
        ("🟡 PACHET MEDIUM", "70 RON", "#eab308", ["1 Bilet Premium în fiecare zi", "Notificări instant Telegram"]), 
        ("🔥 HIGH VIP ELITE", "120 RON", "#ef4444", ["Cota 2 VIP zilnică + Dublare", "Consultanță 1-la-1 privată"])
    ]:
        st.markdown(f"""
        <div class="vip-card-box" style="border-color: {cul} !important;">
            <h3 style='color:{cul}; margin:0; font-size:24px;'>{pachet}</h3>
            <h2 style='margin:10px 0; font-size:36px; color:#ffffff;'>{pret} <span style='font-size:16px; color:#a0aec0;'>/ lună</span></h2>
            <hr style="border-color: rgba(255,255,255,0.05); margin: 10px 0;">
            {"".join([f"<p style='margin:4px 0; font-size:15px;'>✅ {b}</p>" for b in benf])}
            <br>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Abonare {pachet.split()[-1]} 🚀", link_stripe, use_container_width=True)
