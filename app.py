import os
import requests
import pandas as pd
import streamlit as st
from datetime import date

# ============================================
# CONFIG
# ============================================
st.set_page_config(page_title="Analist Pariuri", page_icon="⚽", layout="wide")

API_KEY = "PUNETI_CHEIA_VOASTRA_AICI"  # luati gratuit de pe football-data.org
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}

# ============================================
# CSS - tema verde peste teren.jpg
# ============================================
st.markdown("""aimport streamlit as st
import base64
from datetime import datetime

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-attachment: fixed !important;"
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
    
    /* Carduri tip sticlă mată în nuanțe verzi închise */
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

    /* Selectbox custom să arate bombă pe verde */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: rgba(10, 30, 18, 0.9) !important;
        border: 1px solid #00ff66 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }}

    /* Barele de progres native configurate pe verde aprins */
    div[data-testid="stProgress"] div[role="progressbar"] {{
        background: linear-gradient(90deg, #008f33 0%, #00ff66 100%) !important;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației cu Logo
if logo_base64:
    st.image(f"data:image/png;base64,{logo_base64}", width=280)
else:
    st.title("⚽ PARIURIGO &bull; WORLD LIVE CENTER")

st.write("---")

# Împărțirea ecranului (Fluxul în Stânga, Abonamente în Dreapta)
col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

# BAZA DE DATE CURATĂ DE PYTHON (Fără text HTML încurcat)
meciuri_date = {
    "FCSB vs Rapid București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": 14, "g_os": 11, "med_gz": 1.75, "med_os": 1.37, "gp_gz": 5, "gp_os": 9,
        "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%",
        "p15_gz": "91.20%", "p15_os": "78.50%", "p25_gz": "64.29%", "p25_os": "50.00%",
        "gg_gz": "71.43%", "gg_os": "57.14%", "c_gz": "14.29%", "c_os": "28.57%", "cor_os": "14.29%",
        "prog_15": 0.85, "prog_25": 0.14, "prog_05": 0.85, "prog_05_st": 0.78, "prog_gg": 0.64, "prog_c35": 0.21, "prog_cor95": 0.14
    },
    "CFR Cluj vs Universitatea Craiova": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": 11, "g_os": 13, "med_gz": 1.37, "med_os": 1.62, "gp_gz": 7, "gp_os": 6,
        "ht_gz": "75.00%", "ht_os": "62.50%", "st_gz": "87.50%", "st_os": "75.00%",
        "p15_gz": "87.50%", "p15_os": "75.00%", "p25_gz": "50.00%", "p25_os": "62.50%",
        "gg_gz": "62.50%", "gg_os": "62.50%", "c_gz": "25.00%", "c_os": "37.50%", "cor_os": "25.00%",
        "prog_15": 0.81, "prog_25": 0.56, "prog_05": 0.68, "prog_05_st": 0.81, "prog_gg": 0.62, "prog_c35": 0.31, "prog_cor95": 0.18
    },
    "Bașakșehir vs Kocaelispor": {
        "liga": "SUPER LIG &bull; TURKEY",
        "g_gz": 7, "g_os": 3, "med_gz": 1.00, "med_os": 0.43, "gp_gz": 8, "gp_os": 6,
        "ht_gz": "71.43%", "ht_os": "57.14%", "st_gz": "71.43%", "st_os": "57.14%",
        "p15_gz": "85.71%", "p15_os": "42.86%", "p25_gz": "28.57%", "p25_os": "42.86%",
        "gg_gz": "57.14%", "gg_os": "42.86%", "c_gz": "14.29%", "c_os": "28.57%", "cor_os": "14.29%",
        "prog_15": 0.64, "prog_25": 0.14, "prog_05": 0.64, "prog_05_st": 0.64, "prog_gg": 0.50, "prog_c35": 0.21, "prog_cor95": 0.07
    }
}

# 3. SECȚIUNEA DIN STÂNGA: CELE DOUĂ TAB-URI CARE MERGEAU BRICI LA ÎNCEPUT
with col_meciuri:
    tab_global, tab_analiza = st.tabs(["🌍 TOATE MECIURILE LIVE", "📊 GRAFIC STATISTICI PREMIUM"])
    
    with tab_global:
        st.write("")
        st.markdown("""
            <div style="width:100%; height:550px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px;">
                <iframe src="https://scorebat.com" frameborder="0" width="100%" height="520px" allowfullscreen allow="autoplay; fullscreen"></iframe>
            </div>
        """, unsafe_allow_html=True)
        
    with tab_analiza:
        st.write("")
        meci_ales = st.selectbox("🎯 SELECTEAZĂ MECIUL DE AZI PENTRU GRAFIC:", list(meciuri_date.keys()))
        m = meciuri_date[meci_ales]
        
        with st.container():
            st.write(f"📈 **MECI RECOMANDAT • DATE LA ZI {data_azi}**")
            st.write(f"## {meci_ales}")
            st.caption(f"🏆 {m['liga']}")
            st.write("---")
            
            # Cifrele superioare native (Total goluri marcate, medie goluri, goluri primite)
            c1, c2, c3 = st.columns(3)
            c1.metric(label="⚽ Total Goluri Marcate (Gazde)", value=m["g_gz"])
            c2.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>TOTAL GOLURI MARCATE</p>", unsafe_allow_html=True)
            c3.metric(label="⚽ Total Goluri Marcate (Oaspeți)", value=m["g_os"])
            
            c4, c5, c6 = st.columns(3)
            c4.metric(label="📈 Medie Goluri (Gazde)", value=m["med_gz"])
            c5.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>MEDIE GOLURI / MECI</p>", unsafe_allow_html=True)
            c6.metric(label="📈 Medie Goluri (Oaspeți)", value=m["med_os"])
            
            c7, c8, c9 = st.columns(3)
            c7.metric(label="🛡️ Goluri Primite (Gazde)", value=m["gp_gz"])
            c8.markdown("<p style='text-align:center; color:#a0aec0; margin-top:25px;'>GOLURI PRIMITE</p>", unsafe_allow_html=True)
            c9.metric(label="🛡️ Goluri Primite (Oaspeți)", value=m["gp_os"])
            
            st.write("---")
            st.write("**📋 PROCENTE ȘI PROBABILITĂȚI REALE (HT/ST/GOLURI):**")
            
            # Căsuțele cu procente pentru HT/ST din poza ta
            cx1, cx2, cx3 = st.columns(3)
            cx1.metric(label="🟢 Peste 0.5 HT (Prima Repriză)", value=m["ht_gz"], delta=f"{m['ht_os']} Oaspeți", delta_color="off")
            cx2.metric(label="🟢 Peste 0.5 ST (A doua Repriză)", value=m["st_gz"], delta=f"{m['st_os']} Oaspeți", delta_color="off")
            cx3.metric(label="🟢 Peste 1.5 goluri în meci", value=m["p15_gz"], delta=f"{m['p15_os']} Oaspeți", delta_color="off")
            
            cx4, cx5, cx6 = st.columns(3)
            cx4.metric(label="🟢 Peste 2.5 goluri în meci", value=m["p25_gz"], delta=f"{m['p25_os']} Oaspeți", delta_color="off")
            cx5.metric(label="🟢 Ambele echipe marchează (GG)", value=m["gg_gz"], delta=f"{m['gg_os']} Oaspeți", delta_color="off")
            cx6.metric(label="🟡 Peste 3.5 Cartonașe / 9.5 Cornere", value=m["c_gz"], delta=f"{m['c_os']} | {m['cor_os']} Cornere", delta_color="off")
            
            st.write("---")
            st.write("**📈 BARE EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:**")
            
            # Barele orizontale din imaginea ta redesenate curat în Python
            st.write(f"🔹 Peste 1.5 total: **{int(m['prog_15']*100)}%**")
            st.progress(m['prog_15'])
            
            st.write(f"🔹 Peste 2.5 total: **{int(m['prog_25']*100)}%**")
            st.progress(m['prog_25'])
            
            st.write(f"🔹 Peste 0.5 R1: **{int(m['prog_05']*100)}%**")
            st.progress(m['prog_05'])
            
            st.write(f"🔹 Peste 0.5 R2: **{int(m['prog_05_st']*100)}%**")
            st.progress(m['prog_05_st'])
            
            st.write(f"🔹 Ambele marchează (GG): **{int(m['prog_gg']*100)}%**")
            st.progress(m['prog_gg'])
            
            st.write(f"🔹 +3.5 Cartonașe: **{int(m['prog_c35']*100)}%**")
            st.progress(m['prog_c35'])
            
            st.write(f"🔹 +9.5 Cornere: **{int(m['prog_cor95']*100)}%**")
            st.progress(m['prog_cor95'])
            
            st.write("---")
            st.info(f"🔸 **Sistem Algoritm Automat PariuriGO** • Date actualizate automat.")

# 4. SECȚIUNE ABONAMENTE VIP STRUCTURATĂ PE TABURI (Exact cum mergea la început de tot!)
with col_abonamente:
    st.subheader("🏆 Abonamente VIP")
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    link_telegram_afacere = "https://t.me"
    
    with tab_low:
        st.write("")
        st.write("### PACHET LOW")
        st.write("## 40 RON / lună")
        st.write("---")
        st.write("✅ 3 Bilete gata analizate pe săptămână")
        st.write("✅ Cote sigure selectate din ligile mari")
        st.write("✅ Acces grup comunitate chat")
        st.write("")
        st.link_button("Abonare LOW 🚀", link_telegram_afacere, use_container_width=True)

    with tab_med:
        st.write("")
        st.write("### PACHET MEDIUM")
        st.write("## 70 RON / lună")
        st.write("---")

<style>
.stApp {
    background:
        linear-gradient(rgba(6, 34, 20, 0.88), rgba(6, 34, 20, 0.93)),
        url("app/static/teren.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
h1, h2, h3 {
    color: #d4ffb8 !important;
    font-family: 'Segoe UI', sans-serif;
    text-shadow: 0 0 8px rgba(0,0,0,0.6);
}
.card {
    background: rgba(10, 40, 22, 0.75);
    border: 1px solid rgba(120, 255, 120, 0.25);
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.45);
}
.stat-row {
    display: flex; align-items: center; justify-content: space-between;
    margin: 10px 0; gap: 14px;
}
.stat-label { color: #eafbe0; font-weight: 600; font-size: 0.95rem; min-width: 150px; }
.bar-track {
    flex: 1; background: rgba(255,255,255,0.06); border-radius: 8px;
    height: 30px; overflow: hidden; position: relative;
}
.bar-fill {
    height: 100%; background: linear-gradient(90deg, #1f7a1f, #7ed957);
    display: flex; align-items: center; justify-content: flex-end;
    padding-right: 10px; color: #06220f; font-weight: 700; font-size: 0.85rem;
    border-radius: 8px; transition: width 0.6s ease; white-space: nowrap;
}
.bar-fill.low { background: linear-gradient(90deg, #7a1f1f, #d95757); color: #fff0f0; }
.match-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 8px 12px; border-bottom: 1px solid rgba(120,255,120,0.12); color: #eafbe0;
}
.match-row:last-child { border-bottom: none; }
.match-liga { color: #7ed957; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; }
.match-scor { font-weight: 700; color: #d4ffb8; }
</style>
""", unsafe_allow_html=True)

