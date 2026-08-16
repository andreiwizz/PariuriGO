import streamlit as st
import base64

# 1. Configurare Pagină (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție simplă pentru citirea imaginii de fundal
def incarc_imagine(cale):
    try:
        with open(cale, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

teren_base64 = incarc_imagine("teren.jpg")
logo_base64 = incarc_imagine("logo.png")

# Aplicare fundal și font sportiv
bg_style = ""
if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 12, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #06140d !important;"

st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    .stApp {{ {bg_style} color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; }}
    h1, h2, h3, h4, p, span, label, button {{ font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important; }}
    div[data-testid="stVerticalBlockBorder"] {{ background: rgba(8, 20, 14, 0.88) !important; border: 1px solid rgba(0, 255, 102, 0.2) !important; border-radius: 16px !important; padding: 20px !important; }}
    div[data-testid="stProgress"] div[role="progressbar"] {{ background: linear-gradient(90deg, #008f33 0%, #00ff66 100%) !important; }}
</style>
""", unsafe_allow_html=True)

# Afișare Logo sau Titlu
if logo_base64:
    st.image(f"data:image/png;base64,{logo_base64}", width=280)
else:
    st.title("⚽ PARIURIGO &bull; DASHBOARD")

st.write("---")

# Împărțire ecran în două coloane
col_grafic, col_abonamente = st.columns([1.3, 0.7], gap="large")

with col_grafic:
    st.subheader("📊 Modul Algoritm & Probabilități")
    
    with st.container(border=True):
        st.caption("SUPER LIG &bull; TURKEY")
        st.markdown("<h2 style='color:#00ff66;'>BAȘAKȘEHIR vs KOCAELISPOR</h2>", unsafe_allow_html=True)
        st.write("---")
        
        # Partea 1: Cifre simple meci
        c1, c2, c3 = st.columns(3)
        c1.metric(label="⚽ GOLURI MARCATE (Gazde - Oaspeți)", value="7 - 3")
        c2.metric(label="📈 MEDIE GOLURI", value="1.00 - 0.43")
        c3.metric(label="🛡️ GOLURI PRIMITE", value="8 - 6")
        
        st.write("---")
        
        # Partea 2: Procente tip tabel cu metrici native
        st.write("**📋 PROCENTE ȘANSE EVENIMENTE:**")
        cx1, cx2, cx3 = st.columns(3)
        cx1.metric(label="🟢 PESTE 0.5 HT", value="71.43%", delta="57.14% Oaspeți", delta_color="off")
        cx2.metric(label="🟢 PESTE 0.5 ST", value="71.43%", delta="57.14% Oaspeți", delta_color="off")
        cx3.metric(label="🟢 PESTE 1.5 GOLURI", value="85.71%", delta="42.86% Oaspeți", delta_color="off")
        
        st.write("---")
        
        # Partea 3: Barele de progres în nuanță verde
        st.write("**📈 EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:**")
        
        st.write("🔹 Peste 1.5 Goluri: **64.29%**")
        st.progress(0.64)
        
        st.write("🔹 Peste 2.5 Goluri: **14.29%**")
        st.progress(0.14)
        
        st.write("🔹 Peste 0.5 R1: **64.29%**")
        st.progress(0.64)
        
        st.write("🔹 Ambele marchează: **50.00%**")
        st.progress(0.50)
        
        st.write("---")
        st.info("🔸 **Stats arbitru &bull; probabilitate matematică**\nM. Turkmen &bull; 7/7 meciuri din ligă analizate cu succes")

with col_abonamente:
    st.subheader("🏆 Abonamente VIP")
    
    t_low, t_med, t_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with t_low:
        with st.container(border=True):
            st.markdown("<h4 style='color:#22c55e;'>PACHET LOW</h4>", unsafe_allow_html=True)
            st.subheader("40 RON / lună")
            st.write("✅ 3 Bilete analizate / săptămână")
            st.button("Abonare LOW", key="b_low", use_container_width=True)

    with t_med:
        with st.container(border=True):
            st.markdown("<h4 style='color:#eab308;'>PACHET MEDIUM</h4>", unsafe_allow_html=True)
            st.subheader("70 RON / lună")
            st.write("✅ 1 Bilet Premium în fiecare zi")
            st.button("Abonare MEDIUM", key="b_med", use_container_width=True)

    with t_high:
        with st.container(border=True):
            st.markdown("<h4 style='color:#ef4444;'>HIGH VIP ELITE</h4>", unsafe_allow_html=True)
            st.subheader("120 RON / lună")
            st.write("✅ Cota 2 VIP zilnică asigurată")
            st.button("Deblochează VIP ELITE", key="b_high", use_container_width=True)
