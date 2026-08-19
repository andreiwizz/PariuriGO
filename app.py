import streamlit as st
from datetime import datetime
from baza import aplica_stiluri_aplicatie_nativa, date_fotbal_interactiv, date_cs2_interactiv

# 1. Configurare Pagina principala Full-Screen
st.set_page_config(page_title="PariuriGO Application Center", page_icon="🎮", layout="wide", initial_sidebar_state="collapsed")
data_azi = datetime.now().strftime("%d.%m.%Y")

# Aplicare stiluri native de aplicatie mobila din baza.py
aplica_stiluri_aplicatie_nativa()

# Initializam starea de navigare in aplicatie
if "ecran_activ" not in st.session_state:
    st.session_state.ecran_activ = "meniu_sporturi"

# BARA DE CAUTARE DE SUS STIL TIKTOK APP
st.markdown("""
<div class="app-search-bar">
    <div style="font-size: 15px; color: #a1a1aa; font-weight: 700;">Gaseste meciuri sau statistici avansate...</div>
    <div style="font-size: 18px; color: #b042ff; font-weight: 800;">🔍</div>
</div>
""", unsafe_allow_html=True)

# ECRANUL PRINCIPAL: SELECTIE CATEGORII SPORTURI
if st.session_state.ecran_activ == "meniu_sporturi":
    st.markdown('<p style="color:#b042ff; font-size:14px; font-weight:800; margin-bottom:15px; text-transform:uppercase; letter-spacing:0.5px;">🔥 Categorii Disponibile in Algoritm</p>', unsafe_allow_html=True)
    
    # Selector interactiv rapid plasat deasupra listei pentru navigare instantanee
    optiune_sport = st.selectbox("⚡ SELECTEAZA PENTRU DESCHIDERE PORTAL:", ["Alege un sport activ...", "⚽ FOTBAL (Predictions Engine)", "🎮 COUNTER-STRIKE 2 (CS2)"], key="selector_nativ_app")
    
    if optiune_sport == "⚽ FOTBAL (Predictions Engine)":
        st.session_state.ecran_activ = "modul_fotbal"
        st.rerun()
    elif optiune_sport == "🎮 COUNTER-STRIKE 2 (CS2)":
        st.session_state.ecran_activ = "modul_cs2"
        st.rerun()

    st.write("")

    # CARD 1: FOTBAL VISUAL
    st.markdown("""
    <div class="native-card">
        <div class="native-flex">
            <div class="native-left">
                <span style="font-size: 26px;">⚽</span>
                <div>
                    <div class="native-title">Fotbal</div>
                    <div class="native-desc">Advanced Filters • Goals Predictions • Half-Time Analytics</div>
                </div>
            </div>
            <span class="status-available">AVAILABLE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CARD 2: CS2 VISUAL
    st.markdown("""
    <div class="native-card" style="border-color: rgba(176, 66, 255, 0.25) !important;">
        <div class="native-flex">
            <div class="native-left">
                <span style="font-size: 26px;">🎮</span>
                <div>
                    <div class="native-title" style="color: #b042ff;">Counter-Strike 2 (CS2)</div>
                    <div class="native-desc">eSports Analytics • Pistol Rounds Winrate • Map Predictions</div>
                </div>
            </div>
            <span class="status-available" style="background:rgba(176,66,255,0.15) !important;">AVAILABLE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CARD 3: BASCHET
    st.markdown("""
    <div class="native-card" style="opacity: 0.4;">
        <div class="native-flex">
            <div class="native-left">
                <span style="font-size: 26px;">🏀</span>
                <div>
                    <div class="native-title">Baschet</div>
                    <div class="native-desc">NBA Advanced Stats & Player Props</div>
                </div>
            </div>
            <span class="status-soon">SOON</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CARD 4: HOCHEY
    st.markdown("""
    <div class="native-card" style="opacity: 0.4;">
        <div class="native-flex">
            <div class="native-left">
                <span style="font-size: 26px;">🏒</span>
                <div>
                    <div class="native-title">Hockey</div>
                    <div class="native-desc">NHL Predictions Engine & Over/Under Lines</div>
                </div>
            </div>
            <span class="status-soon">SOON</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CARD 5: TENIS
    st.markdown("""
    <div class="native-card" style="opacity: 0.4;">
        <div class="native-flex">
            <div class="native-left">
                <span style="font-size: 26px;">🎾</span>
                <div>
                    <div class="native-title">Tenis</div>
                    <div class="native-desc">WTA & ATP Live Odds Analytics</div>
                </div>
            </div>
            <span class="status-soon">SOON</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: rgba(255,255,255,0.02); padding: 12px; border-radius: 12px; margin-top: 20px; border: 1px solid rgba(255,255,255,0.05);">
        <span style="color:#a1a1aa; font-size:13px;">ℹ️ <b>Disclaimer:</b> Licente date active • Probabilitati bazate pe modele matematice • Destinat persoanelor majorizate 18+</span>
    </div>
    """, unsafe_allow_html=True)
