import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="GoldenTips Professional Clone",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru transformarea imaginii locale teren.jpg în fundal web
def aplica_fundal_teren_calibrat(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            @import url('https://googleapis.com');
            
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.85), rgba(6, 4, 15, 0.88)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
                color: #ffffff !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }
            
            h1, h2, h3, h4, p, span, label { font-family: 'Plus Jakarta Sans', sans-serif !important; }

            #MainMenu, footer, header { display: none !important; }
            div[data-testid="stToolbar"] { display: none !important; }

            /* BARA DE SUS VERDE NEON (BRANDING BETGO) */
            .betgo-header {
                background: linear-gradient(90deg, #001675 0%, #00d6ff 100%) !important;
                padding: 12px 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-radius: 8px;
                margin-bottom: 20px;
                box-shadow: 0 4px 15px rgba(0, 220, 118, 0.25);
            }
            .betgo-logo { font-size: 24px; font-weight: 950; color: #ffffff !important; letter-spacing: -1px; }
            .betgo-auth-buttons { display: flex; gap: 10px; }
            
            .btn-betgo-black { background: rgba(0, 0, 0, 0.2) !important; color: #ffffff !important; border: 1px solid #ffffff !important; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700; }
            .btn-betgo-dark { background: #111111 !important; color: #001675 !important; border: none !important; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4); }

            /* STRUCTURA DE RÂNDURI ORIZONTALE A MECIURILOR */
            .betgo-row-container {
                background: rgba(255, 255, 255, 0.96) !important;
                border-bottom: 1px solid #e2e8f0;
                padding: 12px 16px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 4px;
                border-radius: 6px;
            }

            .betgo-row-left {
                display: flex;
                align-items: center;
                gap: 15px;
                width: 45%;
            }

            .betgo-time-box {
                font-size: 11px;
                color: #ef4444;
                font-weight: 700;
                text-align: center;
                min-width: 45px;
                line-height: 1.2;
            }

            .betgo-time-gray { color: #64748b !important; }

            .betgo-teams-block {
                display: flex;
                flex-direction: column;
                gap: 2px;
            }

            .betgo-team-name {
                font-size: 14px;
                font-weight: 800;
                color: #1e293b !important;
            }

            .betgo-meta-info {
                font-size: 11px;
                color: #94a3b8;
                font-weight: 600;
            }

            .betgo-row-right {
                display: flex;
                gap: 6px;
                width: 50%;
                justify-content: flex-end;
            }

            .betgo-bet-button {
                background: #f8fafc !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 6px !important;
                padding: 10px 0 !important;
                width: 95px !important;
                text-align: center !important;
                display: flex !important;
                justify-content: space-between !important;
                padding-left: 12px !important;
                padding-right: 12px !important;
                align-items: center !important;
            }

            .betgo-label-odd { font-size: 11px; color: #64748b; font-weight: 600; }
            .betgo-val-odd { font-size: 13px; color: #001675; font-weight: 800; }

            /* Subsol de avertizare joc responsabil */
            .betgo-footer-compliance {
                background: rgba(15, 15, 22, 0.7) !important;
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                padding: 15px;
                text-align: center;
                margin-top: 30px;
            }
            .compliance-badge {
                background: #ff5700;
                color: #ffffff !important;
                font-size: 11px;
                font-weight: 800;
                padding: 3px 10px;
                border-radius: 6px;
                display: inline-block;
                margin-bottom: 8px;
            }
            .compliance-text {
                font-size: 12px;
                color: #94a3b8;
                line-height: 1.5;
                margin: 0;
            }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

# Activăm imaginea cu terenul
aplica_fundal_teren_calibrat("teren.jpg")

# ---- BARA DE SUS DIN BRADINGUL NOULUI COD ----
st.markdown("""
<div class="betgo-header">
    <div class="betgo-logo">BetGO</div>
    <div class="betgo-auth-buttons">
        <button class="btn-betgo-black">ÎNREGISTRARE</button>
        <button class="btn-betgo-dark">CONECTARE</button>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- STRUCTURA PE 3 COLOANE ----
col_stanga, col_mijloc, col_dreapta = st.columns([0.7, 2.3, 1.0], gap="medium")

with col_stanga:
    st.markdown("<p style='color:#00d6ff; font-weight:800; font-size:12px; margin-bottom:10px;'>📌 FAVORITE</p>", unsafe_allow_html=True)
    st.button("🇲🇩 Superliga Națională", key="fav_l1_betgo")
    st.button("🇪🇺 UEFA Champions League", key="fav_ucl_betgo")
    st.button("🇪🇺 UEFA Europa League", key="fav_uel_betgo")

with col_mijloc:
    st.markdown("<p style='color:#ffffff; font-weight:800; font-size:15px; margin-bottom:12px;'>⚽ MECIURI ACTIVE &bull; PRELIMINARII</p>", unsafe_allow_html=True)
    
    # RÂNDUL 1
    st.markdown("""
    <div class="betgo-row-container">
        <div class="betgo-row-left">
            <div class="betgo-time-box">20.08<br><span class="betgo-time-gray">20:00</span></div>
            <div class="betgo-teams-block">
                <div class="betano-team-name">LASK Linz</div>
                <div class="betano-team-name">FCSB 🇷🇴</div>
                <div class="betgo-meta-info">Europa League &bull; Play-off</div>
            </div>
        </div>
        <div class="betgo-row-right">
            <div class="betgo-bet-button"><span>1</span><span class="betgo-val-odd">2.15</span></div>
            <div class="betgo-bet-button"><span>X</span><span class="betgo-val-odd">3.40</span></div>
            <div class="betgo-bet-button" style="border-color:#00d6ff; background:rgba(0,214,255,0.03);"><span style="color:#00d6ff; font-weight:600; font-size:11px;">2 VIP</span><span style="color:#00d6ff; font-weight:800; font-size:13px;">3.25</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # RÂNDUL 2
    st.markdown("""
    <div class="betgo-row-container">
        <div class="betgo-row-left">
            <div class="betgo-time-box" style="color:#00d6ff;">LIVE<br>Min 42</div>
            <div class="betgo-teams-block">
                <div class="betano-team-name">CFR Cluj 🇷🇴</div>
                <div class="betano-team-name">Pafos FC</div>
                <div class="betgo-meta-info">Conference League &bull; Play-off</div>
            </div>
        </div>
        <div class="betgo-row-right">
            <div class="betgo-bet-button" style="border-color:#00d6ff; background:rgba(0,214,255,0.03);"><span style="color:#00d6ff; font-weight:600; font-size:11px;">1 VIP</span><span style="color:#00d6ff; font-weight:800; font-size:13px;">1.62</span></div>
            <div class="betgo-bet-button"><span>X</span><span class="betgo-val-odd">3.75</span></div>
            <div class="betgo-bet-button"><span>2</span><span class="betgo-val-odd">5.40</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_dreapta:
    with st.container(border=True):
        st.markdown("<p style='font-weight:800; font-size:14px; margin:0; text-align:center;'>📋 BILETUL NOSTRU VIP</p>", unsafe_allow_html=True)
        st.write("---")
        st.caption("• LASK Linz vs FCSB ➡️ Peste 1.5 goluri (1.35)")
        st.caption("• CFR Cluj vs Pafos FC ➡️ 1 Solist (1.60)")
        st.write("---")
        st.metric(label="💰 COTĂ RECOMANDATĂ", value="2.16")
        st.link_button("🔒 DEBLOCHEAZĂ CONT PRIN STRIPE", "https://stripe.com", use_container_width=True)

# BARA DE COMPLIANCE DE JOS PENTRU JOC RESPONSABIL
st.markdown("""
<div class="betgo-footer-compliance">
    <div class="compliance-badge">🔞 JUCAȚI RESPONSABIL</div>
    <p class="compliance-text">
