import streamlit as st
import base64

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO Live Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru citirea imaginii de fundal de pe GitHub
def incarc_teren_fotbal(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

img_data = incarc_teren_fotbal("teren.png")

# Aplicare design curat și font sportiv prin CSS simplu
css_fond = ""
if img_data:
    css_fond = f"background: linear-gradient(rgba(10, 24, 15, 0.9), rgba(10, 24, 15, 0.9)), url('data:image/png;base64,{img_data}') !important; background-size: cover !important; background-attachment: fixed !important;"
else:
    css_fond = "background-color: #06110b !important;"

st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    
    .stApp {{
        {css_fond}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    h1, h2, h3, h4, p, span, label, .stTabs button {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    /* Carduri stilizate tip sticlă */
    div[data-testid="stVerticalBlockBorder"] {{
        background: rgba(13, 31, 23, 0.7) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0,0,0,0.5) !important;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației
st.title("⚽ PARIURIGO &bull; LIVE CENTER")
st.caption("Dashboard Sportiv Premium v2.0 &bull; Actualizat în timp real")
st.write("---")

# Împărțirea ecranului în două secțiuni: Meciuri (Stânga) și Abonamente (Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# 3. SECȚIUNEA DIN STÂNGA: MECIURI LIVE ȘI STATISTICI
with col_meciuri:
    st.subheader("🏟️ Meciuri în Desfășurare")
    
    # MECIUL 1 - BOX LIVE
    with st.container(border=True):
        col_header1, col_header2 = st.columns([1, 1])
        with col_header1:
            st.error("🔴 LIVE &bull; MIN 76")
        with col_header2:
            st.markdown("<p style='text-align:right; color:#94a3b8;'>LALIGA</p>", unsafe_allow_html=True)
            
        st.markdown("<h2 style='text-align:center; color:#ffcc00; margin: 10px 0;'>REAL MADRID &nbsp;&nbsp; 2 - 1 &nbsp;&nbsp; BARCELONA</h2>", unsafe_allow_html=True)
        st.write("---")
        
        # Afișare Statistici Live folosind metrici native
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric(label="📊 POSESIE MINGE", value="52%", delta="Real Madrid")
        with c2:
            st.metric(label="🎯 ȘUTURI PE POARTĂ", value="7 - 4")
        with c3:
            st.metric(label="🛑 FAULTURI COMISE", value="12 - 14")
        with c4:
            st.metric(label="🟨 CARTONAȘE", value="🟨2 &bull; 🟨3")
            
        st.write("---")
        st.write("**🧠 PUGAL RECOMANDAT DE INTELIGENȚA ARTIFICIALĂ:**")
        
        # Caseta cu pontul zilei
        st.success("🔥 **Ambele echipe marchează (GG)** &nbsp;|&nbsp; **Cotă: 1.72**")
        
    st.write("") # Spațiere
    
    # MECIUL 2 - BOX PRE-MECI
    with st.container(border=True):
        col_p1, col_p2 = st.columns([1, 1])
        with col_p1:
            st.info("🟢 PRE-MECI &bull; 22:00")
        with col_p2:
            st.markdown("<p style='text-align:right; color:#94a3b8;'>PREMIER LEAGUE</p>", unsafe_allow_html=True)
            
        st.markdown("<h3 style='text-align:center; color:#ffffff; margin: 10px 0;'>MANCHESTER CITY &nbsp;&nbsp; vs &nbsp;&nbsp; LIVERPOOL</h3>", unsafe_allow_html=True)
        st.write("---")
        
        # Butoane rapide de cote 1 X 2
        st.write("**Cote Finale 1X2 (Speranță de câștig):**")
        cx1, cx2, cx3 = st.columns(3)
        cx1.button("1 &bull; cota 2.15", key="c1", use_container_width=True)
        cx2.button("X &bull; cota 3.60", key="cx", use_container_width=True)
        cx3.button("2 &bull; cota 3.20", key="c2", use_container_width=True)

# 4. SECȚIUNEA DIN DREAPTA: PACHETE ABONAMENT VIP
with col_abonamente:
    st.subheader("🏆 Acces VIP Premium")
    
    opțiune_pachet = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with opțiune_pachet[0]:
        with st.container(border=True):
            st.markdown("<h3 style='color:#22c55e; text-align:center;'>PACHET LOW</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center;'>19 RON <span style='font-size:16px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("---")
            st.write("✅ 3 Bilete gata analizate pe săptămână")
            st.write("✅ Cote sigure cu probabilitate mare")
            st.button("Abonare Standard LOW", key="b_low", use_container_width=True)

    with opțiune_pachet[1]:
        with st.container(border=True):
            st.markdown("<h3 style='color:#eab308; text-align:center;'>PACHET MEDIUM</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center;'>49 RON <span style='font-size:16px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("---")
            st.write("✅ 1 Bilet Premium oferit în fiecare zi")
            st.write("✅ Notificări instatanee pe Telegram Bot")
            st.button("Abonare Gold MEDIUM", key="b_med", use_container_width=True)

    with opțiune_pachet[2]:
        with st.container(border=True):
            st.markdown("<h3 style='color:#ef4444; text-align:center;'>HIGH VIP ELITE</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center;'>99 RON <span style='font-size:16px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("---")
            st.write("✅ Acces total la Proiect Dublare & Toate sistemele")
            st.write("✅ Cota 2 VIP zilnică + Suport privat 1-la-1")
            st.button("Deblochează VIP ELITE", key="b_high", use_container_width=True)
