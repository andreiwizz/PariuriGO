import streamlit as st
import base64
from datetime import datetime

# ==============================================================================
# 1. CONFIGURARE PAGINĂ PRINCIPALĂ (MANDATORIU PRIMA LINIE STREAMLIT)
# ==============================================================================
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# ==============================================================================
# 2. CITIRE ȘI CONFIGURARE RESURSE VIZUALE (BASE64)
# ==============================================================================
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.95), rgba(2, 6, 4, 0.97)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #030a05 !important;"

# ==============================================================================
# 3. STILIZARE CSS PREMIUM (HOLOGRAPHIC CYBERPUNK - GLASSMORPHISM)
# ==============================================================================
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
    
    /* FIX DEFINITIV TEXT BUTOANE (REZOLVĂ BUG-UL CU CERCULEȚELE) */
    div.stButton > button div {{
        font-size: 15px !important;
    }}
    
    .vip-card-box {{
        background: linear-gradient(135deg, rgba(6, 20, 13, 0.75) 0%, rgba(3, 10, 6, 0.9) 100%) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 18px !important;
        padding: 26px !important;
        margin-bottom: 25px !important;
    }}

    .border-low {{
        border: 1px solid rgba(0, 255, 102, 0.25) !important;
        box-shadow: 0 10px 30px rgba(0, 255, 102, 0.03), inset 0 0 15px rgba(0, 255, 102, 0.02) !important;
    }}

    .stTextInput input {{
        background: rgba(0, 0, 0, 0.6) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 14px !important;
        font-size: 16px !important;
        font-family: 'Rajdhani', sans-serif !important;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8) !important;
        transition: all 0.3s ease;
    }}
    
    .stTextInput input:focus {{
        border-color: #00ff66 !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.25), inset 0 2px 8px rgba(0, 0, 0, 0.8) !important;
        background: rgba(2, 12, 6, 0.7) !important;
    }}

    div.stButton > button {{
        background: linear-gradient(135deg, rgba(0, 255, 102, 0.1) 0%, rgba(0, 92, 32, 0.05) 100%) !important;
        color: #00ff66 !important;
        border: 1px solid rgba(0, 255, 102, 0.6) !important;
        font-weight: 800 !important;
        font-size: 15px !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        border-radius: 12px !important;
        padding: 12px 25px !important;
        width: 100% !important;
        transition: all 0.4s ease !important;
    }}

    div.stButton > button:hover {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(0, 255, 102, 0.5) !important;
        transform: translateY(-2px);
    }}

    @keyframes cyberScan {{
        0% {{ top: 0%; opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ top: 100%; opacity: 0; }}
    }}

    .full-screen-login-card {{
        position: relative;
        background: linear-gradient(135deg, rgba(6, 26, 14, 0.9) 0%, rgba(2, 12, 6, 0.98) 100%) !important;
        backdrop-filter: blur(25px) !important;
        border: 2px solid rgba(0, 255, 102, 0.4) !important;
        border-radius: 24px !important;
        padding: 45px !important;
        max-width: 500px;
        margin: 40px auto !important;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(0, 255, 102, 0.1) !important;
        overflow: hidden;
    }}

    .full-screen-login-card::after {{
        content: '';
        position: absolute;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, transparent, #00ff66, transparent);
        box-shadow: 0 0 20px #00ff66, 0 0 40px #00ff66;
        animation: cyberScan 3.5s infinite linear;
    }}

    .status-badge-secure {{
        background: rgba(0, 255, 102, 0.1);
        border: 1px solid #00ff66;
        color: #00ff66;
        font-size: 12px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: 6px 16px;
        border-radius: 30px;
        display: inline-block;
        margin-bottom: 20px;
    }}

    .admin-box {{
        background: linear-gradient(145deg, rgba(8, 28, 16, 0.6) 0%, rgba(4, 14, 8, 0.8) 100%) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        margin-bottom: 25px;
    }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800; text-shadow: 0 0 15px rgba(0,255,102,0.2);'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")
# ==============================================================================
# 5. INITIALIZARE STĂRI SECURIZATE ȘI LIVE DATA
# ==============================================================================
if "lista_membri" not in st.session_state:
    st.session_state.lista_membri = {"admin": "pariurigo"}

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

if "ecran_login" not in st.session_state:
    st.session_state.ecran_login = False

seed_zi = sum(ord(c) for c in data_azi)
if seed_zi % 2 == 0:
    partide = ["Manchester United vs Liverpool", "AC Milan vs Juventus Roma", "Bayern Munchen vs Dortmund"]
else:
    partide = ["Real Madrid vs Man City", "Arsenal vs Chelsea Londra", "Inter Milano vs Napoli"]
    
meciuri_date_zi = {}
for i, p in enumerate(partide):
    g_gz = str((seed_zi + i * 7) % 15 + 10)
    g_os = str((seed_zi + i * 4) % 15 + 10)
    med_gz = f"{round(1.5 + (seed_zi % 10) / 10, 1)}"
    meciuri_date_zi[p] = {
        "liga": "Meciuri Oficiale Pro Live", "g_gz": g_gz, "g_os": g_os, "med_gz": med_gz, "med_os": f"{round(1.2 + (i % 5) / 10, 1)}", 
        "gp_gz": str((seed_zi) % 8 + 5), "gp_os": str((seed_zi + i) % 9 + 5),
        "ht_gz": f"{60 + (seed_zi % 25)}%", "st_gz": f"{65 + (i * 5) % 25}%", 
        "p15_gz": f"{70 + (seed_zi % 20)}%", "p25_gz": f"{50 + (i * 7) % 35}%", "gg_gz": f"{45 + (seed_zi % 40)}%",
        "w_p15": f"{70 + (seed_zi % 20)}%", "w_p25": f"{50 + (i * 7) % 35}%", 
        "w_p05r1": f"{60 + (seed_zi % 25)}%", "w_gg": f"{45 + (seed_zi % 40)}%", "w_c35": f"{40 + (seed_zi % 45)}%"
    }

# ==============================================================================
# 6. LOGICĂ RENDERING INTERFAȚĂ DINAMICĂ
# ==============================================================================
if st.session_state.ecran_login and not st.session_state.vip:
    st.markdown("""
        <div class="full-screen-login-card" style="text-align: center;">
            <div class="status-badge-secure">🔒 SECURE ENCRYPTION ACTIVE</div>
            <h1 style='color: #ffffff; font-weight: 800; font-size: 36px; margin: 0 0 10px 0;'>VIP PORTAL</h1>
            <p style='color: #94a3b8; font-size: 15px;'>Sistemul necesită autorizare oficială pentru deblocarea datelor.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="User de acces...", key="lux_user_final")
        parola = st.text_input("PAROLĂ SECURIZATĂ", placeholder="••••••••", type="password", key="lux_pass_final")
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE ⚡", key="btn_lux_submit_final"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False
                if utilizator == "admin":
                    st.session_state.admin = True
                st.success("Acces Permis!")
                st.rerun()
            else:
                st.error("Date invalide!")
        if c_b2.button("ÎNAPOI ↩️", key="btn_lux_back_final"):
            st.session_state.ecran_login = False
            st.rerun()

else:
    if st.session_state.admin:
        st.markdown("<h2 style='color: #00ff66; font-weight: 800;'>🛠 PANOU ADMINISTRATOR</h2>", unsafe_allow_html=True)
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            nume = st.text_input("Nume Utilizator nou:", key="add_user_input")
            passw = st.text_input("Parolă nouă:", type="password", key="add_pass_input")
            if st.button("ACORDĂ PRIVILEGII VIP 💎", key="btn_add_member"):
                if nume and passw:
                    st.session_state.lista_membri[nume] = passw
                    st.success("Membru activat!")
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col_adm2:
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            for user_nume in list(st.session_state.lista_membri.keys()):
                c_u, c_b = st.columns([2.5, 1.5])
                c_u.write(f"👤 Cont: {user_nume}")
                if user_nume != "admin" and c_b.button("Șterge ❌", key=f"del_{user_nume}"):
                    del st.session_state.lista_membri[user_nume]
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        st.write("---")

    col_stinga, col_abonamente = st.columns([1.9, 1.1])

    with col_stinga:
        st.markdown('<h3 style="color: #00ff66; font-weight:800; margin-bottom:15px;">📊 SCORURI LIVE & VIDEOCLIPURI SCOREBAT</h3>', unsafe_allow_html=True)
        st.components.v1.html(
            """
            <div style="border: 2px solid rgba(0, 255, 102, 0.3); border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.8); background: #111;">
                <iframe src="https://scorebat.com" style="width: 100%; height: 750px; border: none; background: #111;" allow="autoplay; fullscreen" loading="lazy"></iframe>
            </div>
            """,
            height=770,
            scrolling=False
        )

    with col_abonamente:
        if not st.session_state.vip:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            if st.button("🔐 DEBLOCHEAZĂ PORTAL VIP", key="btn_portal_master_unic"):
                st.session_state.ecran_login = True
                st.rerun()
        else:
            st.markdown(f"""
                <div class="vip-card-box border-low" style="text-align: center; border-color: #00ff66 !important; margin-top:25px;">
                    <h4 style="color:#00ff66; margin:0; font-weight:800;">🟢 CONEXIUNE VALIDĂ</h4>
                    <p style="color:#ffffff; margin:8px 0 0 0; font-size:16px;">Sesiune complet autorizată</p>
                </div>
            """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #475569; font-size: 14px; font-weight:600;'>&copy; 2026 PariuriGO World Live Center. Toate drepturile rezervate. Pariază responsabil.</p>", unsafe_allow_html=True)
