import streamlit as st
import pandas as pd

# Configurarea paginii
st.set_page_config(page_title="Pariuri Go", page_icon="⚽", layout="wide")

# Titlul aplicației
st.title("⚽ Pariuri Go - Panou de Analiză și Bilet Virtual")
st.markdown("Aplicația ta inteligentă pentru ponturi, meciuri și calcularea cotelor.")

# Meniu lateral (Sidebar) pentru secțiuni
menu = st.sidebar.selectbox("Navigare", ["Meciuri & Cote", "Calculator Bilet", "Despre Proiect"])

# Date simulate pentru meciuri
meciuri_data = {
    "Meci": ["FCSB vs Rapid", "Real Madrid vs Barcelona", "Manchester City vs Liverpool", "AC Milan vs Inter"],
    "Cota 1 (1)": [2.10, 2.30, 1.85, 2.70],
    "Cota X (X)": [3.30, 3.40, 3.60, 3.10],
    "Cota 2 (2)": [3.50, 2.90, 4.00, 2.75]
}
df_meciuri = pd.DataFrame(meciuri_data)

if menu == "Meciuri & Cote":
    st.header("📅 Oferta Zilei - Meciuri Populare")
    st.dataframe(df_meciuri, use_container_width=True)
    
    st.info("💡 Sfat Pariuri Go: Analizează forma de moment înainte de a plasa un bilet.")

elif menu == "Calculator Bilet":
    st.header("🧮 Calculator Bilet Virtual")
    
    # Selectarea meciului și a pronosticului
    meci_ales = st.selectbox("Alege meciul:", df_meciuri["Meci"])
    
    # Preluarea cotelor pentru meciul ales
    row = df_meciuri[df_meciuri["Meci"] == meci_ales].iloc[0]
    
    pronostic_ales = st.selectbox("Alege pronosticul:", ["1 (Gazda)", "X (Egal)", "2 (Oaspete)"])
    
    if "1" in pronostic_ales:
        cota_selectata = row["Cota 1 (1)"]
    elif "X" in pronostic_ales:
        cota_selectata = row["Cota X (X)"]
    else:
        cota_selectata = row["Cota 2 (2)"]
        
    st.metric(label="Cota Selectată", value=cota_selectata)
    
    # Suma pariată
    miza = st.number_input("Introdu miza (RON):", min_value=1.0, max_value=10000.0, value=50.0, step=10.0)
    
    # Calcul câștig
    castig_potenial = miza * cota_selectata
    st.success(f"💰 Câștig potențial estimat: **{castig_potenial:.2f} RON**")

elif menu == "Despre Proiect":
    st.header("Despre Pariuri Go")
    st.write("Această aplicație este creată în Python cu Streamlit și publicată pe GitHub.")
    st.markdown("Poți extinde acest cod adăugând un API real de fotbal sau un model de Machine Learning pentru predicții.")
