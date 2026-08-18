import streamlit as st
import base64
import os

# 1. Configurare pagină (Full Screen)
st.set_page_config(page_title="PariuriGo • Live Center", page_icon="⚽", layout="wide")

# Funcție pentru a converti imaginea locală într-un fundal CSS
def adauga_imagine_fundal(nume_fisier):
    if os.path.exists(nume_fisier):
        with open(nume_fisier, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(5, 11, 14, 0.85), rgba(5, 11, 14, 0.85)), url("data:image/jpg;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        # Fallback în caz că imaginea nu este găsită încă pe GitHub
        st.markdown(
            """
            <style>
            .stApp { background-color: #050b0e; color: #ffffff; font-family: 'Segoe UI', sans-serif; }
            </style>
            """,
            unsafe_allow_html=True
        )

# Aplică fundalul din fișierul tău
adauga_imagine_fundal("fundal.jpg")

# 2. Injectare restul de stiluri CSS pentru carduri (păstrând transparența peste fundal)
st.markdown("""
    <style>
    /* Header principal */
    .main-header { font-size: 28px; font-weight: bold; letter-spacing: 1px; color: #ffffff; margin-bottom: 5px; }
    .sub-header-text { color: #8a9da8; font-size: 11px; margin-bottom: 30px; }
    
    /* Titluri secțiuni */
    .section-title { font-size: 16px; font-weight: bold; color: #ffffff; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }
    
    /* Card meci Live (Oțelul vs Craiova) - fundal ușor transparent pentru a lăsa poza să se vadă discret */
    .live-card { background-color: rgba(10, 17, 22, 0.9); border: 1px solid #14222b; border-radius: 8px; padding: 20px; margin-bottom: 20px; position: relative; }
    .live-badge { background-color: #4c1c1f; color: #ff4d4d; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 4px; display: inline-block; margin-bottom: 15px; }
    .league-tag { float: right; color: #5f7582; font-size: 11px; font-weight: bold; text-transform: uppercase; }
    
    /* Scor și echipe */
    .teams-container { text-align: center; margin: 15px 0; font-size: 22px; font-weight: bold; }
    .team-home { color: #00ff87; }
    .score { color: #ffffff; margin: 0 20px; font-size: 26px; }
    .team-away { color: #00ff87; }
    
    /* Grid de statistici live */
    .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); text-align: center; margin-top: 25px; padding-top: 15px; border-top: 1px solid #14222b; }
    .stat-label { color: #5f7582; font-size: 10px; text-transform: uppercase; font-weight: bold; margin-bottom: 5px; }
    .stat-values { font-size: 18px; font-weight: bold; color: #ffffff; }
    
    /* Caseta Sugestie AI */
    .ai-box { background-color: #091715; border-left: 4px solid #00ff87; border-radius: 4px; padding: 12px; margin-top: 20px; }
    .ai-title { color: #00ff87; font-size: 11px; font-weight: bold; text-transform: uppercase; margin-bottom: 5px; }
    .ai-content { color: #ffffff; font-size: 13px; font-weight: 500; }
    
    /* Card meci Pre-meci (Corvinul vs CFR Cluj) */
    .prematch-card { background-color: rgba(10, 17, 22, 0.9); border: 1px solid #14222b; border-radius: 8px; padding: 20px; margin-bottom: 20px; }
    .prematch-badge { background-color: #162a35; color: #00bfff; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 4px; display: inline-block; margin-bottom: 15px; }
    .prematch-teams { text-align: center; font-size: 18px; font-weight: bold; margin: 20px 0; color: #ffffff; }
    .vs-text { color: #5f7582; font-size: 14px; font-weight: normal; margin: 0 15px; }
    
    /* Căsuțe Cote 1X2 */
    .odds-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 15px; }
    .odd-box { background-color: #111e27; border: 1px solid #1a2f3d; border-radius: 4px; padding: 10px; text-align: center; font-size: 12px; color: #ffffff; font-weight: 500; }
    
    /* Caseta Recomandare Tipster */
    .tipster-box { background-color: #1a1910; border-left: 4px solid #ffcc00; border-radius: 4px; padding: 12px; margin-top: 20px; }
    .tipster-title { color: #ffcc00; font-size: 11px; font-weight: bold; text-transform: uppercase; margin-bottom: 5px; }
    .tipster-content { color: #ffffff; font-size: 13px; font-weight: 500; }
    
    /* Coloana din dreapta - Card VIP */
    .vip-card { background-color: rgba(10, 17, 22, 0.9); border: 1px solid #14222b; border-radius: 8px; padding: 25px; text-align: center; }
    .vip-pills { display: flex; justify-content: center; gap: 15px; margin-bottom: 25px; font-size: 11px; font-weight: bold; }
    .pill-low { color: #00ff87; }
    .pill-med { color: #ffaa00; }
    .pill-high { color: #ff4d4d; }
    .pachet-title { color: #00ff87; font-size: 18px; font-weight: bold; letter-spacing: 1px; margin-bottom: 10px; text-transform: uppercase; }
    .pachet-price { font-size: 26px; font-weight: bold; color: #ffffff; margin-bottom: 25px; }
    .pachet-price span { font-size: 14px; color: #5f7582; font-weight: normal; }
    .vip-features { text-align: left; margin-bottom: 30px; font-size: 13px; color: #ffffff; line-height: 1.8; }
    
    /* Stil pentru butonul de abonare din Streamlit */
    div.stButton > button {
        background-color: transparent !important;
        color: #ffffff !important;
        border: 1px solid #233948 !important;
        border-radius: 4px !important;
        width: 100% !important;
        padding: 8px 0 !important;
        font-size: 12px !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        border-color: #00ff87 !important;
        color: #00ff87 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Aplicație
st.markdown('<div class="main-header">⚽ PARIURIGO • LIVE CENTER</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header-text">Meciurile Reale de Astăzi • Design Premium Stadium-Watermark</div>', unsafe_allow_html=True)

# 4. Structura pe două coloane (Stânga: 70% Meciuri, Dreapta: 30% VIP)
col_stanga, col_dreapta = st.columns([0.7, 0.3])

with col_stanga:
    st.markdown('<div class="section-title">🏟️ Meciurile Zilei (SuperLiga)</div>', unsafe_allow_html=True)
    
    # CARD 1: MECI LIVE (Oțelul Galați vs Univ. Craiova)
    st.markdown("""
    <div class="live-card">
        <span class="live-badge">● LIVE - MIN 65</span>
        <span class="league-tag">România Superliga</span>
        <div class="teams-container">
            <span class="team-home">OȚELUL GALAȚI</span>
            <span class="score">1 - 1</span>
            <span class="team-away">UNIV. CRAIOVA</span>
        </div>
        <div class="stats-grid">
            <div>
                <div class="stat-label">📊 Posesie Minge</div>
                <div class="stat-values">46% - 54%</div>
            </div>
            <div>
                <div class="stat-label">🎯 Șuturi pe Poartă</div>
                <div class="stat-values">4 - 5</div>
            </div>
            <div>
                <div class="stat-label">🛑 Faulturi Comise</div>
                <div class="stat-values">15 - 11</div>
            </div>
            <div>
                <div class="stat-label">🟨 Cartonașe Live</div>
                <div class="stat-values">3 - 2</div>
            </div>
        </div>
        <div class="ai-box">
            <div class="ai-title">🤖 Sugestie Algoritm Inteligență Artificială:</div>
            <div class="ai-content">🟢 Pont: Sub 2.5 goluri în meci | Cotă live: 1.85</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # CARD 2: PRE-MECI (Corvinul Hunedoara vs CFR Cluj)
    st.markdown("""
    <div class="prematch-card">
        <span class="prematch-badge">● PRE-MECI - 21:30</span>
        <span class="league-tag">România Superliga</span>
        <div class="prematch-teams">
            CORVINUL HUNEDOARA <span class="vs-text">vs</span> CFR CLUJ
        </div>
        <div style="color: #5f7582; font-size: 11px; font-weight: bold; margin-bottom: 8px;">Cote Finale Disponibile (1X2):</div>
        <div class="odds-row">
            <div class="odd-box">1 (Corvinul) • 3.80</div>
            <div class="odd-box">X (Egal) • 3.40</div>
            <div class="odd-box">2 (CFR Cluj) • 1.95</div>
        </div>
        <div class="tipster-box">
            <div class="tipster-title">⭐ Recomandare Tipster Premium:</div>
            <div class="tipster-content">🔥 Pont: Victorie CFR Cluj (2) sau Egal | Cotă: 1.40</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_dreapta:
    st.markdown('<div class="section-title">🏆 Acces VIP Premium</div>', unsafe_allow_html=True)
    
    # CARD DREAPTA: PACHET LOW
    st.markdown("""
    <div class="vip-card">
        <div class="vip-pills">
            <span class="pill-low">● LOW</span>
            <span class="pill-med" style="opacity: 0.4;">● MEDIUM</span>
            <span class="pill-high" style="opacity: 0.4;">● HIGH</span>
        </div>
        <div class="pachet-title">Pachet Low</div>
        <div class="pachet-price">19 RON <span>/ lună</span></div>
        <div class="vip-features">
            🟩 <b>3 Bilete</b> gata analizate pe săptămână<br>
            🟩 <b>Cote sigure</b> din Liga 1 și ligile mari
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Butonul oficial Streamlit centrat sub card pentru acțiune (Abonare)
    if st.button("Abonare Standard LOW"):
        st.success("Redirecționare securizată către plată...")
