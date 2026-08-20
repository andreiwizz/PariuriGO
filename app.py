import streamlit as st
from datetime import datetime

# 1. Configurare Pagina Full-Screen (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO • VIP Portal",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# Injectam stilurile profesionale OLED, Telefon Centrat si noile butoane-card interactive
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #030305 !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    h1, h2, h3, h4, p, span, label { font-family: 'Plus Jakarta Sans', sans-serif !important; }

    /* TELEFON MOBIL CENTRAT STIL IPHONE */
    .phone-wrapper-container {
        max-width: 410px;
        margin: 20px auto;
        background: #09090b !important;
        border: 1px solid #1c1917;
        border-radius: 40px;
        padding: 24px;
        box-shadow: 0 25px 60px -15px rgba(176, 66, 255, 0.12);
        position: relative;
        min-height: 720px;
    }
    
    .phone-notch {
        width: 120px; height: 25px; background: #000000;
        margin: -10px auto 20px auto; border-radius: 20px; border: 1px solid #1c1917;
    }

    .app-top-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding: 0 5px; }
    .fantasy-banner-card { background: linear-gradient(135deg, #1c150c 0%, #0c0a07 100%); border-radius: 20px; padding: 16px; margin-bottom: 18px; }
    .fantasy-badge { font-size: 10px; font-weight: 800; padding: 4px 10px; border-radius: 12px; display: inline-block; margin-bottom: 8px; }

    /* TOATE BUTOANELE TRANSFORMATE IN CARDURI TIP LISTA TIKTOK */
    div.stButton > button {
        background: #141419 !important;
        border: 1px solid #27272a !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        border-radius: 16px !important;
        padding: 15px 18px !important;
        width: 100% !important;
        text-align: left !important;
        display: block !important;
        margin-bottom: -5px !important;
        transition: all 0.2s ease !important;
    }

    .stripe-lock-box { background: linear-gradient(135deg, #1c1010 0%, #0d0707 100%) !important; border: 1px solid #ef4444 !important; border-radius: 20px !important; padding: 20px !important; text-align: center !important; }
    .match-card-container { background: #141419 !important; border: 1px solid #27272a !important; border-radius: 16px !important; padding: 18px !important; margin-bottom: 12px !important; text-align: center; }
    .match-header-info { font-size: 11px; font-weight: 700; margin-bottom: 8px; text-transform: uppercase; }
    .match-teams-grid { display: flex; justify-content: space-around; align-items: center; margin: 10px 0; }
    .team-box-app { width: 45%; text-align: center; }
    .team-name-app { font-size: 15px; font-weight: 800; color: #ffffff; }
    .vs-text-app { font-size: 13px; font-weight: 700; color: #71717a; }

    .app-bottom-navbar { display: flex; justify-content: space-around; align-items: center; background: #141419; border-top: 1px solid #27272a; padding: 12px 5px; margin-top: 25px; border-radius: 0 0 24px 24px; }
    .nav-item-bottom { text-align: center; font-size: 11px; color: #a1a1aa; font-weight: 700; }
    .nav-item-center-gold { width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; margin-top: -24px; }
    
    .stTextInput div[data-baseweb="input"] { background-color: rgba(255,255,255,0.02) !important; border: 1px solid #27272a !important; border-radius: 14px !important; }
    .stTextInput input { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# Initializam starile in memorie
if "user_logat" not in st.session_state: st.session_state.user_logat = False
if "pachet_utilizator" not in st.session_state: st.session_state.pachet_utilizator = "free"
if "baza_date_utilizatori" not in st.session_state: st.session_state.baza_date_utilizatori = {"admin": "pariurigo", "andreiwizz": "Parola123parola"}
if "mod_ecran_autentificare" not in st.session_state: st.session_state.mod_ecran_autentificare = "login"
if "functie_activa" not in st.session_state: st.session_state.functie_activa = "meniu_acasa"
if "tema_culoare" not in st.session_state: st.session_state.tema_culoare = "🟣 Mov VIP"

meciuri_f = {
    "LASK Linz vs FCSB": { "liga": "UEFA EUROPA LEAGUE", "w_p15": "90%", "w_gg": "64%" },
    "CFR Cluj vs Pafos FC": { "liga": "UEFA CONFERENCE LEAGUE", "w_p15": "85%", "w_gg": "58%" }
}

# Setare culori dinamice
if st.session_state.tema_culoare == "🟣 Mov VIP":
    c_primara = "#b042ff"; c_gradient = "linear-gradient(135deg, #b042ff 0%, #7900f2 100%)"; c_glow = "rgba(176, 66, 255, 0.2)"
elif st.session_state.tema_culoare == "🟡 Aurit Premium":
    c_primara = "#f59e0b"; c_gradient = "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)"; c_glow = "rgba(245, 158, 11, 0.2)"
else:
    c_primara = "#00ff66"; c_gradient = "linear-gradient(135deg, #00ff66 0%, #009933 100%)"; c_glow = "rgba(0, 255, 102, 0.2)"

st.markdown(f"""
<style>
    .dynamic-txt-color {{ color: {c_primara} !important; }}
    .fantasy-banner-card {{ border: 1px solid {c_primara} !important; box-shadow: 0 10px 30px {c_glow} !important; }}
    .fantasy-badge {{ color: {c_primara} !important; background: {c_glow} !important; }}
    div.stButton > button:hover {{ border-color: {c_primara} !important; }}
    .nav-item-center-gold {{ background: {c_gradient} !important; box-shadow: 0 4px 15px {c_glow} !important; }}
</style>
""", unsafe_allow_html=True)

# DESCHIDEM CORPUL TELEFONULUI
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

if not st.session_state.user_logat:
    if st.session_state.mod_ecran_autentificare == "login":
        st.markdown(f"<h1 style='text-align:center; font-size:32px; font-weight:800; color:{c_primara}; letter-spacing:0.5px;'>PariuriGO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:-10px; margin-bottom:20px;'>Sign in to access your VIP prediction engine</p>", unsafe_allow_html=True)
        u_in = st.text_input("USER IDENTITY", placeholder="Username...", key="u_key_v4")
        p_in = st.text_input("SECURE KEY", type="password", placeholder="Password...", key="p_key_v4")
        st.write("")
        if st.button("👉 CONNECT TO PORTAL", key="btn_login_exec_v4"):
            if u_in in st.session_state.baza_date_utilizatori and st.session_state.baza_date_utilizatori[u_in] == p_in:
                st.session_state.user_logat = True
                if u_in in ["admin", "andreiwizz"]: st.session_state.pachet_utilizator = "full"
                else: st.session_state.pachet_utilizator = "free"
                st.rerun()
            else: st.error("Access Denied!")
        st.write("---")
        if st.button("➕ CREATE PROFILE ACCOUNT", key="btn_go_reg_v4"):
            st.session_state.mod_ecran_autentificare = "register"
            st.rerun()
    elif st.session_state.mod_ecran_autentificare == "register":
        st.markdown(f"<h1 style='text-align:center; font-size:28px; font-weight:800; color:{c_primara};'>Sign Up</h1>", unsafe_allow_html=True)
        reg_u = st.text_input("CHOOSE USERNAME", placeholder="Pick user name...", key="ru_v4")
        reg_p = st.text_input("CHOOSE SECURE KEY", type="password", placeholder="Password...", key="rp_v4")
        reg_cp = st.text_input("CONFIRM SECURE KEY", type="password", placeholder="Repeat password...", key="rcp_v4")
        st.write("")
        if st.button("✨ REGISTER PROFILE NOW", key="btn_reg_exec_v4"):
            if not reg_u or not reg_p: st.error("All areas required!")
            elif reg_u in st.session_state.baza_date_utilizatori: st.error("Username taken!")
            elif reg_p != reg_cp: st.error("Keys mismatch!")
            else:
                st.session_state.baza_date_utilizatori[reg_u] = reg_p
                st.success("Account created!")
                st.session_state.mod_ecran_autentificare = "login"
                st.rerun()
        st.write("---")
        if st.button("⬅️ BACK TO LOG IN", key="btn_back_v4"):
            st.session_state.mod_ecran_autentificare = "login"
            st.rerun()
# ================== INTERFATA B: UTILIZATORUL LOGAT REUSIT ==================
else:
    st.markdown(f"""
    <div class="app-top-header">
        <span style="font-size: 16px; font-weight: 700; color: #71717a;">🔀</span>
        <span style="font-size: 20px; font-weight: 800; color: #ffffff;"><span class="dynamic-txt-color">PariuriGO</span> VIP</span>
        <span style="font-size: 16px; color: {c_primara};">☰</span>
    </div>
    <div class="fantasy-banner-card">
        <div class="fantasy-badge">&bull; LIVE ENGINE</div>
        <h3 style="margin: 0 0 4px 0; font-size: 19px; font-weight: 800; color: #ffffff;">PARIURIGO FANTASY</h3>
        <p style="margin: 0; font-size: 11px; color: #a1a1aa; line-height: 1.4;">Construieste-ti echipa si urca instant in clasamentul comunitatii.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.functie_activa == "meniu_acasa":
        st.session_state.tema_culoare = st.selectbox("🎨 Alege culoarea aplicatiei:", ["🟣 Mov VIP", "🟡 Aurit Premium", "🟢 Verde Neon"], key="theme_sel_final")
        st.write("")

        if st.button("💬 &nbsp;&nbsp;&nbsp;&nbsp; Live Chat \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Discutii sportive in timp real", key="chat_f_v4"):
            if st.session_state.pachet_utilizator == "full": st.session_state.functie_activa = "ecran_chat_deschis"
            else: st.session_state.functie_activa = "ecran_blocat_stripe"
            st.rerun()
        st.write("")
        if st.button("📊 &nbsp;&nbsp;&nbsp;&nbsp; Statistici avansate \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Filtreaza dupa pronosticurile preferate", key="stats_f_v4"):
            if st.session_state.pachet_utilizator == "full": st.session_state.functie_activa = "ecran_fotbal_deschis"
            else: st.session_state.functie_activa = "ecran_blocat_stripe"
            st.rerun()
        st.write("")
        if st.button("💰 &nbsp;&nbsp;&nbsp;&nbsp; Manage your Bankroll \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Urmareste evolutia si strategia", key="bank_f_v4"):
            st.session_state.functie_activa = "ecran_blocat_stripe"; st.rerun()

    elif st.session_state.functie_activa == "ecran_blocat_stripe":
        st.markdown("""
        <div class="stripe-lock-box">
            <h3 style="color:#ef4444; margin:0 0 6px 0; font-size:20px; font-weight:800;">🔒 ACCES RESTRÂNS</h3>
            <p style="color:#cbd5e1; font-size:12px; line-height:1.4; margin-bottom:12px;">Sectiune blocata. Deblocheaza pachetul complet din link-ul Stripe de mai jos.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("💳 CUMPĂRĂ ACCES ACUM", "https://stripe.com", use_container_width=True)
        st.write("")
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_l_v4"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()

    elif st.session_state.functie_activa == "ecran_fotbal_deschis":
        st.markdown(f'<div style="text-align:center; color:{c_primara}; font-size:14px; font-weight:800; margin-bottom:12px; text-transform:uppercase;">⚽ ENGINE STATISTICI AVANSATE</div>', unsafe_allow_html=True)
        for titlu, d in meciuri_f.items():
            ec = titlu.split(" vs ")
            st.markdown(f"""
            <div class="match-card-container">
                <div class="match-header-info">{d['liga']}</div>
                <div class="match-teams-grid">
                    <div class="team-box-app"><div style="font-size:22px;">🛡️</div><div class="team-name-app">{ec[0]}</div></div>
                    <div class="vs-text-app" style="color:{c_primara}; font-weight:800;">VS</div>
                    <div class="team-box-app"><div style="font-size:22px;">⚔️</div><div class="team-name-app">{ec[1]}</div></div>
                </div>
                <div style="display:flex; height:5px; border-radius:10px; overflow:hidden; width:95%; margin:0 auto; background:#1f1f2e;">
                    <div style="width:60%; background:#00ff66;"></div><div style="width:25%; background:#eab308;"></div><div style="width:15%; background:#ef4444;"></div>
                </div>
                <div style="margin-top:10px; font-size:11px; color:#cbd5e1; text-align:left; background:rgba(255,255,255,0.02); padding:8px; border-radius:6px;">
                    📈 Probabilitate +1.5 Goluri: <b>{d['w_p15']}</b><br>⚙️ Sansa Ambele marcheaza (GG): <b>{d['w_gg']}</b>
                </div>
            </div>
            """, unsafe_allow_html=True)
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_f_v4"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()

    elif st.session_state.functie_activa == "ecran_chat_deschis":
        st.markdown(f'<div style="text-align:center; color:{c_primara}; font-size:14px; font-weight:800;">💬 COMUNITATE LIVE CHAT</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:#141419; border:1px solid #27272a; padding:12px; border-radius:12px; font-size:12px; min-height:160px; margin-bottom:10px;">
            <p style="margin:2px 0;"><b style="color:{c_primara};">AndreiWizz:</b> Biletele pe astazi sunt incarcate! Cota 2.10 gata! 🚀</p>
            <p style="margin:2px 0;"><b style="color:#a1a1aa;">Membru_771:</b> Algoritmul are procente super mari diseara!</p>
        </div>
        """, unsafe_allow_html=True)
        st.text_input("Scrie un mesaj...", placeholder="Mesaj...", key="c_in_v4")
        st.write("")
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_c_v4"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()

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
        if st.button("🔒 Sign Out / Deconectare", use_container_width=True, key="s_out_v4"):
            st.session_state.user_logat = False
            st.session_state.functie_activa = "meniu_acasa"
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Inchide phone-wrapper-container
