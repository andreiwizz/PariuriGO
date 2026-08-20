import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="BetGO • Core VIP",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru injectarea imaginii teren.jpg cu opacitate
def aplica_fundal_teren_calibrat(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.85), rgba(6, 4, 15, 0.88)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }
            #MainMenu, footer, header { display: none !important; }
            div[data-testid="stToolbar"] { display: none !important; }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

aplica_fundal_teren_calibrat("teren.jpg")

# Structură CSS: Bara Verde & Grila de Meciuri Albă
st.markdown("""
<style>
    /* 1. BARA DE SUS VERDE NEON (BRANDING BETGO) */
    .betgo-header {
        background: linear-gradient(90deg, #00E676 0%, #00B0FF 100%) !important;
        padding: 12px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 230, 118, 0.25);
    }
    .betgo-logo { font-size: 24px; font-weight: 900; color: #000000 !important; letter-spacing: -1px; }
    .betgo-auth-buttons { display: flex; gap: 10px; }
    
    .btn-betgo-black {
        background: rgba(0, 0, 0, 0.2) !important;
        color: #000000 !important; border: 1px solid #000000 !important;
        padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700;
    }
    .btn-betgo-dark {
        background: #111115 !important; color: #00E676 !important; border: none !important;
        padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }

    /* 2. CARDURILE DE MECIURI STIL GRILĂ ALBĂ CURATĂ */
    .match-row-white {
        background: #ffffff !important;
        color: #111111 !important;
        border-radius: 8px;
        padding: 12px 18px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        border-left: 5px solid #00E676;
    }
    .match-teams { font-size: 15px; font-weight: 800; color: #111; }
    .match-league { font-size: 11px; color: #666; font-weight: 600; }
    
    /* Caseta Cota Verde */
    .odd-tag {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #15803d;
        font-weight: 800;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ---- 1. RANDAREA BAREI VERZI DE SUS ----
st.markdown("""
<div class="betgo-header">
    <div class="betgo-logo">⚡ BetGO</div>
    <div class="betgo-auth-buttons">
        <button class="btn-betgo-black">ÎNREGISTRARE</button>
        <button class="btn-betgo-dark">CONECTARE</button>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- 2. STRUCTURA PE 3 COLOANE ----
col_stanga, col_mijloc, col_dreapta = st.columns([0.8, 2.2, 1.0], gap="medium")

# COLOANA 1: MENIUL LATERAL
with col_stanga:
    st.markdown("<p style='color:#00E676; font-weight:800; font-size:12px; margin-bottom:10px;'>📌 FAVORITE</p>", unsafe_allow_html=True)
    st.button("🇷🇴 Liga 1 România", key="menu_l1")
    st.button("🇪🇺 Liga Campionilor", key="menu_champs")
    st.button("🎮 CS2 Esports Pro", key="menu_cs2")
    
    st.write("")
    st.markdown("<p style='color:#888; font-weight:800; font-size:12px; margin-bottom:10px;'>⚽ SPORTURI</p>", unsafe_allow_html=True)
    st.caption("Fotbal • Tenis • Baschet • Handbal")

# COLOANA 2: PANOU CENTRAL - GRILĂ MECIURI
with col_mijloc:
    st.markdown("<p style='color:#ffffff; font-weight:800; font-size:16px; margin-bottom:15px;'>🔥 MECIURI RECOMANDATE ÎN ACTION</p>", unsafe_allow_html=True)
    
    meciuri = [
        {"meci": "LASK Linz vs FCSB", "liga": "UEFA Europa League", "pronostic": "Peste 1.5 goluri", "cota": "1.35"},
        {"meci": "CFR Cluj vs Pafos FC", "liga": "Superliga", "pronostic": "1 Solist", "cota": "1.65"},
        {"meci": "Universitatea Craiova vs FC Ararat-Armenia", "liga": "Liga Europa", "pronostic": "1 Solist", "cota": "1.40"},
        {"meci": "FC Inter Turku vs FC Copenhagen", "liga": "Conference League", "pronostic": "2 Solist", "cota": "1.85"},
        {"meci": "SL Benfica vs Aarhus GF", "liga": "Liga Europa", "pronostic": "Peste 2.5 Goluri", "cota": "1.55"}
    ]

    for m in meciuri:
        st.markdown(f"""
        <div class="match-row-white">
            <div>
                <div class="match-teams">{m['meci']}</div>
                <div class="match-league">🏆 {m['liga']} &nbsp;•&nbsp; Tip: <b style="color:#00c853;">{m['pronostic']}</b></div>
            </div>
            <div class="odd-tag">Cotă {m['cota']}</div>
        </div>
        """, unsafe_allow_html=True)

# COLOANA 3: BILETUL MEU (PANOU DREAPTA)
with col_dreapta:
    with st.container(border=True):
        st.markdown("<p style='font-weight:800; font-size:14px; margin:0; text-align:center;'>📋 BILETUL MEU VIP</p>", unsafe_allow_html=True)
        st.write("---")
        st.caption("• LASK Linz vs FCSB ➡️ Peste 1.5 goluri (1.35)")
        st.caption("• CFR Cluj vs Pafos FC ➡️ 1 Solist (1.60)")
        st.write("---")
        st.metric(label="💰 COTĂ TOTALĂ", value="2.16")
        st.link_button("🔒 DEBLOCHEAZĂ BILETUL PRIN STRIPE", "https://stripe.com", use_container_width=True)
