import streamlit as st
from datetime import datetime

# 1. Configurare Pagina Full-Screen (MANDATORIU PRIMA LINIE)
st.set_page_config(page_title="GOLDEN CHAT", page_icon="🏆", layout="wide", initial_sidebar_state="collapsed")
data_azi = datetime.now().strftime("%d.%m.%Y")

# INJECTĂM DESIGN-UL ULTRA-PREMIUM GOLD & CARBON (STIL GOLDEN CHAT)
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #030304 !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    h1, h2, h3, h4, p, span, label { font-family: 'Plus Jakarta Sans', sans-serif !important; }

    /* TELEFON MOBIL CENTRAT */
    .phone-wrapper-container {
        max-width: 410px;
        margin: 10px auto;
        background: #09090b !important;
        border: 1px solid #1c1917;
        border-radius: 40px;
        padding: 20px;
        box-shadow: 0 25px 60px -15px rgba(234, 179, 8, 0.12);
        position: relative;
        min-height: 740px;
    }
    
    .phone-notch {
        width: 120px;
        height: 25px;
        background: #000000;
        margin: -10px auto 20px auto;
        border-radius: 20px;
        border: 1px solid #1c1917;
    }

    .app-top-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding: 0 10px; }

    .fantasy-banner-card {
        background: linear-gradient(135deg, #1c150c 0%, #0c0a07 100%);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 18px;
    }
    
    .fantasy-badge {
        background: rgba(245, 158, 11, 0.12); color: #f59e0b !important;
        font-size: 10px; font-weight: 800; padding: 4px 10px; border-radius: 12px; display: inline-block; margin-bottom: 8px;
    }

    /* CARDURI NEGRE LUCIOASE CU TEXT STANGA */
    div.stButton > button {
        background: #141419 !important;
        border: 1px solid #27272a !important;
        color: #ffffff !important;
        border-radius: 16px !important;
        padding: 15px 18px !important;
        width: 100% !important;
        text-align: left !important;
        display: block !important;
        margin-bottom: -5px !important;
    }
    
    div.stButton > button:hover {
        border-color: #f59e0b !important;
        background: #191922 !important;
    }

    .stripe-lock-box {
        background: linear-gradient(135deg, #1c1010 0%, #0d0707 100%) !important;
        border: 1px solid #ef4444 !important;
        border-radius: 20px !important;
        padding: 24px !important;
        text-align: center !important;
    }

    .match-card-container {
        background: #141419 !important; border: 1px solid #27272a !important;
        border-radius: 16px !important; padding: 18px !important; margin-bottom: 12px !important; text-align: center;
    }
    .match-header-info { font-size: 12px; color: #f59e0b; font-weight: 700; margin-bottom: 10px; }
    .match-teams-grid { display: flex; justify-content: space-around; align-items: center; margin: 12px 0; }
    .team-box-app { width: 45%; text-align: center; }
    .team-name-app { font-size: 15px; font-weight: 800; color: #ffffff; }
    .vs-text-app { font-size: 13px; font-weight: 700; color: #71717a; }

    .app-bottom-navbar { display: flex; justify-content: space-around; align-items: center; background: #141419; border-top: 1px solid #27272a; padding: 12px 5px; margin-top: 25px; border-radius: 0 0 24px 24px; }
    .nav-item-bottom { text-align: center; font-size: 11px; color: #a1a1aa; font-weight: 700; }
    .nav-item-center-gold { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; margin-top: -24px; }
    
    .stTextInput div[data-baseweb="input"] { background-color: rgba(255,255,255,0.02) !important; border: 1px solid #27272a !important; border-radius: 14px !important; }
    .stTextInput input { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

if "user_logat" not in st.session_state: st.session_state.user_logat = False
if "pachet_utilizator" not in st.session_state: st.session_state.pachet_utilizator = "free"
if "baza_date_utilizatori" not in st.session_state: st.session_state.baza_date_utilizatori = {"admin": "pariurigo", "andreiwizz": "Parola123parola"}
if "mod_ecran_autentificare" not in st.session_state: st.session_state.mod_ecran_autentificare = "login"
if "functie_activa" not in st.session_state: st.session_state.functie_activa = "meniu_acasa"

meciuri_f = {
    "LASK Linz vs FCSB": { "liga": "UEFA EUROPA LEAGUE", "g_gz": "16", "g_os": "14", "w_p15": "90%", "w_gg": "64%" },
    "CFR Cluj vs Pafos FC": { "liga": "UEFA CONFERENCE LEAGUE", "g_gz": "15", "g_os": "11", "w_p15": "85%", "w_gg": "58%" }
}

st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

if not st.session_state.user_logat:
    if st.session_state.mod_ecran_autentificare == "login":
        st.markdown("<h1 style='text-align:center; font-size:28px; font-weight:800; background: linear-gradient(135deg, #ffffff 0%, #f59e0b 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>GOLDEN CHAT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:12px; margin-top:0; margin-bottom:20px;'>Sign in to unlock your Premium Prediction Center</p>", unsafe_allow_html=True)
        u_in = st.text_input("USER IDENTITY", placeholder="Enter username...", key="u_key")
        p_in = st.text_input("SECURE KEY", type="password", placeholder="Enter password...", key="p_key")
        st.write("")
        if st.button("👉 CONNECT TO GOLDEN PORTAL", key="btn_login_exec"):
            if u_in in st.session_state.baza_date_utilizatori and st.session_state.baza_date_utilizatori[u_in] == p_in:
                st.session_state.user_logat = True
                if u_in == "admin" or u_in == "andreiwizz": st.session_state.pachet_utilizator = "full"
                else: st.session_state.pachet_utilizator = "free"
                st.rerun()
            else: st.error("Access Denied!")
        st.write("---")
        if st.button("➕ CREATE PROFILE ACCOUNT 🚀", key="btn_go_reg"):
            st.session_state.mod_ecran_autentificare = "register"
            st.rerun()
    elif st.session_state.mod_ecran_autentificare == "register":
        st.markdown("<h1 style='text-align:center; font-size:26px; font-weight:800; color:#f59e0b;'>Register Profile</h1>", unsafe_allow_html=True)
        reg_u = st.text_input("CHOOSE USERNAME", placeholder="Username...", key="ru")
        reg_p = st.text_input("CHOOSE SECURE KEY", type="password", placeholder="Password...", key="rp")
        reg_cp = st.text_input("CONFIRM SECURE KEY", type="password", placeholder="Repeat password...", key="rcp")
        st.write("")
        if st.button("✨ CREATE MY PROFILE", key="btn_reg_exec"):
            if not reg_u or not reg_p: st.error("Required!")
            elif reg_u in st.session_state.baza_date_utilizatori: st.error("Taken!")
            elif reg_p != reg_cp: st.error("Mismatch!")
            else:
                st.session_state.baza_date_utilizatori[reg_u] = reg_p
                st.success("Created!")
                st.session_state.mod_ecran_autentificare = "login"
                st.rerun()
        st.write("---")
        if st.button("⬅️ BACK TO LOG IN", key="btn_back"):
            st.session_state.mod_ecran_autentificare = "login"
            st.rerun()
# ================== INTERFAȚA PREMIUM DEBLOCATĂ (STIL MODULAR RECOLORABIL) ==================
else:
    # 1. Selectorul secret de culori integrat inteligent în sesiune
    if "tema_culoare" not in st.session_state:
        st.session_state.tema_culoare = "🟣 Mov VIP"

    # Definim codurile de culoare în funcție de ce alege utilizatorul
    if st.session_state.tema_culoare == "🟣 Mov VIP":
        c_primara = "#b042ff"
        c_gradient = "linear-gradient(135deg, #b042ff 0%, #7900f2 100%)"
        c_glow = "rgba(176, 66, 255, 0.2)"
    elif st.session_state.tema_culoare == "🟡 Aurit Premium":
        c_primara = "#f59e0b"
        c_gradient = "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)"
        c_glow = "rgba(245, 158, 11, 0.2)"
    else:  # 🟢 Verde Neon
        c_primara = "#00ff66"
        c_gradient = "linear-gradient(135deg, #00ff66 0%, #009933 100%)"
        c_glow = "rgba(0, 255, 102, 0.2)"

    # Aplicăm dinamic stilurile culorii alese pe butoane și bannere
    st.markdown(f"""
    <style>
        .dynamic-txt-color {{ color: {c_primara} !important; }}
        .fantasy-banner-card {{ border: 1px solid {c_primara} !important; box-shadow: 0 10px 30px {c_glow} !important; }}
        .fantasy-badge {{ color: {c_primara} !important; background: {c_glow} !important; }}
        div.stButton > button:hover {{ border-color: {c_primara} !important; }}
        .badge-purple-neon {{ background: {c_gradient} !important; }}
        .nav-item-center-gold {{ background: {c_gradient} !important; box-shadow: 0 4px 15px {c_glow} !important; }}
    </style>
    """, unsafe_allow_html=True)

    # BARA DE TITLU DE SUS (HEADER COMPLET PERSONALIZABIL)
    st.markdown(f"""
    <div class="app-top-header">
        <span style="font-size: 18px; font-weight: 700; color: #71717a;">🔀</span>
        <span style="font-size: 20px; font-weight: 800; letter-spacing: 0.5px; color: #ffffff;">👑 <span class="dynamic-txt-color">PARIURIGO</span> APP</span>
        <span style="font-size: 18px; color: {c_primara};">☰</span>
    </div>
    """, unsafe_allow_html=True)

    # CARDUL MARE JOCURI (GOLDEN/MOV FANTASY)
    st.markdown(f"""
    <div class="fantasy-banner-card">
        <div class="fantasy-badge">&bull; JOCUL ESTE LIVE</div>
        <h3 style="margin: 0 0 5px 0; font-size: 20px; font-weight: 800; color: #ffffff;">PARIURIGO FANTASY</h3>
        <p style="margin: 0; font-size: 11px; color: #a1a1aa; line-height: 1.4;">Construieste-ti echipa, intra in competitie si urca instant in clasamentul comunitatii globale.</p>
    </div>
    """, unsafe_allow_html=True)

    # VERIFICĂM FILTRUL DE NAVIGARE ÎN INTERIORUL TELEFONULUI
    if st.session_state.functie_activa == "meniu_acasa":
        
        # Panoul de schimbare a culorilor plasat la îndemână în interiorul aplicației
        st.session_state.tema_culoare = st.selectbox("🎨 Personalizează culoarea aplicației:", ["🟣 Mov VIP", "🟡 Aurit Premium", "🟢 Verde Neon"], key="set_theme_color_app")
        st.write("")

        if st.button("💬 &nbsp;&nbsp;&nbsp;&nbsp; Live Chat \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Discutii sportive in timp real", key="fn_chat"):
            if st.session_state.pachet_utilizator == "full": st.session_state.functie_activa = "ecran_chat_deschis"
            else: st.session_state.functie_activa = "ecran_blocat_stripe"
            st.rerun()
            
        st.write("")
        if st.button("📊 &nbsp;&nbsp;&nbsp;&nbsp; Statistici avansate \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Filtreaza dupa pronosticurile tale preferate", key="fn_stats"):
            if st.session_state.pachet_utilizator == "full": st.session_state.functie_activa = "ecran_fotbal_deschis"
            else: st.session_state.functie_activa = "ecran_blocat_stripe"
            st.rerun()
            
        st.write("")
        if st.button("💰 &nbsp;&nbsp;&nbsp;&nbsp; Manage your Bankroll \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Urmareste evolutia si strategia", key="fn_bankroll"):
            st.session_state.functie_activa = "ecran_blocat_stripe"
            st.rerun()
            
        st.write("")
        if st.button("🏆 &nbsp;&nbsp;&nbsp;&nbsp; Clubul Founderilor \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Meciuri urmarite atent de admini", key="fn_founder"):
            st.session_state.functie_activa = "ecran_blocat_stripe"
            st.rerun()

    # ---- CAZUL A: SECȚIUNEA BLOCATĂ STRIPE PENTRU UTILIZATORII GRATUIȚI ----
    elif st.session_state.functie_activa == "ecran_blocat_stripe":
        st.markdown(f"""
        <div class="stripe-lock-box">
            <h3 style="color:#ef4444; margin:0 0 8px 0; font-size:22px; font-weight:800;">🔒 ACCES VIP BLOCAT</h3>
            <p style="color:#cbd5e1; font-size:13px; line-height:1.4; margin-bottom:15px;">Aceasta sectiune contine biletul zilei si analizele avansate ale algoritmului. Deblocheaza contul tau VIP acum!</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("💳 CUMPĂRĂ ACCES VIP (STRIPE)", "https://stripe.com", use_container_width=True)
        st.write("")
        if st.button("⬅️ ÎNAPOI LA MENIU", key="btn_back_lock"):
            st.session_state.functie_activa = "meniu_acasa"
            st.rerun()

    # ---- CAZUL B: STATISTICI DEBLOCATE FACĂ ÎN FAȚĂ CU COMBINAȚIE DINAMICĂ ----
    elif st.session_state.functie_activa == "ecran_fotbal_deschis":
        st.markdown(f'<p style="color:{c_primara}; font-size:13px; font-weight:800; margin-bottom:12px; text-transform:uppercase; text-align:center;">⚽ ENGINE STATISTICI AVANSATE (UNLOCKED)</p>', unsafe_allow_html=True)
        
        for titlu, d in meciuri_f.items():
            ec = titlu.split(" vs ")
            st.markdown(f"""
            <div class="match-card-container">
                <div class="match-header-info">{d['liga']}</div>
                <div class="match-teams-grid">
                    <div class="team-box-app"><div style="font-size:24px;">🛡️</div><div class="team-name-app">{ec[0]}</div></div>
                    <div class="vs-text-app" style="color:{c_primara};">VS</div>
                    <div class="team-box-app"><div style="font-size:24px;">⚔️</div><div class="team-name-app">{ec[1]}</div></div>
                </div>
                <div style="display:flex; height:5px; border-radius:10px; overflow:hidden; width:95%; margin:0 auto; background:#1f1f2e;">
                    <div style="width:60%; background:#00ff66;"></div><div style="width:25%; background:#eab308;"></div><div style="width:15%; background:#ef4444;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; width:95%; margin:4px auto 0 auto; font-size:10px; color:#71717a; font-weight:700;">
                    <span>WIN: 60%</span><span>DRAW: 25%</span><span>LOSS: 15%</span>
                </div>
                <div style="margin-top:10px; font-size:12px; color:#cbd5e1; text-align:left; background:rgba(255,255,255,0.02); padding:8px; border-radius:6px;">
                    📈 Probabilitate +1.5 Goluri: <b>{d['w_p15']}</b><br>
                    🤝 Sansa Ambele marcheaza (GG): <b>{d['w_gg']}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        if st.button("⬅️ ÎNAPOI LA MENIU", key="btn_back_f_ok"):
            st.session_state.functie_activa = "meniu_acasa"
            st.rerun()

    # ---- CAZUL C: LIVE CHAT ACTIV ----
    elif st.session_state.functie_activa == "ecran_chat_deschis":
        st.markdown(f'<p style="color:{c_primara}; font-size:13px; font-weight:800; margin-bottom:12px; text-transform:uppercase; text-align:center;">💬 COMUNITATE LIVE CHAT (VIP)</p>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:#141419; border:1px solid #27272a; padding:12px; border-radius:12px; font-size:13px; min-height:180px; margin-bottom:15px;">
            <p style="margin:4px 0;"><b style="color:{c_primara};">AndreiWizz:</b> Biletele pe astazi sunt incarcate! Cota 2.10 gata de profit! 🚀</p>
            <p style="margin:4px 0;"><b style="color:#a1a1aa;">Membru_771:</b> Algoritmul a dat 90% pe FCSB diseara, am urcat biletul!</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Scrie in chat...", placeholder="Mesajul tau...", key="chat_msg_premium")
        st.write("")
        if st.button("⬅️ ÎNAPOI LA MENIU", key="btn_back_chat"):
            st.session_state.functie_activa = "meniu_acasa"
            st.rerun()

    # BARA DE NAVIGARE ORIZONTALĂ DE JOS DIN DESIGN-UL PRELUAT
    st.markdown(f"""
    <div class="app-bottom-navbar">
        <div class="nav-item-bottom">🤖<br><span style="color:{c_primara};">AI Predict</span></div>
        <div class="nav-item-bottom">⚽<br>Live</div>
        <div class="nav-item-center-gold">🏠</div>
        <div class="nav-item-bottom">❓<br>Quiz</div>
        <div class="nav-item-bottom">📞<br>Contact</div>
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        if st.button("🔒 Sign Out / Deconectare", use_container_width=True, key="sidebar_logout_gold_v2"):
            st.session_state.user_logat = False
            st.session_state.functie_activa = "meniu_acasa"
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Închide corect phone-wrapper-container

# ABONAMENTE DROPDOWNS SECRETE SUB TELEFON PENTRU SIGURANȚĂ FISCALĂ
st.write("---")
col_o1, col_o2 = st.columns(2)
with col_o1:
    with st.popover("💳 Pachete VIP Detaliate & Stripe", use_container_width=True):
        st.write("🟢 **Pachet LOW** - 40 RON / luna")
        st.write("🟡 **Pachet MEDIUM** - 70 RON / luna")
        st.write("🔥 **HIGH VIP ELITE** - 120 RON / luna")
    # Text de branding cu numele tau asamblat discret la subsolul telefonului
    st.markdown("<p style='text-align:center; font-size:10px; color:#27272a; margin-top:15px; font-weight:700;'>BUILD OPTIMIZED &bull; PARIURIGO PLATFORM TEAM</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Inchide corect phone-wrapper-container
