import streamlit as st
import base64
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

# Funcție pentru citirea imaginii locale JPG de pe GitHub
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-repeat: no-repeat !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #040e08 !important;"

st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    
    .stApp {{
        {bg_style}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    
    h1, h2, h3, h4, p, span, label, .stTabs button {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Carduri tip sticlă mată în nuanțe verzi închise pentru stânga */
    .glass-box-container {{
        background: rgba(8, 20, 14, 0.88) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.7) !important;
        margin-bottom: 25px !important;
    }}

    /* Carduri speciale pentru pachetele din dreapta să nu se facă negre */
    .vip-card-box {{
        background: rgba(10, 25, 18, 0.9) !important;
        border: 1px solid rgba(0, 255, 102, 0.3) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.6) !important;
    }}

    /* Meniu selectare meci */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: rgba(10, 30, 18, 0.9) !important;
        border: 1px solid #00ff66 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }}

    /* DESIGN PREMIUM PENTRU GRAFIC (TENTĂ VERDE CONFORM IMAGINII) */
    .stat-container {{ width: 100%; margin: 0 auto; }}
    .stat-row {{ display: flex; justify-content: space-between; align-items: center; margin: 12px 0; text-align: center; }}
    .stat-left-val, .stat-right-val {{ width: 20%; font-size: 22px; font-weight: 800; color: #ffffff; text-align: center; }}
    .stat-center-label {{ width: 60%; font-size: 16px; font-weight: 700; color: #a0aec0; text-transform: uppercase; letter-spacing: 0.5px; }}
    
    .green-badge {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%);
        color: #000000 !important;
        padding: 5px 18px;
        border-radius: 6px;
        font-size: 16px;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 2px 12px rgba(0, 255, 102, 0.3);
    }}
    
    .bar-wrapper {{ display: flex; align-items: center; margin: 14px 0; }}
    .bar-label {{ width: 28%; font-size: 16px; font-weight: 700; color: #ffffff; }}
    .bar-container {{ width: 72%; background: rgba(255, 255, 255, 0.05); border-radius: 12px; overflow: hidden; height: 26px; position: relative; border: 1px solid rgba(255,255,255,0.05); }}
    
    .bar-fill-neon {{
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
    }}
    .bar-fill-soft {{
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
    }}
    .green-footer-box {{ background: rgba(0, 255, 102, 0.05); border: 1px solid rgba(0, 255, 102, 0.18); border-radius: 10px; padding: 12px 20px; margin-top: 20px; display: flex; align-items: center; gap: 12px; }}

    /* FORȚARE VIZIBILITATE BUTOANE NATIIVE STREAMLIT (VERDE STRĂLUCITOR) */
    div[data-testid="stLinkButton"] a {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        text-decoration: none !important;
        box-shadow: 0 4px 15px rgba(0, 255, 102, 0.3) !important;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal ORIGINAL (Logo + Titlu Oficial corect)
if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)

st.write("---")

# Împărțirea ecranului (Mecuri în Stânga, Abonamente în Dreapta)
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

# 3. SECȚIUNEA DIN STÂNGA: WIDGET REALE SCOREBAT + GRAFIC PREMIUM RECONSTRUIT VERDE
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
    st.markdown("<p style='text-align:center; color:#94a3b8; font-size:14px; margin-top:2px;'>" + m['liga'] + "</p>", unsafe_allow_html=True)
    st.markdown('<hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">', unsafe_allow_html=True)
    
    # Rânduri de statistici simetrice
    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["g_gz"] + '</div><div class="stat-center-label">Total goluri marcate</div><div class="stat-right-val">' + m["g_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["med_gz"] + '</div><div class="stat-center-label">Medie goluri</div><div class="stat-right-val">' + m["med_os"] + '</div></div>', unsafe_allow_html=True)
