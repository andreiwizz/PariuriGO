import streamlit as st
import base64

# 1. Configurare Pagină (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție simplă pentru citirea imaginii locale JPG de pe GitHub
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# Citim terenul de fotbal și logo-ul din proiectul tău GitHub
teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-repeat: no-repeat !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #040e08 !important;"

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
        background: rgba(8, 22, 15, 0.88) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.22) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.65) !important;
    }}

    /* Stiluri pentru butoanele mari din pachete */
    .stButton > button {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        width: 100%;
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
    st.title("⚽ PARIURIGO &bull; WORLD LIVE CENTER")

st.write("---")

# Împărțirea ecranului (Fluxul în Stânga, Abonamente în Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# 3. SECȚIUNEA DIN STÂNGA: MECIURILE LIVE (WIDGET SCOREBAT)
with col_meciuri:
    st.subheader("🌍 Meciuri Live din Toate Ligele Lumii")
    st.caption("Scoruri reale actualizate automat secundă de secundă.")
    
    # Inserare widget live ScoreBat în siguranță
    st.markdown("""
        <div style="width:100%; height:550px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px;">
            <iframe src="https://scorebat.com" frameborder="0" width="100%" height="520px" allowfullscreen allow="autoplay; fullscreen"></iframe>
        </div>
    """, unsafe_allow_html=True)

# 4. SECȚIUNE ABONAMENTE VIP REPARATĂ PENTRU TOTDEAUNA (Dreapta)
with col_abonamente:
    st.subheader("🏆 Abonamente VIP")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with tab_low:
        st.write("")
        st.write("### PACHET LOW")
        st.write("## 40 RON / lună")
        st.write("---")
        st.write("✅ 3 Bilete gata analizate pe săptămână")
        st.write("✅ Cote sigure selectate din ligile mari")
        st.write("")
        st.button("Abonare LOW", key="b_low")

    with tab_med:
        st.write("")
        st.write("### PACHET MEDIUM")
        st.write("## 70 RON / lună")
        st.write("---")
        st.write("✅ 1 Bilet Premium în fiecare zi calendaristică")
        st.write("✅ Analize și procente detaliate")
        st.write("")
        st.button("Abonare MEDIUM", key="b_med")

    with tab_high:
        st.write("")
        st.write("### HIGH VIP ELITE")
        st.write("## 120 RON / lună")
        st.write("---")
        st.write("✅ Cota 2 VIP zilnică + Proiect Dublare")
        st.write("✅ Suport privat 1-la-1 direct cu tipsterul")
        st.write("")
        st.button("Deblochează VIP ELITE", key="b_high")
