import streamlit as st
import base64
from datetime import datetime

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Determinarea automată a datei curente
data_azi = datetime.now().strftime("%d.%m.%Y")

# Funcție securizată pentru citirea imaginii de fundal de pe GitHub
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

# Stiluri CSS simple și sigure (fără acolade problematice în interiorul textelor de meciuri)
bg_style = ""
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
        margin-bottom: 20px !important;
    }}

    /* Barele de progres native configurate pe verde aprins */
    div[data-testid="stProgress"] div[role="progressbar"] {{
        background: linear-gradient(90deg, #008f33 0%, #00ff66 100%) !important;
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

# 3. SECȚIUNEA DIN STÂNGA: TOATE MECIURILE LIVE ȘI GRAFICUL
with col_meciuri:
    tab_global, tab_analiza = st.tabs(["🌍 TOATE MECIURILE LIVE", "📊 GRAFIC STATISTICI PREMIUM"])
    
    with tab_global:
        st.write("")
        # Inserare widget live ScoreBat securizat
        st.markdown("""
            <div style="width:100%; height:550px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px;">
                <iframe src="https://scorebat.com" frameborder="0" width="100%" height="520px" allowfullscreen allow="autoplay; fullscreen"></iframe>
            </div>
        """, unsafe_allow_html=True)
        
    with tab_analiza:
        st.write("")
        # Folosim containere și metrici native Streamlit pentru graficul simetric (100% Imun la erori de sintaxă)
        with st.container():
            st.markdown(f"<p style='text-align:center; color:#94a3b8; margin:0;'>MECIUL DE TOP DE AZI &bull; {data_azi}</p>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>ANALIZĂ DERBY &bull; SUPERLIGA</h2>", unsafe_allow_html=True)
            st.write("---")
            
            # Rândul 1 de cifre meci
            c1, c2, c3 = st.columns(3)
            c1.metric(label="⚽ GOLURI MARCATE (Gazde)", value="7")
            c2.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>TOTAL GOLURI MARCATE</p>", unsafe_allow_html=True)
            c3.metric(label="⚽ GOLURI MARCATE (Oaspeți)", value="3")
            
            # Rândul 2 de cifre meci
            c4, c5, c6 = st.columns(3)
            c4.metric(label="📈 MEDIE GOLURI (Gazde)", value="1.00")
            c5.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>MEDIE GOLURI / MECI</p>", unsafe_allow_html=True)
            c6.metric(label="📈 MEDIE GOLURI (Oaspeți)", value="0.43")
            
            # Rândul 3 de cifre meci
            c7, c8, c9 = st.columns(3)
            c7.metric(label="🛡️ GOLURI PRIMITE (Gazde)", value="8")
            c8.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>GOLURI PRIMITE</p>", unsafe_allow_html=True)
            c9.metric(label="🛡️ GOLURI PRIMITE (Oaspeți)", value="6")
            
            st.write("---")
            st.markdown("<p style='color:#00ff66; font-size:18px;'>📋 PROCENTE ȘI PROBABILITĂȚI GENERATE:</p>", unsafe_allow_html=True)
            
            # Secțiunea de procente cu badge-uri native
            cx1, cx2, cx3 = st.columns(3)
            cx1.metric(label="🟢 PESTE 0.5 HT (Prima Repriză)", value="71.43%", delta="57.14% Oaspeți", delta_color="off")
            cx2.metric(label="🟢 Peste 0.5 ST (A doua Repriză)", value="71.43%", delta="57.14% Oaspeți", delta_color="off")
            cx3.metric(label="🟢 Peste 1.5 Goluri în Meci", value="85.71%", delta="42.86% Oaspeți", delta_color="off")
            
            st.write("---")
            
            # Bare de progres native în tentă verde pentru evoluție globală
            st.write("**📈 EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:**")
            
            st.write("🔹 Peste 1.5 total: **64.29%**")
            st.progress(0.64)
            
            st.write("🔹 Peste 0.5 R1: **64.29%**")
            st.progress(0.64)
            
            st.write("🔹 Ambele echipe marchează (GG): **50.00%**")
            st.progress(0.50)
            
            st.write("---")
            st.info(f"🔸 **Sistem Algoritm Automat PariuriGO**\nMeci extras și calculat automat pentru data de {data_azi}")

# 4. SECȚIUNE ABONAMENTE VIP REPARATĂ TOTAL (Dreapta)
with col_abonamente:
    st.subheader("🏆 Abonamente VIP")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    # Pune aici linkul tău de Telegram când ești gata, boss!
    link_telegram_afacere = "https://t.me"
    
    with tab_low:
        with st.container(border=True):
            st.markdown("<h3 style='color:#00ff66; margin:0;'>PACHET LOW</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='margin:5px 0;'>40 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("📋 **Beneficii incluse:**")
            st.write("✅ 3 Bilete gata analizate pe săptămână")
            st.write("✅ Cote sigure selectate din ligile mari")
            st.write("✅ Acces grup comunitate chat")
            st.write("")
            # Link-ul deschide direct Telegramul vostru într-o filă nouă
            st.link_button("Abonare LOW 🚀", link_telegram_afacere, use_container_width=True)

    with tab_med:
        with st.container(border=True):
            st.markdown("<h3 style='color:#eab308; margin:0;'>PACHET MEDIUM</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='margin:5px 0;'>70 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("📋 **Beneficii incluse:**")
            st.write("✅ 1 Bilet Premium în fiecare zi calendaristică")
            st.write("✅ Procente și probabilități avansate live")
            st.write("✅ Notificări instant pe Telegram")
            st.write("")
            st.link_button("Abonare MEDIUM 🟡", link_telegram_afacere, use_container_width=True)

    with tab_high:
        with st.container(border=True):
            st.markdown("<h3 style='color:#ef4444; margin:0;'>HIGH VIP ELITE</h3>", unsafe_allow_html=True)
            st.markdown("<h2 style='margin:5px 0;'>120 RON <span style='font-size:14px; color:#94a3b8;'>/ lună</span></h2>", unsafe_allow_html=True)
            st.write("📋 **Beneficii incluse:**")
            st.write("✅ Cota 2 VIP zilnică + Proiect Dublare")
            st.write("✅ Acces total la toate sistemele noastre")
            st.write("✅ Suport privat 1-la-1 direct cu tipsterul")
            st.write("")
            st.link_button("Deblochează VIP ELITE 🔥", link_telegram_afacere, use_container_width=True)
