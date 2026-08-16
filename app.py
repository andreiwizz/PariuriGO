import streamlit as st
import base64

# 1. Configurare Pagină (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
    div[data-testid="stVerticalBlockBorder"] {{
        background: rgba(8, 22, 15, 0.86) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.22) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.65) !important;
        margin-bottom: 25px !important;
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
    .bar-fill-soft-green {{ height: 100%; background: linear-gradient(90deg, #024c1c 0%, #00bc43 100%); border-radius: 8px; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; font-size: 13px; font-weight: 800; color: #ffffff; }}
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

# 3. SECȚIUNEA DIN STÂNGA: REPARATĂ CU JOCURI REALE ȘI STATISTICI PE SATE
with col_meciuri:
    # Am creat două secțiuni separate (Tab-uri clare) ca Streamlit să nu mai ascundă graficul sub ScoreBat
    tab_global, tab_analiza = st.tabs(["🌍 TOATE MECIURILE LIVE", "📊 GRAFIC STATISTICI PREMIUM"])
    
    with tab_global:
        st.caption("Scoruri reale din toată lumea actualizate automat secundă de secundă.")
        # Inserare widget live ScoreBat
        st.markdown("""
            <div style="width:100%; height:550px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px;">
                <iframe src="https://scorebat.com" frameborder="0" width="100%" height="520px" allowfullscreen allow="autoplay; fullscreen"></iframe>
            </div>
        """, unsafe_allow_html=True)
        
    with tab_analiza:
        st.caption("Analiză matematică avansată bazată pe istoricul meciurilor.")
        # Graficul tău premium copiat exact din poză, în tentă verde
        with st.container():
            st.markdown("<p style='text-align:center; color:#94a3b8; margin:0;'>SUPER LIG &bull; TURKEY</p>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>BAȘAKȘEHIR vs KOCAELISPOR</h2>", unsafe_allow_html=True)
            st.write("---")
            
            st.markdown("""
            <div class="stat-container">
                <div class="stat-row">
                    <div class="stat-left-val">7</div>
                    <div class="stat-center-label">Total goluri marcate</div>
                    <div class="stat-right-val">3</div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val">1.00</div>
                    <div class="stat-center-label">Medie goluri</div>
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
                    <div class="stat-center-label">Peste 0.5 HT</div>
                    <div class="stat-right-val"><span class="green-badge">57.14%</span></div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val"><span class="green-badge">71.43%</span></div>
                    <div class="stat-center-label">Peste 0.5 ST</div>
                    <div class="stat-right-val"><span class="green-badge">57.14%</span></div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val"><span class="green-badge">85.71%</span></div>
                    <div class="stat-center-label">Peste 1.5 goluri</div>
                    <div class="stat-right-val"><span class="green-badge">42.86%</span></div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val" style="color:#00ff66;">28.57%</div>
                    <div class="stat-center-label">Peste 2.5 goluri</div>
                    <div class="stat-right-val" style="color:#00ff66;">42.86%</div>
                </div>
                <div class="stat-row">
                    <div class="stat-left-val" style="color:#00ff66;">57.14%</div>
                    <div class="stat-center-label">Ambele marchează</div>
                    <div class="stat-right-val" style="color:#00ff66;">42.86%</div>
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.05); margin: 20px 0;">
            """, unsafe_allow_html=True)
            
            st.write("**📈 EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:**")
            st.markdown("""
            <div class="bar-wrapper">
                <div class="bar-label">Peste 1.5:</div>
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
                <div style="font-size:20px; color:#00ff66;">🔸</div>
                <div>
                    <strong>Stats arbitru &bull; probabilitate matematică</strong><br>
                    <span style="color:#a0aec0; font-size:14px;">M. Turkmen &bull; 7/7 meciuri din ligă analizate cu succes</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# 4. SECȚIUNE ABONAMENTE VIP (Dreapta)
with col_abonamente:
    st.subheader("🏆 Abonamente VIP")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
