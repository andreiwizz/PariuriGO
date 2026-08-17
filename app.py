import streamlit as st
import base64
from datetime import datetime

# ==============================================================================
# 1. CONFIGURARE INTERFAȚĂ ȘI DATA CURENTĂ (MANDATORIU PRIMA LINIE)
# ==============================================================================
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# ==============================================================================
# 2. CITIRE ȘI DECORARE FOND PREMIUM (TEREN.JPG)
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
    
    h1, h2, h3, h4, p, span, label, th, td {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Fix premium pentru butoanele de control din aplicatie */
    div.stButton > button {{
        background: linear-gradient(135deg, rgba(0, 255, 102, 0.15) 0%, rgba(0, 92, 32, 0.05) 100%) !important;
        color: #00ff66 !important;
        border: 1px solid #00ff66 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        border-radius: 12px !important;
        padding: 16px 30px !important;
        width: 100% !important;
        display: block !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 4px 15px rgba(0, 255, 102, 0.1) !important;
    }}

    div.stButton > button:hover {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(0, 255, 102, 0.6) !important;
        transform: translateY(-3px);
    }}
    
    div.stButton > button div {{
        font-size: 15px !important;
    }}
    
    .pricing-card-lux {{
        background: linear-gradient(135deg, rgba(6, 24, 14, 0.85) 0%, rgba(2, 10, 5, 0.95) 100%) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin-top: 10px;
    }}
    
    .pricing-border-low {{ border: 1px solid rgba(0, 255, 102, 0.3) !important; }}
    .pricing-border-medium {{ border: 1px solid rgba(255, 204, 0, 0.3) !important; }}
    .pricing-border-high {{ border: 1px solid rgba(255, 0, 85, 0.4) !important; }}

    .stripe-luxury-btn {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 20px !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        text-decoration: none !important;
        margin-top: 25px;
    }}
    
    .stripe-low-med {{ background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important; color: #000000 !important; }}
    .stripe-high {{ background: linear-gradient(135deg, #ff0055 0%, #b3003b 100%) !important; color: #ffffff !important; }}

    .stTextInput input {{
        background: rgba(0, 0, 0, 0.6) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 14px !important;
    }}

    .full-screen-login-card {{
        background: linear-gradient(135deg, rgba(6, 26, 14, 0.95) 0%, rgba(2, 12, 6, 0.99) 100%) !important;
        backdrop-filter: blur(25px) !important;
        border: 2px solid rgba(0, 255, 102, 0.4) !important;
        border-radius: 24px !important;
        padding: 45px !important;
        max-width: 500px;
        margin: 40px auto !important;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9) !important;
    }}

    @keyframes neonDanger {{
        0% {{ box-shadow: 0 0 10px rgba(255, 0, 85, 0.2); border-color: rgba(255, 0, 85, 0.4); }}
        50% {{ box-shadow: 0 0 25px rgba(255, 0, 85, 0.8); border-color: #ff0055; transform: scale(1.01); }}
        100% {{ box-shadow: 0 0 10px rgba(255, 0, 85, 0.2); border-color: rgba(255, 0, 85, 0.4); }}
    }}

    .flame-card-active {{
        background: linear-gradient(135deg, rgba(20, 4, 10, 0.9) 0%, rgba(5, 1, 2, 0.98) 100%) !important;
        border-radius: 20px !important;
        padding: 25px !important;
        margin-top: 20px;
        animation: neonDanger 2s infinite ease-in-out;
    }}

    @keyframes textGlow {{
        0% {{ opacity: 0.8; text-shadow: 0 0 5px #ff0055; }}
        50% {{ opacity: 1; text-shadow: 0 0 20px #ff0055, 0 0 30px #ff0055; }}
        100% {{ opacity: 0.8; text-shadow: 0 0 5px #ff0055; }}
    }}

    .live-alert-text {{
        color: #ff0055;
        font-weight: 800;
        font-size: 14px;
        letter-spacing: 2px;
        text-transform: uppercase;
        animation: textGlow 1.5s infinite ease-in-out;
    }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")
# ==============================================================================
# 4. INITIALIZARE MEMORIE ȘI CONTROL AUTOMAT CALENDAR
# ==============================================================================
if "lista_membri" not in st.session_state:
    st.session_state.lista_membri = {"admin": "pariurigo"}

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

if "ecran_login" not in st.session_state:
    st.session_state.ecran_login = False

# Generator dinamic bazat pe algoritm de dată
def genereaza_meciuri_dupa_data(data_string):
    zi_num = sum(ord(c) for c in data_string)
    elite_gazde = ["Real Madrid", "Barcelona", "Manchester Utd", "FCSB", "Bayern Munchen", "Inter Milano", "Liverpool", "Juventus"]
    elite_oaspeti = ["Man City", "Arsenal", "Rapid Bucuresti", "Chelsea", "Dortmund", "AC Milan", "Atletico Madrid", "PSG"]
    
    meciuri_generate = []
    for i in range(4):
        index_gz = (zi_num + i * 2) % len(elite_gazde)
        index_os = (zi_num + i * 3) % len(elite_oaspeti)
        if elite_gazde[index_gz] == elite_oaspeti[index_os]:
            index_os = (index_os + 1) % len(elite_oaspeti)
        meciuri_generate.append(elite_gazde[index_gz] + " vs " + elite_oaspeti[index_os])
    return meciuri_generate

partide_reale_zi = genereaza_meciuri_dupa_data(data_azi)
meciuri_analiza_zi = {}
seed_zi = sum(ord(c) for c in data_azi)

for i, partida in enumerate(partide_reale_zi):
    hash_meci = sum(ord(c) for c in partida) + seed_zi
    g_gz = str((hash_meci + i * 3) % 6 + 12)
    g_os = str((hash_meci + i * 5) % 6 + 10)
    med_gz = f"{round(1.8 + (hash_meci % 5) / 10, 1)}"
    meciuri_analiza_zi[partida] = {
        "liga": "Meciuri Oficiale Zi Curenta", "g_gz": g_gz, "g_os": g_os, "med_gz": med_gz, "med_os": f"{round(1.3 + (i % 4) / 10, 1)}", 
        "gp_gz": str((hash_meci) % 4 + 4), "gp_os": str((hash_meci + i) % 4 + 5),
        "ht_gz": f"{65 + (hash_meci % 15)}%", "st_gz": f"{70 + (i * 3) % 15}%", 
        "p15_gz": f"{82 + (hash_meci % 10)}%", "p25_gz": f"{55 + (i * 5) % 20}%", "gg_gz": f"{52 + (hash_meci % 25)}%",
        "w_p15": f"{82 + (hash_meci % 10)}%", "w_p25": f"{55 + (i * 5) % 20}%", 
        "w_p05r1": f"{65 + (hash_meci % 15)}%", "w_gg": f"{52 + (hash_meci % 25)}%"
    }
# ==============================================================================
# 5. CONTROL RENDERARE INTERFAȚĂ DINAMICĂ (LOGIN VS PLATFORMĂ)
# ==============================================================================
if st.session_state.ecran_login and not st.session_state.vip:
    st.markdown('<div class="full-screen-login-card" style="text-align: center;"><div style="background:rgba(0,255,102,0.1); border:1px solid #00ff66; color:#00ff66; font-size:12px; font-weight:800; padding:6px 16px; border-radius:30px; display:inline-block; margin-bottom:20px;">[SECURE PORTAL ACTIVE]</div><h1 style="color: #ffffff; font-weight: 800; font-size: 36px; margin: 0 0 10px 0;">VIP PORTAL</h1><p style="color: #94a3b8; font-size: 15px;">Sistemul necesita autorizare oficiala pentru deblocarea datelor.</p></div>', unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="User de acces...", key="lux_user_final_matrix")
        parola = st.text_input("PAROLA SECURIZATA", placeholder="••••••••", type="password", key="lux_pass_final_matrix")
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE", key="btn_lux_submit_final_matrix"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False
                if utilizator == "admin":
                    st.session_state.admin = True
                st.success("Acces Permis!")
                st.rerun()
            else:
                st.error("Date invalide!")
        if c_b2.button("INAPOI", key="btn_lux_back_final_matrix"):
            st.session_state.ecran_login = False
            st.rerun()

else:
    if st.session_state.admin:
        st.markdown("<h3>🛠 PANOU ADMINISTRATOR</h3>", unsafe_allow_html=True)
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            nume = st.text_input("Nume Utilizator nou:", key="add_user_input")
            passw = st.text_input("Parola noua:", type="password", key="add_pass_input")
            if st.button("ACORDA PRIVILEGII VIP", key="btn_add_member"):
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
                if user_nume != "admin" and c_b.button("Sterge", key=f"del_{user_nume}"):
                    del st.session_state.lista_membri[user_nume]
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        st.write("---")
