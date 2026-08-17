import streamlit as st
import base64
from datetime import datetime

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE ÎN STREAMLIT)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# 2. Citire imagine de fundal (teren.jpg)
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"background: linear-gradient(rgba(3, 12, 6, 0.94), rgba(1, 5, 2, 0.97)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #020703 !important;"
# 3. Injectare stiluri CSS executive și motorul de animație laser
st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    
    .stApp {{
        {bg_style}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    
    h1, h2, h3, h4, p, span, label {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Inputuri premium text */
    .stTextInput input {{
        background: rgba(0, 0, 0, 0.7) !important;
        border: 1px solid rgba(0, 255, 102, 0.25) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 14px !important;
        font-size: 16px !important;
        font-family: 'Rajdhani', sans-serif !important;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.9) !important;
    }}
    
    .stTextInput input:focus {{
        border-color: #00ff66 !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.3) !important;
    }}

    /* Butoane native mari din viitor */
    div.stButton > button {{
        background: linear-gradient(135deg, rgba(0, 255, 102, 0.12) 0%, rgba(0, 92, 32, 0.04) 100%) !important;
        color: #00ff66 !important;
        border: 1px solid rgba(0, 255, 102, 0.5) !important;
        font-weight: 800 !important;
        font-size: 15px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        border-radius: 12px !important;
        padding: 12px 25px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }}

    div.stButton > button:hover {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 20px rgba(0, 255, 102, 0.4) !important;
        transform: translateY(-2px);
    }}

    /* Caseta login centrală cinematică */
    .full-screen-login-card {{
        position: relative;
        background: linear-gradient(135deg, rgba(4, 22, 11, 0.92) 0%, rgba(1, 10, 5, 0.98) 100%) !important;
        backdrop-filter: blur(20px) !important;
        border: 2px solid rgba(0, 255, 102, 0.35) !important;
        border-radius: 24px !important;
        padding: 40px !important;
        max-width: 480px;
        margin: 50px auto !important;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.9) !important;
        overflow: hidden;
    }}

    @keyframes cyberScan {{
        0% {{ top: 0%; opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ top: 100%; opacity: 0; }}
    }}

    .full-screen-login-card::after {{
        content: '';
        position: absolute;
        left: 0; right: 0; height: 3px;
        background: linear-gradient(90deg, transparent, #00ff66, transparent);
        box-shadow: 0 0 15px #00ff66;
        animation: cyberScan 3.5s infinite linear;
    }}

    .vip-card-box {{
        background: linear-gradient(135deg, rgba(6, 20, 13, 0.8) 0%, rgba(2, 8, 4, 0.95) 100%) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 18px !important;
        padding: 24px !important;
    }}
</style>
""", unsafe_allow_html=True)

# 4. Header vizual (Logo și Titlu)
if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800; text-shadow: 0 0 15px rgba(0,255,102,0.2);'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")
# ==============================================================================
# 5. INITIALIZARE STĂRI SECURIZATE ȘI MEMORIE CONTURI
# ==============================================================================
if "lista_membri" not in st.session_state:
    st.session_state.lista_membri = {"admin": "pariurigo"}

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

if "ecran_login" not in st.session_state:
    st.session_state.ecran_login = False

# ==============================================================================
# 6. MANAGEMENT RENDERARE INTERFAȚĂ (LOGIN FULL-SCREEN VS PLATFORMĂ)
# ==============================================================================

# SITUAȚIA A: Utilizatorul a cerut login-ul (Se ascunde tot și apare doar portalul)
if st.session_state.ecran_login and not st.session_state.vip:
    st.markdown("""
        <div class="full-screen-login-card" style="text-align: center;">
            <div style="background:rgba(0,255,102,0.1); border:1px solid #00ff66; color:#00ff66; font-size:11px; font-weight:800; padding:6px 16px; border-radius:30px; display:inline-block; margin-bottom:20px; letter-spacing:1px;">🔒 SECURE MATRIX ACTIVE</div>
            <h1 style='color: #ffffff; font-weight: 800; font-size: 34px; margin: 0 0 10px 0;'>VIP PORTAL</h1>
            <p style='color: #94a3b8; font-size: 15px; margin-bottom:0;'>Introdu acreditările de acces autorizat.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="Cont utilizator...", key="lux_user_v6")
        parola = st.text_input("PAROLĂ SECURIZATĂ", placeholder="••••••••", type="password", key="lux_pass_v6")
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE ⚡", key="btn_lux_submit_v6"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False
                if utilizator == "admin":
                    st.session_state.admin = True
                st.success("Sistem deblocat!")
                st.rerun()
            else:
                st.error("Date de identificare incorecte!")
                
        if c_b2.button("ÎNAPOI ↩️", key="btn_lux_back_v6"):
            st.session_state.ecran_login = False
            st.rerun()

# SITUAȚIA B: Interfața principală (Apare la pornire sau după logarea cu succes)
else:
    # Crearea layout-ului pe coloane
    col_stinga, col_abonamente = st.columns([1.9, 1.1])

    # Coloana Stângă: Platforma de scoruri și meciuri live ScoreBat
    with col_stinga:
        st.markdown('<h3 style="color: #00ff66; font-weight:800; margin-bottom:15px;">📊 CENTRALIZATOR MECIURI LIVE SCOREBAT</h3>', unsafe_allow_html=True)
        st.components.v1.html(
            """
            <div style="border: 2px solid rgba(0, 255, 102, 0.3); border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.8); background: #111;">
                <iframe src="https://scorebat.com" style="width: 100%; height: 750px; border: none; background: #111;" allow="autoplay; fullscreen" loading="lazy"></iframe>
            </div>
            """,
            height=770,
            scrolling=False
        )

    # Coloana Dreaptă: Control acces și înrolare buton de lux
    with col_abonamente:
        if not st.session_state.vip:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            if st.button("🔐 DEBLOCHEAZĂ PORTAL VIP", key="btn_portal_master_v6"):
                st.session_state.ecran_login = True
                st.rerun()
        else:
            st.markdown(f"""
                <div class="vip-card-box" style="text-align: center; border: 1px solid #00ff66 !important; margin-top:25px;">
                    <h4 style="color:#00ff66; margin:0; font-weight:800;">🟢 CONEXIUNE SECURIZATĂ</h4>
                    <p style="color:#ffffff; margin:8px 0 0 0; font-size:16px;">Datele VIP au fost sincronizate cu succes.</p>
                </div>
            """, unsafe_allow_html=True)

# Subsol global fixat la sfârșitul paginii
st.markdown("<br><p style='text-align: center; color: #475569; font-size: 14px; font-weight:600;'>&copy; 2026 PariuriGO World Live Center. Toate drepturile rezervate. Pariază responsabil.</p>", unsafe_allow_html=True)
    /
