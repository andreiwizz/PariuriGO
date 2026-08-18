import streamlit as st

def setari_estetice(bg_style):
    st.markdown(f"""
    <style>
        @import url('https://googleapis.com');
        .stApp {{ background-color: #030805 !important; color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; }}
        h1, h2, h3, h4, p, span, label {{ font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important; }}
        div[data-testid="column"]:nth-of-type(1) {{
            background-color: #06140c !important; border-right: 2px solid rgba(0, 255, 102, 0.2) !important;
            padding: 30px 25px !important; border-radius: 20px 0 0 20px !important; box-shadow: inset -10px 0 30px rgba(0,0,0,0.5) !important;
        }}
        div[data-testid="column"]:nth-of-type(2) {{
            background-color: #0d0d0d !important; padding: 30px 25px !important;
            border-radius: 0 20px 20px 0 !important; box-shadow: inset 10px 0 30px rgba(0,0,0,0.8) !important;
        }}
        button div {{ font-size: 0px !important; }} button div:before {{ font-size: 16px !important; }}
        .inner-cyber-card {{ background: rgba(0, 0, 0, 0.4) !important; border: 1px solid rgba(0, 255, 102, 0.15) !important; border-radius: 14px !important; padding: 20px !important; margin-bottom: 20px !important; }}
        .vip-card-box {{ background: #121212 !important; border-left: 4px solid #00ff66 !important; border-radius: 8px !important; padding: 22px !important; margin-bottom: 22px !important; }}
        div[data-testid="stSelectbox"] div[data-baseweb="select"] {{ background-color: #020503 !important; border: 1px solid #00ff66 !important; color: #ffffff !important; border-radius: 8px !important; }}
        .cyber-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; text-align: center; margin: 20px 0; }}
        .cyber-grid-item {{ background: rgba(0, 255, 102, 0.02); border: 1px solid rgba(0, 255, 102, 0.08); border-radius: 10px; padding: 14px 10px; }}
        .cyber-num {{ font-size: 26px; font-weight: 800; color: #00ff66; }}
        .cyber-label {{ font-size: 13px; color: #94a3b8; text-transform: uppercase; }}
        .proc-row {{ display: flex; justify-content: space-between; align-items: center; background: rgba(0, 255, 102, 0.03); border-left: 3px solid #00ff66; padding: 12px 16px; margin: 10px 0; }}
        .proc-badge {{ background: #00ff66; color: #000000; font-weight: 800; padding: 4px 10px; border-radius: 4px; }}
        .bar-wrapper {{ margin: 16px 0; }} .bar-title-flex {{ display: flex; justify-content: space-between; font-size: 15px; }}
        .bar-container-custom {{ width: 100%; background: rgba(255, 255, 255, 0.04); border-radius: 10px; height: 16px; overflow: hidden; }}
        .bar-fill-neon-custom {{ height: 100%; background: linear-gradient(90deg, #005c20 0%, #00ff66 100%); border-radius: 10px; }}
        div[data-testid="stLinkButton"] a {{
            background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important; color: #000000 !important;
            font-weight: 800 !important; font-size: 18px !important; border-radius: 8px !important; padding: 14px 20px !important;
            display: block !important; text-align: center !important; text-decoration: none !important;
            box-shadow: 0 4px 20px rgba(0, 255, 102, 0.3) !important; animation: glowPulseAnimate 2s infinite ease-in-out !important;
        }}
        @keyframes glowPulseAnimate {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.02); }} 100% {{ transform: scale(1); }} }}
    </style>
    """, unsafe_allow_html=True)

def preia_meciuri():
    return {
        "FCSB vs Rapid București": {
            "liga": "ROMÂNIA SUPERLIGA", "g_gz": "14", "g_os": "11", "med_gz": "1.75", "med_os": "1.37", "gp_gz": "5", "gp_os": "9",
            "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%", "p15_gz": "91.20%", "p25_gz": "64.29%", "gg_gz": "71.43%",
            "w_p15": "85%", "w_p25": "64%", "w_p05r1": "85%", "w_gg": "71%"
        },
        "CFR Cluj vs Universitatea Craiova": {
            "liga": "ROMÂNIA SUPERLIGA", "g_gz": "11", "g_os": "13", "med_gz": "1.37", "med_os": "1.62", "gp_gz": "7", "gp_os": "6",
            "ht_gz": "75.00%", "ht_os": "62.50%", "st_gz": "87.50%", "st_os": "75.00%", "p15_gz": "87.50%", "p25_gz": "50.00%", "gg_gz": "62.50%",
            "w_p15": "81%", "w_p25": "56%", "w_p05r1": "68%", "w_gg": "62%"
        }
    }

import streamlit as st
import base64
from datetime import datetime
from config import setari_estetice, preia_meciuri

