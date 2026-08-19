import streamlit as st
import base64
from datetime import datetime
from baza import aplica_stiluri_landing_premium, preia_meciuri_comunitate

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE ÎN APP.PY)
st.set_page_config(
    page_title="PariuriGO • World Sports Community",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# Aplicare stiluri premium de landing din baza.py
aplica_stiluri_landing_premium()
meciuri_date = preia_meciuri_comunitate()

def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

logo_base64 = incarc_imagine_locala("logo.png")

# ================== SECTIUNEA HERO (SUS DE TOT CA IN IMAGINEA TA) ==================
st.markdown("""
<div class="hero-title-container">
    <h1 style="font-size: 42px; font-weight: 800; letter-spacing: 1px; margin-bottom: 5px;">
        PariuriGO s-a mutat acum în aplicație!
    </h1>
    <p style="font-size: 18px; color: #a0aec0; font-weight: 600; margin-top: 0;">
        Descarcă acum și bucură-te de cea mai puternică comunitate de sport.
    </p>
</div>
""", unsafe_allow_html=True)

# Mockup-ul central cu telefoanele (Folosim o grafică simbolică stilizată cu ecranele noastre active)
st.markdown('<div class="mockup-wrapper">', unsafe_allow_html=True)
col_mock1, col_mock2, col_mock3 = st.columns([1, 1.2, 1])

with col_mock2:
    # Caseta centrală care simulează ecranul aplicației mov deschisă pe telefon
    st.markdown("""
    <div style="background: #000000; border: 4px solid #1c123c; border-radius: 32px; padding: 20px; box-shadow: 0 0 40px rgba(176,66,255,0.25); min-height: 400px;">
        <div style="width: 60px; height: 18px; background: #1c123c; margin: 0 auto 15px auto; border-radius: 10px;"></div>
        <h4 style="text-align:center; color:#b042ff; margin:0; font-size:20px;">📊 ALGORITM PARIURIGO</h4>
        <p style="text-align:center; font-size:12px; color:#cbd5e1; margin:2px 0 15px 0;">Premium Prediction Engine</p>
    """, unsafe_allow_html=True)
    
    # Adăugăm un selector rapid direct în interiorul telefonului generat pe ecran
    meci_ales = st.selectbox("🎯 Selectează meciul activ din aplicație:", list(meciuri_date.keys()), label_visibility="collapsed")
    m = meciuri_date[meci_ales]
    
    st.markdown(f"""
        <hr style="border-color: #1a0f30; margin: 10px 0;">
        <div style="text-align:center; font-weight:800; font-size:16px; color:#ffffff;">{meci_ales}</div>
        <p style="text-align:center; font-size:11px; color:#a0aec0; margin:2px 0 10px 0;">🏆 {m['liga']}</p>
        
        <div class="stat-container">
            <div class="stat-row"><span style="font-size:16px;">{m['g_gz']}</span><span style="font-size:12px; color:#a0aec0;">Goluri Marcate</span><span style="font-size:16px;">{m['g_os']}</span></div>
            <div class="stat-row"><span style="font-size:16px;">{m['med_gz']}</span><span style="font-size:12px; color:#a0aec0;">Medie Goluri</span><span style="font-size:16px;">{m['med_os']}</span></div>
        </div>
        
        <hr style="border-color: #1a0f30; margin: 10px 0;">
        <div class="stat-row"><span>Peste 1.5 Goluri</span><span class="mov-badge-premium">{m['w_p15']}</span></div>
        <div class="stat-row" style="margin-top:10px;"><span>Ambele marchează (GG)</span><span class="mov-badge-premium">{m['w_gg']}</span></div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ================== BUTOANELE DE STORE (SUB TELEFON CA IN IMAGINE) ==================
st.markdown("""
<div class="store-buttons-container">
    <a class="store-btn" href="https://t.me" target="_blank">
        <img src="https://wikimedia.org" height="42">
    </a>
    <a class="store-btn" href="https://t.me" target="_blank">
        <img src="https://wikimedia.org" height="42">
    </a>
</div>
""", unsafe_allow_html=True)

# ================== MENIUL ORIZONTAL DE JOS (NAVBAR DIN IMAGINEA TA) ==================
st.write("---")
col_nav_logo, col_nav_butoane = st.columns([0.6, 1.4], gap="medium")

with col_nav_logo:
    if logo_base64:
        st.markdown(f'<div style="display:flex; align-items:center; gap:10px; padding-top:5px;"><img src="data:image/png;base64,{logo_base64}" width="50"><span style="font-size:24px; font-weight:800; letter-spacing:1px;">PARIURIGO</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="padding-top:5px;"><span style="font-size:26px; font-weight:800; color:#b042ff; letter-spacing:1px;">⚽ PARIURIGO</span></div>', unsafe_allow_html=True)

with col_nav_butoane:
    # Generăm butoanele interactive expandabile chiar în bara orizontală
    nav_col1, nav_nav2, nav_col3, nav_col4 = st.columns(4)
    
    with nav_col1:
        with st.popover("🟢 Pasi Probă Moca"):
            st.markdown("### 🎁 3 ZILE GRATUITE")
            st.write("Vrei să testezi algoritmul PariuriGO complet moca? Intră pe grupul nostru și primești acces 72 de ore.")
            st.link_button("RECLAMĂ ACCES GRATUIT 🚀", "https://t.me", use_container_width=True)
            
    with nav_nav2:
        with st.popover("🏆 Pachete VIP"):
            st.markdown("### CHOOSE YOUR VIP PLAN")
            st.write("🟢 **Pachet LOW** - 40 RON / lună")
            st.write("🟡 **Pachet MEDIUM** - 70 RON / lună")
            st.write("🔥 **HIGH VIP ELITE** - 120 RON / lună")
            st.link_button("DESCHIDE PLATĂ STRIPE 💳", "https://stripe.com", use_container_width=True)

    with nav_col3:
        with st.popover("📜 Termeni Legali"):
            st.markdown("### ⚖️ TERMENI ȘI REGULAMENT")
            st.write("Platforma oferă analize predictive bazate pe statistică matematică. Nu garantăm profit. Destinat exclusiv persoanelor majorizate (18+). Jucați responsabil!")

    with nav_col4:
        with st.popover("🔐 Conectare VIP"):
            st.markdown("### 🔐 PANOU AUTENTIFICARE")
            utilizator = st.text_input("Utilizator", key="nav_user")
            parola = st.text_input("Parolă", type="password", key="nav_pass")
            if st.button("AUTENTIFICARE CONT", use_container_width=True):
                if utilizator == "admin" and parola == "pariurigo":
                    st.success("Conectat la portal!")
                else:
                    st.error("Date incorecte!")
