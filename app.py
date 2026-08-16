import streamlit as st
import base64

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO Live Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție pentru citirea imaginii locale JPG de pe GitHub și transformarea ei în fundal
def decodifica_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# REPARAT: Citim fișierul tău exact cu extensia .jpg
teren_base64 = decodifica_imagine_locala("teren.jpg")
logo_base64 = decodifica_imagine_locala("logo.png")

# Reglați fundalul: dăm prioritate imaginii teren.jpg
if teren_base64:
    bg_style = f"""
        background: linear-gradient(rgba(6, 22, 13, 0.85), rgba(4, 14, 8, 0.88)), 
                    url('data:image/jpeg;base64,{teren_base64}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    """
else:
    bg_style = "background: radial-gradient(circle at center, #0a1f14 0%, #030c08 100%) !important;"

st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    
    .stApp {{
        {bg_style}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    
    h1, h2, h3, h4, p, span, label, .stTabs button {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Carduri tip sticlă mată în nuanțe verzi, perfect transparente peste gazon */
    div[data-testid="stVerticalBlockBorder"] {{
        background: rgba(10, 26, 18, 0.75) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.18) !important;
        border-radius: 16px !important;
        padding: 22px !important;
        box-shadow: 0 10px 40px 0 rgba(0,0,0,0.6) !important;
    }}

    /* Barele de progres native configurate pe verde aprins */
    div[data-testid="stProgress"] div[role="progressbar"] {{
        background: linear-gradient(90deg, #00ea53 0%, #00ff66 100%) !important;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației cu noul tău Logo
if logo_base64:
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <img src="data:image/png;base64,{logo_base64}" width="280">
        </div>
        """, 
        unsafe_allow_html=True
    )
else:
    st.markdown("<h1 style='text-align: center; color: #00ff66;'>⚽ PARIURIGO &bull; LIVE CENTER</h1>", unsafe_allow_html=True)

st.write("---")

# Împărțirea ecranului în două secțiuni: Meciuri (Stânga) și Abonamente (Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# 3. SECȚIUNEA DIN STÂNGA: MECIURI REALE DIN SUPERLIGĂ
with col_meciuri:
    st.subheader("🏟️ Meciurile Zilei (SuperLiga)")
    
    # OȚELUL GALAȚI vs UNIVERSITATEA CRAIOVA
    with st.container(border=True):
        col_header1, col_header2 = st.columns(2)
        with col_header1:
            st.error("🔴 LIVE &bull; MIN 65")
        with col_header2:
            st.markdown("<p style='text-align:right; color:#94a3b8; margin:0;'>ROMÂNIA SUPERLIGA</p>", unsafe_allow_html=True)
            
        st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 10px 0;'>OȚELUL GALAȚI &nbsp;&nbsp; 1 - 1 &nbsp;&nbsp; UNIV. CRAIOVA</h2>", unsafe_allow_html=True)
        st.write("---")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric(label="📊 POSESIE MINGE", value="46% - 54%")
        with c2:
            st.metric(label="🎯 ȘUTURI PE POARTĂ", value="4 - 5")
        with c3:
            st.metric(label="🛑 FAULTURI COMISE", value="15 - 11")
        with c4:
            st.metric(label="🟨 CARTONAȘE LIVE", value="3 - 2")
            
        st.write("---")
        st.write("**🧠 SUGESTIE ALGORITM INTELIGENȚĂ ARTIFICIALĂ:**")
        st.success("🔥 **Pont: Sub 2.5 goluri în meci** &nbsp;|&nbsp; **Cotă live: 1.65**")
        
    st.write("") # Spațiere
    
    # CORVINUL HUNEDOARA vs CFR CLUJ
    with st.container(border=True):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.info("🟢 PRE-MECI &bull; 21:30")
        with col_p2:
            st.markdown("<p style='text-align:right; color:#94a3b8; margin:0;'>ROMÂNIA SUPERLIGA</p>", unsafe_allow_html=True)
            
        st.markdown("<h3 style='text-align:center; color:#ffffff; margin: 10px 0;'>CORVINUL HUNEDOARA &nbsp;&nbsp; vs &nbsp;&nbsp; CFR CLUJ</h3>", unsafe_allow_html=True)
        st.write("---")
        
        st.write("**Cote Finale Disponibile (1X2):**")
        cx1, cx2, cx3 = st.columns(3)
        cx1.button("1 (Corvinul) &bull; 3.80", key="c_corv", use_container_width=True)
        cx2.button("X (Egal) &bull; 3.40", key="c_egal", use_container_width=True)
        cx3.button("2 (CFR Cluj) &bull; 1.95", key="c_cfr", use_container_width=True)
        
        st.write("**🧠 RECOMANDARE TIPSTER PREMIUM:**")
        st.warning("⭐️ **Pont: Victorie CFR Cluj (2) sau Egal** &nbsp;|&nbsp; **Cotă: 1.40**")

# 4. SECȚIUNEA DIN DREAPTA: PACHETE ABONAMENT VIP
with col_abonamente:
    st.subheader("🏆 Acces VIP Premium")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with tab_low:
        with st.container(border=True):
            st.markdown("<h3 style='color:#22c55e; text-align:center; margin:0;'>PACHET LOW</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center; margin:10px 0;'>19 RON <span style='font-size:15px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("---")
            st.write("✅ 3 Bilete gata analizate pe săptămână")
            st.write("✅ Cote sigure din Liga 1 și ligile mari")
            st.button("Abonare Standard LOW", key="b_low", use_container_width=True)

    with tab_med:
        with st.container(border=True):
            st.markdown("<h3 style='color:#eab308; text-align:center; margin:0;'>PACHET MEDIUM</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center; margin:10px 0;'>49 RON <span style='font-size:15px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("---")
            st.write("✅ 1 Bilet Premium oferit în fiecare zi")
            st.write("✅ Notificări instatanee pe Telegram Bot")
            st.button("Abonare Gold MEDIUM", key="b_med", use_container_width=True)

    with tab_high:
        with st.container(border=True):
            st.markdown("<h3 style='color:#ef4444; text-align:center; margin:0;'>HIGH VIP ELITE</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center; margin:10px 0;'>99 RON <span style='font-size:15px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("---")
            st.write("✅ Acces total la Proiect Dublare & Sistem")
            st.write("✅ Cota 2 VIP zilnică + Suport privat 1-la-1")
            st.button("Deblochează VIP ELITE", key="b_high", use_container_width=True)
            import streamlit as st
import base64

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO Live Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție pentru citirea imaginii locale JPG de pe GitHub și transformarea ei în fundal
def decodifica_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# Citim terenul de fotbal și logo-ul din proiectul tău GitHub
teren_base64 = decodifica_imagine_locala("teren.jpg")
logo_base64 = decodifica_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"""
        background: linear-gradient(rgba(4, 14, 8, 0.88), rgba(2, 8, 4, 0.93)), 
                    url('data:image/jpeg;base64,{teren_base64}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    """
else:
    bg_style = "background: radial-gradient(circle at center, #0a1f14 0%, #030c08 100%) !important;"

st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    
    .stApp {{
        {bg_style}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    
    h1, h2, h3, h4, p, span, label, .stTabs button {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Carduri tip sticlă mată în nuanțe verzi */
    div[data-testid="stVerticalBlockBorder"] {{
        background: rgba(10, 26, 18, 0.8) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.18) !important;
        border-radius: 16px !important;
        padding: 22px !important;
        box-shadow: 0 10px 40px 0 rgba(0,0,0,0.6) !important;
    }}

    /* Barele de progres native configurate pe verde aprins */
    div[data-testid="stProgress"] div[role="progressbar"] {{
        background: linear-gradient(90deg, #00ea53 0%, #00ff66 100%) !important;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației cu Logo
if logo_base64:
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <img src="data:image/png;base64,{logo_base64}" width="280">
        </div>
        """, 
        unsafe_allow_html=True
    )
else:
    st.markdown("<h1 style='text-align: center; color: #00ff66;'>⚽ PARIURIGO &bull; LIVE CENTER</h1>", unsafe_allow_html=True)

st.write("---")

# 3. ZONĂ NOUĂ ȘI SPECIALĂ: ACȚIUNE FLASH SUB 1 DOLAR
st.markdown("<h3 style='color: #ffcc00; text-align: center;'>🔥 PROMOȚIE FLASH &bull; ÎNCEARCĂ UN SINGUR BILET</h3>", unsafe_allow_html=True)
with st.container():
    c_st, c_dr = st.columns([1.2, 0.8], gap="medium")
    
    with c_st:
        st.markdown("#### 🎫 Biletul Premium de Astăzi (Single Match)")
        st.write("Nu vrei abonament? Cumpără doar biletul calculat de algoritmul nostru pentru meciul de top din această seară.")
        st.info("📊 **Probabilitate matematică de câștig: 91.4%** | **Cotă estimată: 1.85+**")
        
    with c_dr:
        st.markdown("<h3 style='color: #00ff66; margin:0;'>PREȚ: 4.50 RON <span style='font-size:14px; color:#94a3b8;'>(~ $0.99)</span></h3>", unsafe_allow_html=True)
        
        # Câmp de email pentru livrarea biletului cumpărat
        email_client = st.text_input("Introdu adresa de email pentru primirea biletului:", placeholder="nume@email.com", key="flash_email")
        
        if st.button("🚀 CUMPĂRĂ BILETUL ACUM", key="buy_flash", use_container_width=True):
            if email_client:
                st.success(f"Perfect! Adresa {email_client} a fost înregistrată. Te redirecționăm către link-ul de plată securizat...")
                # Aici poți pune pe viitor un link real de plată, momentan e o simulare
            else:
                st.error("Te rog să introduci o adresă de email validă înainte de a cumpăra!")

st.write("---")

# Împărțirea ecranului în două secțiuni standard pentru restul site-ului
col_meciuri, col_abonamente = st.columns([1.2, 0.8], gap="large")

# 4. SECȚIUNEA MECIURI (Stânga)
with col_meciuri:
    st.subheader("🏟️ Meciurile Zilei în Desfășurare")
    
    # OȚELUL GALAȚI vs UNIVERSITATEA CRAIOVA
    with st.container(border=True):
        col_header1, col_header2 = st.columns(2)
        with col_header1:
            st.error("🔴 LIVE &bull; MIN 65")
        with col_header2:
            st.markdown("<p style='text-align:right; color:#94a3b8; margin:0;'>ROMÂNIA SUPERLIGA</p>", unsafe_allow_html=True)
            
        st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 10px 0;'>OȚELUL GALAȚI &nbsp;&nbsp; 1 - 1 &nbsp;&nbsp; UNIV. CRAIOVA</h2>", unsafe_allow_html=True)
        st.write("---")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric(label="📊 POSESIE", value="46% - 54%")
        c2.metric(label="🎯 ȘUTURI POARTĂ", value="4 - 5")
        c3.metric(label="🛑 FAULTURI", value="15 - 11")
        c4.metric(label="🟨 CARTONAȘE", value="3 - 2")

# 5. SECȚIUNE ABONAMENTE (Dreapta)
with col_abonamente:
    st.subheader("🏆 Abonamente Lunare VIP")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with tab_low:
        with st.container(border=True):
            st.markdown("<h4 style='color:#22c55e; text-align:center;'>PACHET LOW</h4>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;'>19 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h3>", unsafe_allow_html=True)
            st.write("✅ 3 Bilete analizate / săptămână")
            st.button("Abonare LOW", key="b_low", use_container_width=True)

    with tab_med:
        with st.container(border=True):
            st.markdown("<h4 style='color:#eab308; text-align:center;'>PACHET MEDIUM</h4>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;'>49 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h3>", unsafe_allow_html=True)
            st.write("✅ 1 Bilet Premium în fiecare zi")
            st.button("Abonare MEDIUM", key="b_med", use_container_width=True)

    with tab_high:
        with st.container(border=True):
            st.markdown("<h4 style='color:#ef4444; text-align:center;'>HIGH VIP ELITE</h4>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;'>99 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h3>", unsafe_allow_html=True)
            st.write("✅ Cota 2 VIP zilnică + Suport 1-la-1")
            st.button("Deblochează VIP ELITE", key="b_high", use_container_width=True)

