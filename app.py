import streamlit as st
import base64

# 1. Configurare Pagină (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
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
        background: linear-gradient(rgba(4, 14, 8, 0.92), rgba(2, 8, 4, 0.96)), 
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
        background: rgba(8, 22, 15, 0.85) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.22) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.65) !important;
        margin-bottom: 20px !important;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației cu Logo
if logo_base64:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <img src="data:image/png;base64,{logo_base64}" width="280">
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center; color: #00ff66;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)

st.write("---")

# Împărțirea ecranului direct în cele două secțiuni principale (Widget Stânga, Pachet Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# 3. SECȚIUNEA DIN STÂNGA: WIDGET GLOBAL REALE ÎN TIMP REAL
with col_meciuri:
    st.subheader("🌍 Meciuri Live din Toate Ligele Lumii")
    st.caption("Scoruri reale din ziua respectivă actualizate automat secundă de secundă.")
    
    # Inserare widget live internațional nativ securizat
    st.markdown("""
        <div style="width:100%; height:550px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px; margin-bottom: 25px;">
            <iframe src="https://scorebat.com" frameborder="0" width="100%" height="530px" allowfullscreen allow="autoplay; fullscreen"></iframe>
        </div>
    """, unsafe_allow_html=True)

# 4. SECȚIUNE ABONAMENTE CU PREȚURILE TALE CORECTE (Dreapta)
with col_abonamente:
    st.subheader("🏆 Abonamente VIP")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with tab_low:
        with st.container(border=True):
            st.markdown("<h4 style='color:#22c55e; text-align:center;'>PACHET LOW</h4>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;'>40 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h3>", unsafe_allow_html=True)
            st.write("✅ 3 Bilete analizate / săptămână")
            st.button("Abonare LOW", key="b_low", use_container_width=True)

    with tab_med:
        with st.container(border=True):
            st.markdown("<h4 style='color:#eab308; text-align:center;'>PACHET MEDIUM</h4>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;'>70 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h3>", unsafe_allow_html=True)
            st.write("✅ 1 Bilet Premium în fiecare zi")
            st.button("Abonare MEDIUM", key="b_med", use_container_width=True)

    with tab_high:
        with st.container(border=True):
            st.markdown("<h4 style='color:#ef4444; text-align:center;'>HIGH VIP ELITE</h4>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;'>120 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h3>", unsafe_allow_html=True)
            st.write("✅ Cota 2 VIP zilnică asigurată")
            st.button("Deblochează VIP ELITE", key="b_high", use_container_width=True)
