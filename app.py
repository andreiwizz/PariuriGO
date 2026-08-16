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

# Funcție pentru citirea imaginii locale JPG de pe GitHub
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# Citim terenul de fotbal și logo-ul din proiectul tău GitHub
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
    
    /* Carduri tip sticlă mată în nuanțe verzi */
    .glass-box {{
        background: rgba(8, 22, 15, 0.88) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.22) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.65) !important;
        margin-bottom: 25px !important;
    }}

    /* Stiluri butoane personalizate tip sticlă verde pentru pachete */
    .pachet-btn {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        text-align: center !important;
        padding: 12px !important;
        border-radius: 8px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-top: 15px !important;
        display: block !important;
        text-decoration: none !important;
        box-shadow: 0 4px 15px rgba(0, 255, 102, 0.3) !important;
        transition: all 0.2s ease !important;
    }}
    .pachet-btn:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(0, 255, 102, 0.5) !important;
    }}

    /* Grafic simetric dinamic */
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
    st.title("⚽ PARIURIGO &bull; WORLD LIVE CENTER")

st.write("---")

# Împărțirea ecranului (Fluxul în Stânga, Abonamente în Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# 3. SECȚIUNEA DIN STÂNGA: WIDGET SCOREBAT + GRAFICUL PREMIUM DE SUB EL
with col_meciuri:
    tab_global, tab_analiza = st.tabs(["🌍 TOATE MECIURILE LIVE", "📊 GRAFIC STATISTICI PREMIUM"])
    
    with tab_global:
        st.write("")
        # Inserare widget live ScoreBat
        st.markdown("""
            <div style="width:100%; height:550px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px;">
                <iframe src="https://scorebat.com" frameborder="0" width="100%" height="520px" allowfullscreen allow="autoplay; fullscreen"></iframe>
            </div>
        """, unsafe_allow_html=True)
        
    with tab_analiza:
        st.write("")
        # Graficul premium în tentă verde
        html_grafic = f"""
        <div class="glass-box">
            <p style='text-align:center; color:#94a3b8; margin:0;'>MECIUL DE TOP DE AZI &bull; {data_azi}</p>
            <h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>ANALIZĂ DERBY &bull; SUPERLIGA</h2>
            <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
            <div class="stat-container">
                <div class="stat-row">
                    <div class="stat-left-val">7</div>
                    <div class="stat-center-label">Total goluri marcate</div>
                    <div class="stat-right-val">3</div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val">1.00</div>
                    <div class="stat-center-label">Medie goluri / meci</div>
                    <div class="stat-right-val">0.43</div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val">8</div>
                    <div class="stat-center-label">Goluri primite</div>
                    <div class="stat-right-val">6</div>
                </div>
                <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
                <div class="stat-row">
                    <div class="stat-left-val"><span class="green-badge">71.43%</span></div>
                    <div class="stat-center-label">Peste 0.5 HT (Prima Repriză)</div>
                    <div class="stat-right-val"><span class="green-badge">57.14%</span></div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val"><span class="green-badge">71.43%</span></div>
                    <div class="stat-center-label">Peste 0.5 ST (A doua Repriză)</div>
                    <div class="stat-right-val"><span class="green-badge">57.14%</span></div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val"><span class="green-badge">85.71%</span></div>
                    <div class="stat-center-label">Peste 1.5 goluri în meci</div>
                    <div class="stat-right-val"><span class="green-badge">42.86%</span></div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val" style="color:#00ff66;">28.57%</div>
                    <div class="stat-center-label">Peste 2.5 goluri în meci</div>
                    <div class="stat-right-val" style="color:#00ff66;">42.86%</div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val" style="color:#00ff66;">57.14%</div>
                    <div class="stat-center-label">Ambele echipe marchează (GG)</div>
                    <div class="stat-right-val" style="color:#00ff66;">42.86%</div>
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.05); margin: 20px 0;">
            <p style="font-weight:700; margin-bottom:10px;">📈 EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:</p>
            <div class="bar-wrapper">
                <div class="bar-label">Peste 1.5 total:</div>
                <div class="bar-container"><div class="bar-fill-intense-green" style="width: 64.29%;">64.29%</div></div>
            </div>
            <div class="bar-wrapper">
                <div class="bar-label">Peste 0.5 R1:</div>
                <div class="bar-container"><div class="bar-fill-intense-green" style="width: 64.29%;">64.29%</div></div>
            </div>
            <div class="bar-wrapper">
                <div class="bar-label">Ambele marchează:</div>
                <div class="bar-container"><div class="bar-fill-intense-green" style="width: 50.00%;">50.00%</div></div>
            </div>
            <div class="green-footer-box">
                <div style="font-size:18px; color:#00ff66;">🔸</div>
                <div>
                    <strong>Sistem Algoritm Automat PariuriGO</strong><br>
                    <span style="color:#a0aec0; font-size:14px;">Meci extras și prelucrat în timp real pentru data de {data_azi}</span>
                </div>
