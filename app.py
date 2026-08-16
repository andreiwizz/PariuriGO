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

data_azi = datetime.now().strftime("%d.%m.%Y")

# Funcție securizată pentru citirea imaginii de fundal de pe GitHub
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
    
    h1, h2, h3, h4, p, span, label {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Carduri tip sticlă mată în nuanțe verzi */
    .pachet-box {{
        background: rgba(8, 22, 15, 0.9) !important;
        border: 1px solid rgba(0, 255, 102, 0.3) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.7) !important;
        margin-bottom: 25px !important;
    }}

    /* Selectbox custom să arate bombă pe verde */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: rgba(10, 30, 18, 0.9) !important;
        border: 1px solid #00ff66 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }}

    /* Barele de progres native configurate pe verde aprins */
    div[data-testid="stProgress"] div[role="progressbar"] {{
        background: linear-gradient(90deg, #008f33 0%, #00ff66 100%) !important;
    }}
    
    /* Forțare butoane mari verzi, mereu vizibile */
    .stButton > button {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(0, 255, 102, 0.3) !important;
    }}
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

# BAZA DE DATE CURATĂ PENTRU MECIURILE REALE
meciuri_date = {
    "FCSB vs Rapid București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gazde": "14", "g_oaspeti": "11",
        "m_gazde": "1.75", "m_oaspeti": "1.37",
        "gp_gazde": "5", "gp_oaspeti": "9",
        "p_ht": "85.71%", "d_ht": "71.43% Oaspeți",
        "p_st": "78.50%", "d_st": "64.25% Oaspeți",
        "p_15": "91.20%", "d_15": "78.50% Oaspeți",
        "p_25": "64.29%", "d_25": "50.00% Oaspeți",
        "p_gg": "71.43%", "d_gg": "57.14% Oaspeți",
        "prog_15": 0.85, "prog_05": 0.78, "prog_gg": 0.64,
        "arbitru": "Radu Petrescu &bull; 5/5 meciuri analizate"
    },
    "CFR Cluj vs Universitatea Craiova": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gazde": "11", "g_oaspeti": "13",
        "m_gazde": "1.37", "m_oaspeti": "1.62",
        "gp_gazde": "7", "gp_oaspeti": "6",
        "p_ht": "75.00%", "d_ht": "62.50% Oaspeți",
        "p_st": "87.50%", "d_st": "75.00% Oaspeți",
        "p_15": "87.50%", "d_15": "75.00% Oaspeți",
        "p_25": "50.00%", "d_25": "62.50% Oaspeți",
        "p_gg": "62.50%", "d_gg": "62.50% Oaspeți",
        "prog_15": 0.81, "prog_05": 0.68, "prog_gg": 0.62,
        "arbitru": "Istvan Kovacs &bull; 8/8 meciuri analizate"
    },
    "Oțelul Galați vs Dinamo București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gazde": "8", "g_oaspeti": "10",
        "m_gazde": "1.00", "m_oaspeti": "1.25",
        "gp_gazde": "4", "gp_oaspeti": "8",
        "p_ht": "50.00%", "d_ht": "50.00% Oaspeți",
        "p_st": "62.50%", "d_st": "75.00% Oaspeți",
        "p_15": "62.50%", "d_15": "75.00% Oaspeți",
        "p_25": "25.00%", "d_25": "50.00% Oaspeți",
        "p_gg": "37.50%", "d_gg": "50.00% Oaspeți",
        "prog_15": 0.68, "prog_05": 0.50, "prog_gg": 0.43,
        "arbitru": "Marian Barbu &bull; 4/4 meciuri analizate"
    },
    "Bașakșehir vs Kocaelispor": {
        "liga": "SUPER LIG &bull; TURKEY",
        "g_gazde": "7", "g_oaspeti": "3",
        "m_gazde": "1.00", "m_oaspeti": "0.43",
        "gp_gazde": "8", "gp_oaspeti": "6",
        "p_ht": "71.43%", "d_ht": "57.14% Oaspeți",
        "p_st": "71.43%", "d_st": "57.14% Oaspeți",
        "p_15": "85.71%", "d_15": "42.86% Oaspeți",
        "p_25": "28.57%", "d_25": "42.86% Oaspeți",
        "p_gg": "57.14%", "d_gg": "42.86% Oaspeți",
        "prog_15": 0.64, "prog_05": 0.64, "prog_gg": 0.50,
        "arbitru": "M. Turkmen &bull; 7/7 meciuri analizate"
    }
}

