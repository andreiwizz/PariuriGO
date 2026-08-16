import streamlit as st

# 1. Configurare Pagină principală
st.set_page_config(
    page_title="PariuriGO - Premium Glass UI",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inițializare stare pentru temă (implicit "dark" pentru aspect premium)
if "tema" not in st.session_state:
    st.session_state.tema = "dark"

# Antetul împărțit corect în 2 coloane
col_logo, col_theme = st.columns(2)

with col_theme:
    if st.button("🌓 Schimbă Tema", key="toggle_theme", use_container_width=True):
        st.session_state.tema = "light" if st.session_state.tema == "dark" else "dark"
        st.rerun()

# REPARAT: Link-ul direct și complet către imaginea ta cu terenul de fotbal
bg_image_url = "https://ibb.co"

# Ajustarea filtrelor în funcție de tema selectată
if st.session_state.tema == "dark":
    overlay_color = "rgba(6, 17, 11, 0.82)"
    text_principal = "#ffffff"
    text_secundar = "#94a3b8"
    glass_bg = "rgba(18, 48, 32, 0.5)"
    glass_border = "rgba(0, 255, 102, 0.3)"
    glass_shadow = "rgba(0, 0, 0, 0.6)"
else:
    overlay_color = "rgba(235, 245, 238, 0.85)"
    text_principal = "#0f172a"
    text_secundar = "#475569"
    glass_bg = "rgba(255, 255, 255, 0.6)"
    glass_border = "rgba(32, 77, 58, 0.25)"
    glass_shadow = "rgba(0, 0, 0, 0.12)"

# Injectare stiluri CSS cu terenul tău de fotbal pe fundal
st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient({overlay_color}, {overlay_color}), url('{bg_image_url}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: {text_principal} !important;
        transition: all 0.4s ease;
    }}
    
    .glass-card {{
        background: {glass_bg};
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid {glass_border};
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 35px 0 {glass_shadow};
    }}
    
    .stButton > button {{
        background: {glass_bg} !important;
        color: {text_principal} !important;
        border: 1px solid {glass_border} !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 4px 15px {glass_shadow};
    }}
    
    .stButton > button:hover {{
        background: rgba(0, 255, 102, 0.35) !important;
        border-color: #00ff66 !important;
        box-shadow: 0 0 18px rgba(0, 255, 102, 0.6) !important;
        transform: translateY(-2px);
    }}

    .meci-titlu {{
        font-size: 19px !important;
        font-weight: bold;
        color: {text_principal};
    }}
    .pachet-titlu {{
        font-size: 22px !important;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Antetul Aplicației
with col_logo:
    st.markdown("<h1 style='margin:0; color: #00ff66; text-shadow: 0 3px 12px rgba(0,0,0,0.6);'>⚽ PariuriGO</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='color: {text_secundar}; font-size: 16px; font-weight: 500;'>Design personalizat cu fundal teren de fotbal.</p>", unsafe_allow_html=True)
st.markdown("---")

# Împărțirea ecranului în 2 secțiuni egale
col_meciuri, col_pachete = st.columns(2)

# 3. Panoul cu meciuri
with col_meciuri:
    st.markdown("### 📅 Biletele Zilei")
    
    st.markdown(f"""
    <div class="glass-card">
        <span style="background-color: #ef4444; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">LIVE • Min 72</span>
        <p class="meci-titlu" style="margin-top:10px;">Real Madrid 🆚 Barcelona</p>
        <p style="color: {text_secundar};">Pont selectat: Ambele marchează (GG)</p>
        <h4 style="color: #00ff66; margin:0;">Cotă: 1.65</h4>
    </div>
    <div class="glass-card">
        <span style="background-color: #22c55e; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">PRE-MECI</span>
        <p class="meci-titlu" style="margin-top:10px;">Manchester City 🆚 Liverpool</p>
        <p style="color: {text_secundar};">Pont selectat: Peste 2.5 Goluri</p>
        <h4 style="color: #00ff66; margin:0;">Cotă: 1.80</h4>
    </div>
    """, unsafe_allow_html=True)

# 4. Panoul cu Pachete
with col_pachete:
    st.markdown("### 🏆 Oferte și Pachete VIP")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with tab_low:
        st.markdown(f"""
        <div class="glass-card">
            <p class="pachet-titlu" style="color: #22c55e;">Pachet LOW</p>
            <h2 style="text-align: center; margin:0; color: {text_principal};">19 RON <span style='font-size:14px; color:{text_secundar};'>/ lună</span></h2>
            <hr style="border-color:{glass_border};">
            <p>✅ 3 Bilete analizate / săptămână</p>
            <p>✅ Suport comunitate</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Abonare Rapidă LOW", key="click_low", use_container_width=True)

    with tab_med:
        st.markdown(f"""
        <div class="glass-card">
            <p class="pachet-titlu" style="color: #eab308;">Pachet MEDIUM</p>
            <h2 style="text-align: center; margin:0; color: {text_principal};">49 RON <span style='font-size:14px; color:{text_secundar};'>/ lună</span></h2>
            <hr style="border-color:{glass_border};">
            <p>✅ 1 Bilet premium în fiecare zi</p>
            <p>✅ Notificări rapids prin Telegram</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Abonare Rapidă MEDIUM", key="click_med", use_container_width=True)

    with tab_high:
        st.markdown(f"""
        <div class="glass-card">
            <p class="pachet-titlu" style="color: #ef4444;">Pachet HIGH (VIP)</p>
            <h2 style="text-align: center; margin:0; color: {text_principal};">99 RON <span style='font-size:14px; color:{text_secundar};'>/ lună</span></h2>
            <hr style="border-color:{glass_border};">
            <p>✅ Toate sistemele incluse + Cota 2 VIP</p>
            <p>✅ Consiliere și suport direct 1-la-1</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Abonare Rapidă HIGH VIP", key="click_high", use_container_width=True)
