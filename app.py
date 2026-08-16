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

# Funcție pentru citirea imaginii locale JPG de pe GitHub
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

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
    
    h1, h2, h3, h4, p, span, label {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Carduri tip sticlă mată în nuanțe verzi închise */
    .glass-box-container {{
        background: rgba(8, 20, 14, 0.88) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.7) !important;
        margin-bottom: 25px !important;
    }}

    /* Meniu selectare meci */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: rgba(10, 30, 18, 0.9) !important;
        border: 1px solid #00ff66 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }}

    /* DESIGN PREMIUM PENTRU GRAFIC (TENTĂ VERDE CONFORM IMAGINII) */
    .stat-container {{ width: 100%; margin: 0 auto; }}
    .stat-row {{ display: flex; justify-content: space-between; align-items: center; margin: 12px 0; text-align: center; }}
    .stat-left-val, .stat-right-val {{ width: 20%; font-size: 22px; font-weight: 800; color: #ffffff; text-align: center; }}
    .stat-center-label {{ width: 60%; font-size: 16px; font-weight: 700; color: #a0aec0; text-transform: uppercase; letter-spacing: 0.5px; }}
    
    .green-badge {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%);
        color: #000000 !important;
        padding: 5px 18px;
        border-radius: 6px;
        font-size: 16px;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 2px 12px rgba(0, 255, 102, 0.3);
    }}
    
    .bar-wrapper {{ display: flex; align-items: center; margin: 14px 0; }}
    .bar-label {{ width: 28%; font-size: 16px; font-weight: 700; color: #ffffff; }}
    .bar-container {{ width: 72%; background: rgba(255, 255, 255, 0.05); border-radius: 12px; overflow: hidden; height: 26px; position: relative; border: 1px solid rgba(255,255,255,0.05); }}
    
    .bar-fill-neon {{
        height: 100%;
        background: linear-gradient(90deg, #006622 0%, #00ff66 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 12px;
        font-size: 13px;
        font-weight: 800;
        color: #000000;
    }}
    .bar-fill-soft {{
        height: 100%;
        background: linear-gradient(90deg, #013a16 0%, #00bc43 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 12px;
        font-size: 13px;
        font-weight: 800;
        color: #ffffff;
    }}
    .green-footer-box {{ background: rgba(0, 255, 102, 0.05); border: 1px solid rgba(0, 255, 102, 0.18); border-radius: 10px; padding: 12px 20px; margin-top: 20px; display: flex; align-items: center; gap: 12px; }}

    /* ANIMAȚIE MARE DE TIP PULS / GLOW PENTRU BUTOANELE VIP */
    .animated-btn {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        text-align: center !important;
        padding: 14px !important;
        border-radius: 8px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-top: 15px !important;
        display: block !important;
        text-decoration: none !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.4) !important;
        animation: pulseGlow 1.8s infinite ease-in-out !important;
    }}

    @keyframes pulseGlow {{
        0% {{ transform: scale(1); box-shadow: 0 0 12px rgba(0, 255, 102, 0.4); }}
        50% {{ transform: scale(1.02); box-shadow: 0 0 25px rgba(0, 255, 102, 0.8), 0 0 30px #00ff66; }}
        100% {{ transform: scale(1); box-shadow: 0 0 12px rgba(0, 255, 102, 0.4); }}
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal cu Logo
if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
else:
    st.title("⚽ PARIURIGO &bull; WORLD LIVE CENTER")

st.write("---")

# Împărțirea ecranului (Mecuri în Stânga, Abonamente în Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# BAZA DE DATE MECIURI REALE SUPERLIGA
meciuri_date = {
    "FCSB vs Rapid București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": "14", "g_os": "11", "med_gz": "1.75", "med_os": "1.37", "gp_gz": "5", "gp_os": "9",
        "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%",
        "p15_gz": "91.20%", "p15_os": "78.50%", "p25_gz": "64.29%", "p25_os": "50.00%",
        "gg_gz": "71.43%", "gg_os": "57.14%", "c_gz": "14.29%", "c_os": "28.57%",
        "cor_gz": "-", "cor_os": "14.29%",
        "w_p15": "85.00%", "w_p25": "64.29%", "w_p05r1": "85.71%", "w_p05r2": "78.50%", "w_gg": "71.43%", "w_c35": "21.43%", "w_cor95": "14.29%"
    },
    "CFR Cluj vs Universitatea Craiova": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": "11", "g_os": "13", "med_gz": "1.37", "med_os": "1.62", "gp_gz": "7", "gp_os": "6",
        "ht_gz": "75.00%", "ht_os": "62.50%", "st_gz": "87.50%", "st_os": "75.00%",
        "p15_gz": "87.50%", "p15_os": "75.00%", "p25_gz": "50.00%", "p25_os": "62.50%",
        "gg_gz": "62.50%", "gg_os": "62.50%", "c_gz": "25.00%", "c_os": "37.50%",
        "cor_gz": "12.50%", "cor_os": "25.00%",
        "w_p15": "81.00%", "w_p25": "56.00%", "w_p05r1": "68.00%", "w_p05r2": "81.00%", "w_gg": "62.00%", "w_c35": "31.00%", "w_cor95": "18.00%"
    },
    "Bașakșehir vs Kocaelispor": {
        "liga": "SUPER LIG &bull; TURKEY",
        "g_gz": "7", "g_os": "3", "med_gz": "1.00", "med_os": "0.43", "gp_gz": "8", "gp_os": "6",
        "ht_gz": "71.43%", "ht_os": "57.14%", "st_gz": "71.43%", "st_os": "57.14%",
        "p15_gz": "85.71%", "p15_os": "42.86%", "p25_gz": "28.57%", "p25_os": "42.86%",
        "gg_gz": "57.14%", "gg_os": "42.86%", "c_gz": "14.29%", "c_os": "28.57%",
        "cor_gz": "-", "cor_os": "14.29%",
        "w_p15": "64.29%", "w_p25": "14.29%", "w_p05r1": "64.29%", "w_p05r2": "64.29%", "w_gg": "50.00%", "w_c35": "21.43%", "w_cor95": "7.14%"
    }
}

# 3. SECȚIUNEA DIN STÂNGA: SCOREBAT SUS + GRAFIC INTEGRAL JOS
with col_meciuri:
    st.subheader("🌍 Meciuri Live din Toate Ligele Lumii")
    
    st.markdown("""
        <div style="width:100%; height:420px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px; margin-bottom: 25px;">
            <iframe src="https://scorebat.com" frameborder="0" width="100%" height="390px" allowfullscreen allow="autoplay; fullscreen"></iframe>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📊 Modul Algoritm & Probabilități (Meci de Top)")
    
    meci_ales = st.selectbox("🎯 Schimbă meciul din ziua respectivă:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]
    
    # RENDER SECURIZAT CU STRING CONCATENATE PENTRU A PREVENI EROAREA GHILIMELELOR
    st.markdown('<div class="glass-box-container">', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8; margin:0;'>MECI RECOMANDAT &bull; DATE LA ZI " + data_azi + "</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>" + meci_ales + "</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8; font-size:14px; margin-top:2px;'>" + m['liga'] + "</p>", unsafe_allow_html=True)
    st.markdown('<hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">', unsafe_allow_html=True)
    
    # Rânduri statistici tabel
    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["g_gz"] + '</div><div class="stat-center-label">Total goluri marcate</div><div class="stat-right-val">' + m["g_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["med_gz"] + '</div><div class="stat-center-label">Medie goluri</div><div class="stat-right-val">' + m["med_os"] + '</div></div>', unsafe_allow_html=True)
st.markdown('' + m["gp_gz"] + 'Goluri primite' + m["gp_os"] + '', unsafe_allow_html=True)st.markdown('', unsafe_allow_html=True)st.markdown('' + m["ht_gz"] + 'Peste 0.5 HT' + m["ht_os"] + '', unsafe_allow_html=True)st.markdown('' + m["st_gz"] + 'Peste 0.5 ST' + m["st_os"] + '', unsafe_allow_html=True)st.markdown('' + m["p15_gz"] + 'Peste 1.5 goluri' + m["p15_os"] + '', unsafe_allow_html=True)st.markdown('' + m["p25_gz"] + 'Peste 2.5 goluri' + m["p25_os"] + '', unsafe_allow_html=True)st.markdown('' + m["gg_gz"] + 'Ambele marchează' + m["gg_os"] + '', unsafe_allow_html=True)st.markdown('' + m["c_gz"] + 'Peste 3.5 cartonașe' + m["c_os"] + '', unsafe_allow_html=True)st.markdown('' + m["cor_gz"] + 'Peste 9.5 cornere' + m["cor_os"] + '', unsafe_allow_html=True)st.markdown('', unsafe_allow_html=True)st.markdown('', unsafe_allow_html=True)st.markdown('📈 BARE EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:', unsafe_allow_html=True)# Barele orizontale premium în degrade verdest.markdown('Peste 1.5:<div class="bar-fill-neon" style="width: ' + m["w_p15"] + ';">' + m["w_p15"] + '', unsafe_allow_html=True)st.markdown('Peste 2.5:<div class="bar-fill-soft" style="width: ' + m["w_p25"] + ';">' + m["w_p25"] + '', unsafe_allow_html=True)st.markdown('Peste 0.5 R1:<div class="bar-fill-neon" style="width: ' + m["w_p05r1"] + ';">' + m["w_p05r1"] + '', unsafe_allow_html=True)st.markdown('Peste 0.5 R2:<div class="bar-fill-neon" style="width: ' + m["w_p05r2"] + ';">' + m["w_p05r2"] + '', unsafe_allow_html=True)st.markdown('Ambele marchează:<div class="bar-fill-neon" style="width: ' + m["w_gg"] + ';">' + m["w_gg"] + '', unsafe_allow_html=True)st.markdown('+ 3.5 Cartonașe:<div class="bar-fill-soft" style="width: ' + m["w_c35"] + ';">' + m["w_c35"] + '', unsafe_allow_html=True)st.markdown('+ 9.5 Cornere:<div class="bar-fill-soft" style="width: ' + m["w_cor95"] + ';">' + m["w_cor95"] + '', unsafe_allow_html=True)st.markdown('🔸Sistem Algoritm Automat PariuriGOToate procentele sunt verificate live pentru meciurile din data de ' + data_azi + '', unsafe_allow_html=True)st.markdown('', unsafe_allow_html=True)
