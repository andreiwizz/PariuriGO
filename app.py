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
# ================== 3. ECRANUL ELEMENTE DE FOTBAL (ALGORITM GOLURI) ==================
elif st.session_state.ecran_activ == "modul_fotbal":
    meciuri_f = date_fotbal_interactiv()
    
    st.markdown('<div class="native-card">', unsafe_allow_html=True)
    st.markdown('<h2 style="margin:0 0 10px 0; font-size:24px; color:#b042ff;">⚽ MODUL ANALIZĂ FOTBAL</h2>', unsafe_allow_html=True)
    
    meci_ales_f = st.selectbox("🎯 Schimbă meciul activ:", list(meciuri_f.keys()), key="sel_f_native")
    m = meciuri_f[meci_ales_f]
    
    st.markdown("<hr style='border-color: #222230; margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center; margin:0; font-size:26px;'>{meci_ales_f}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-size:14px; color:#a1a1aa; margin:3px 0 15px 0;'>🏆 {m['liga']} &bull; {data_azi}</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="module-table">', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Goluri Marcate Gazde</span><span class="module-val">{m["g_gz"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Goluri Marcate Oaspeți</span><span class="module-val">{m["g_os"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Medie Goluri Gazde</span><span class="module-val">{m["med_gz"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Medie Goluri Oaspeți</span><span class="module-val">{m["med_os"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Peste 0.5 goluri HT</span><span class="module-val">{m["ht_gz"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Probabilitate Peste 1.5</span><span class="badge-purple-neon">{m["w_p15"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Șansă Ambele Marchează</span><span class="badge-purple-neon">{m["w_gg"]}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("⬅️ ÎNAPOI LA SPORTURI", key="back_from_f"):
        st.session_state.ecran_activ = "meniu_sporturi"
        st.rerun()

# ================== 4. ECRANUL ELEMENTE DE CS2 (ESPORTS DATA ANALYTICS) ==================
elif st.session_state.ecran_activ == "modul_cs2":
    meciuri_c = date_cs2_interactiv()
    
    st.markdown('<div class="native-card" style="border-color: #b042ff !important;">', unsafe_allow_html=True)
    st.markdown('<h2 style="margin:0 0 10px 0; font-size:24px; color:#b042ff;">🎮 MODUL ANALIZĂ COUNTER-STRIKE 2</h2>', unsafe_allow_html=True)
    
    meci_ales_c = st.selectbox("🎯 Schimbă confruntarea eSports:", list(meciuri_c.keys()), key="sel_c_native")
    mc = meciuri_c[meci_ales_c]
    
    st.markdown("<hr style='border-color: #222230; margin: 15px 0;'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center; margin:0; font-size:26px; color:#ffffff;'>{meci_ales_c}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-size:14px; color:#b042ff; margin:3px 0 15px 0;'>🏆 {mc['liga']} &bull; LIVE STATS</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="module-table">', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Winrate General Hărți Gazde</span><span class="module-val">{mc["maps_gz"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Winrate General Hărți Oaspeți</span><span class="module-val">{mc["maps_os"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Scurgere Pistol Rounds Gazde</span><span class="module-val">{mc["pistol_gz"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Scurgere Pistol Rounds Oaspeți</span><span class="module-val">{mc["pistol_os"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Eficiență Clutcheuri 1vX</span><span class="module-val">{mc["clutch_gz"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row"><span class="module-label">Șansă Peste 2.5 Hărți Finale</span><span class="badge-purple-neon">{mc["w_over"]}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="module-row" style="background: rgba(176,66,255,0.05); padding: 15px 8px; border-radius: 6px;"><span class="module-label" style="color:#b042ff;">🔮 CÂȘTIGĂTOR PREZIS DE ALGORITM</span><span class="module-val" style="color:#00ff66; font-size:18px;">{mc["w_winner"]} WIN</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("⬅️ ÎNAPOI LA SPORTURI", key="back_from_c"):
        st.session_state.ecran_activ = "meniu_sporturi"
        st.rerun()

# ================== 5. EXTRA NAVIGARE JOS (ABONAMENTE ȘI TERMENI EXPANDABILI) ==================
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
        st.write("<b>Termeni și Condiții:</b> Analizele și predicțiile statistice au caracter strict informativ. Nu oferim garanții financiare de profit.")
        st.write("<b>Politică de Confidențialitate:</b> Toate datele de plată sunt procesate direct, criptat și securizat de partenerii noștri de la Stripe.")
