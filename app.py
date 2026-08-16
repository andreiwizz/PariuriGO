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
st.markdown("""
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
