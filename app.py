import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • Core VIP",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru injectarea imaginii teren.jpg cu opacitate perfect echilibrată
def aplica_fundal_teren_calibrat(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            /* Am setat opacitatea la 0.82 ca să fie o idee mai vizibil și mai clar terenul */
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.82), rgba(6, 4, 15, 0.86)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }
            
            /* Ascundem complet meniurile de fundal Streamlit */
            #MainMenu, footer, header { display: none !important; }
            div[data-testid="stToolbar"] { display: none !important; }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

# Activăm imaginea cu terenul în varianta perfect vizibilă, dar profesională
aplica_fundal_teren_calibrat("teren.jpg")
# ================== UPDATE ULTRAPRO: INTERFAȚA PREMIUM STIL BETANO ==================

# Injectăm CSS-ul pentru structura pe coloane, bara portocalie și cardurile cu meciuri
st.markdown("""
<style>
    /* 1. BARA DE SUS PORTOCALIE (IDENTICĂ BETANO) */
    .betano-header {
        background: linear-gradient(90deg, #f95700 0%, #ff6a00 100%) !important;
        padding: 12px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(249, 87, 0, 0.25);
    }
    .betano-logo { font-size: 24px; font-weight: 900; color: #ffffff !important; letter-spacing: -1px; }
    .betano-auth-buttons { display: flex; gap: 10px; }
    
    /* 2. BUTOANELE ALBE ȘI VERZI DE SUS */
    .btn-betano-white {
        background: rgba(255, 255, 255, 0.15) !important;
        color: #ffffff !important; border: 1px solid #ffffff !important;
        padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700;
    }
    .btn-betano-green {
        background: #00db66 !important; color: #000000 !important; border: none !important;
        padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700;
        box-shadow: 0 2px 8px rgba(0, 219, 102, 0.3);
    }

    /* 3. CARDURILE DE MECIURI MARI DE MIJLOC (SLIDERELE DIN IMAGINE) */
    .betano-match-card {
        background: rgba(20, 20, 28, 0.92) !important;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px; padding: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        margin-bottom: 15px;
    }
    .betano-badge-live { background: #ff0000; color: #ffffff; font-size: 9px; font-weight: 800; padding: 2px 6px; border-radius: 4px; }
    .betano-odds-row { display: flex; gap: 8px; margin-top: 12px; }
    
    /* Căsuțele cu cote 1 X 2 */
    .betano-odd-box {
        flex: 1; background: #222232; border: 1px solid #333348;
        border-radius: 6px; padding: 8px; text-align: center; font-weight: 800; color: #00ff66;
    }
    .betano-odd-box span { display: block; font-size: 11px; color: #8888a0; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ---- 1. RANDAREA BAREI PORTOCALII DE SUS ----
st.markdown("""
<div class="betano-header">
    <div class="betano-logo">PariuriGO</div>
    <div class="betano-auth-buttons">
        <button class="btn-betano-white">ÎNREGISTRARE</button>
        <button class="btn-betano-green">CONECTARE</button>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- 2. STRUCTURA PE 3 COLOANE (MENIU STÂNGA | MECIURI MIJLOC | BILET DREAPTA) ----
col_stanga, col_mijloc, col_dreapta = st.columns([0.8, 2.2, 1.0], gap="medium")

# COLOANA 1: MENIUL LATERAL (SPORTURI)
with col_stanga:
    st.markdown("<p style='color:#ff6a00; font-weight:800; font-size:12px; margin-bottom:10px;'>📌 FAVORITE</p>", unsafe_allow_html=True)
    st.button("🇷🇴 Liga 1 România", key="menu_l1")
    st.button("🇪🇺 Liga Campionilor", key="menu_champs")
    st.button("🎮 CS2 Esports Pro", key="menu_cs2")
    
    st.write("")
    st.markdown("<p style='color:#888; font-weight:800; font-size:12px; margin-bottom:10px;'>⚽ SPORTURI</p>", unsafe_allow_html=True)
    st.caption("Fotbal • Tenis • Baschet • Handbal")

# COLOANA 2: PANOU CENTRAL (CARDURILE DE MECIURI TOP CU COTE INTERACTIVE)
with col_mijloc:
    st.markdown("<p style='color:#ffffff; font-weight:800; font-size:16px; margin-bottom:15px;'>🔥 MECIURI RECOMANDATE ÎN ACTION</p>", unsafe_allow_html=True)
    
    # Meciul 1 din Imagine
    st.markdown("""
    <div class="betano-match-card">
        <span class="betano-badge-live">DISEARĂ 21:45</span>
        <span style="color:#8888a0; font-size:12px; float:right;">🏆 UEFA EUROPA LEAGUE</span>
        <h3 style="margin: 8px 0; font-size: 18px; font-weight: 800;">LASK Linz vs FCSB</h3>
        <p style="color:#cbd5e1; font-size:12px; margin:0;">💡 Recomandare Algoritm: <b style="color:#00ff66;">Peste 1.5 goluri</b></p>
        <div class="betano-odds-row">
            <div class="betano-odd-box"><span>1</span>2.20</div>
            <div class="betano-odd-box"><span>X</span>3.40</div>
            <div class="betano-odd-box"><span>2</span>3.10</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Meciul 2 din Imagine
    st.markdown("""
    <div class="betano-match-card">
        <span class="betano-badge-live" style="background:#ff6a00;">LIVE MIN 62</span>
        <span style="color:#8888a0; font-size:12px; float:right;">🏆 SUPERLIGA</span>
        <h3 style="margin: 8px 0; font-size: 18px; font-weight: 800;">CFR Cluj vs Pafos FC</h3>
        <p style="color:#cbd5e1; font-size:12px; margin:0;">💡 Recomandare Algoritm: <b style="color:#00ff66;">1 Solist</b></p>
        <div class="betano-odds-row">
            <div class="betano-odd-box" style="border-color:#ff6a00;"><span>1</span>1.65</div>
            <div class="betano-odd-box"><span>X</span>3.75</div>
            <div class="betano-odd-box"><span>2</span>5.20</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# COLOANA 3: BILETUL MEU (PANOU DREAPTA SPECIFIC BETANO)
with col_dreapta:
    with st.container(border=True):
        st.markdown("<p style='font-weight:800; font-size:14px; margin:0; text-align:center;'>📋 BILETUL MEU VIP</p>", unsafe_allow_html=True)
        st.write("---")
        st.caption("• LASK Linz vs FCSB ➡️ Peste 1.5 goluri (1.35)")
        st.caption("• CFR Cluj vs Pafos FC ➡️ 1 Solist (1.60)")
        st.write("---")
        st.metric(label="💰 COTĂ TOTALĂ", value="2.16")
        st.link_button("🔒 DEBLOCHEAZĂ BILETUL PRIN STRIPE", "https://stripe.com", use_container_width=True)
