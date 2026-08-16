import streamlit as st
import base64
import time

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
        background: linear-gradient(rgba(4, 14, 8, 0.91), rgba(2, 8, 4, 0.94)), 
                    url('data:image/jpeg;base64,{teren_base64}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    """
else:
    bg_style = "background: radial-gradient(circle at center, #0a1f14 0%, #030c08 100%) !important;"

# Injectare stiluri CSS cu animația avansată pentru MINGEA ÎN FLĂCĂRI (Goal Overlay)
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
        background: rgba(8, 22, 15, 0.84) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.22) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.65) !important;
        margin-bottom: 15px !important;
    }}

    /* Barele de progres native configurate pe verde aprins */
    div[data-testid="stProgress"] div[role="progressbar"] {{
        background: linear-gradient(90deg, #00ea53 0%, #00ff66 100%) !important;
    }}

    /* ANIMAȚIE GOOOL: Ecran complet, minge în flăcări */
    .goal-overlay {{
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: rgba(0, 0, 0, 0.85);
        z-index: 99999;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        animation: screenShake 0.5s ease-in-out infinite alternate;
    }}

    .fireball {{
        width: 180px;
        height: 180px;
        background: url('https://flaticon.com') no-repeat center;
        background-size: contain;
        filter: drop-shadow(0 0 20px #ff4500) drop-shadow(0 0 40px #ffcc00);
        animation: spinAndBurn 0.8s linear infinite;
    }}

    .goal-text {{
        font-size: 80px !important;
        font-weight: 900 !important;
        color: #ffcc00;
        text-shadow: 0 0 20px #ff4500, 0 0 40px #ff3300;
        margin-top: 20px;
        letter-spacing: 4px;
        animation: pulseText 0.5s infinite alternate;
    }}

    @keyframes spinAndBurn {{
        0% {{ transform: rotate(0deg) scale(1); filter: drop-shadow(0 0 20px #ff3300); }}
        50% {{ transform: rotate(180deg) scale(1.15); filter: drop-shadow(0 0 45px #ffcc00); }}
        100% {{ transform: rotate(360deg) scale(1); filter: drop-shadow(0 0 20px #ff3300); }}
    }}

    @keyframes pulseText {{
        0% {{ transform: scale(1); }}
        100% {{ transform: scale(1.1); }}
    }}

    @keyframes screenShake {{
        0% {{ transform: translate(2px, 1px) rotate(0deg); }}
        10% {{ transform: translate(-1px, -2px) rotate(-1deg); }}
        20% {{ transform: translate(-3px, 0px) rotate(1deg); }}
        30% {{ transform: translate(0px, 2px) rotate(0deg); }}
        40% {{ transform: translate(1px, -1px) rotate(1deg); }}
        50% {{ transform: translate(-1px, 2px) rotate(-1deg); }}
        100% {{ transform: translate(1px, -2px) rotate(0deg); }}
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației cu Logo urcat local
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

# Înregistrare stări pentru scorurile live în cache-ul aplicației
if "otelul_scor" not in st.session_state: st.session_state.otelul_scor = 1
if "craiova_scor" not in st.session_state: st.session_state.craiova_scor = 1
if "corvinul_scor" not in st.session_state: st.session_state.corvinul_scor = 0
if "cluj_scor" not in st.session_state: st.session_state.cluj_scor = 0
if "show_goal" not in st.session_state: st.session_state.show_goal = False

# MECANISM DECLANȘARE ANIMAȚIE MINGE ÎN FLĂCĂRI
if st.session_state.show_goal:
    placeholder_gol = st.empty()
    with placeholder_gol:
        st.markdown("""
        <div class="goal-overlay">
            <div class="fireball"></div>
            <div class="goal-text">GOOOOOL!!!</div>
        </div>
        """, unsafe_allow_html=True)
    time.sleep(3.5) # Animația rulează spectaculos timp de 3.5 secunde
    st.session_state.show_goal = False
    placeholder_gol.empty()
    st.rerun()

# 3. PROMOȚIE FLASH SUB 1 DOLAR
st.markdown("<h3 style='color: #ffcc00; text-align: center;'>🔥 PROMOȚIE FLASH &bull; ÎNCEARCĂ UN SINGUR BILET</h3>", unsafe_allow_html=True)
with st.container():
    c_st, c_dr = st.columns([1.2, 0.8], gap="medium")
    with c_st:
        st.markdown("#### 🎫 Biletul Premium de Astăzi (Single Match)")
        st.write("Cumpără doar biletul calculat de algoritmul nostru pentru meciul de top din această seară, fără obligații lunare.")
        st.info("📊 **Probabilitate matematică de câștig: 91.4%** | **Cotă estimată: 1.85+**")
    with c_dr:
        st.markdown("<h3 style='color: #00ff66; margin:0;'>PREȚ: 4.50 RON <span style='font-size:14px; color:#94a3b8;'>(~ $0.99)</span></h3>", unsafe_allow_html=True)
        email_client = st.text_input("Introdu adresa de email pentru primirea biletului:", placeholder="nume@email.com", key="flash_email")
        if st.button("🚀 CUMPĂRĂ BILETUL ACUM", key="buy_flash", use_container_width=True):
            if email_client:
                st.success(f"Perfect! Adresa {email_client} a fost înregistrată. Redirecționare plată...")
            else:
                st.error("Te rog să introduci o adresă de email validă!")

st.write("---")

# Împărțirea ecranului: Meciuri Active (Stânga) și Abonamente VIP (Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# 4. SECȚIUNEA EXTINSĂ MECIURI ÎN TIMP REAL (Stânga)
with col_meciuri:
    st.subheader("🏟️ Panoul de Control Meciuri Live (Actualizat 2026)")
    
    # MECIUL 1 LIVE REAL: OȚELUL GALAȚI vs UNIVERSITATEA CRAIOVA
    with st.container(border=True):
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            st.error("🔴 ÎN DESFĂȘURARE &bull; LIVE Min 65")
        with col_h2:
            st.markdown("<p style='text-align:right; color:#94a3b8; margin:0;'>ETAPA 5 &bull; SUPERLIGA</p>", unsafe_allow_html=True)
            
        st.markdown(f"<h2 style='text-align:center; color:#ffcc00; margin: 10px 0;'>OȚELUL GALAȚI &nbsp;&nbsp; {st.session_state.otelul_scor} - {st.session_state.craiova_scor} &nbsp;&nbsp; UNIV. CRAIOVA</h2>", unsafe_allow_html=True)
        st.write("---")
        
        # Panou control admin live asuns/direct pentru adăugare goluri real-time
        cg1, cg2 = st.columns(2)
        if cg1.button("+ Gol Oțelul", key="g_ot"):
            st.session_state.otelul_scor += 1
            st.session_state.show_goal = True
            st.rerun()
        if cg2.button("+ Gol Craiova", key="g_cr"):
            st.session_state.craiova_scor += 1
            st.session_state.show_goal = True
            st.rerun()

        st.write("**📊 Statistici Meci în Timp Real:**")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric(label="⚽ Posesie minge", value="46% - 54%")
        c2.metric(label="🎯 Șuturi pe poartă", value="4 - 5")
        c3.metric(label="🛑 Faulturi comise", value="15 - 11")
        c4.metric(label="🟨 Cartonașe galbene", value="3 - 2")
        
        st.write("---")
        st.write("**🧠 SUGESTIE AI PARIURIGO:**")
        st.success("🔥 **Pont recomandat: Sub 2.5 goluri în meci** &nbsp;|&nbsp; **Cotă live: 1.65**")

    st.write("") # Spațiere între meciuri

    # MECIUL 2 LIVE REAL: FC CORVINUL HUNEDOARA vs CFR CLUJ
    with st.container(border=True):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.error("🔴 ÎN DESFĂȘURARE &bull; LIVE Min 12")
        with col_p2:
            st.markdown("<p style='text-align:right; color:#94a3b8; margin:0;'>ETAPA 5 &bull; SUPERLIGA</p>", unsafe_allow_html=True)
            
        st.markdown(f"<h2 style='text-align:center; color:#ffffff; margin: 10px 0;'>CORVINUL HUNEDOARA &nbsp;&nbsp; {st.session_state.corvinul_scor} - {st.session_state.cluj_scor} &nbsp;&nbsp; CFR CLUJ</h2>", unsafe_allow_html=True)
        st.write("---")
        
        cg3, cg4 = st.columns(2)
        if cg3.button("+ Gol Corvinul", key="g_co"):
            st.session_state.corvinul_scor += 1
            st.session_state.show_goal = True
            st.rerun()
        if cg4.button("+ Gol CFR Cluj", key="g_cl"):
            st.session_state.cluj_scor += 1
