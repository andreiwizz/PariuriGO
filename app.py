import sqlite3
import requests

# ===== VIP MEMBERS =====
conn = sqlite3.connect("members.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS members(username TEXT PRIMARY KEY,password TEXT)")
conn.commit()

def adauga_membru(u,p):
    c.execute("INSERT OR REPLACE INTO members VALUES(?,?)",(u,p))
    conn.commit()

# ADAUGĂ AICI MEMBRII TĂI
adauga_membru("andrei","1234")
adauga_membru("vip1","9999")

API_KEY = "PUNE_CHEIA_TA_API_FOOTBALL"
HEADERS={"x-apisports-key":API_KEY}

def meciuri_live():
    try:
        r=requests.get("https://v3.football.api-sports.io/fixtures?live=all",headers=HEADERS,timeout=10)
        if r.status_code!=200:
            return []
        return r.json()["response"]
    except:
        return []


import streamlit as st
from datetime import datetime

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Determinarea datei curente
data_azi = datetime.now().strftime("%d.%m.%Y")

# Stilul general nativ
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700;800&display=swap');

    .stApp {
        background-color: #040e08 !important;
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }

    h1, h2, h3, h4, p, span, label, .stTabs button {
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }

    .glass-box-container {
        background: rgba(8, 20, 14, 0.88) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.7) !important;
        margin-bottom: 25px !important;
    }

    .vip-card-box {
        background: rgba(10, 25, 18, 0.9) !important;
        border: 1px solid rgba(0, 255, 102, 0.3) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.6) !important;
    }

    .vip-title {
        font-size: 20px !important;
        font-weight: 800 !important;
        color: #00ff66 !important;
        margin: 0 0 4px 0 !important;
    }
    .vip-price {
        font-size: 15px !important;
        color: #94a3b8 !important;
        margin: 0 0 12px 0 !important;
    }
    .vip-feature {
        font-size: 14px !important;
        color: #e2e8f0 !important;
        margin: 4px 0 !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        background-color: rgba(10, 30, 18, 0.9) !important;
        border: 1px solid #00ff66 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }

    .stat-container { width: 100%; margin: 0 auto; }
    .stat-row { display: flex; justify-content: space-between; align-items: center; margin: 12px 0; text-align: center; }
    .stat-left-val, .stat-right-val { width: 20%; font-size: 22px; font-weight: 800; color: #ffffff; text-align: center; }
    .stat-center-label { width: 60%; font-size: 16px; font-weight: 700; color: #a0aec0; text-transform: uppercase; letter-spacing: 0.5px; }

    .green-badge {
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%);
        color: #000000 !important;
        padding: 5px 18px;
        border-radius: 6px;
        font-size: 16px;
        font-weight: 800;
        display: inline-block;
    }

    .bar-wrapper { display: flex; align-items: center; margin: 14px 0; }
    .bar-label { width: 28%; font-size: 16px; font-weight: 700; color: #ffffff; }
    .bar-container { width: 72%; background: rgba(255, 255, 255, 0.05); border-radius: 12px; overflow: hidden; height: 26px; position: relative; }

    .bar-fill-neon {
        height: 100%;
        background: linear-gradient(90deg, #006622 0%, #00ff66 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 12px;
        font-size: 13px;
        font-weight: 800;
        color: #000000;
    }
    .bar-fill-soft {
        height: 100%;
        background: linear-gradient(90deg, #013a16 0%, #00bc43 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 12px;
        font-size: 13px;
        font-weight: 800;
        color: #ffffff;
    }

    div[data-testid="stLinkButton"] a {
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        text-decoration: none !important;
        box-shadow: 0 0 12px rgba(0, 255, 102, 0.4) !important;
        animation: pulsareGlow 1.8s infinite ease-in-out !important;
    }

    @keyframes pulsareGlow {
        0% { transform: scale(1); box-shadow: 0 0 12px rgba(0, 255, 102, 0.4); }
        50% { transform: scale(1.02); box-shadow: 0 0 25px rgba(0, 255, 102, 0.7); }
        100% { transform: scale(1); box-shadow: 0 0 12px rgba(0, 255, 102, 0.4); }
    }
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal cu Titlu
st.markdown("<h1 style='text-align: center; color: #ffffff;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")

# Împărțirea ecranului (Meciuri în Stânga, Abonamente în Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# BAZA DE DATE MECIURI REALE SUPERLIGA
meciuri_date = {
    "FCSB vs Rapid București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": "14", "g_os": "11", "med_gz": "1.75", "med_os": "1.37", "gp_gz": "5", "gp_os": "9",
        "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%",
        "p15_gz": "91.20%", "p15_os": "78.50%", "p25_gz": "64.29%", "p25_os": "50.00%",
        "gg_gz": "71.43%", "gg_os": "57.14%", "c_gz": "14.29%", "c_os": "28.57%",
        "cor_gz": "-", "cor_os": "14.29%",
        "w_p15": "85.00%", "w_p25": "64.29%", "w_p05r1": "85.71%", "w_p05r2": "78.50%", "w_gg": "71.43%", "w_c35": "21.43%", "w_cor95": "14.29%"
    },
    "CFR Cluj vs Universitatea Craiova": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": "11", "g_os": "13", "med_gz": "1.37", "med_os": "1.62", "gp_gz": "7", "gp_os": "6",
        "ht_gz": "75.00%", "ht_os": "62.50%", "st_gz": "87.50%", "st_os": "75.00%",
        "p15_gz": "87.50%", "p15_os": "75.00%", "p25_gz": "50.00%", "p25_os": "62.50%",
        "gg_gz": "62.50%", "gg_os": "62.50%", "c_gz": "25.00%", "c_os": "37.50%",
        "cor_gz": "12.50%", "cor_os": "25.00%",
        "w_p15": "81.00%", "w_p25": "56.00%", "w_p05r1": "68.00%", "w_p05r2": "81.00%", "w_gg": "62.00%", "w_c35": "31.00%", "w_cor95": "18.00%"
    },
    "Bașakșehir vs Kocaelispor": {
        "liga": "SUPER LIG &bull; TURKEY",
        "g_gz": "7", "g_os": "3", "med_gz": "1.00", "med_os": "0.43", "gp_gz": "8", "gp_os": "6",
        "ht_gz": "71.43%", "ht_os": "57.14%", "st_gz": "71.43%", "st_os": "57.14%",
        "p15_gz": "85.71%", "p15_os": "42.86%", "p25_gz": "28.57%", "p25_os": "42.86%",
        "gg_gz": "57.14%", "gg_os": "42.86%", "c_gz": "14.29%", "c_os": "28.57%",
        "cor_gz": "-", "cor_os": "14.29%",
        "w_p15": "64.29%", "w_p25": "14.29%", "w_p05r1": "64.29%", "w_p05r2": "64.29%", "w_gg": "50.00%", "w_c35": "21.43%", "w_cor95": "7.14%"
    }
}

# Etichete pentru barele de probabilitate calculate de algoritm
bare_probabilitate = [
    ("w_p15", "Peste 1.5 goluri"),
    ("w_p25", "Peste 2.5 goluri"),
    ("w_p05r1", "Peste 0.5 Repriza 1"),
    ("w_p05r2", "Peste 0.5 Repriza 2"),
    ("w_gg", "Ambele echipe marchează (GG)"),
    ("w_c35", "Cartonașe peste 3.5"),
    ("w_cor95", "Cornere peste 9.5"),
]

# 3. SECȚIUNEA DIN STÂNGA: SCOREBAT SUS + GRAFIC PREMIUM
with col_meciuri:
    st.subheader("🌍 Meciuri Live din Toate Ligele Lumii")

    st.markdown("""
        <div style="width:100%; height:420px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px; margin-bottom: 25px;">
            <iframe src="https://scorebat.com" frameborder="0" width="100%" height="390px" allowfullscreen allow="autoplay; fullscreen"></iframe>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("📊 Modul Algoritm & Probabilități (Meci de Top)")

    meci_ales = st.selectbox("🎯 Schimbă meciul din ziua respectivă:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]

    st.markdown('<div class="glass-box-container">', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8; margin:0;'>MECI RECOMANDAT &bull; DATE LA ZI " + data_azi + "</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>" + meci_ales + "</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8; font-size:14px; margin-top:2px;'> " + m['liga'] + "</p>", unsafe_allow_html=True)
    st.markdown('<hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">', unsafe_allow_html=True)

    # Rânduri statistici directe (gazde vs oaspeți)
    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["g_gz"] + '</div><div class="stat-center-label">Total goluri marcate</div><div class="stat-right-val">' + m["g_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["med_gz"] + '</div><div class="stat-center-label">Medie goluri</div><div class="stat-right-val">' + m["med_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["gp_gz"] + '</div><div class="stat-center-label">Goluri primite</div><div class="stat-right-val">' + m["gp_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="green-badge">' + m["ht_gz"] + '</span></div><div class="stat-center-label">Peste 0.5 HT</div><div class="stat-right-val"><span class="green-badge">' + m["ht_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="green-badge">' + m["st_gz"] + '</span></div><div class="stat-center-label">Peste 0.5 ST</div><div class="stat-right-val"><span class="green-badge">' + m["st_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="green-badge">' + m["p15_gz"] + '</span></div><div class="stat-center-label">Peste 1.5 goluri</div><div class="stat-right-val"><span class="green-badge">' + m["p15_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="green-badge">' + m["p25_gz"] + '</span></div><div class="stat-center-label">Peste 2.5 goluri</div><div class="stat-right-val"><span class="green-badge">' + m["p25_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="green-badge">' + m["gg_gz"] + '</span></div><div class="stat-center-label">Ambele echipe marchează</div><div class="stat-right-val"><span class="green-badge">' + m["gg_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="green-badge">' + m["c_gz"] + '</span></div><div class="stat-center-label">Cartonaș roșu</div><div class="stat-right-val"><span class="green-badge">' + m["c_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="green-badge">' + m["cor_gz"] + '</span></div><div class="stat-center-label">Cornere peste 4.5</div><div class="stat-right-val"><span class="green-badge">' + m["cor_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # închide stat-container

    st.markdown('<hr style="border-color: rgba(255,255,255,0.08); margin: 20px 0;">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#ffffff; margin-bottom: 15px;'>🧠 Probabilitate calculată de algoritm</h3>", unsafe_allow_html=True)

    # Barele de probabilitate (alternăm stilul neon / soft)
    for i, (cheie, eticheta) in enumerate(bare_probabilitate):
        valoare = m[cheie]
        try:
            procent = float(valoare.replace("%", ""))
        except ValueError:
            procent = 0
        clasa_bara = "bar-fill-neon" if i % 2 == 0 else "bar-fill-soft"
        st.markdown(
            '<div class="bar-wrapper">'
            f'<div class="bar-label">{eticheta}</div>'
            '<div class="bar-container">'
            f'<div class="{clasa_bara}" style="width:{procent}%;">{valoare}</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)  # închide glass-box-container

# 4. SECȚIUNEA DIN DREAPTA: PACHETE VIP / ABONAMENTE
with col_abonamente:
    st.subheader("💎 Pachete VIP")

    pachete = [
        {
            "nume": "🥉 PACHET LOW",
            "pret": "49 RON / lună",
            "beneficii": ["1-2 ponturi pe zi", "Acces grup Telegram Low", "Analiză statistică de bază"],
            "link_telegram": "https://t.me/PariuriGO_Low",
            "link_stripe": "https://buy.stripe.com/inlocuiește_cu_linkul_tau_low"
        },
        {
            "nume": "🥈 PACHET MEDIUM",
            "pret": "99 RON / lună",
            "beneficii": ["3-5 ponturi pe zi", "Acces grup Telegram Medium", "Analiză algoritm avansată", "Statistici live"],
            "link_telegram": "https://t.me/PariuriGO_Medium",
            "link_stripe": "https://buy.stripe.com/inlocuiește_cu_linkul_tau_medium"
        },
        {
            "nume": "🥇 PACHET HIGH",
            "pret": "199 RON / lună",
            "beneficii": ["Ponturi nelimitate", "Acces grup Telegram VIP High", "Analiză completă + suport direct", "Predicții premium în timp real"],
            "link_telegram": "https://t.me/PariuriGO_High",
            "link_stripe": "https://buy.stripe.com/inlocuiește_cu_linkul_tau_high"
        }
    ]

    for pachet in pachete:
        st.markdown('<div class="vip-card-box">', unsafe_allow_html=True)
        st.markdown(f'<p class="vip-title">{pachet["nume"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="vip-price">{pachet["pret"]}</p>', unsafe_allow_html=True)
        for beneficiu in pachet["beneficii"]:
            st.markdown(f'<p class="vip-feature">✔️ {beneficiu}</p>', unsafe_allow_html=True)
        
        st.link_button("💳 Plătește cu Card (Stripe)", pachet["link_stripe"])
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    st.caption("Actualizat automat la data de " + data_azi)
