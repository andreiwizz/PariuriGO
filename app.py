import streamlit as st
from datetime import datetime
from baza import aplica_stiluri_aplicatie_nativa, obtine_meciurile_zilei_automat

st.set_page_config(
    page_title="PariuriGO Application Center",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")
aplica_stiluri_aplicatie_nativa()

if "ecran_activ" not in st.session_state:
    st.session_state.ecran_activ = "meniu_sporturi"

# BARA DE CĂUTARE DE SUS STIL TIKTOK APP
st.markdown("""
<div class="app-search-bar">
    <div style="font-size: 15px; color: #a1a1aa; font-weight: 700;">Găsește meciuri sau statistici avansate...</div>
    <div style="font-size: 18px; color: #b042ff; font-weight: 800;">🔍</div>
</div>
""", unsafe_allow_html=True)

# ECRANUL PRINCIPAL: SELECȚIE CATEGORII SPORTURI
if st.session_state.ecran_activ == "meniu_sporturi":
    st.markdown('<p style="color:#b042ff; font-size:14px; font-weight:800; margin-bottom:15px; text-transform:uppercase; letter-spacing:0.5px;">🔥 Categorii Disponibile în Algoritm</p>', unsafe_allow_html=True)
    
    optiune_sport = st.selectbox("⚡ SELECTEAZĂ PENTRU DESCHIDERE PORTAL:", ["Alege un sport activ...", "⚽ FOTBAL (Predictions Engine)", "🎮 COUNTER-STRIKE 2 (CS2)"], key="selector_nativ_app")
    
    if optiune_sport == "⚽ FOTBAL (Predictions Engine)":
        st.session_state.ecran_activ = "modul_fotbal"
        st.rerun()
    elif optiune_sport == "🎮 COUNTER-STRIKE 2 (CS2)":
        st.session_state.ecran_activ = "modul_cs2"
        st.rerun()

    st.write("")

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
    <div style="background: rgba(255,255,255,0.02); padding: 12px; border-radius: 12px; margin-top: 20px; border: 1px solid rgba(255,255,255,0.05);">
        <span style="color:#a1a1aa; font-size:13px;">ℹ️ <b>Disclaimer:</b> Licențe date active • Probabilități bazate pe modele matematice • Destinat persoanelor majorizate 18+</span>
    </div>
    """, unsafe_allow_html=True)
elif st.session_state.ecran_activ == "modul_fotbal":
    meciuri_f = obtine_meciurile_zilei_automat()
    st.markdown('<p style="color:#b042ff; font-size:14px; font-weight:800; margin-bottom:15px; text-transform:uppercase;">⚽ PROGRAM FOTBAL LIVE INTERACTIV</p>', unsafe_allow_html=True)
    
    for titlu_meci, date_meci in meciuri_f.items():
        echipe = titlu_meci.split(" vs ")
        st.markdown(f"""
        <div class="match-card-container">
            <div class="match-header-info">NS &bull; {date_meci['liga']}</div>
            <div class="match-teams-grid">
                <div class="team-box-app"><div style="font-size:32px;">🛡️</div><div class="team-name-app">{echipe[0]}</div></div>
                <div class="vs-text-app">VS</div>
                <div class="team-box-app"><div style="font-size:32px;">⚔️</div><div class="team-name-app">{echipe[1]}</div></div>
            </div>
            <div style="display:flex; height:6px; border-radius:10px; overflow:hidden; width:90%; margin: 0 auto;">
                <div style="width:55%; background:#00ff66; box-shadow: 0 0 5px #00ff66;"></div>
                <div style="width:25%; background:#eab308;"></div>
                <div style="width:20%; background:#ef4444;"></div>
            </div>
            <div style="display:flex; justify-content:space-between; width:90%; margin:5px auto 0 auto; font-size:11px; color:#71717a; font-weight:700;">
                <span>WIN: 55%</span><span>DRAW: 25%</span><span>LOSS: 20%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"📊 Analiză Algoritm: {titlu_meci}"):
            st.markdown('<div class="module-table">', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Total Goluri</span><span class="module-val">{date_meci["g_gz"]} - {date_meci["g_os"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Medie Goluri</span><span class="module-val">{date_meci["med_gz"]} - {date_meci["med_os"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Șansă Gol R1 (HT)</span><span class="module-val">{date_meci["ht_gz"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Probabilitate Peste 1.5</span><span class="badge-purple-neon">{date_meci["w_p15"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Ambele Marchează (GG)</span><span class="badge-purple-neon">{date_meci["w_gg"]}</span></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
    st.write("")
    if st.button("⬅️ ÎNAPOI LA SPORTURI", key="back_from_f_auto"):
        st.session_state.ecran_activ = "meniu_sporturi"
        st.rerun()

elif st.session_state.ecran_activ == "modul_cs2":
    from baza import obtine_cs2_zilei_automat
    meciuri_c = obtine_cs2_zilei_automat()
    st.markdown('<p style="color:#b042ff; font-size:14px; font-weight:800; margin-bottom:15px; text-transform:uppercase;">🎮 PROGRAM CS2 LIVE INTERACTIV</p>', unsafe_allow_html=True)
    
    for titlu_meci, date_meci in meciuri_c.items():
        echipe = titlu_meci.split(" vs ")
        st.markdown(f"""
        <div class="match-card-container" style="border-color: rgba(176, 66, 255, 0.3) !important;">
            <div class="match-header-info">NS &bull; {date_meci['liga']}</div>
            <div class="match-teams-grid">
                <div class="team-box-app"><div style="font-size:32px;">🎮</div><div class="team-name-app">{echipe[0]}</div></div>
                <div class="vs-text-app" style="color:#b042ff;">VS</div>
                <div class="team-box-app"><div style="font-size:32px;">⚡</div><div class="team-name-app">{echipe[1]}</div></div>
            </div>
            <div style="display:flex; height:6px; border-radius:10px; overflow:hidden; width:90%; margin: 0 auto;">
                <div style="width:60%; background:#b042ff; box-shadow: 0 0 5px #b042ff;"></div>
                <div style="width:40%; background:#ef4444;"></div>
            </div>
            <div style="display:flex; justify-content:space-between; width:90%; margin:5px auto 0 auto; font-size:11px; color:#71717a; font-weight:700;">
                <span>WIN {echipe[0]}: {date_meci['maps_gz']}</span><span>WIN {echipe[1]}: {date_meci['maps_os']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(f"📊 Date Algoritm CS2: {titlu_meci}"):
            st.markdown('<div class="module-table">', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Winrate Hărți</span><span class="module-val">{date_meci["maps_gz"]} vs {date_meci["maps_os"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Pistol Rounds</span><span class="module-val">{date_meci["pistol_gz"]} vs {date_meci["pistol_os"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Eficiență Clutcheuri</span><span class="module-val">{date_meci["clutch_gz"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row"><span class="module-label">Șansă Decider (+2.5)</span><span class="badge-purple-neon">{date_meci["w_over"]}</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="module-row" style="background: rgba(176,66,255,0.05); padding: 12px 8px; border-radius: 6px;"><span class="module-label" style="color:#b042ff;">🔮 PREZICERE CÂȘTIGĂTOR</span><span class="module-val" style="color:#00ff66; font-size:16px;">{date_meci["w_winner"]} WIN</span></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("⬅️ ÎNAPOI LA SPORTURI", key="back_from_c_auto"):
        st.session_state.ecran_activ = "meniu_sporturi"
        st.rerun()

# EXTRA SETĂRI JOS
st.write("---")
col_nav_1, col_nav_2 = st.columns(2)
with col_nav_1:
    with st.popover("💳 Deblochează Pachete VIP & Stripe"):
        st.markdown("### 🏆 ABONAMENTE PREMIUM PARIURIGO")
        st.write("🟢 **Pachet LOW** - 40 RON / lună")
        st.write("🟡 **Pachet MEDIUM** - 70 RON / lună")
        st.write("🔥 **HIGH VIP ELITE** - 120 RON / lună")
        st.link_button("DESCHIDE PLATĂ SECURIZATĂ STRIPE 🚀", "https://stripe.com", use_container_width=True)
with col_nav_2:
    with st.popover("📜 Politici și Reguli Legale (18+)"):
        st.markdown("### ⚖️ TERMENI ȘI CONFIDENȚIALITATE")
        st.write("<b>Termeni și Condiții:</b> Analizele și predicțiile au caracter strict informativ. Nu oferim garanții financiare de profit.")
