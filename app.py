import streamlit as st
from datetime import datetime

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="Analist PariuriGO",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

st.title("⚽ Analist Pariuri &bull; World Live Center")
st.write(f"Data curentă: {data_azi}")
st.write("---")

# Împărțirea ecranului în două coloane (Stânga: Statistici, Dreapta: Abonamente)
col_stanga, col_dreapta = st.columns([1.4, 0.6], gap="large")

with col_stanga:
    st.subheader("📊 Statistici echipă")
    
    # Meniu de selecție simplu, nativ din Python
    meci_selectat = st.selectbox("🎯 Schimbă meciul din ziua respectivă:", [
        "FCSB vs Rapid București",
        "CFR Cluj vs Universitatea Craiova",
        "Bașakșehir vs Kocaelispor"
    ])
    
    st.write("---")
    
    # Configurarea datelor în mod direct din Python
    if meci_selectat == "FCSB vs Rapid București":
        g_marc, g_prim, med_g = 14, 5, 1.75
        p_ht, p_st, p_15, p_25, p_gg, p_cart, p_corn = 0.85, 0.78, 0.91, 0.64, 0.71, 0.21, 0.14
    elif meci_selectat == "CFR Cluj vs Universitatea Craiova":
        g_marc, g_prim, med_g = 11, 7, 1.37
        p_ht, p_st, p_15, p_25, p_gg, p_cart, p_corn = 0.73, 0.71, 0.85, 0.28, 0.57, 0.14, 0.05
    else:
        g_marc, g_prim, med_g = 7, 8, 1.00
        p_ht, p_st, p_15, p_25, p_gg, p_cart, p_corn = 0.71, 0.71, 0.85, 0.28, 0.57, 0.14, 0.07

    # Afișare metrici superioare din poza ta
    c1, c2, c3 = st.columns(3)
    c1.metric(label="Total goluri marcate", value=str(g_marc))
    c2.metric(label="Goluri primite", value=str(g_prim))
    c3.metric(label="Medie goluri", value=str(med_g))
    
    st.write("---")
    
    # Barele de progres native, exact ca în poza ta trimisă
    st.write(f"Peste 0.5 HT: **{int(p_ht*100)}%**")
    st.progress(p_ht)
    
    st.write(f"Peste 0.5 ST: **{int(p_st*100)}%**")
    st.progress(p_st)
    
    st.write(f"Peste 1.5 goluri: **{int(p_15*100)}%**")
    st.progress(p_15)
    
    st.write(f"Peste 2.5 goluri: **{int(p_25*100)}%**")
    st.progress(p_25)
    
    st.write(f"Ambele marchează: **{int(p_gg*100)}%**")
    st.progress(p_gg)
    
    st.write(f"Peste 3.5 cartonașe: **{int(p_cart*100)}%**")
    st.progress(p_cart)
    
    st.write(f"Peste 9.5 cornere: **{int(p_corn*100)}%**")
    st.progress(p_corn)

with col_dreapta:
    st.subheader("🏆 Abonamente VIP")
    
    link_tg = "https://t.me"
    
    # Pachetele VIP așezate la linie, curate, cu butoane native vizibile
    st.info("### 🟢 PACHET LOW\n**40 RON / lună**\n\n✅ 3 Bilete gata analizate pe săptămână\n\n✅ Cote sigure selectate din ligile mari")
    st.link_button("CUMPĂRĂ LOW 🚀", link_tg, use_container_width=True)
    
    st.write("")
    
    st.warning("### 🟡 PACHET MEDIUM\n**70 RON / lună**\n\n✅ 1 Bilet Premium în fiecare zi calendaristică\n\n✅ Procente și probabilități avansate live")
    st.link_button("CUMPĂRĂ MEDIUM 🟡", link_tg, use_container_width=True)
    
    st.write("")
    
    st.error("### 🔥 HIGH VIP ELITE\n**120 RON / lună**\n\n✅ Cota 2 VIP zilnică + Proiect Dublare\n\n✅ Suport privat 1-la-1 direct cu tipsterul")
    st.link_button("DEBLOCHEAZĂ VIP ELITE 🔥", link_tg, use_container_width=True)
