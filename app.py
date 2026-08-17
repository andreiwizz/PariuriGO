import streamlit as st
import base64
from datetime import datetime

# ==============================================================================
# 1. CONFIGURARE INTERFAȚĂ ȘI DATA CURENTĂ
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
# 3. STILIZARE CSS PREMIUM (HOLOGRAPHIC LUX)
# ==============================================================================
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

    div.stButton > button {{
        background: linear-gradient(135deg, rgba(0, 255, 102, 0.15) 0%, rgba(0, 92, 32, 0.05) 100%) !important;
        color: #00ff66 !important;
        border: 1px solid #00ff66 !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        padding: 14px 20px !important;
        width: 100% !important;
    }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")
# ==============================================================================
# 4. INITIALIZARE MEMORIE ȘI SESIUNI CONTURI
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
# 5. CONTROL RENDERARE PAGINI (LOGIN SAU PLATFORMĂ PRINCIPALĂ)
# ==============================================================================
if st.session_state.ecran_login and not st.session_state.vip:
    st.markdown("<h2 style='text-align:center; color:#00ff66;'>🔐 VIP ACCES SECURIZAT</h2>", unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="Introdu user-ul...", key="user_field_final")
        parola = st.text_input("PAROLĂ SECURIZATĂ", placeholder="••••••••", type="password", key="pass_field_final")
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE ⚡", key="btn_submit_login"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False
                if utilizator == "admin":
                    st.session_state.admin = True
                st.rerun()
            else:
                st.error("Date invalide!")
                
        if c_b2.button("ÎNAPOI ↩️", key="btn_cancel_login"):
            st.session_state.ecran_login = False
            st.rerun()

else:
    if st.session_state.admin:
        st.markdown("<h3>🛠 PANOU ADMINISTRATOR</h3>", unsafe_allow_html=True)
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            nume = st.text_input("Nume Utilizator nou:", key="add_user_input")
            passw = st.text_input("Parolă nouă:", type="password", key="add_pass_input")
            if st.button("ADĂUGĂ MEMBRU VIP", key="btn_add_member"):
                if nume and passw:
                    st.session_state.lista_membri[nume] = passw
                    st.success("Membru activat!")
                    st.rerun()
        with col_adm2:
            for user_nume in list(st.session_state.lista_membri.keys()):
                c_u, c_b = st.columns([2.5, 1.5])
                c_u.write(f"👤 Cont: {user_nume}")
                if user_nume != "admin" and c_b.button("Șterge", key=f"del_{user_nume}"):
                    del st.session_state.lista_membri[user_nume]
                    st.rerun()
        st.write("---")

    col_stinga, col_abonamente = st.columns([1.9, 1.1])

    with col_stinga:
        st.markdown('<h3 style="color: #00ff66; margin-bottom:15px;">📊 SCORURI ȘI REZUMATE LIVE</h3>', unsafe_allow_html=True)
        st.components.v1.html(
            '<iframe src="https://scorebat.com" style="width:100%; height:750px; border:2px solid rgba(0,255,102,0.3); border-radius:20px; background:#111;" allow="autoplay; fullscreen" loading="lazy"></iframe>',
            height=770,
            scrolling=False
        )

    with col_abonamente:
        if not st.session_state.vip:
            st.markdown('<h3 style="color:#ffffff; margin-bottom:15px;">🏆 ABONAMENTE DISPONIBILE</h3>', unsafe_allow_html=True)
            pachet_selectat = st.selectbox(
                "Alege pachetul dorit:",
                ["PACHET LOW", "PACHET MEDIUM", "HIGH VIP ELITE"],
                key="pachet_dropdown"
            )
            
            link_stripe = "https://stripe.com"

            if pachet_selectat == "PACHET LOW":
                st.markdown(f'<div class="pricing-card-lux pricing-border-low"><h4 style="color:#00ff66; margin:0;">PACHET LOW</h4><h2 style="margin:10px 0 20px 0; font-size:32px;">40 RON <span style="font-size:14px; color:#94a3b8;">/ luna</span></h2><p>✅ 3 Bilete complet analizate pe saptamana</p><p>✅ Selectie exclusiva din ligile mari europene</p><a class="stripe-luxury-btn stripe-low-med" href="{link_stripe}" target="_blank">CUMPARA ACCES LOW 🚀</a></div>', unsafe_allow_html=True)

            elif pachet_selectat == "PACHET MEDIUM":
                st.markdown(f'<div class="pricing-card-lux pricing-border-medium"><h4 style="color:#ffcc00; margin:0;">PACHET MEDIUM</h4><h2 style="margin:10px 0 20px 0; font-size:32px;">70 RON <span style="font-size:14px; color:#94a3b8;">/ luna</span></h2><p>✅ 1 Bilet Premium in fiecare zi calendaristica</p><p>✅ Algoritm avansat pentru probabilitati live</p><a class="stripe-luxury-btn stripe-low-med" href="{link_stripe}" target="_blank">CUMPARA ACCES MEDIUM 🟡</a></div>', unsafe_allow_html=True)

            elif pachet_selectat == "HIGH VIP ELITE":
                st.markdown(f'<div class="pricing-card-lux pricing-border-high"><h4 style="color:#ff0055; margin:0;">HIGH VIP ELITE</h4><h2 style="margin:10px 0 20px 0; font-size:32px;">120 RON <span style="font-size:14px; color:#94a3b8;">/ luna</span></h2><p>✅ Cota 2 VIP zilnica + Proiect Dublare</p><p>✅ Monitorizare live non-stop pe sisteme</p><a class="stripe-luxury-btn stripe-high" href="{link_stripe}" target="_blank">DEBLOCHEAZA ACCES HIGH 🔥</a></div>', unsafe_allow_html=True)

            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            if st.button("🔐 LOGARE PANOU ACCES CLIENT", key="btn_open_login_view"):
                st.session_state.ecran_login = True
                st.rerun()
        else:
            st.markdown('<div class="pricing-card-lux pricing-border-low" style="text-align:center;"><h4 style="color:#00ff66; margin:0;">🟢 CONEXIUNE VALIDĂ</h4><p style="margin-top:10px;">Sesiune complet autorizată în sistem.</p></div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #475569; font-size: 14px;'>&copy; 2026 PariuriGO World Live Center. Toate drepturile rezervate. Pariază responsabil.</p>", unsafe_allow_html=True)
