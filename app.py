import streamlit as st
import base64
from datetime import datetime
from baza import aplica_stiluri_landing_premium, date_fotbal_real, date_cs2_real

st.set_page_config(
    page_title="PariuriGO • World Sports Community",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")
aplica_stiluri_landing_premium()

# Inițializăm starea paginii din interiorul telefonului
if "pagina_curenta" not in st.session_state:
    st.session_state.pagina_curenta = "meniu_principal"

def incarc_logo_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

logo_base64 = incarc_logo_local("logo.png")

# HERO TITLE SECTION
st.markdown("""
<div class="hero-title-container">
    <h1 style="font-size: 38px; font-weight: 800; letter-spacing: 1px; margin-bottom: 5px; text-align: center;">
        PariuriGO s-a mutat acum în aplicație!
    </h1>
    <p style="font-size: 17px; color: #a0aec0; font-weight: 600; margin-top: 0; text-align: center;">
        Alege sportul preferat pentru statistici și filtre avansate de predictivitate.
    </p>
</div>
""", unsafe_allow_html=True)

# MOCKUP CENTRAL INTERACTIV
st.markdown('<div class="mockup-wrapper">', unsafe_allow_html=True)
col_mock1, col_mock2, col_mock3 = st.columns([1, 1.3, 1])

with col_mock2:
    st.markdown("""
    <div style="background: #09090d; border: 4px solid #1c123c; border-radius: 32px; padding: 20px; box-shadow: 0 0 40px rgba(176,66,255,0.25); min-height: 480px;">
        <div style="width: 60px; height: 16px; background: #1c123c; margin: 0 auto 15px auto; border-radius: 10px;"></div>
    """, unsafe_allow_html=True)
    
    # ---- 1. ECRANUL PRINCIPAL: MENIUL CU TOATE SPORTURILE ----
    if st.session_state.pagina_curenta == "meniu_principal":
        st.markdown('<p style="color:#cbd5e1; font-size:13px; font-weight:700; margin-bottom:15px; opacity:0.8;">Alege sportul pentru statistici:</p>', unsafe_allow_html=True)
        
        # Folosim butoane native stilizate ca și carduri
        if st.button("⚽ FOTBAL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AVAILABLE", key="btn_fotbal"):
            st.session_state.pagina_curenta = "pag_fotbal"
            st.rerun()
            
        if st.button("🎮 COUNTER-STRIKE 2 (CS2) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AVAILABLE", key="btn_cs2"):
            st.session_state.pagina_curenta = "pag_cs2"
            st.rerun()
            
        st.write("")
        st.markdown("""
        <div style="opacity: 0.4;">
            <div class="phone-row"><span class="phone-label">🏀 Baschet</span><span class="badge-soon">SOON</span></div>
            <div class="phone-row"><span class="phone-label">🏒 Hockey</span><span class="badge-soon">SOON</span></div>
            <div class="phone-row"><span class="phone-label">🎾 Tenis</span><span class="badge-soon">SOON</span></div>
        </div>
        """, unsafe_allow_html=True)
    # ---- 2. AFISARE MODUL MECIURI IN INTERIORUL TELEFONULUI ----
    else:
        # Preluam datele in functie de ce a salvat aplicatia
        if st.session_state.pagina_curenta == "pag_cs2":
            meciuri_sport = date_cs2_real()
            titlu_modul = "🎮 CS2 STATS"
        else:
            meciuri_sport = date_fotbal_real()
            titlu_modul = "📊 FOTBAL STATS"
            
        st.markdown(f'<h4 style="text-align:center; color:#b042ff; margin:0; font-size:22px; font-weight:800;">{titlu_modul}</h4>', unsafe_allow_html=True)
        
        lista_meciuri_disponibile = list(meciuri_sport.keys())
        meci_ales = st.selectbox("🎯 Schimba meciul:", lista_meciuri_disponibile, key="sel_meci_mobil_v2")
        m = meciuri_sport[meci_ales]
        
        st.markdown("<hr style='border-color: #1a0f30; margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; margin:0; font-size:22px; color:#ffffff;'>{meci_ales}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; font-size:13px; color:#a0aec0; margin:2px 0 15px 0;'>🏆 {m['liga']}</p>", unsafe_allow_html=True)
        
        st.markdown('<div class="phone-table">', unsafe_allow_html=True)
        st.markdown(f'<div class="phone-row"><span class="phone-label">Total Marcate Gazde</span><span class="phone-val">{m["g_gz"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="phone-row"><span class="phone-label">Total Marcate Oaspeti</span><span class="phone-val">{m["g_os"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="phone-row"><span class="phone-label">Medie Goluri Gz</span><span class="phone-val">{m["med_gz"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="phone-row"><span class="phone-label">Medie Goluri Os</span><span class="phone-val">{m["med_os"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="phone-row"><span class="phone-label">Peste 0.5 HT Gazde</span><span class="phone-val">{m["ht_gz"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="phone-row"><span class="phone-label">Probabilitate +1.5</span><span class="mov-badge-premium">{m["w_p15"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="phone-row"><span class="phone-label">Sansa Ambele Marcheaza</span><span class="mov-badge-premium">{m["w_gg"]}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("")
        if st.button("⬅️ INAPOI LA SPORTURI", key="back_to_menu"):
            st.session_state.pagina_curenta = "meniu_principal"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ================== STORE BUTTONS (SUB TELEFON) ==================
st.markdown("""
<div class="store-buttons-container">
    <a class="store-btn" href="https://t.me" target="_blank">
        <span style="color:#ffffff; font-size:12px; font-weight:800; display:block; opacity:0.7; text-align:left;">GET IT ON</span>
        <span style="color:#00ff66; font-size:17px; font-weight:800;">Google Play</span>
    </a>
    <a class="store-btn" href="https://t.me" target="_blank">
        <span style="color:#ffffff; font-size:12px; font-weight:800; display:block; opacity:0.7; text-align:left;">Download on the</span>
        <span style="color:#b042ff; font-size:17px; font-weight:800;">App Store</span>
    </a>
</div>
""", unsafe_allow_html=True)

# ================== MENIUL PREMIUM DE JOS DROPDOWNS ==================
st.write("---")
col_nav_logo, col_nav_butoane = st.columns([0.6, 1.4], gap="medium")

with col_nav_logo:
    if logo_base64:
        st.markdown(f'<div style="display:flex; align-items:center; gap:10px; padding-top:5px;"><img src="data:image/png;base64,{logo_base64}" width="42"><span style="font-size:22px; font-weight:800; letter-spacing:1px;">PARIURIGO</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="padding-top:5px;"><span style="font-size:24px; font-weight:800; color:#b042ff; letter-spacing:1px;">⚽ PARIURIGO</span></div>', unsafe_allow_html=True)

with col_nav_butoane:
    nav_col1, nav_nav2, nav_col3, nav_col4 = st.columns(4)
    
    with nav_col1:
        with st.popover("🟢 Proba Moca 3 Zile"):
            st.markdown("### 🎁 3 ZILE DE PROBA GRATUITA")
            st.write("Vrei sa testezi algoritmul PariuriGO fara sa platesti nimic? Iti oferim acces complet timp de 72 de ore pe canalul nostru VIP!")
            st.link_button("RECLAMA CONT ACCES 🚀", "https://t.me", use_container_width=True)
            
    with nav_nav2:
        with st.popover("🏆 Pachete VIP"):
            st.markdown("### ALEGE ABONAMENTUL VIP")
            st.write("🟢 **Pachet LOW** - 40 RON / luna")
            st.write("🟡 **Pachet MEDIUM** - 70 RON / luna")
            st.write("🔥 **HIGH VIP ELITE** - 120 RON / luna")
            st.link_button("DESCHIDE PLATA STRIPE 💳", "https://stripe.com", use_container_width=True)

    with nav_col3:
        with st.popover("📜 Termeni Legali"):
            st.markdown("### ⚖️ REGULAMENT DIRECT PE SITE")
            st.write("<b>Termeni si Conditii:</b> Platforma ofera analize statistice matematice. Nu garantam profit sigur. Destinat exclusiv persoanelor de peste 18 ani (18+). Jucati responsabil!")
            st.write("<b>Politica de Confidentialitate:</b> Nu stocam datele cardurilor tale. Toate tranzactiile financiare sunt rulate criptat si securizat prin Stripe.")

    with nav_col4:
        with st.popover("🔐 Conectare VIP"):
            st.markdown("### 🔐 LOGIN ACCES MEMBRI")
            utilizator = st.text_input("Utilizator", key="nav_user_premium_final")
            parola = st.text_input("Parola", type="password", key="nav_pass_premium_final")
            if st.button("AUTENTIFICARE VIP", use_container_width=True):
                if utilizator == "admin" and parola == "pariurigo":
                    st.success("Conectat cu succes la baza!")
                else:
                    st.error("Date incorecte!")
