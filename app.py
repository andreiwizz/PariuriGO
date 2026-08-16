import streamlit as st
import base64
from datetime import datetime

# 1. Configurare Pagină (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Determinarea automată a datei curente
data_azi = datetime.now().strftime("%d.%m.%Y")

# Funcție pentru citirea imaginii locale JPG de pe GitHub și transformarea ei în fundal
def decodifica_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# Citim terenul de fotbal și logo-ul din proiectul tău GitHub
teren_base64 = decodifica_imagine_locala("teren.jpg")
logo_base64 = decodifica_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-repeat: no-repeat !important; background-attachment: fixed !important;"
else:
    bg_style = "background: radial-gradient(circle at center, #0a1f14 0%, #030c08 100%) !important;"

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
    
    /* Carduri tip sticlă mată în nuanțe verzi */
    .glass-box {{
        background: rgba(8, 22, 15, 0.86) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.22) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.65) !important;
        margin-bottom: 25px !important;
    }}

    /* Stiluri pentru selectbox native Streamlit să se asorteze */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: rgba(10, 30, 18, 0.9) !important;
        border: 1px solid #00ff66 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }}

    /* Stiluri pentru butoanele mari din pachete */
    .stButton > button {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        transition: all 0.2s ease-in-out !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.5) !important;
    }}

    /* Stiluri grafic în tentă verde */
    .stat-container {{ width: 100%; margin: 0 auto; }}
    .stat-row {{ display: flex; justify-content: space-between; align-items: center; margin: 10px 0; text-align: center; }}
    .stat-left-val, .stat-right-val {{ width: 20%; font-size: 22px; font-weight: 800; color: #ffffff; text-align: center; }}
    .stat-center-label {{ width: 60%; font-size: 16px; font-weight: 700; color: #a0aec0; text-transform: uppercase; letter-spacing: 0.5px; }}
    
    .green-badge {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%);
        color: #000000 !important;
        padding: 4px 15px;
        border-radius: 6px;
        font-size: 16px;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 2px 10px rgba(0, 255, 102, 0.25);
    }}
    
    .bar-wrapper {{ display: flex; align-items: center; margin: 12px 0; }}
    .bar-label {{ width: 25%; font-size: 16px; font-weight: 700; color: #ffffff; }}
    .bar-container {{ width: 75%; background: rgba(255, 255, 255, 0.05); border-radius: 8px; overflow: hidden; height: 24px; position: relative; border: 1px solid rgba(255,255,255,0.05); }}
    .bar-fill-intense-green {{ height: 100%; background: linear-gradient(90deg, #008f33 0%, #00ff66 100%); border-radius: 8px; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; font-size: 13px; font-weight: 800; color: #000000; }}
    .green-footer-box {{ background: rgba(0, 255, 102, 0.05); border: 1px solid rgba(0, 255, 102, 0.18); border-radius: 10px; padding: 12px 20px; margin-top: 20px; display: flex; align-items: center; gap: 12px; }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației cu Logo
if logo_base64:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <img src="data:image/png;base64,{logo_base64}" width="280">
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center; color: #00ff66;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)

st.write("---")

# Împărțirea ecranului (Fluxul în Stânga, Abonamente în Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# Baza de date pentru meciuri selectabile
meciuri_date = {
    "FCSB vs Rapid București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_stg": "14", "g_drp": "11", "m_stg": "1.75", "m_drp": "1.37", "gp_stg": "5", "gp_drp": "9",
        "ht_stg": "85.71%", "ht_drp": "71.43%", "st_stg": "78.50%", "st_drp": "64.25%",
        "p15_stg": "91.20%", "p15_drp": "78.50%", "p25_stg": "64.29%", "p25_drp": "50.00%",
        "gg_stg": "71.43%", "gg_drp": "57.14%", "p15_total": "85.00%", "p05_r1": "78.00%", "gg_total": "64.00%",
        "p15_w": "85%", "p05_w": "78%", "gg_w": "64%",
        "arbitru": "Radu Petrescu &bull; 5/5 meciuri analizate"
    },
    "CFR Cluj vs Universitatea Craiova": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_stg": "11", "g_drp": "13", "m_stg": "1.37", "m_drp": "1.62", "gp_stg": "7", "gp_drp": "6",
        "ht_stg": "75.00%", "ht_drp": "62.50%", "st_stg": "87.50%", "st_drp": "75.00%",
        "p15_stg": "87.50%", "p15_drp": "75.00%", "p25_stg": "50.00%", "p25_drp": "62.50%",
        "gg_stg": "62.50%", "gg_drp": "62.50%", "p15_total": "81.00%", "p05_r1": "68.00%", "gg_total": "62.00%",
        "p15_w": "81%", "p05_w": "68%", "gg_w": "62%",
        "arbitru": "Istvan Kovacs &bull; 8/8 meciuri analizate"
    },
    "Oțelul Galați vs Dinamo București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_stg": "8", "g_drp": "10", "m_stg": "1.00", "m_drp": "1.25", "gp_stg": "4", "gp_drp": "8",
        "ht_stg": "50.00%", "ht_drp": "50.00%", "st_stg": "62.50%", "st_drp": "75.00%",
        "p15_stg": "62.50%", "p15_drp": "75.00%", "p25_stg": "25.00%", "p25_drp": "50.00%",
        "gg_stg": "37.50%", "gg_drp": "50.00%", "p15_total": "68.00%", "p05_r1": "50.00%", "gg_total": "43.00%",
        "p15_w": "68%", "p05_w": "50%", "gg_w": "43%",
        "arbitru": "Marian Barbu &bull; 4/4 meciuri analizate"
    },
    "Bașakșehir vs Kocaelispor": {
        "liga": "SUPER LIG &bull; TURKEY",
        "g_stg": "7", "g_drp": "3", "m_stg": "1.00", "m_drp": "0.43", "gp_stg": "8", "gp_drp": "6",
        "ht_stg": "71.43%", "ht_drp": "57.14%", "st_stg": "71.43%", "st_drp": "57.14%",
        "p15_stg": "85.71%", "p15_drp": "42.86%", "p25_stg": "28.57%", "p25_drp": "42.86%",
        "gg_stg": "57.14%", "gg_drp": "42.86%", "p15_total": "64.20%", "p05_r1": "64.20%", "gg_total": "50.00%",
        "p15_w": "64.2%", "p05_w": "64.2%", "gg_w": "50%",
        "arbitru": "M. Turkmen &bull; 7/7 meciuri analizate"
    }
}

# 3. SECȚIUNEA DIN STÂNGA: WIDGET REALE + STATISTICI AUTOMATE PE ZILE
with col_meciuri:
    tab_global, tab_analiza = st.tabs(["🌍 TOATE MECIURILE LIVE", "📊 SELECTEAZĂ ȘI RECOMANDĂ MECI"])
    
    with tab_global:
        st.write("")
        st.markdown("""
            <div style="width:100%; height:550px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px;">
                <iframe src="https://scorebat.com" frameborder="0" width="100%" height="520px" allowfullscreen allow="autoplay; fullscreen"></iframe>
            </div>
        """, unsafe_allow_html=True)
        
    with tab_analiza:
        st.write("")
        
        # MENIUL DROPDOWN DE SELECȚIE MECI
        meci_selectat = st.selectbox("🎯 Alege meciul pentru afișarea analizei din bază:", list(meciuri_date.keys()))
        
        # Preluăm datele meciului selectat
        d = meciuri_date[meci_selectat]
        
        # Construim HTML-ul în siguranță totală fără variabile complexe în interiorul lui f-string
        html_grafic = f"""
        <div class="glass-box">
            <p style='text-align:center; color:#94a3b8; margin:0;'>MECI RECOMANDAT &bull; DATE LA ZI {data_azi}</p>
            <h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>{meci_selectat}</h2>
            <p style='text-align:center; color:#94a3b8; font-size:14px; margin-top:2px;'>{d['liga']}</p>
            <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
            <div class="stat-container">
                <div class="stat-row">
                    <div class="stat-left-val">{d['g_stg']}</div>
                    <div class="stat-center-label">Total goluri marcate</div>
                    <div class="stat-right-val">{d['g_drp']}</div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val">{d['m_stg']}</div>
                    <div class="stat-center-label">Medie goluri / meci</div>
                    <div class="stat-right-val">{d['m_drp']}</div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val">{d['gp_stg']}</div>
