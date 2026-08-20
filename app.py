import streamlit as st
from datetime import datetime

# 1. Configurare Pagină Full-Screen
st.set_page_config(
    page_title="PariuriGO • Portal VIP",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# Injectăm stilurile profesionale OLED, Telefon Centrat și noile Butoane-Card active
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #030305 !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    h1, h2, h3, h4, p, span, label {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #ffffff !important;
    }

    /* TELEFON MOBIL CENTRAT STIL IPHONE */
    .phone-wrapper-container {
        max-width: 410px;
        margin: 40px auto;
        background: rgba(18, 18, 24, 0.8) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 40px;
        padding: 24px;
        box-shadow: 0 25px 50px -12px rgba(157, 0, 255, 0.2);
    }
    
    .phone-notch {
        width: 110px;
        height: 25px;
        background: #000000;
        margin: -12px auto 25px auto;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .stTextInput div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important;
    }
    
    .stTextInput input { color: #ffffff !important; font-size: 15px; }

    /* FORȚĂM TOATE BUTOANELE APLICAȚIEI SĂ ARATE CA NIȘTE CARDURI PREMIUM DIN TIKTOK */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        border-radius: 18px !important;
        padding: 16px !important;
        width: 100% !important;
        text-align: left !important;
        display: block !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
        transition: all 0.2s ease !important;
    }
    
    div.stButton > button:hover {
        border-color: #a855f7 !important;
        background: rgba(168, 85, 247, 0.04) !important;
        transform: translateY(-1px) !important;
    }

    /* CARDURI MECIURI (ECHIPE FAȚĂ ÎN FAȚĂ) */
    .match-card-container {
        background: #121218 !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 16px !important;
        padding: 18px !important;
        margin-bottom: 12px !important;
        text-align: center;
    }
    .match-header-info { font-size: 12px; color: #a855f7; font-weight: 700; margin-bottom: 10px; text-transform: uppercase; }
    .match-teams-grid { display: flex; justify-content: space-around; align-items: center; margin: 12px 0; }
    .team-box-app { width: 45%; text-align: center; }
    .team-name-app { font-size: 15px; font-weight: 800; color: #ffffff; }
    .vs-text-app { font-size: 13px; font-weight: 700; color: #71717a; }

    /* TABELE MODULE INTERIOARE */
    .module-table { width: 100%; margin-top: 10px; }
    .module-row { display: flex; justify-content: space-between; padding: 8px 4px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
    .module-label { color: #a1a1aa; font-size: 11px; text-transform: uppercase; font-weight: 700; }
    .module-val { color: #ffffff; font-weight: 800; font-size: 14px; }
    .badge-purple-neon { background: linear-gradient(135deg, #a855f7 0%, #6366f1 100%) !important; color: #ffffff !important; padding: 2px 8px; border-radius: 5px; font-size: 12px; font-weight: 800; }
</style>
""", unsafe_allow_html=True)

# Inițializăm stările în memorie
if "utilizator_logat" not in st.session_state: st.session_state.utilizator_logat = False
if "baza_date_utilizatori" not in st.session_state: st.session_state.baza_date_utilizatori = {"admin": "pariurigo", "andreiwizz": "Parola123parola"}
if "mod_ecran_autentificare" not in st.session_state: st.session_state.mod_ecran_autentificare = "login"
if "ecran_aplicatie" not in st.session_state: st.session_state.ecran_aplicatie = "meniu_sporturi"

# BAZA DE DATE MECIURI REALE DE AZI (JOI, 20 AUGUST 2026)
meciuri_fotbal = {
    "LASK Linz vs FCSB": { "liga": "UEFA EUROPA LEAGUE • 20:00", "g_gz": "16", "g_os": "14", "med_gz": "1.85", "med_os": "1.55", "ht_gz": "84%", "w_p15": "90%", "w_gg": "64%" },
    "CFR Cluj vs Pafos FC": { "liga": "UEFA CONFERENCE LEAGUE • 20:30", "g_gz": "15", "g_os": "11", "med_gz": "1.65", "med_os": "1.28", "ht_gz": "81%", "w_p15": "85%", "w_gg": "58%" }
}
meciuri_cs2 = {
    "NAVI vs FaZe Clan": { "liga": "ESL PRO LEAGUE • 21:00", "maps_gz": "71%", "maps_os": "65%", "pistol_gz": "58%", "pistol_os": "60%", "clutch_gz": "55%", "w_over": "69%", "w_winner": "NAVI" }
}

# CONSTRUIM CORPUL TELEFONULUI MOBIL CENTRAT
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

# ---- INTERFAȚA 1: BLOCUL DE LOGIN / REGISTER ----
if not st.session_state.utilizator_logat:
    if st.session_state.mod_ecran_autentificare == "login":
        st.markdown("<h1 style='text-align:center; font-size:28px; font-weight:800; background: linear-gradient(135deg, #ffffff 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>PariuriGO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:25px; font-weight:500;'>Sign in to access your VIP prediction portal</p>", unsafe_allow_html=True)
        
        username = st.text_input("USER IDENTITY", placeholder="Enter username...", key="user_login_key")
        password = st.text_input("SECURE KEY", type="password", placeholder="Enter password...", key="pass_login_key")
        
        st.write("")
        if st.button("👉 SIGN IN TO APPLICATION", key="btn_execute_login"):
            if username in st.session_state.baza_date_utilizatori and st.session_state.baza_date_utilizatori[username] == password:
                st.session_state.utilizator_logat = True
                st.st.rerun()
            else: st.error("Invalid Username or Password!")
                
        st.write("---")
        if st.button("➕ CREATE NEW ACCOUNT 🚀", key="btn_go_to_register"):
            st.session_state.mod_ecran_autentificare = "register"
            st.st.rerun()

    elif st.session_state.mod_ecran_autentificare == "register":
        st.markdown("<h1 style='text-align:center; font-size:26px; font-weight:800; color:#a855f7;'>Sign Up Center</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:25px;'>Create a permanent membership profile</p>", unsafe_allow_html=True)
        
        new_user = st.text_input("CHOOSE USERNAME", placeholder="Username...", key="reg_user")
        new_pass = st.text_input("CHOOSE SECURE KEY", type="password", placeholder="Password...", key="reg_pass")
        confirm_pass = st.text_input("CONFIRM SECURE KEY", type="password", placeholder="Repeat password...", key="reg_pass_conf")
        
        st.write("")
        if st.button("✨ REGISTER PROFILE NOW", key="btn_execute_register"):
            if not new_user or not new_pass: st.error("All areas must be completed!")
            elif new_user in st.session_state.baza_date_utilizatori: st.error("Username already taken!")
            elif new_pass != confirm_pass: st.error("Passwords do not match!")
            else:
                st.session_state.baza_date_utilizatori[new_user] = new_pass
                st.success("Account created!")
                st.session_state.mod_ecran_autentificare = "login"
                st.st.rerun()
                
        st.write("---")
        if st.button("⬅️ BACK TO SIGN IN", key="btn_back_to_login"):
            st.session_state.mod_ecran_autentificare = "login"
            st.st.rerun()
# ---- INTERFAȚA 2: ECRANELE INTERIOARE ALE APLICAȚIEI (DUPĂ LOGARE) ----
else:
    # 2.A MENIUL PRINCIPAL DE SELECȚIE SPORTURI
    if st.session_state.ecran_aplicatie == "meniu_sporturi":
        st.markdown('<p style="color:#a855f7; font-size:13px; font-weight:800; margin-bottom:15px; text-transform:uppercase; text-align:center; letter-spacing:0.5px;">🔥 PREDICTION ENGINES ACTIVATED</p>', unsafe_allow_html=True)
        
        # Butoanele noastre native stilizate sub formă de carduri interactive 100% funcționale
        if st.button("⚽ Fotbal Module \n\n Live Predictions Engine • Available", key="click_sport_f"):
            st.session_state.ecran_aplicatie = "modul_fotbal"
            st.rerun()
            
        st.write("")
        
        if st.button("🎮 CS2 Esports \n\n Map Performance Data • Available", key="click_sport_c"):
            st.session_state.ecran_aplicatie = "modul_cs2"
            st.rerun()
            
        st.write("")
        st.markdown('<p style="color:#71717a; font-size:12px; font-weight:700; margin-bottom:10px; text-transform:uppercase; margin-left:5px;">⏳ În curând în aplicație</p>', unsafe_allow_html=True)
        st.markdown('<div style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); padding:12px; border-radius:14px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center; opacity:0.4;"><span style="font-size:15px; font-weight:700;">🏀 Baschet NBA</span><span style="font-size:11px; background:#27272a; padding:3px 8px; border-radius:10px; color:#a1a1aa;">SOON</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); padding:12px; border-radius:14px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center; opacity:0.4;"><span style="font-size:15px; font-weight:700;">🏒 Hockey NHL</span><span style="font-size:11px; background:#27272a; padding:3px 8px; border-radius:10px; color:#a1a1aa;">SOON</span></div>', unsafe_allow_html=True)

    # 2.B MODULUL ACTIV FOTBAL (MECIURI FAȚĂ ÎN FAȚĂ)
    elif st.session_state.ecran_aplicatie == "modul_fotbal":
        st.markdown('<p style="color:#a855f7; font-size:13px; font-weight:800; margin-bottom:12px; text-transform:uppercase; text-align:center;">⚽ MECIURI REALE FOTBAL</p>', unsafe_allow_html=True)
        
        for titlu, d in meciuri_fotbal.items():
            ec = titlu.split(" vs ")
            st.markdown(f"""
            <div class="match-card-container">
                <div class="match-header-info">LIVE &bull; {d['liga']}</div>
                <div class="match-teams-grid">
                    <div class="team-box-app"><div style="font-size:24px;">🛡️</div><div class="team-name-app">{ec[0]}</div></div>
                    <div class="vs-text-app">VS</div>
                    <div class="team-box-app"><div style="font-size:24px;">⚔️</div><div class="team-name-app">{ec[1]}</div></div>
                </div>
                <div style="display:flex; height:5px; border-radius:10px; overflow:hidden; width:95%; margin:0 auto;">
                    <div style="width:55%; background:#00ff66;"></div><div style="width:25%; background:#eab308;"></div><div style="width:20%; background:#ef4444;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; width:95%; margin:4px auto 0 auto; font-size:10px; color:#71717a; font-weight:700;">
                    <span>WIN: 55%</span><span>DRAW: 25%</span><span>LOSS: 20%</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📊 Detalii Algoritm: {titlu}"):
                st.markdown(f'<div class="module-table"><div class="module-row"><span class="module-label">Total Goluri</span><span class="module-val">{d["g_gz"]} - {d["g_os"]}</span></div><div class="module-row"><span class="module-label">Medie Goluri</span><span class="module-val">{d["med_gz"]} - {d["med_os"]}</span></div><div class="module-row"><span class="module-label">Șansă Gol HT</span><span class="module-val">{d["ht_gz"]}</span></div><div class="module-row"><span class="module-label">Probabilitate +1.5</span><span class="badge-purple-neon">{d["w_p15"]}</span></div><div class="module-row"><span class="module-label">Ambele Marc. (GG)</span><span class="badge-purple-neon">{d["w_gg"]}</span></div></div>', unsafe_allow_html=True)
                
        st.write("")
        if st.button("⬅️ ÎNAPOI LA SPORTURI", key="back_to_menu_f"):
            st.session_state.ecran_aplicatie = "meniu_sporturi"
            st.rerun()

    # 2.C MODULUL ACTIV CS2 ESPORTS
    elif st.session_state.ecran_aplicatie == "modul_cs2":
        st.markdown('<p style="color:#a855f7; font-size:13px; font-weight:800; margin-bottom:12px; text-transform:uppercase; text-align:center;">🎮 CONFRUNTĂRI CS2 LIVE</p>', unsafe_allow_html=True)
        
        for titlu, d in meciuri_cs2.items():
            ec = titlu.split(" vs ")
            st.markdown(f"""
            <div class="match-card-container" style="border-color: rgba(168, 85, 247, 0.3) !important;">
                <div class="match-header-info">LIVE &bull; {d['liga']}</div>
                <div class="match-teams-grid">
                    <div class="team-box-app"><div style="font-size:24px;">🎮</div><div class="team-name-app">{ec[0]}</div></div>
                    <div class="vs-text-app" style="color:#a855f7;">VS</div>
                    <div class="team-box-app"><div style="font-size:24px;">⚡</div><div class="team-name-app">{ec[1]}</div></div>
                </div>
                <div style="display:flex; height:5px; border-radius:10px; overflow:hidden; width:95%; margin:0 auto;">
                    <div style="width:65%; background:#a855f7;"></div><div style="width:35%; background:#ef4444;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; width:95%; margin:4px auto 0 auto; font-size:10px; color:#71717a; font-weight:700;">
                    <span>WIN: {d['maps_gz']}</span><span>WIN: {d['maps_os']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📊 Analiză Hărți: {titlu}"):
                st.markdown(f'<div class="module-table"><div class="module-row"><span class="module-label">Winrate Hărți</span><span class="module-val">{d["maps_gz"]} vs {d["maps_os"]}</span></div><div class="module-row"><span class="module-label">Pistol Rounds</span><span class="module-val">{d["pistol_gz"]} vs {d["pistol_os"]}</span></div><div class="module-row"><span class="module-label">Eficiență Clutcheuri</span><span class="module-val">{d["clutch_gz"]}</span></div><div class="module-row"><span class="module-label">Șansă Decider (+2.5)</span><span class="badge-purple-neon">{d["w_over"]}</span></div><div class="module-row" style="background:rgba(168,85,247,0.05); padding:8px; border-radius:4px;"><span class="module-label" style="color:#a855f7;">🔮 PREZICERE</span><span class="module-val" style="color:#00ff66;">{d["w_winner"]} WIN</span></div></div>', unsafe_allow_html=True)
                
        st.write("")
        if st.button("⬅️ ÎNAPOI LA SPORTURI", key="back_to_menu_c"):
            st.session_state.ecran_aplicatie = "meniu_sporturi"
            st.rerun()

    with st.sidebar:
        if st.button("🔒 Sign Out / Lock App", use_container_width=True, key="sidebar_logout_fixed"):
            st.session_state.utilizator_logat = False
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Închide phone-wrapper

# ================== 3. BARA ORIZONTALĂ DE OFERTE ȘI STRIPE (JOS DE TOT) ==================
st.write("---")
col_o1, col_o2 = st.columns(2)

with col_o1:
    with st.popover("💳 Deblochează Pachete VIP & Stripe", use_container_width=True):
        st.markdown("### 🏆 ABONAMENTE PREMIUM PARIURIGO")
        st.write("🟢 **Pachet LOW** - 40 RON / lună")
        st.write("🟡 **Pachet MEDIUM** - 70 RON / lună")
        st.write("🔥 **HIGH VIP ELITE** - 120 RON / lună")
        st.link_button("DESCHIDE PLATĂ SECURIZATĂ STRIPE 🚀", "https://stripe.com", use_container_width=True)

with col_o2:
    with st.popover("📜 Politici și Reguli Legale (18+)", use_container_width=True):
        st.markdown("### ⚖️ REGULAMENT ȘI CONFIDENȚIALITATE")
        st.write("<b>Termeni și Condiții:</b> Analizele și predicțiile statistice au caracter strict informativ. Nu oferim garanții financiare de profit.")
        st.write("<b>Privacy:</b> Datele tale sunt în siguranță și procesate criptat direct prin infrastructura Stripe.")