# 3. SECȚIUNEA DIN STÂNGA: LIVESCORE MONDIAL + GRAFIC SELECTABIL
with col_meciuri:
    st.subheader("🌍 Meciuri Live din Toate Ligele Lumii (Flashscore Global)")
    
    # NOU: Widget oficial Livescore.in / Flashscore. Toate meciurile din lume, live real!
    st.markdown("""
        <div style="width:100%; height:480px; overflow:auto; background:#111111; border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:5px;">
            <iframe src="https://livescore.in" frameborder="0" width="100%" height="450px" allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📊 Meniu Selectare și Grafic Procente")
    
    meci_ales = st.selectbox("🎯 ALEGE MECIUL DE AZI PENTRU RECOMANDARE VIZUALĂ:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]
    
    st.markdown(f"<p style='text-align:center; color:#94a3b8; margin:0;'>MECIUL SELECTAT &bull; DATE LA ZI {data_azi}</p>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>{meci_ales}</h2>", unsafe_allow_html=True)
    st.caption(f"<p style='text-align:center; color:#a0aec0;'>{m['liga']}</p>", unsafe_allow_html=True)
    st.write("---")
    
    c1, c2, c3 = st.columns(3)
    c1.metric(label="⚽ GOLURI MARCATE (Gazde)", value=m["g_gazde"])
    c2.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>TOTAL GOLURI MARCATE</p>", unsafe_allow_html=True)
    c3.metric(label="⚽ GOLURI MARCATE (Oaspeți)", value=m["g_oaspeti"])
    
    c4, c5, c6 = st.columns(3)
    c4.metric(label="📈 MEDIE GOLURI (Gazde)", value=m["m_gazde"])
    c5.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>MEDIE GOLURI / MECI</p>", unsafe_allow_html=True)
    c6.metric(label="📈 MEDIE GOLURI (Oaspeți)", value=m["m_oaspeti"])
    
    st.write("---")
    st.write("**📋 Procente Evenimente:**")
    cx1, cx2, cx3 = st.columns(3)
    cx1.metric(label="🟢 PESTE 0.5 HT", value=m["p_ht"], delta=m["d_ht"], delta_color="off")
    cx2.metric(label="🟢 PESTE 0.5 ST", value=m["p_st"], delta=m["d_st"], delta_color="off")
    cx3.metric(label="🟢 PESTE 1.5 GOLURI", value=m["p_15"], delta=m["d_15"], delta_color="off")
    
    st.write("---")
    st.write("**📈 BARE EVOLUȚIE PROBABILITĂȚI GLOBAL:**")
    st.write(f"🔹 Peste 1.5 total: **{int(m['prog_15']*100)}%**")
    st.progress(m['prog_15'])
    st.write(f"🔹 Peste 0.5 R1: **{int(m['prog_05']*100)}%**")
    st.progress(m['prog_05'])
    st.write(f"🔹 Ambele echipe marchează (GG): **{int(m['prog_gg']*100)}%**")
    st.progress(m['prog_gg'])

# 4. SECȚIUNE ABONAMENTE VIP STRUCTURATĂ LINIAR (Fără tab-uri care se ascund)
with col_abonamente:
    st.subheader("🏆 Toate Abonamentele VIP")
    
    link_telegram_afacere = "https://t.me"
    
    # 1. LOW
    st.markdown('<div class="pachet-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#00ff66; margin:0;'>🟢 PACHET LOW</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin:5px 0;'>40 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
    st.write("📋 **Beneficii incluse:**")
    st.write("• 3 Bilete gata analizate pe săptămână")
    st.write("• Cote sigure selectate din ligile mari")
    st.write("• Acces grup comunitate chat")
    if st.button("CUMPĂRĂ PACHET LOW 🚀", key="btn_l"):
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link_telegram_afacere}\'">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. MEDIUM
    st.markdown('<div class="pachet-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#eab308; margin:0;'>🟡 PACHET MEDIUM</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin:5px 0;'>70 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
    st.write("📋 **Beneficii incluse:**")
    st.write("• 1 Bilet Premium în fiecare zi calendaristică")
    st.write("• Procente și probabilități avansate live")
    st.write("• Notificări instant pe Telegram")
