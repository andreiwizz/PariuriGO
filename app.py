import streamlit as st

# Configurare pagină
st.set_page_config(page_title="Pachete PariuriGO", layout="wide")

# Font personalizat pentru titlu (Low, Medium, High) folosind HTML/CSS
st.markdown("""
<style>
    .pachet-titlu {
        font-size: 24px !important;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 10px;
    }
    .pachet-pret {
        font-size: 20px !important;
        font-weight: bold;
        text-align: center;
        color: #2E7D32;
    }
</style>
""", unsafe_allow_html=True)

st.title("Alege Pachetul Tău PariuriGO")
st.write("Selectează nivelul de acces care ți se potrivește cel mai bine:")

# Crearea celor 3 coloane pentru pachete
col1, col2, col3 = st.columns(3)

# 1. PACHETUL LOW
with col1:
    # Imagine mică (înlocuiește link-ul cu imaginea ta dacă dorești)
    st.image("https://flaticon.com", width=70)
    st.markdown('<p class="pachet-titlu">Pachet LOW</p>', unsafe_allow_html=True)
    st.markdown('<p class="pachet-pret">19 RON / lună</p>', unsafe_allow_html=True)
    st.write("- 3 ponturi pe zi")
    st.write("- Cote între 1.50 - 2.00")
    st.write("- Suport de bază")
    if st.button("Cumpără LOW", key="low"):
        st.success("Ai ales pachetul Low! Redirecționare către plată...")

# 2. PACHETUL MEDIUM
with col2:
    st.image("https://flaticon.com", width=70)
    st.markdown('<p class="pachet-titlu">Pachet MEDIUM</p>', unsafe_allow_html=True)
    st.markdown('<p class="pachet-pret">49 RON / lună</p>', unsafe_allow_html=True)
    st.write("- 7 ponturi pe zi")
    st.write("- Cote între 2.00 - 5.00")
    st.write("- Acces la grupul de chat")
    if st.button("Cumpără MEDIUM", key="medium"):
        st.success("Ai ales pachetul Medium! Redirecționare către plată...")

# 3. PACHETUL HIGH
with col3:
    st.image("https://flaticon.com", width=70)
    st.markdown('<p class="pachet-titlu">Pachet HIGH</p>', unsafe_allow_html=True)
    st.markdown('<p class="pachet-pret">99 RON / lună</p>', unsafe_allow_html=True)
    st.write("- Toate ponturile incluse")
    st.write("- Cote VIP (peste 5.00)")
    st.write("- Suport dedicat 24/7")
    if st.button("Cumpără HIGH", key="high"):
        st.success("Ai ales pachetul High! Redirecționare către plată...")

import streamlit as st

