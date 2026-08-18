import streamlit as st
import pandas as pd

# Configurare pagină
st.set_page_config(page_title="Pariuri Go - Pro Betting", page_icon="⚡", layout="wide")

# Design modern (Dark Mode avansat)
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #ffffff; }
    .match-card { background-color: #131b2e; padding: 20px; border-radius: 12px; border: 1px solid #1f2c47; margin-bottom: 15px; }
    .badge-low { background-color: #10b981; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 12px; }
    .badge-med { background-color: #f59e0b; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 12px; }
    .badge-high { background-color: #ef4444; color: white; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# Titlu și Meniu Lateral
st.title("⚡ Pariuri Go | AI Predictions & Analytics")
st.sidebar.markdown("## 👑 Meniu & Pachete VIP")
pachet_ales = st.sidebar.selectbox("Selectează Nivelul:", ["Toate (Demo)", "Pachet Low Risk (Cote 1.4 - 1.6)", "Pachet Medium Risk (Cote 1.7 - 2.1)", "Pachet High Risk (Cote 2.2+)"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Pariuri Go PRO**: Algoritmii analizează peste 50 de parametrii înainte de a afișa pontul.")

# Bază de date simulată dar foarte aspectuoasă (Stil BetMines)
date_meciuri = [
    {"id": 1, "meci": "Manchester United vs Tottenham", "ora": "19:30", "liga": "Premier League", "cota1": 1.95, "cotax": 3.50, "cota2": 3.70, "prob1": 55, "probx": 25, "prob2": 20, "tip": "Pachet Medium Risk (Cote 1.7 - 2.1)", "pronostic": "1x & Peste 1.5 goluri"},
    {"id": 2, "meci": "Inter Milano vs Napoli", "ora": "21:45", "liga": "Serie A", "cota1": 1.72, "cotax": 3.60, "cota2": 4.80, "prob1": 62, "probx": 23, "prob2": 15, "tip": "Pachet Low Risk (Cote 1.4 - 1.6)", "pronostic": "1 solist (Sigur)"},
    {"id": 3, "meci": "Villareal vs Atletico Madrid", "ora": "22:00", "liga": "La Liga", "cota1": 2.90, "cotax": 3.30, "cota2": 2.45, "prob1": 30, "probx": 30, "prob2": 40, "tip": "Pachet High Risk (Cote 2.2+)", "pronostic": "2 solist / GG"},
    {"id": 4, "meci": "Feyenoord vs PSV", "ora": "15:00", "liga": "Eredivisie", "cota1": 2.20, "cotax": 3.40, "cota2": 3.10, "prob1": 45, "probx": 30, "prob2": 25, "tip": "Pachet Medium Risk (Cote 1.7 - 2.1)", "pronostic": "Ambele marchează (GG)"},
    {"id": 5, "meci": "Standard Liege vs Anderlecht", "ora": "18:30", "liga": "Jupiler Pro League", "cota1": 3.20, "cotax": 3.50, "cota2": 2.20, "prob1": 25, "probx": 25, "prob2": 50, "tip": "Pachet High Risk (Cote 2.2+)", "pronostic": "22 & Peste 2.5 goluri"}
]

# Filtrare
if pachet_ales == "Toate (Demo)":
    meciuri_filtrate = date_meciuri
else:
    meciuri_filtrate = [m for m in date_meciuri if m["tip"] == pachet_ales]

st.header(f"🎯 Ponturi recomandate: {pachet_ales}")

# Afișare sub formă de carduri moderne (nu tabele seci)
for m in meciuri_filtrate:
    badge_class = "badge-low" if "Low" in m["tip"] else ("badge-med" if "Medium" in m["tip"] else "badge-high")
    
    with st.container():
        st.markdown(f"""
        <div class="match-card">
            <span class="{badge_class}">{m["tip"].split(" ")[1]} Risk</span> &nbsp; <b>{m["liga"]}</b> | 🕒 {m["ora"]}
            <h3>{m["meci"]}</h3>
            <p><b>Pronostic AI:</b> {m["pronostic"]}</p>
            <p>📊 <b>Probabilități:</b> 1: {m["prob1"]}% | X: {m["probx"]}% | 2: {m["prob2"]}% &nbsp;&nbsp;|&nbsp;&nbsp; <b>Cote:</b> 1({m["cota1"]}) X({m["cotax"]}) 2({m["cota2"]})</p>
        </div>
        """, unsafe_allow_html=True)

# Secțiune Prețuri / Abonamente vizuale
st.markdown("---")
st.subheader("💎 Activează accesul complet la toate ponturile VIP")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Low Risk\n* **Cote sigure** (1.40 - 1.60)\n* Win-rate ridicat (~85%)\n* **49 RON / lună**")
    st.button("Abonează-te Low", key="b1")

with col2:
    st.markdown("### Medium Risk\n* **Cote echilibrate** (1.70 - 2.10)\n* Analiză statistică extinsă\n* **99 RON / lună**")
    st.button("Abonează-te Medium", key="b2")

with col3:
    st.markdown("### High Risk\n* **Cote mari / Combo** (2.20+)\n* Bilete exprimate / Surprize\n* **149 RON / lună**")
    st.button("Abonează-te High", key="b3")
