import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from datetime import datetime

# 1. CONFIGURARE INTERFAȚĂ PREMIUM (STIL GOLDENTIPS)
st.set_page_config(page_title="GoldenTips Professional Clone", page_icon="⚽", layout="wide")

# Forțare stil vizual Dark Mode cu accente aurii (Premium)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; color: #ffffff; }
    .stTabs [aria-selected="true"] { color: #ffd700 !important; border-bottom-color: #ffd700 !important; }
    div.stButton > button:first-child { background-color: #ffd700; color: #000000; font-weight: bold; }
    .css-12w0qpk { background-color: #151a24; border-radius: 10px; padding: 20px; }
    </style>
""", unsafe_with_html=True)

# 2. INIȚIALIZARE BAZĂ DE DATE LOCALĂ (Pentru stocare mesaje și utilizatori)
conn = sqlite3.connect('goldentips_data.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS chat (id INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, msg TEXT, time TEXT)''')
conn.commit()

# 3. DATE STATISTICE ȘI MECIURI (Structură complexă de date)
# În producție, acestea se pot lega la un API de fotbal (ex: API-Football)
if 'meciuri' not in st.session_state:
    st.session_state.meciuri = [
        {"id": 1, "tip": "FREE", "sport": "Fotbal", "meci": "FCSB vs Rapid", "predictie": "Peste 2.5 goluri", "cota": 1.85, "status": "Câștigat"},
        {"id": 2, "tip": "VIP", "sport": "Fotbal", "meci": "Real Madrid vs Barcelona", "predictie": "Meci Egal (X)", "cota": 3.60, "status": "În desfășurare"},
        {"id": 3, "tip": "VIP", "sport": "Tenis", "meci": "Alcaraz vs Sinner", "predictie": "Sinner +1.5 Seturi", "cota": 1.75, "status": "Câștigat"},
        {"id": 4, "tip": "FREE", "sport": "Baschet", "meci": "Los Angeles Lakers vs Boston Celtics", "predictie": "Lakers -4.5 puncte", "cota": 1.90, "status": "Pierdut"}
    ]

# --- LOGICĂ HEADERS ---
st.title("⚽ GOLDEN TIPS - PRO SYSTEM")
st.write(f"Server Status: **ONLINE** | Data sistemului: {datetime.now().strftime('%d-%m-%Y')}")
st.markdown("---")

# 4. MENIUL PRINCIPAL PE COMPONENTE
tab_dashboard, tab_free, tab_vip, tab_comunitate = st.tabs(["📊 Panou Statistici", "🆓 Free Tips", "👑 VIP Premium", "💬 Chat Oficial"])

# ================= TAB: STATISTICI VIZUALE (MODUL GOLDENTIPS) =================
with tab_dashboard:
    st.subheader("📈 Performanța și Rata de Câștig (Win Rate)")
    
    # Transformăm datele în DataFrame pentru calcule matematice automate
    df = pd.DataFrame(st.session_state.meciuri)
    
    # Calcule automate KPI
    total_meciuri = len(df)
    castigate = len(df[df['status'] == 'Câștigat'])
    pierdute = len(df[df['status'] == 'Pierdut'])
    in_desfasurare = len(df[df['status'] == 'În desfășurare'])
    
    win_rate = (castigate / (castigate + pierdute)) * 100 if (castigate + pierdute) > 0 else 0
    
    # Afișare metrici pe coloane ca în aplicațiile native
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Pronosticuri", total_meciuri)
    col2.metric("✅ Câștigate", castigate)
    col3.metric("❌ Pierdute", pierdute)
    col4.metric("📊 Win Rate General", f"{win_rate:.1f}%")
    
    st.markdown("### 📊 Distribuția Profitului pe Sporturi")
    # Generare grafic interactiv cu Plotly
    fig = px.pie(df, names='sport', values='cota', title="Unde se prind cele mai mari cote?", hole=0.4, color_discrete_sequence=px.colors.sequential.Amber)
    st.plotly_chart(fig, use_container_width=True)

# ================= TAB: MECIURI FREE =================
with tab_free:
    st.subheader("💡 Bilete și Pronosticuri Gratuite")
    df_free = df[df['tip'] == 'FREE']
    
    for _, row in df_free.iterrows():
        with st.expander(f"⚽ {row['meci']} — Cotă {row['cota']}", expanded=True):
            c1, c2, c3 = st.columns(3)
            c1.markdown(f"**Sport:** {row['sport']}")
            c2.markdown(f"**Pronostic:** {row['predictie']}")
            if row['status'] == 'Câștigat':
                c3.success(f"Status: {row['status']}")
            elif row['status'] == 'Pierdut':
                c3.error(f"Status: {row['status']}")
            else:
                c3.warning(f"Status: {row['status']}")

# ================= TAB: VIP PREMIUM (SISTEM PAYWALL AVANSAT) =================
with tab_vip:
    st.subheader("👑 Secțiunea VIP — Golden Premium")
    
    # Sistem de securitate bazat pe token/parolă session_state
    if "is_vip" not in st.session_state:
        st.session_state.is_vip = False
        
    if not st.session_state.is_vip:
        st.error("🔒 Conținutul VIP este blocat! Ai nevoie de licență activă.")
        cc1, cc2 = st.columns(2)
        with cc1:
            cod_secret = st.text_input("Introdu Cheia de Activare VIP:", type="password")
            # Înlocuiește 'GOLDENTIPS2026' cu cheia ta privată
            if st.button("Verifică Licența 🔑"):
                if cod_secret == "GOLDENTIPS2026":
                    st.session_state.is_vip = True
                    st.rerun()
                else:
                    st.error("Cheie invalidă sau expirată!")
        with cc2:
            st.info("ℹ️ Cum devii membru VIP?\n\nContactează echipa pe Telegram și achiziționează un token de acces valabil 30 de zile.")
    else:
        st.success("🔓 Mod VIP Activ! Bun venit în rândul profesioniștilor.")
        if st.button("Deconectare din modul VIP"):
            st.session_state.is_vip = False
            st.rerun()
            
        df_vip = df[df['tip'] == 'VIP']
        st.dataframe(df_vip[['sport', 'meci', 'predictie', 'cota', 'status']], use_container_width=True)

# ================= TAB: CHAT DIRECT ÎN BAZA DE DATE =================
with tab_comunitate:
    st.subheader("💬 Comunitatea GoldenTips (Live Chat)")
    
    # Formular adăugare mesaj
    with st.form("chat_form", clear_on_submit=True):
        username = st.text_input("Pseudonim (User):", value="Tipster_Anonim")
        user_msg = st.text_area("Mesaj:")
        submit_msg = st.form_submit_button("Postează pe Canal")
        
        if submit_msg and user_msg:
            now = datetime.now().strftime("%H:%M:%S")
            cursor.execute("INSERT INTO chat (user, msg, time) VALUES (?, ?, ?)", (username, user_msg, now))
            conn.commit()
            st.rerun()
            
    # Afișare mesaje din baza de date SQLite
    st.markdown("### 💬 Mesaje recente:")
    cursor.execute("SELECT user, msg, time FROM chat ORDER BY id DESC LIMIT 20")
    for row in cursor.fetchall():
        st.markdown(f"⏱️ `{row[2]}` **{row[0]}**: {row[1]}")