# ============================================
# FUNCTII
# ============================================
def get_meciuri_azi():
    azi = date.today().isoformat()
    url = f"{BASE_URL}/matches"
    params = {"dateFrom": azi, "dateTo": azi}
    try:
        r = requests.get(url, headers=HEADERS, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        return pd.DataFrame(), str(e)

    meciuri = []
    for m in data.get("matches", []):
        meciuri.append({
            "Liga": m["competition"]["name"],
            "Ora": m["utcDate"][11:16],
            "Gazda": m["homeTeam"]["name"],
            "Oaspete": m["awayTeam"]["name"],
            "Scor Gazda": m["score"]["fullTime"]["home"],
            "Scor Oaspete": m["score"]["fullTime"]["away"],
        })
    return pd.DataFrame(meciuri), None


def get_statistici_echipa_demo(nume_echipa):
    return {
        "goluri_marcate": 7, "medie_goluri": 1.00, "goluri_primite": 8,
        "peste_0_5_ht": 71.43, "peste_0_5_st": 71.43, "peste_1_5": 85.71,
        "peste_2_5": 28.57, "ambele_marcheaza": 57.14,
        "peste_3_5_cartonase": 14.29, "peste_9_5_cornere": 0.0,
    }


def bara_procent(eticheta, procent, prag_scazut=30.0):
    clasa = "low" if procent < prag_scazut else ""
    st.markdown(f"""
        <div class="stat-row">
            <div class="stat-label">{eticheta}</div>
            <div class="bar-track">
                <div class="bar-fill {clasa}" style="width:{procent}%">{procent:.2f}%</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================================
# INTERFATA
# ============================================
st.title("⚽ Analist Pariuri")
st.caption("Aplicatie Streamlit — tema verde, date live")

st.markdown("### 📊 Statistici echipa")
echipa = st.text_input("Nume echipa (demo)", value="Echipa Exemplu")
stats = get_statistici_echipa_demo(echipa)

st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.metric("Total goluri marcate", stats["goluri_marcate"])
    st.metric("Medie goluri", stats["medie_goluri"])
with col2:
    st.metric("Goluri primite", stats["goluri_primite"])

bara_procent("Peste 0.5 HT", stats["peste_0_5_ht"])
bara_procent("Peste 0.5 ST", stats["peste_0_5_st"])
bara_procent("Peste 1.5 goluri", stats["peste_1_5"])
bara_procent("Peste 2.5 goluri", stats["peste_2_5"])
bara_procent("Ambele marcheaza", stats["ambele_marcheaza"])
bara_procent("Peste 3.5 cartonase", stats["peste_3_5_cartonase"])
bara_procent("Peste 9.5 cornere", stats["peste_9_5_cornere"])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### 📅 Meciurile zilei")
df, eroare = get_meciuri_azi()

st.markdown('<div class="card">', unsafe_allow_html=True)
if eroare:
    st.warning(f"Nu am putut aduce meciurile de pe API. Verificati cheia. Detaliu: {eroare}")
elif df.empty:
    st.info("Nu exista meciuri programate azi.")
else:
    for _, row in df.iterrows():
        scor = f"{row['Scor Gazda']} - {row['Scor Oaspete']}" if row["Scor Gazda"] is not None else "vs"
        st.markdown(f"""
            <div class="match-row">
                <div>
                    <div class="match-liga">{row['Liga']}</div>
                    <div>{row['Gazda']} <span class="match-scor">{scor}</span> {row['Oaspete']}</div>
                </div>
                <div>{row['Ora']}</div>
            </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