# 1. Configurare Pagină și Tematică Vizuală (Skin)
st.set_page_config(
    page_title="PariuriGO - Premium Football Tips",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Stiluri CSS pentru a schimba complet aspectul (Culori fotbal: verde, gri închis, text alb/auriu)
st.markdown("""
<style>
    /* Fundalul general al aplicației */
    .stApp {
        background-color: #0d1b15; /* Verde extrem de închis, stil stadion nocturn */
        color: #ffffff;
    }
    
    /* Cardurile pentru Meciuri și Pachete */
    .custom-card {
        background-color: #162e24; /* Verde închis pentru contrast */
        border: 2px solid #204d3a;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Stiluri text */
    .meci-titlu {
        font-size: 18px !important;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 5px;
    }
    .cota-text {
        font-size: 22px !important;
        font-weight: 800;
        color: #00ff66; /* Verde neon pentru cote și câștiguri */
    }
    .pachet-premium-titlu {
        font-size: 24px !important;
        font-weight: 800;
        text-align: center;
        color: #ffcc00; /* Auriu pentru pachetele VIP */
        text-transform: uppercase;
    }
    .pret-premium {
        font-size: 26px !important;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 2. Header-ul Aplicației (Interfața de Sus)
st.markdown("<h1 style='text-align: center; color: #00ff66;'>⚽ PariuriGO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #a0aec0;'>Platforma ta de analiză și ponturi premium din fotbal</p>", unsafe_allow_html=True)
st.markdown("---")

# Spacing pentru organizare
col_stanga, col_dreapta = st.columns([2, 1])

# 3. ZONA DIN STÂNGA: Meciurile Zilei (Interfață tip Casă de Pariuri)
with col_stanga:
    st.markdown("### 📅 Meciurile Recomandate de Azi")
    
    # Meciul 1
    st.markdown("""
    <div class="custom-card">
        <span style="background-color: #ff3333; color: white; padding: 3px 8px; border-radius: 5px; font-size: 12px; font-weight: bold;">LIVE • Min 65</span>
        <p class="meci-titlu">Real Madrid 🆚 Barcelona</p>
        <p style="color: #a0aec0; margin-bottom: 10px;">Pont: Ambele marchează (GG)</p>
        <span class="cota-text">Cotă: 1.65</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Meciul 2
    st.markdown("""
    <div class="custom-card">
        <span style="background-color: #204d3a; color: #00ff66; padding: 3px 8px; border-radius: 5px; font-size: 12px; font-weight: bold;">PRE-MECI • 21:45</span>
        <p class="meci-titlu">Manchester City 🆚 Liverpool</p>
        <p style="color: #a0aec0; margin-bottom: 10px;">Pont: Peste 2.5 goluri în meci</p>
        <span class="cota-text">Cotă: 1.80</span>
    </div>
    """, unsafe_allow_html=True)

# 4. ZONA DIN DREAPTA: Pachetele de Cumpărat (Low, Medium, High)
with col_dreapta:
    st.markdown("### 🏆 Deblochează Toate Ponturile")
    
    # Selector vizual rapid pentru utilizator
    pachet_selectat = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with pachet_selectat[0]:
        st.markdown("""
        <div class="custom-card" style="border-color: #00ff66;">
            <p class="pachet-premium-titlu" style="color: #00ff66;">Pachet LOW</p>
            <p class="pret-premium">19 RON <span style='font-size:14px; color:#a0aec0;'>/ lună</span></p>
            <p>✅ 3 Biletul Zilei / săptămână</p>
            <p>✅ Cote sigure (1.40 - 1.80)</p>
            <p>✅ Acces grup public</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Abonare LOW", key="btn_low", use_container_width=True):
            st.success("Redirecționare securizată către plata Pachetului Low...")

    with pachet_selectat[1]:
        st.markdown("""
        <div class="custom-card" style="border-color: #ffcc00;">
            <p class="pachet-premium-titlu" style="color: #ffcc00;">Pachet MEDIUM</p>
            <p class="pret-premium">49 RON <span style='font-size:14px; color:#a0aec0;'>/ lună</span></p>
            <p>✅ 1 Bilet pe zi garantat</p>
            <p>✅ Cote medii (2.00 - 4.00)</p>
            <p>✅ Notificări instant Telegram</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Abonare MEDIUM", key="btn_med", use_container_width=True):
            st.success("Redirecționare securizată către plata Pachetului Medium...")

    with pachet_selectat[2]:
        st.markdown("""
        <div class="custom-card" style="border-color: #ff3333;">
            <p class="pachet-premium-titlu" style="color: #ff3333;">Pachet HIGH (VIP)</p>
            <p class="pret-premium">99 RON <span style='font-size:14px; color:#a0aec0;'>/ lună</span></p>
            <p>✅ Toate biletele + Proiect Dublare</p>
            <p>✅ Cote mari & Cota 2 VIP zilnic</p>
            <p>✅ Suport privat 1-la-1</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Abonare HIGH VIP", key="btn_high", use_container_width=True):
            st.success("Redirecționare securizată către plata Pachetului High VIP...")

import streamlit as st

# 1. Configurare Pagină principală
st.set_page_config(
    page_title="PariuriGO - Premium Glass UI",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inițializare stare pentru temă (implicit "dark")
if "tema" not in st.session_state:
    st.session_state.tema = "dark"

# Zona superioară pentru butonul de control al temei
col_logo, col_theme = st.columns([6, 1])

with col_theme:
    # Buton stilizat tip Glassmorphism pentru comutarea temei (Luminos/Întunecat)
    if st.button("🌓 Schimbă Tema", key="toggle_theme", use_container_width=True):
        st.session_state.tema = "light" if st.session_state.tema == "dark" else "dark"
        st.rerun()

# Stabilirea variabilelor de design în funcție de starea curentă
if st.session_state.tema == "dark":
    bg_app = "linear-gradient(135deg, #091711 0%, #050b08 100%)"
    text_principal = "#ffffff"
    text_secundar = "#94a3b8"
    glass_bg = "rgba(22, 46, 36, 0.4)"
    glass_border = "rgba(0, 255, 102, 0.2)"
    glass_shadow = "rgba(0, 0, 0, 0.5)"
else:
    bg_app = "linear-gradient(135deg, #f0fdf4 0%, #e2e8f0 100%)"
    text_principal = "#0f172a"
    text_secundar = "#475569"
    glass_bg = "rgba(255, 255, 255, 0.4)"
    glass_border = "rgba(32, 77, 58, 0.15)"
    glass_shadow = "rgba(0, 0, 0, 0.08)"

# Injectare stiluri CSS dinamice pentru temă și stilul de sticlă (Glassmorphism)
st.markdown(f"""
<style>
    /* Aplicarea fundalului general */
    .stApp {{
        background: {bg_app} !important;
        color: {text_principal} !important;
        transition: background 0.3s ease;
    }}
    
    /* Carduri și panouri cu efect de sticlă (Glassmorphism) */
    .glass-card {{
        background: {glass_bg};
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid {glass_border};
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 {glass_shadow};
    }}
    
    /* Suprascrierea butoanelor native Streamlit pentru a avea aspect de sticlă */
    .stButton > button {{
        background: {glass_bg} !important;
        color: {text_principal} !important;
        border: 1px solid {glass_border} !important;
        backdrop-filter: blur(8px) !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out !important;
    }}
    
    .stButton > button:hover {{
        background: rgba(0, 255, 102, 0.2) !important;
        border-color: #00ff66 !important;
        box-shadow: 0 0 12px rgba(0, 255, 102, 0.4) !important;
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

# 2. Header Aplicație
with col_logo:
    st.markdown("<h1 style='margin:0; color: #00ff66;'>⚽ PariuriGO</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='color: {text_secundar}; font-size: 16px;'>Interfață Premium cu design ajustabil. Mod curent: {st.session_state.tema.upper()}</p>", unsafe_allow_html=True)
st.markdown("---")

col_meciuri, col_pachete = st.columns([1, 1])

# 3. Secțiune Meciuri
with col_meciuri:
    st.markdown(f"### 📅 Evenimente Active ({st.session_state.tema})")
    
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

# 4. Secțiune Pachete
with col_pachete:
    st.markdown("### 🏆 Niveluri de Abonament")
    
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
            <p>✅ Notificări rapide prin Telegram</p>
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
        import streamlit as st

# 1. Configurare Pagină principală
st.set_page_config(
    page_title="PariuriGO - Premium Glass UI",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inițializare stare pentru temă (implicit "dark")
if "tema" not in st.session_state:
    st.session_state.tema = "dark"

# Zona superioară pentru butonul de control al temei
col_logo, col_theme = st.columns()

with col_theme:
    # Buton stilizat tip Glassmorphism pentru comutarea temei (Luminos/Întunecat)
    if st.button("🌓 Schimbă Tema", key="toggle_theme", use_container_width=True):
        st.session_state.tema = "light" if st.session_state.tema == "dark" else "dark"
        st.rerun()

# Stabilirea imaginii de fundal și a culorilor în funcție de temă
if st.session_state.tema == "dark":
    # Imagine cu un teren de fotbal nocturn, întunecat pentru contrast bun cu textul alb
    bg_image_url = "https://unsplash.com"
    # Filtrul aplicat peste imagine (negru semi-transparent pentru a nu deranja ochii)
    overlay_color = "rgba(10, 20, 15, 0.85)"
    text_principal = "#ffffff"
    text_secundar = "#94a3b8"
    glass_bg = "rgba(22, 46, 36, 0.45)"
    glass_border = "rgba(0, 255, 102, 0.25)"
    glass_shadow = "rgba(0, 0, 0, 0.6)"
else:
    # Imagine cu un teren de fotbal pe timp de zi, luminoasă
    bg_image_url = "https://unsplash.com"
    # Filtrul aplicat peste imagine (alb/gri semi-transparent)
    overlay_color = "rgba(240, 245, 242, 0.85)"
    text_principal = "#0f172a"
    text_secundar = "#475569"
    glass_bg = "rgba(255, 255, 255, 0.5)"
    glass_border = "rgba(32, 77, 58, 0.2)"
    glass_shadow = "rgba(0, 0, 0, 0.1)"

# Injectare stiluri CSS avansate pentru fundalul cu teren de fotbal și Glassmorphism
st.markdown(f"""
<style>
    /* Fundalul general cu imaginea terenului de fotbal */
    .stApp {{
        background: linear-gradient({overlay_color}, {overlay_color}), url('{bg_image_url}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: {text_principal} !important;
        transition: all 0.5s ease;
    }}
    
    /* Carduri și panouri cu efect intens de sticlă mată (Glassmorphism) */
    .glass-card {{
        background: {glass_bg};
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {glass_border};
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 {glass_shadow};
    }}
    
    /* Suprascrierea butoanelor native Streamlit cu aspect de sticlă */
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
        background: rgba(0, 255, 102, 0.3) !important;
        border-color: #00ff66 !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.5) !important;
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

# 2. Header Aplicație
with col_logo:
    st.markdown("<h1 style='margin:0; color: #00ff66; text-shadow: 0 2px 10px rgba(0,0,0,0.5);'>⚽ PariuriGO</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='color: {text_secundar}; font-size: 16px; font-weight: 500;'>Interfață Premium Stadium Glass. Mod curent: {st.session_state.tema.upper()}</p>", unsafe_allow_html=True)
st.markdown("---")

col_meciuri, col_pachete = st.columns()

# 3. Secțiune Meciuri
with col_meciuri:
    st.markdown("### 📅 Evenimente Active")
    
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

# 4. Secțiune Simple Pachete
with col_pachete:
    st.markdown("### 🏆 Niveluri de Abonament")
    
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
            <p>✅ Notificări rapide prin Telegram</p>
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