# 1. Inițializare Pagină principală
st.set_page_config(page_title="PariuriGO World Live Center", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")
data_azi = datetime.now().strftime("%d.%m.%Y")

def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")
bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-attachment: fixed !important;" if teren_base64 else "background-color: #030805 !important;"

# Aplicăm stilul și preluăm baza de date din Part 1
setari_estetice(bg_style)
meciuri_date = preia_meciuri()

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800; letter-spacing: 1px;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")

# Session state admin/login
if "lista_membri" not in st.session_state: st.session_state.lista_membri = {"admin": "pariurigo"}
if "vip" not in st.session_state: st.session_state.vip = False
if "admin" not in st.session_state: st.session_state.admin = False

with st.sidebar:
    st.title("🔐 LOGIN PANOU")
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
    st.header("🛠 ADMIN CONTROL PANEL")
    nume = st.text_input("Nume membru nou")
    passw = st.text_input("Parolă membru nou")
    if st.button("➕ Adaugă în bază"):
        if nume:
            st.session_state.lista_membri[nume] = passw
            st.success("Membru salvat!")
            st.rerun()

st.write("---")
col_stanga_verde, col_dreapta_negru = st.columns([1.25, 0.75], gap="small")

with col_stanga_verde:
    st.markdown('<p style="font-size: 22px; color: #00ff66; margin-bottom: 10px;">🌍 STREAM LIVE SCOREBAT</p>', unsafe_allow_html=True)
    st.markdown('<div class="inner-cyber-card"><iframe src="https://scorebat.com" frameborder="0" width="100%" height="380px" allowfullscreen></iframe></div>', unsafe_allow_html=True)
    st.write("---")
    meci_ales = st.selectbox("🎯 Alege partida din lista zilei:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]
    
    st.markdown(f"""
    <div class="inner-cyber-card" style="border: 1px solid rgba(0, 255, 102, 0.3);">
        <h2 style='text-align:center; color:#00ff66; margin: 4px 0; font-size: 30px;'>{meci_ales}</h2>
        <p style='text-align:center; color:#ffffff; font-size:14px; opacity:0.7;'>🏆 {m['liga']} &bull; {data_azi}</p>
        <div class="cyber-grid">
            <div class="cyber-grid-item"><div class="cyber-num">{m['g_gz']}</div><div class="cyber-label">Goluri Gz</div></div>
            <div class="cyber-grid-item"><div class="cyber-num" style="color:#ffffff;">{m['med_gz']} : {m['med_os']}</div><div class="cyber-label">Medie Meci</div></div>
            <div class="cyber-grid-item"><div class="cyber-num">{m['g_os']}</div><div class="cyber-label">Goluri Os</div></div>
        </div>
        <div class="cyber-grid" style="grid-template-columns: repeat(2, 1fr); margin-top:0;">
            <div class="cyber-grid-item"><div class="cyber-num" style="color:#ffcc00;">{m['gp_gz']}</div><div class="cyber-label">Primite Gz</div></div>
            <div class="cyber-grid-item"><div class="cyber-num" style="color:#ffcc00;">{m['gp_os']}</div><div class="cyber-label">Primite Os</div></div>
        </div>
        <hr style="border-color: rgba(0, 255, 102, 0.1); margin: 15px 0;">
        <div class="proc-row"><span class="proc-text">Peste 0.5 HT (Prima Repriză)</span><span class="proc-badge">{m['ht_gz']}</span></div>
        <div class="proc-row"><span class="proc-text">Peste 0.5 ST (A doua Repriză)</span><span class="proc-badge">{m['st_gz']}</span></div>
        <div class="proc-row"><span class="proc-text">Peste 1.5 Goluri Finale</span><span class="proc-badge">{m['p15_gz']}</span></div>
        <div class="proc-row"><span class="proc-text">Peste 2.5 Goluri Finale</span><span class="proc-badge" style="background:#ffcc00;">{m['p25_gz']}</span></div>
        <div class="proc-row"><span class="proc-text">Ambele echipe marchează (GG)</span><span class="proc-badge">{m['gg_gz']}</span></div>
        <hr style="border-color: rgba(0, 255, 102, 0.1); margin: 20px 0;">
        <div class="bar-wrapper">
            <div class="bar-title-flex"><span>🔹 Probabilitate Peste 1.5 Goluri</span><span>{m['w_p15']}</span></div>
            <div class="bar-container-custom"><div class="bar-fill-neon-custom" style="width: {m['w_p15']};"></div></div>
        </div>
        <div class="bar-wrapper">
            <div class="bar-title-flex"><span>🔹 Probabilitate Peste 2.5 Goluri</span><span>{m['w_p25']}</span></div>
            <div class="bar-container-custom"><div class="bar-fill-neon-custom" style="width: {m['w_p25']};"></div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_dreapta_negru:
    st.markdown('<p style="font-size: 22px; color: #00ff66; margin-bottom: 10px;">🏆 PACHETE ABONAMENT VIP</p>', unsafe_allow_html=True)
    link_stripe = "https://stripe.com"
    
    for pachet, pret, cul, benf in [("🟢 PACHET LOW", "40 RON", "#00ff66", ["3 Bilete analizate / săptămână", "Selecție ligi mari europene", "Acces grup comunitate chat"]), 
                                    ("🟡 PACHET MEDIUM", "70 RON", "#eab308", ["1 Bilet Premium în fiecare zi", "Probabilități live avansate", "Notificări instant Telegram"]), 
                                    ("🔥 HIGH VIP ELITE", "120 RON", "#ef4444", ["Cota 2 VIP zilnică + Dublare", "Monitorizare live non-stop", "Consultanță 1-la-1 privată"])]:
        st.markdown(f"""
        <div class="vip-card-box" style="border-left: 4px solid {cul};">
            <h3 style='color:{cul}; margin:0; font-size:22px;'>{pachet}</h3>
            <h2 style='margin:8px 0; font-size:34px; color:#ffffff; font-weight:800;'>{pret} <span style='font-size:14px; color:#94a3b8; font-weight:500;'>/ lună</span></h2>
            <hr style="border-color: rgba(255,255,255,0.05); margin: 10px 0;">
            {"".join([f"<p style='margin:4px 0; font-size:14px;'>✅ {b}</p>" for b in benf])}
            <br><a class="animated-btn" href="{link_stripe}" target="_blank">ABONARE {pachet.split()[-1]}</a>
        </div>
        """, unsafe_allow_html=True)
