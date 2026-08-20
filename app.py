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
import streamlit as st
from baza import init_db, adauga_pont, get_ponturi, salveaza_user, verfica_acces

init_db()

st.set_page_config(page_title="BetGO VIP", page_icon="⚡", layout="centered")

# CSS Modern Style
st.markdown("""
    <style>
    .stApp { background-color: #0d0e15; }
    .card-pricing {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    .card-vip {
        border: 1px solid #00E676;
        box-shadow: 0px 0px 15px rgba(0, 230, 118, 0.2);
    }
    .badge-price {
        font-size: 24px;
        font-weight: 800;
        color: #00E676;
    }
    .card-match {
        background: #161822;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        border-left: 4px solid #00E676;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ BetGO")

# Session State Auth Simpla
if "user_email" not in st.session_state:
    st.session_state["user_email"] = None

# Autentificare
if not st.session_state["user_email"]:
    st.subheader("🔑 Autentificare")
    email_input = st.text_input("Introdu adresa de e-mail (Google / Apple / Email):")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Autentificare cu Email", use_container_width=True):
            if "@" in email_input:
                st.session_state["user_email"] = email_input
                salveaza_user(email_input)
                st.rerun()
            else:
                st.error("E-mail invalid.")
    with col2:
        if st.button("Continue with Google / Apple", use_container_width=True):
            st.info("Aici se conectează furnizorul OAuth direct.")
else:
    email = st.session_state["user_email"]
    platit, abonament = verfica_acces(email)
    
    st.write(f"Conectat ca: **{email}** | Plan: **{abonament}**")
    if st.button("Deconectare"):
        st.session_state["user_email"] = None
        st.rerun()
        
    st.divider()

    # Daca NU are abonament platit -> Afiseaza Pachtele de Pret
    if not platit:
        st.subheader("🔒 Alege un plan pentru acces la ponturi")
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("""
                <div class="card-pricing">
                    <h4>Săptămânal</h4>
                    <div class="badge-price">40 LEI</div>
                    <p style="color: #aaa; font-size: 12px;">7 Zile Acces VIP</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Cumpără (40 L)", key="p1", use_container_width=True):
                # Link checkout Stripe
                salveaza_user(email, "Săptămânal", 1)
                st.rerun()

        with c2:
            st.markdown("""
                <div class="card-pricing card-vip">
                    <h4 style="color:#00E676;">Medium ⭐</h4>
                    <div class="badge-price">70 LEI</div>
                    <p style="color: #aaa; font-size: 12px;">1 Lună Acces VIP</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Cumpără (70 L)", key="p2", type="primary", use_container_width=True):
                salveaza_user(email, "Medium", 1)
                st.rerun()

        with c3:
            st.markdown("""
                <div class="card-pricing">
                    <h4>Pro VIP 🔥</h4>
                    <div class="badge-price">120 LEI</div>
                    <p style="color: #aaa; font-size: 12px;">3 Luni Acces Full</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Cumpără (120 L)", key="p3", use_container_width=True):
                salveaza_user(email, "Pro VIP", 1)
                st.rerun()

    # Daca ARE abonament -> Afiseaza Ponturile
    else:
        st.success("✨ Abonament Activ! Ai acces complet la ponturi.")
        
        tab_azi, tab_maine, tab_admin = st.tabs(["🔥 Ponturi Azi", "📅 Ponturi Mâine", "⚙️ Admin"])

        def afiseaza_ponturi_design(ziua):
            meciuri = get_ponturi(ziua)
            if not meciuri:
                st.info("Niciun pont adăugat pentru moment.")
            for m in meciuri:
                st.markdown(f"""
                    <div class="card-match">
                        <small style="color: #888;">{m[1]}</small>
                        <div style="font-size: 16px; font-weight: bold; margin: 4px 0;">{m[0]}</div>
                        <div style="color: #00E676; font-weight: bold;">Pronostic: {m[2]} <span style="float:right; color:#fff; background:#222; padding:2px 8px; border-radius:4px;">Cotă {m[3]}</span></div>
                    </div>
                """, unsafe_allow_html=True)

        with tab_azi:
            afiseaza_ponturi_design("Azi")
            
        with tab_maine:
            afiseaza_ponturi_design("Mâine")
            
        with tab_admin:
            st.write("Panou Admin")
            with st.form("add_p"):
                m = st.text_input("Meci")
                c = st.text_input("Competiție")
                p = st.text_input("Pronostic")
                cota = st.number_input("Cotă", min_value=1.0)
                z = st.selectbox("Ziua", ["Azi", "Mâine"])
                if st.form_submit_button("Adaugă Pont"):
                    adauga_pont(m, c, p, cota, z)
                    st.success("Adăugat!")
                    st.rerun()
