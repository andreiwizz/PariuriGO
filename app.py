import streamlit as st
from baza import init_db, adauga_pont, get_ponturi

# Initializam baza de date
init_db()

# Configurare pagina
st.set_page_config(page_title="BetGO - VIP Tips", page_icon="⚽", layout="centered")

# CSS curat pentru carduri moderne de ponturi
st.markdown("""
    <style>
    .card-pont {
        background-color: #1E1E2E;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #00FF66;
        margin-bottom: 15px;
        color: white;
    }
    .cota-badge {
        background-color: #00FF66;
        color: #000;
        font-weight: bold;
        padding: 4px 8px;
        border-radius: 6px;
        float: right;
    }
    .comp-title {
        font-size: 0.8rem;
        color: #888;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Titlu Principal
st.title("⚽ BetGO")
st.caption("Predicții și ponturi zilnice de încredere")

# Tabs pentru navigare simplă
tab_azi, tab_maine, tab_admin = st.tabs(["🔥 Ponturi Azi", "📅 Ponturi Mâine", "⚙️ Admin Panel"])

def afiseaza_meciuri(ziua):
    meciuri = get_ponturi(ziua)
    if not meciuri:
        st.info(f"Nu există ponturi adăugate pentru {ziua.lower()}.")
    else:
        for meci in meciuri:
            nume_meci, comp, pronostic, cota, status = meci
            st.markdown(f"""
                <div class="card-pont">
                    <div class="comp-title">{comp}</div>
                    <div style="font-size: 1.1rem; font-weight: bold;">{nume_meci} <span class="cota-badge">Cotă {cota}</span></div>
                    <div style="margin-top: 8px; color: #00FF66;">Pronostic: <b>{pronostic}</b></div>
                </div>
            """, unsafe_allow_html=True)

with tab_azi:
    afiseaza_meciuri("Azi")

with tab_maine:
    afiseaza_meciuri("Mâine")

with tab_admin:
    st.subheader("➕ Adaugă un pont nou")
    
    with st.form("form_pont"):
        meci = st.text_input("Meciul (ex: Real Madrid vs Man City)")
        competitie = st.text_input("Competiție & Ora (ex: UCL - 22:00)")
        pronostic = st.text_input("Pronostic (ex: Peste 2.5 goluri)")
        cota = st.number_input("Cotă", min_value=1.01, step=0.05, value=1.85)
        ziua = st.radio("Ziua", ["Azi", "Mâine"], horizontal=True)
        
        submit = st.form_submit_button("Publică Pontul")
        
        if submit:
            if meci and competitie and pronostic:
                adauga_pont(meci, competitie, pronostic, cota, ziua)
                st.success("Pontul a fost adăugat cu succes!")
                st.rerun()
            else:
                st.error("Te rugăm să completezi toate câmpurile.")
import streamlit as st

# Pagina de Abonamente / Paywall
st.subheader("🔒 Alege un plan pentru a debloca ponturile VIP")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style="background-color: #262730; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Săptămânal</h3>
            <h2>40 lei <span>/săpt</span></h2>
            <p>✅ Acces la ponturile zilnice</p>
            <p>✅ Suport dedicat</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abonează-te (40 lei)", key="sapt"):
        st.info("Redirecționare către plata Stripe...")

with col2:
    st.markdown("""
        <div style="background-color: #1E3A8A; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #3B82F6;">
            <h3>Medium ⭐</h3>
            <h2>70 lei <span>/lună</span></h2>
            <p>✅ Acces la ponturi zilnice</p>
            <p>✅ Statistici avansate</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abonează-te (70 lei)", key="med"):
        st.info("Redirecționare către plata Stripe...")

with col3:
    st.markdown("""
        <div style="background-color: #064E3B; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #10B981;">
            <h3>Pro (VIP) 🔥</h3>
            <h2>120 lei <span>/3 luni</span></h2>
            <p>✅ Acces la absolut toate ponturile</p>
            <p>✅ Cota 2 & Biletul Zilei</p>
            <p>✅ Notification Alert</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abonează-te (120 lei)", key="pro"):
        st.info("Redirecționare către plata Stripe...")
