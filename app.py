import streamlit as st
import base64
from datetime import datetime
from baza import aplica_stiluri_landing_premium

# 1. Configurare Pagină principală
st.set_page_config(
    page_title="PariuriGO • World Sports Community",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

aplica_stiluri_landing_premium()

def incarc_logo_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

logo_base64 = incarc_logo_local("logo.png")

# HERO TITLE SECTION (SUS CA IN IMAGINE)
st.markdown("""
<div class="hero-title-container">
    <h1 style="font-size: 38px; font-weight: 800; letter-spacing: 1px; margin-bottom: 5px; text-align: center;">
        PariuriGO s-a mutat acum în aplicație!
    </h1>
    <p style="font-size: 17px; color: #a0aec0; font-weight: 600; margin-top: 0; text-align: center;">
        Descarcă acum și verifică statisticile avansate direct pe ecran.
    </p>
</div>
""", unsafe_allow_html=True)

# MOCKUP CENTRAL GENERAT DUPĂ FILMETUL TĂU TIKTOK (FĂRĂ REDIRECȚIONĂRI COMPLICATE)
st.markdown('<div class="mockup-wrapper">', unsafe_allow_html=True)
col_mock1, col_mock2, col_mock3 = st.columns([1, 1.3, 1])

with col_mock2:
    st.markdown("""
    <div style="background: #09090d; border: 4px solid #1c123c; border-radius: 32px; padding: 22px; box-shadow: 0 0 40px rgba(176,66,255,0.25); min-height: 480px;">
        <div style="width: 60px; height: 16px; background: #1c123c; margin: 0 auto 15px auto; border-radius: 10px;"></div>
        <p style="color:#cbd5e1; font-size:13px; font-weight:700; margin-bottom:15px; opacity:0.8;">Alege sportul pentru statistici:</p>
        
        <!-- 1. FOTBAL AVAILABLE -->
        <div class="sport-card">
            <div class="sport-info">
                <span style="font-size:20px;">⚽</span>
                <div>
                    <p class="sport-title">Fotbal</p>
                    <p class="sport-desc">Advanced Filters • Predictions Engine</p>
                </div>
            </div>
            <span class="badge-available">AVAILABLE</span>
        </div>
        
        <!-- 2. BASCHET AVAILABLE -->
        <div class="sport-card">
            <div class="sport-info">
                <span style="font-size:20px;">🏀</span>
                <div>
                    <p class="sport-title">Baschet</p>
                    <p class="sport-desc">NBA • Advanced Stats & Lineups</p>
                </div>
            </div>
            <span class="badge-available">AVAILABLE</span>
        </div>
        
        <!-- 3. HOCHEY AVAILABLE -->
        <div class="sport-card">
            <div class="sport-info">
                <span style="font-size:20px;">🏒</span>
                <div>
                    <p class="sport-title">Hockey</p>
                    <p class="sport-desc">Statistici avansate NHL & Europa</p>
                </div>
            </div>
            <span class="badge-available">AVAILABLE</span>
        </div>
        
        <!-- 4. CS2 AVAILABLE ADĂUGAT DE NOI -->
        <div class="sport-card" style="background: rgba(176, 66, 255, 0.03); border-color: rgba(176, 66, 255, 0.15);">
            <div class="sport-info">
                <span style="font-size:20px;">🎮</span>
                <div>
                    <p class="sport-title" style="color:#b042ff;">Counter-Strike 2 (CS2)</p>
                    <p class="sport-desc">eSports Predictions • Major Data Analytics</p>
                </div>
            </div>
            <span class="badge-available" style="color:#b042ff !important; border-color:#b042ff;">AVAILABLE</span>
        </div>
        
        <!-- 5. TENIS AVAILABLE -->
        <div class="sport-card">
            <div class="sport-info">
                <span style="font-size:20px;">🎾</span>
                <div>
                    <p class="sport-title">Tenis</p>
                    <p class="sport-desc">ATP & WTA Live Analytics</p>
                </div>
            </div>
            <span class="badge-available">AVAILABLE</span>
        </div>
        
        <!-- 6. HANDBAL SOON -->
        <div class="sport-card" style="opacity: 0.5;">
            <div class="sport-info">
                <span style="font-size:20px;">🤾</span>
                <div>
                    <p class="sport-title">Handbal</p>
                    <p class="sport-desc">Soon</p>
                </div>
            </div>
            <span class="badge-soon">SOON</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# BUTTONS REFACHUTE ELEGANT SUB MOBIL
st.markdown("""
<div class="store-buttons-container">
    <a class="store-btn" href="https://t.me" target="_blank">
        <span style="color:#ffffff; font-size:11px; font-weight:800; display:block; opacity:0.7;">GET IT ON</span>
        <span style="color:#00ff66; font-size:16px; font-weight:800;">Google Play</span>
    </a>
    <a class="store-btn" href="https://t.me" target="_blank">
        <span style="color:#ffffff; font-size:11px; font-weight:800; display:block; opacity:0.7;">Download on the</span>
        <span style="color:#b042ff; font-size:16px; font-weight:800;">App Store</span>
    </a>
</div>
""", unsafe_allow_html=True)

# BARĂ ORIZONTALĂ PREMIUM JOS CU DROPDOWNS PENTRU CLIENTELA REALĂ
st.write("---")
col_nav_logo, col_nav_butoane = st.columns([0.6, 1.4], gap="medium")

with col_nav_logo:
    if logo_base64:
        st.markdown(f'<div style="display:flex; align-items:center; gap:10px;"><img src="data:image/png;base64,{logo_base64}" width="42"><span style="font-size:22px; font-weight:800; letter-spacing:1px;">PARIURIGO</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div><span style="font-size:24px; font-weight:800; color:#b042ff; letter-spacing:1px;">⚽ PARIURIGO</span></div>', unsafe_allow_html=True)

with col_nav_butoane:
    nav_col1, nav_nav2, nav_col3, nav_col4 = st.columns(4)
    
    with nav_col1:
        with st.popover("🟢 Probă Moca 3 Zile"):
            st.markdown("### 🎁 3 ZILE DE PROBĂ GRATUITĂ")
            st.write("Testează algoritmul PariuriGO fără să plătești nimic! Îți oferim acces complet timp de 72 de ore pe canalul nostru VIP.")
            st.link_button("RECLAMĂ CONT ACCES 🚀", "https://t.me", use_container_width=True)
            
    with nav_nav2:
        with st.popover("🏆 Pachete VIP"):
            st.markdown("### ALEGE ABONAMENTUL VIP")
            st.write("🟢 **Pachet LOW** - 40 RON / lună")
            st.write("🟡 **Pachet MEDIUM** - 70 RON / lună")
            st.write("🔥 **HIGH VIP ELITE** - 120 RON / lună")
            st.link_button("DESCHIDE PLATĂ STRIPE 💳", "https://stripe.com", use_container_width=True)

    with nav_col3:
        with st.popover("📜 Termeni Legali"):
            st.markdown("### ⚖️ REGULAMENT DIRECT PE SITE")
            st.write("<b>Termeni și Condiții:</b> Platforma oferă analize statistice matematice. Nu garantăm profit sigur. Destinat exclusiv persoanelor de peste 18 ani (18+). Jucați responsabil!")
            st.write("<b>Politica de Confidențialitate:</b> Nu stocăm datele cardurilor tale. Toate tranzacțiile financiare sunt rulate criptat și securizat prin Stripe.")

    with nav_col4:
        with st.popover("🔐 Conectare VIP"):
            st.markdown("### 🔐 LOGIN ACCES MEMBRI")
            utilizator = st.text_input("Utilizator", key="nav_user_premium_fixed")
            parola = st.text_input("Parolă", type="password", key="nav_pass_premium_fixed")
            if st.button("AUTENTIFICARE VIP", use_container_width=True):
                if utilizator == "admin" and parola == "pariurigo":
                    st.success("Conectat!")
                else:
                    st.error("Date incorecte!")
