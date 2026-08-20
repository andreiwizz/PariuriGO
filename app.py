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
                background: linear-gradient(rgba(4, 3, 8, 0.82), rgba(6, 4, 15, 0.86)), 
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

# Stylings CSS: Header Verde Neon & Grila curată de meciuri
st.markdown("""
<style>
    /* Header Verde Neon */
    .header-verde {
        background: linear-gradient(90deg, #00E676 0%, #00B0FF 100%);
        padding: 15px 25px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #000;
        font-weight: 800;
        box-shadow: 0 4px 20px rgba(0, 230, 118, 0.3);
        margin-bottom: 25px;
    }

    /* Grilă stilizată Meciuri (Card alb curat) */
    .match-row {
        background: #ffffff;
        color: #1a1a1a;
        padding: 12px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #00E676;
    }
    
    .team-name {
        font-weight: 700;
        font-size: 15px;
        color: #111;
    }

    .league-sub {
        font-size: 11px;
        color: #666;
    }

    .odd-box {
        background: #f0f2f5;
        border-radius: 6px;
        padding: 6px 12px;
        font-weight: bold;
        color: #008744;
        font-size: 14px;
        border: 1px solid #e0e0e0;
    }

    /* Caseta de Login */
    .google-login-box {
        max-width: 420px;
        margin: 60px auto;
        background: rgba(13, 11, 22, 0.85) !important;
        backdrop-filter: blur(25px);
        border: 1px solid rgba(0, 230, 118, 0.2);
        border-radius: 24px;
        padding: 30px 24px;
        box-shadow: 0 30px 70px -15px rgba(0, 230, 118, 0.2);
        text-align: center;
    }

    div.stButton > button {
        background-color: #ffffff !important;
        color: #1f1f1f !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

if "utilizator_autentificat_google" not in st.session_state:
    st.session_state.utilizator_autentificat_google = False

# ---- ECRANUL A: LOGARE ----
if not st.session_state.utilizator_autentificat_google:
    st.markdown('<div class="google-login-box">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-size:34px; font-weight:800; color:#00E676; margin-bottom:5px;'>BetGO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-bottom:35px;'>Conectează-te cu Google pentru acces VIP</p>", unsafe_allow_html=True)
    
    if st.button("🔴 &nbsp; Sign in with Google", key="google_auth_btn"):
        st.session_state.utilizator_autentificat_google = True
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# ---- ECRANUL B: INTERFAȚA VIP CU GRILĂ DE MECIURI ----
else:
    # Header Verde Nativ
    st.markdown("""
        <div class="header-verde">
            <span style="font-size:22px;">⚡ BetGO VIP</span>
            <span style="font-size:14px; background:rgba(0,0,0,0.15); padding:4px 12px; border-radius:20px;">
                🟢 CONECTAT
            </span>
        </div>
    """, unsafe_allow_html=True)

    # Grila Curată de Meciuri
    meciuri_demo = [
        {"meci": "Universitatea Craiova vs FC Ararat-Armenia", "liga": "Liga Europa", "pronostic": "1 Solist", "cota": "1.40"},
        {"meci": "FC Inter Turku vs FC Copenhagan", "liga": "Conference League", "pronostic": "2 Solist", "cota": "1.85"},
        {"meci": "SL Benfica vs Aarhus GF", "liga": "Liga Europa", "pronostic": "Peste 2.5 Goluri", "cota": "1.55"},
        {"meci": "Trabzonspor vs Ferencvarosi TC", "liga": "Liga Europa", "pronostic": "Ambele Marchează", "cota": "1.78"},
        {"meci": "LASK Linz vs FCSB", "liga": "UEFA Europa League", "pronostic": "Peste 1.5 Goluri", "cota": "1.35"}
    ]

    st.subheader("🔥 Ponturi Recomandate (Grilă Directă)")
    
    for m in meciuri_demo:
        st.markdown(f"""
            <div class="match-row">
                <div>
                    <div class="team-name">{m['meci']}</div>
                    <div class="league-sub">🏆 {m['liga']} • Pronostic: <b>{m['pronostic']}</b></div>
                </div>
                <div class="odd-box">Cotă {m['cota']}</div>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")
    if st.button("🔒 Deconectare Cont", key="logout_btn"):
        st.session_state.utilizator_autentificat_google = False
        st.rerun()
