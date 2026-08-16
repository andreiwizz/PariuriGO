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

