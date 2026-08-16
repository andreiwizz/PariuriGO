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

# Determinarea datei curente
data_azi = datetime.now().strftime("%d.%m.%Y")

# Funcție simplă și sigură de Python pentru citirea imaginii locale
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

# Aplicare fundal curat din Python
if teren_base64:
    st.markdown(f"""
    <style>
        .stApp {{
            background: linear-gradient(rgba(4, 14, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important;
            background-size: cover !important;
            background-attachment: fixed !important;
        }}
    </style>
    """, unsafe_allow_html=True)

# 2. Afișare Logo sau Titlu
if logo_base64:
    st.image(f"data:image/png;base64,{logo_base64}", width=280)
else:
    st.title("⚽ PARIURIGO • WORLD LIVE CENTER")

st.write("---")

# Împărțirea ecranului în două coloane native (Stânga - Meciuri, Dreapta - Abonamente)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# BAZA DE DATE CURATĂ DE PYTHON (Fără text HTML încurcat)
meciuri_date = {
    "FCSB vs Rapid București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": 14, "g_os": 11, "med_gz": 1.75, "med_os": 1.37, "gp_gz": 5, "gp_os": 9,
        "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%",
        "p15_gz": "91.20%", "p15_os": "78.50%", "p25_gz": "64.29%", "p25_os": "50.00%",
        "gg_gz": "71.43%", "gg_os": "57.14%",
        "prog_15": 0.85, "prog_05": 0.78, "prog_gg": 0.64
    },
    "CFR Cluj vs Universitatea Craiova": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": 11, "g_os": 13, "med_gz": 1.37, "med_os": 1.62, "gp_gz": 7, "gp_os": 6,
        "ht_gz": "75.00%", "ht_os": "62.50%", "st_gz": "87.50%", "st_os": "75.00%",
        "p15_gz": "87.50%", "p15_os": "75.00%", "p25_gz": "50.00%", "p25_os": "62.50%",
        "gg_gz": "62.50%", "gg_os": "62.50%",
        "prog_15": 0.81, "prog_05": 0.68, "prog_gg": 0.62
    },
    "Oțelul Galați vs Dinamo București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": 8, "g_os": 10, "med_gz": 1.00, "med_os": 1.25, "gp_gz": 4, "gp_os": 8,
        "ht_gz": "50.00%", "ht_os": "50.00%", "st_gz": "62.50%", "st_os": "75.00%",
        "p15_gz": "62.50%", "p15_os": "75.00%", "p25_gz": "25.00%", "p25_os": "50.00%",
        "gg_gz": "37.50%", "gg_os": "50.00%",
        "prog_15": 0.68, "prog_05": 0.50, "prog_gg": 0.43
    }
}

# 3. SECȚIUNEA DIN STÂNGA: SCOREBAT + MENIU SELECTARE MECI NATIV
with col_meciuri:
    st.subheader("🌍 Meciuri Live din Toate Ligele Lumii")
    
    # Widget ScoreBat
    st.markdown("""
        <div style="width:100%; height:420px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px;">
            <iframe src="https://scorebat.com" frameborder="0" width="100%" height="390px" allowfullscreen allow="autoplay; fullscreen"></iframe>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📊 Modul Algoritm & Probabilități (Meci de Top)")
    
    # Meniu de selecție pur Python
    meci_ales = st.selectbox("🎯 Schimbă meciul din ziua respectivă:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]
    
    st.write(f"### {meci_ales}")
    st.caption(f"🏆 {m['liga']} • Date la zi: {data_azi}")
    st.write("---")
    
    # Afișare metrici simetrice native (Cifrele mari din poza ta)
    c1, c2 = st.columns(2)
    c1.metric(label="⚽ Goluri Marcate (Gazde)", value=m["g_gz"])
    c2.metric(label="⚽ Goluri Marcate (Oaspeți)", value=m["g_os"])
    
    c3, c4 = st.columns(2)
    c3.metric(label="📈 Medie Goluri / Meci (Gazde)", value=m["med_gz"])
    c4.metric(label="📈 Medie Goluri / Meci (Oaspeți)", value=m["med_os"])
    
    c5, c6 = st.columns(2)
    c5.metric(label="🛡️ Goluri Primite (Gazde)", value=m["gp_gz"])
    c6.metric(label="🛡️ Goluri Primite (Oaspeți)", value=m["gp_os"])
    
    st.write("---")
    st.write("**📋 Procente de probabilitate calculate:**")
    
    cx1, cx2, cx3 = st.columns(3)
    cx1.metric(label="🟢 Peste 0.5 HT (Prima Repriză)", value=m["ht_gz"], delta=f"{m['ht_os']} Oaspeți", delta_color="off")
    cx2.metric(label="🟢 Peste 0.5 ST (Repriza 2)", value=m["st_gz"], delta=f"{m['st_os']} Oaspeți", delta_color="off")
    cx3.metric(label="🟢 Peste 1.5 Goluri în Meci", value=m["p15_gz"], delta=f"{m['p15_os']} Oaspeți", delta_color="off")
    
    cx4, cx5 = st.columns(2)
    cx4.metric(label="🟢 Peste 2.5 Goluri", value=m["p25_gz"], delta=f"{m['p25_os']} Oaspeți", delta_color="off")
    cx5.metric(label="🟢 Ambele marchează (GG)", value=m["gg_gz"], delta=f"{m['gg_os']} Oaspeți", delta_color="off")
    
    st.write("---")
    st.write("**📈 Bare evoluție probabilități globale:**")
    
    st.write(f"🔹 Peste 1.5 total: **{int(m['prog_15'] * 100)}%**")
    st.progress(m["prog_15"])
    
    st.write(f"🔹 Peste 0.5 R1: **{int(m['prog_05'] * 100)}%**")
    st.progress(m["prog_05"])
    
    st.write(f"🔹 Ambele echipe marchează (GG): **{int(m['prog_gg'] * 100)}%**")
    st.progress(m["prog_gg"])

# 4. SECȚIUNE ABONAMENTE VIP NATIVE (Dreapta - Text perfect alb, butoane perfect vizibile)
with col_abonamente:
    st.subheader("🏆 Abonamente VIP")
    
    link_telegram_afacere = "https://t.me"
    
    # Folosim cele 3 structuri deschise liniar pentru a fi 100% sigure
    st.write("### 🟢 PACHET LOW")
    st.write("## 40 RON / lună")
    st.write("• 3 Bilete gata analizate pe săptămână")
    st.write("• Cote sigure selectate din ligile mari")
    st.write("• Acces grup comunitate chat")
    st.link_button("CUMPĂRĂ LOW 🚀", link_telegram_afacere, use_container_width=True)
    
    st.write("---")
    
    st.write("### 🟡 PACHET MEDIUM")
    st.write("## 70 RON / lună")
    st.write("• 1 Bilet Premium în fiecare zi calendaristică")
    st.write("• Procente și probabilități avansate live")
    st.write("• Notificări instant pe Telegram")
    st.link_button("CUMPĂRĂ MEDIUM 🟡", link_telegram_afacere, use_container_width=True)
    
    st.write("---")
    
    st.write("### 🔥 HIGH VIP ELITE")
    st.write("## 120 RON / lună")
    st.write("• Cota 2 VIP zilnică + Proiect Dublare")
    st.write("• Acces total la toate sistemele noastre")
    st.write("• Suport privat 1-la-1 direct cu tipsterul")
    st.link_button("DEBLOCHEAZĂ HIGH 🔥", link_telegram_afacere, use_container_width=True)
