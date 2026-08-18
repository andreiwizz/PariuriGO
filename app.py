import streamlit as st
import pandas as pd
import numpy as np

# Configurare pagină
st.set_page_config(page_title="Pariuri Go - Pro", page_icon="📈", layout="wide")

# Stil personalizat pentru aspect profesional
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #white; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

# Titlu principal
st.title("📈 Pariuri Go | Analiză Statistică & Ponturi VIP")
st.markdown("Platformă avansată de predicții fotbalistice bazată pe algoritmi de probabilitate și statistici live.")

# Meniu Lateral
st.sidebar.title("Navigare & Abonament")
pachet_activ = st.sidebar.selectbox("Alege Pachetul Tău:", ["Gratuit (Demo)", "Low Risk (Sigur)", "Medium Risk (echilibrat)", "High Risk (Combo / Cote Mari)"])
st.sidebar.markdown("---")

# Simulare date meciuri cu algoritmi de probabilitate (stil BetMines)
np.random.seed(42)
meciuri = [
    {"Meci": "Arsenal vs Chelsea", "Ora": "21:45", "Cota 1": 1.95, "Cota X": 3.40, "Cota 2": 3.80, "Prob 1": "58%", "Tip Pachet": "Low Risk"},
    {"Meci": "Juventus vs AS Roma", "Ora": "21:00", "Cota 1": 2.10, "Cota X": 3.20, "Cota 2": 3.60, "Prob 1": "45%", "Tip Pachet": "Medium Risk"},
    {"Meci": "Porto vs Benfica", "Ora": "22:30", "Cota 1": 2.45, "Cota X": 3.10, "Cota 2": 2.90, "Prob X": "38%", "Tip Pachet": "Medium Risk"},
    {"Meci": "Lyon vs Marseille", "Ora": "19:00", "Cota 1": 2.80, "Cota X": 3.50, "Cota 2": 2.40, "Prob 2": "42%", "Tip Pachet": "High Risk"},
    {"Meci": "Sheriff vs BATE", "Ora": "18:30", "Cota 1": 1.70, "Cota X": 3.60, "Cota 2": 5.00, "Prob 1": "65%", "Tip Pachet": "Low Risk"},
    {"Meci": "Ajax vs Feyenoord", "Ora": "15:30", "Cota 1": 2.90, "Cota X": 3.60, "Cota 2": 2.30, "Prob 2": "47%", "Tip Pachet": "High Risk"}
]

df = pd.DataFrame(meciuri)

# Secțiunea principală în funcție de pachetul selectat
st.header(f"🎯 Selecție Ponturi pentru: {pachet_activ}")

if pachet_activ == "Gratuit (Demo)":
    st.warning("🔒 Vizualizezi doar meciurile gratuite. Fă upgrade la un pachet **Low, Medium sau High** pentru ponturi analizate de algoritmi.")
    df_filtrat = df[df["Tip Pachet"] == "Low Risk"].head(2)
    st.dataframe(df_filtrat[["Meci", "Ora", "Cota 1", "Cota X", "Cota 2"]], use_container_width=True)
    
    st.markdown("### 💳 Activează un pachet PRO:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pachet Low Risk", "49 RON / lună", "Ponturi > 1.60 cota")
        if st.button("Cumpără Low Risk"):
            st.info("Redirecționare către procesatorul de plăti (ex: [Stripe](https://stripe.com))")
    with col2:
        st.metric("Pachet Medium Risk", "99 RON / lună", "Ponturi Cota 2.00+")
        if st.button("Cumpără Medium Risk"):
            st.info("Redirecționare către procesatorul de plăti")
    with col3:
        st.metric("Pachet High Risk", "149 RON / lună", "Bilete 5.00+ / Combo")
        if st.button("Cumpără High Risk"):
            st.info("Redirecționare către procesatorul de plăti")

else:
    # Verificarea accesului bazat pe pachet
    st.success(f"✅ Ai acces activ la secțiunea **{pachet_activ}**!")
    
    if pachet_activ == "Low Risk (Sigur)":
        df_afisat = df[df["Tip Pachet"] == "Low Risk"]
    elif pachet_activ == "Medium Risk (echilibrat)":
        df_afisat = df[df["Tip Pachet"].isin(["Low Risk", "Medium Risk"])]
    else:
        df_afisat = df # Toate meciurile incluzând High Risk
        
    st.dataframe(df_afisat, use_container_width=True)
    
    # Statistici de performanță simulate
    st.markdown("### 📊 Statistici Lunare Algoritm")
    c1, c2, c3 = st.columns(3)
    c1.metric("Rată de Reușită (Win Rate)", "78.4%", "+2.1%")
    c2.metric("Profit Mediu Lunar", "+14.2 Unități")
    c3.metric("Total Analize", "142 Meciuri")

# Secțiune dedicată AI Bet Analyzer
st.markdown("---")
st.subheader("🤖 AI Smart Predictor & Statistici H2H")
meci_selectat = st.selectbox("Selectează meciul pentru analiză detaliată:", df["Meci"])
if st.button("Generează Analiză Detaliată AI"):
    st.info(f"Analizăm statisticile pentru **{meci_selectat}**: Posesie medie, goluri în ultimele 5 meciuri, indisponibilități și tendințe de pariere. Recomandare: **1x & Peste 1.5 goluri**.")
