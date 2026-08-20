import streamlit as st
from datetime import datetime, timedelta

# 1. Configurare Pagină Full-Screen
st.set_page_config(
    page_title="PariuriGO • Golden System",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")
data_maine = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")

# TOATE STILURILE NATIVE DIN GOLDEN TIPS FORȚATE PE MOV VIP
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #040406 !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    h1, h2, h3, h4, p, span, label { font-family: 'Plus Jakarta Sans', sans-serif !important; }

    /* FORMATUL DE TELEFON MOBIL CENTRAT */
    .phone-wrapper-container {
        max-width: 410px;
        margin: 10px auto;
        background: #09090e !important;
        border: 1px solid #1e1b4b;
        border-radius: 40px;
        padding: 20px;
        box-shadow: 0 25px 60px -15px rgba(168, 85, 247, 0.2);
        position: relative;
        min-height: 760px;
    }
    
    .phone-notch {
        width: 120px; height: 23px; background: #000000;
        margin: -10px auto 20px auto; border-radius: 20px; border: 1px solid #1e1b4b;
    }

    .app-top-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; padding: 0 5px; }

    /* BANNER-UL PRINCIPAL DIN GOLDEN TIPS */
    .fantasy-banner-card {
        background: linear-gradient(135deg, #120b2e 0%, #05040f 100%);
        border: 1px solid #b042ff;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 18px;
        box-shadow: 0 8px 25px rgba(176, 66, 255, 0.15);
    }
    
    .fantasy-badge {
        background: rgba(176, 66, 255, 0.2); color: #b042ff !important;
        font-size: 10px; font-weight: 800; padding: 4px 10px; border-radius: 12px; display: inline-block; margin-bottom: 8px;
    }

    /* CARDURILE MARE DE MENIU (BUTOANE ACTIVE) */
    div.stButton > button {
        background: #100f1c !important;
        border: 1px solid #1e1b4b !important;
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        border-radius: 16px !important;
        padding: 14px 16px !important;
        width: 100% !important;
        text-align: left !important;
        display: block !important;
        margin-bottom: -5px !important;
    }
    
    div.stButton > button:hover {
        border-color: #b042ff !important;
        background: #17152b !important;
    }

    /* CASETĂ BILET / MECIURI STIL GOLDEN TIPS */
    .match-card-container {
        background: #100f1c !important;
        border: 1px solid #1e1b4b !important;
        border-radius: 18px !important;
        padding: 16px !important;
        margin-bottom: 12px !important;
        text-align: center;
    }
    .match-header-info { font-size: 11px; color: #b042ff; font-weight: 700; margin-bottom: 8px; text-transform: uppercase; }
    .match-teams-grid { display: flex; justify-content: space-around; align-items: center; margin: 10px 0; }
    .team-name-app { font-size: 14px; font-weight: 800; color: #ffffff; }

    /* NAVBAR DE JOS CURBAT */
    .app-bottom-navbar {
        display: flex;
        justify-content: space-around;
        align-items: center;
        background: #100f1c;
        border-top: 1px solid #1e1b4b;
        padding: 12px 5px;
        margin-top: 25px;
        border-radius: 0 0 24px 24px;
    }
    .nav-item-bottom { text-align: center; font-size: 11px; color: #a1a1aa; font-weight: 700; }
    .nav-item-center-gold {
        background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%);
        width: 44px; height: 44px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center; font-size: 20px;
        margin-top: -24px; box-shadow: 0 4px 15px rgba(176, 66, 255, 0.4);
    }
    
    .stTextInput div[data-baseweb="input"] { background-color: rgba(255,255,255,0.01) !important; border: 1px solid #1e1b4b !important; border-radius: 14px !important; }
    .stTextInput input { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# Inițializăm variabilele de sistem în starea aplicației
if "user_logat" not in st.session_state: st.session_state.user_logat = False
if "pachet_utilizator" not in st.session_state: st.session_state.pachet_utilizator = "free"
if "baza_date_utilizatori" not in st.session_state: st.session_state.baza_date_utilizatori = {"admin": "pariurigo", "andreiwizz": "Parola123parola"}
if "mod_ecran_autentificare" not in st.session_state: st.session_state.mod_ecran_autentificare = "login"
if "functie_activa" not in st.session_state: st.session_state.functie_activa = "meniu_acasa"
if "chat_mesaje" not in st.session_state: st.session_state.chat_mesaje = [{"user": "AndreiWizz 👑", "text": "Biletele pentru meciurile de diseară sunt live la secțiune! Spor la profit!"}]

# MECIURI REALE DE AZI ȘI DE MÂINE (20 - 21 AUGUST 2026)
if "meciuri_fotbal_store" not in st.session_state:
    st.session_state.meciuri_fotbal_store = {
        "LASK Linz vs FCSB": { "zi": "Azi", "liga": "UEFA EUROPA LEAGUE", "win_gz": "45%", "win_os": "55%", "tip": "Peste 1.5 goluri", "cota": "1.35" },
        "CFR Cluj vs Pafos FC": { "zi": "Azi", "liga": "UEFA CONFERENCE LEAGUE", "win_gz": "65%", "win_os": "35%", "tip": "1 Solist", "cota": "1.60" },
        "Borussia Dortmund vs Frankfurt": { "zi": "Mâine", "liga": "GERMAN BUNDESLIGA", "win_gz": "58%", "win_os": "42%", "tip": "Ambele marchează (GG)", "cota": "1.72" }
    }

# DESCHIDEM CADRUL TELEFONULUI MOBIL
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

# LOGIN SYSTEM NATIV ÎN INTERIORUL TELEFONULUI
if not st.session_state.user_logat:
    if st.session_state.mod_ecran_autentificare == "login":
        st.markdown("<h1 style='text-align:center; font-size:32px; font-weight:800; background: linear-gradient(135deg, #ffffff 0%, #b042ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>PariuriGO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:-10px; margin-bottom:25px;'>Connect to the official Golden Tips engine</p>", unsafe_allow_html=True)
        
        u_in = st.text_input("USER IDENTITY", placeholder="Username...", key="u_key_golden")
        p_in = st.text_input("SECURE KEY", type="password", placeholder="Password...", key="p_key_golden")
        
        st.write("")
        if st.button("👉 CONNECT SYSTEM PORTAL", key="btn_login_exec_golden"):
            if u_in in st.session_state.baza_date_utilizatori and st.session_state.baza_date_utilizatori[u_in] == p_in:
                st.session_state.user_logat = True
                if u_in in ["admin", "andreiwizz"]: st.session_state.pachet_utilizator = "full"
                else: st.session_state.pachet_utilizator = "free"
                st.rerun()
            else: st.error("Access Denied!")
            
        st.write("---")
        if st.button("➕ CREATE PREMIUM ACCOUNT", key="btn_go_reg_golden"):
            st.session_state.mod_ecran_autentificare = "register"
            st.rerun()

    elif st.session_state.mod_ecran_autentificare == "register":
        st.markdown("<h1 style='text-align:center; font-size:28px; font-weight:800; color:#b042ff;'>Sign Up</h1>", unsafe_allow_html=True)
        reg_u = st.text_input("CHOOSE USERNAME", placeholder="Pick profile name...", key="ru_golden")
        reg_p = st.text_input("CHOOSE SECURE KEY", type="password", placeholder="Create password...", key="rp_golden")
        reg_cp = st.text_input("CONFIRM SECURE KEY", type="password", placeholder="Repeat password...", key="rcp_golden")
        
        st.write("")
        if st.button("✨ REGISTER PROFILE NOW", key="btn_reg_exec_golden"):
            if not reg_u or not reg_p: st.error("All fields required!")
            elif reg_u in st.session_state.baza_date_utilizatori: st.error("Username taken!")
            elif reg_p != reg_cp: st.error("Passwords do not match!")
            else:
                st.session_state.baza_date_utilizatori[reg_u] = reg_p
                st.success("Account created!")
                st.session_state.mod_ecran_autentificare = "login"
                st.rerun()
        st.write("---")
        if st.button("⬅️ BACK TO LOG IN", key="btn_back_golden"):
            st.session_state.mod_ecran_autentificare = "login"
            st.rerun()
# ================== INTERFATA PREMIUM DEBLOCATĂ (SISTEM IDENTIC GOLDEN TIPS) ==================
else:
    st.markdown("""
    <div class="app-top-header">
        <span style="font-size: 16px; font-weight: 700; color: #71717a;">🔀</span>
        <span style="font-size: 20px; font-weight: 800; color: #ffffff;"><span style="color:#b042ff;">PariuriGO</span> PRO</span>
        <span style="font-size: 16px; color: #b042ff;">☰</span>
    </div>
    <div class="fantasy-banner-card">
        <div class="fantasy-badge">&bull; LIVE METRIC SYSTEM</div>
        <h3 style="margin: 0 0 4px 0; font-size: 19px; font-weight: 800; color: #ffffff;">FANTASY ENGINE</h3>
        <p style="margin: 0; font-size: 11px; color: #a1a1aa; line-height: 1.4;">Sistem automatizat bazat pe algoritmi predictivi si statistici detaliate.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.functie_activa == "meniu_acasa":
        if st.button("💬 &nbsp;&nbsp;&nbsp;&nbsp; Comunitate Live Chat \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Mesaje si ponturi de ultim moment de la admini", key="g_chat"):
            if st.session_state.pachet_utilizator == "full": st.session_state.functie_activa = "ecran_chat_vip"
            else: st.session_state.functie_activa = "ecran_blocat_vip"
            st.rerun()
        st.write("")
        if st.button("📊 &nbsp;&nbsp;&nbsp;&nbsp; Algoritm Meciuri Zilnice \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Lista completa cu meciurile si procentele de AZI / MAINE", key="g_stats"):
            if st.session_state.pachet_utilizator == "full": st.session_state.functie_activa = "ecran_meciuri_vip"
            else: st.session_state.functie_activa = "ecran_blocat_vip"
            st.rerun()
        st.write("")
        if st.button("🎟️ &nbsp;&nbsp;&nbsp;&nbsp; Biletul Zilei / Cota 2 \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Combinatia premium generata automat pentru profit sigur", key="g_bilet"):
            if st.session_state.pachet_utilizator == "full": st.session_state.functie_activa = "ecran_bilet_vip"
            else: st.session_state.functie_activa = "ecran_blocat_vip"
            st.rerun()
        st.write("")
        if st.button("💰 &nbsp;&nbsp;&nbsp;&nbsp; Calculator Profit Bankroll \n\n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Monitorizeaza-ti bugetul si mizele zilnice", key="g_bank"):
            st.session_state.functie_activa = "ecran_bankroll_vip"; st.rerun()

        if st.session_state.pachet_utilizator == "full":
            st.write("---")
            st.markdown("<p style='color:#00ff66; font-size:13px; font-weight:800; text-align:center;'>🛠️ GOLDEN CONTROL PANEL (ADMIN ONLY)</p>", unsafe_allow_html=True)
            with st.expander("➕ ADAUGĂ MECI DIRECT DIN APLICAȚIE"):
                noul_meci = st.text_input("Nume meci (Ex: Real Madrid vs Man. City)", key="adm_nume")
                noua_zi = st.radio("Ziua programata:", ["Azi", "Mâine"], key="adm_zi")
                noua_liga = st.text_input("Competitie & Ora", placeholder="Ex: UEFA CHAMPIONS LEAGUE • 22:00", key="adm_liga")
                noul_pronostic = st.text_input("Pronostic Recomandat", placeholder="Ex: Peste 2.5 goluri", key="adm_prono")
                if st.button("💥 PUBLICA MECIUL INSTANT PE SITE", key="adm_save_btn"):
                    if noul_meci and noua_liga:
                        st.session_state.meciuri_fotbal_store[noul_meci] = {"zi": noua_zi, "liga": noua_liga, "win_gz": "60%", "win_os": "40%", "tip": noul_pronostic, "cota": "1.50"}
                        st.success("Meci publicat!"); st.rerun()

    elif st.session_state.functie_activa == "ecran_blocat_vip":
        st.markdown("""
        <div class="match-card-container" style="border-color:#ef4444 !important; background:linear-gradient(135deg, #1c1010 0%, #05040f 100%) !important;">
            <h3 style="color:#ef4444; margin:0 0 6px 0; font-size:20px; font-weight:800;">🔒 ACCES RESTRÂNS VIP</h3>
            <p style="color:#cbd5e1; font-size:12px; line-height:1.4; margin-bottom:12px;">Sectiunea contine biletul zilei, algoritmul si chat-ul. Deblocheaza pachetul complet prin Stripe!</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("💳 DEBLOCHEAZĂ PACHETUL PREMIUM", "https://stripe.com", use_container_width=True)
        st.write("")
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_lock"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()
    # ------------------ SECTIUNEA 3: ALGORITM MECIURI INTERACTIV (AZI / MAINE) ------------------
    elif st.session_state.functie_activa == "ecran_meciuri_vip":
        st.markdown('<div style="text-align:center; font-size:14px; font-weight:800; color:#b042ff; margin-bottom:10px;">📊 FILTREAZĂ CALENDARUL MECIURILOR</div>', unsafe_allow_html=True)
        filtru_zi = st.radio("Selecteaza programul:", ["Azi", "Mâine"], horizontal=True, key="fil_zi_key")
        st.write("---")
        for titlu, d in st.session_state.meciuri_fotbal_store.items():
            if d["zi"] == filtru_zi:
                ec = titlu.split(" vs ")
                st.markdown(f"""
                <div class="match-card-container">
                    <div class="match-header-info">{d['liga']} &bull; {data_azi if filtru_zi == "Azi" else data_maine}</div>
                    <div class="match-teams-grid">
                        <div class="team-box-app"><div style="font-size:20px;">🛡️</div><div class="team-name-app">{ec[0] if len(ec)>0 else "Gazde"}</div></div>
                        <div class="vs-text-app" style="color:#b042ff; font-weight:800;">VS</div>
                        <div class="team-box-app"><div style="font-size:20px;">⚔️</div><div class="team-name-app">{ec[1] if len(ec)>1 else "Oaspeti"}</div></div>
                    </div>
                    <div style="display:flex; height:5px; border-radius:10px; overflow:hidden; width:95%; margin:0 auto; background:#1e1b4b;">
                        <div style="width:{d['win_gz'].replace('%','') if 'win_gz' in d else '50'}%; background:#00ff66;"></div>
                        <div style="width:{d['win_os'].replace('%','') if 'win_os' in d else '50'}%; background:#ef4444;"></div>
                    </div>
                    <div style="margin-top:10px; font-size:12px; color:#cbd5e1; text-align:left; background:rgba(255,255,255,0.01); padding:8px; border-radius:8px;">
                        🎯 Pronostic recomandat: <b style="color:#00ff66;">{d['tip']}</b><br>
                        📈 Probabilitate calculata: <b>{d['win_gz']} Gazde vs {d['win_os']} Oaspeti</b>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_m_vip"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()

    # ------------------ SECTIUNEA 4: BILETUL ZILEI / COTA 2 ------------------
    elif st.session_state.functie_activa == "ecran_bilet_vip":
        st.markdown('<div style="text-align:center; font-size:14px; font-weight:800; color:#b042ff; margin-bottom:12px;">🎟️ BILETUL ZILEI COMBINAT (COTA 2.15)</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="match-card-container" style="border-color: #00ff66 !important; background: linear-gradient(135deg, #091a10 0%, #05040f 100%) !important;">
            <h4 style="color:#00ff66; margin:0 0 5px 0; font-size:16px;">🟢 BILET RECOMANDAT ACTIV ({data_azi})</h4>
            <p style="text-align:left; font-size:12px; color:#cbd5e1; margin:8px 0 0 0; line-height:1.5;">
                • <b>LASK Linz vs FCSB</b> -> Peste 1.5 Goluri (Cota 1.35)<br>
                • <b>CFR Cluj vs Pafos FC</b> -> 1 Solist (Cota 1.60)<br>
                <hr style="border-color:rgba(255,255,255,0.05); margin:8px 0;">
                💰 <b>COTA TOTALĂ ACCUMULATED: 2.16</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_b_vip"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()

    # ------------------ SECTIUNEA 5: TRACKER PROFIT BANKROLL AUTOMAT ------------------
    elif st.session_state.functie_activa == "ecran_bankroll_vip":
        st.markdown('<div style="text-align:center; font-size:14px; font-weight:800; color:#b042ff; margin-bottom:12px;">💰 CALCULATOR MANAGEMENT BANKROLL</div>', unsafe_allow_html=True)
        miza = st.number_input("Introduceți miza plasată (RON):", min_value=10, value=100, step=10, key="bk_miza")
        cota_utilizator = st.number_input("Introduceți cota biletului:", min_value=1.10, value=2.00, step=0.10, key="bk_cota")
        st.write("")
        if st.button("📊 CALCULEAZĂ CÂȘTIG NET", key="bk_calc_btn"):
            castig_total = miza * cota_utilizator
            profit_pur = castig_total - miza
            st.markdown(f"""
            <div style="background:#100f1c; border:1px solid #00ff66; padding:12px; border-radius:12px; text-align:center; margin-top:10px;">
                <span style="color:#a1a1aa; font-size:12px;">PROFIT NET CALCULAT:</span><br>
                <span style="color:#00ff66; font-size:24px; font-weight:800;">+{profit_pur:.2f} RON</span>
            </div>
            """, unsafe_allow_html=True)
        st.write("")
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_bk_vip"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()

    # ------------------ SECTIUNEA 6: LIVE CHAT ÎN TIMP REAL ------------------
    elif st.session_state.functie_activa == "ecran_chat_vip":
        st.markdown('<div style="text-align:center; font-size:14px; font-weight:800; color:#b042ff; margin-bottom:10px;">💬 LIVE PORTAL COMMUNITY</div>', unsafe_allow_html=True)
        cutie_chat = ""
        for msg in st.session_state.chat_mesaje:
            cutie_chat += f"<p style='margin:4px 0;'><b style='color:#b042ff;'>{msg['user']}:</b> {msg['text']}</p>"
        st.markdown(f"""
        <div style="background:#100f1c; border:1px solid #1e1b4b; padding:12px; border-radius:12px; font-size:12px; min-height:160px; max-height:200px; overflow-y:auto; margin-bottom:12px;">
            {cutie_chat}
        </div>
        """, unsafe_allow_html=True)
        text_mesaj_nou = st.text_input("Scrie un mesaj in comunitate:", placeholder="Scrie mesajul tau public...", key="new_chat_text_box")
        if st.button("🚀 TRIMITE MESAJ", key="btn_send_chat_msg"):
            if text_mesaj_nou:
                expeditor = "AndreiWizz 👑" if st.session_state.pachet_utilizator == "full" else "Membru VIP"
                st.session_state.chat_mesaje.append({"user": expeditor, "text": text_mesaj_nou})
                st.rerun()
        st.write("")
        if st.button("⬅️ ÎNAPOI LA MENIU", key="b_ch_vip"): st.session_state.functie_activa = "meniu_acasa"; st.rerun()

    # BARA ORIZONTALĂ DE ICONIȚE DE JOS (BOTTOM NAVBAR INDIGO)
    st.markdown("""
    <div class="app-bottom-navbar">
        <div class="nav-item-bottom">🤖<br><span style="color:#b042ff;">AI Predict</span></div>
        <div class="nav-item-bottom">⚽<br>Live</div>
        <div class="nav-item-center-gold">🏠</div>
        <div class="nav-item-bottom">🎟️<br>Ticket</div>
        <div class="nav-item-bottom">📞<br>Contact</div>
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        if st.button("🔒 Sign Out / Reset App", use_container_width=True, key="logout_btn_golden_final"):
            st.session_state.user_logat = False
            st.session_state.functie_activa = "meniu_acasa"
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Închide corect phone-wrapper-container
