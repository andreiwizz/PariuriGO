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
# 3. STILIZARE CSS PREMIUM COMPLETĂ (INTEGRATĂ FĂRĂ ERORI DE INDENTARE)
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
    
    /* Fix premium pentru butoanele de control din aplicație */
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
    
    .vip-card-box {{
        background: linear-gradient(135deg, rgba(6, 20, 13, 0.75) 0%, rgba(3, 10, 6, 0.9) 100%) !important;
        backdrop-filter: blur(16px) !important;
        border-radius: 18px !important;
        padding: 26px !important;
        margin-bottom: 25px !important;
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
        left: 0; right: 0; height: 4px;
        background: linear-gradient(90deg, transparent, #00ff66, transparent);
        box-shadow: 0 0 20px #00ff66, 0 0 40px #00ff66;
        animation: cyberScan 3.5s infinite linear;
    }}

    .admin-box {{
        background: linear-gradient(145deg, rgba(8, 28, 16, 0.6) 0%, rgba(4, 14, 8, 0.8) 100%) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        margin-bottom: 25px;
    }}

    /* DESIGN LUX CASETE PREȚURI */
    .pricing-card-lux {{
        background: linear-gradient(135deg, rgba(6, 24, 14, 0.85) 0%, rgba(2, 10, 5, 0.95) 100%) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin-top: 20px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    
    .pricing-border-low {{ border: 1px solid rgba(0, 255, 102, 0.3) !important; box-shadow: 0 15px 35px rgba(0, 255, 102, 0.05) !important; }}
    .pricing-border-medium {{ border: 1px solid rgba(255, 204, 0, 0.3) !important; box-shadow: 0 15px 35px rgba(255, 204, 0, 0.05) !important; }}
    .pricing-border-high {{ border: 1px solid rgba(255, 0, 85, 0.4) !important; box-shadow: 0 15px 35px rgba(255, 0, 85, 0.08) !important; }}

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
        text-align: center !important;# ==============================================================================
# ==============================================================================
# 4. INITIALIZARE STĂRI SECURIZATE ȘI LIVE DATA
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
# 5. LOGICĂ RENDERING INTERFAȚĂ DINAMICĂ
# ==============================================================================
if st.session_state.ecran_login and not st.session_state.vip:
    st.markdown("""
        <div class="full-screen-login-card" style="text-align: center;">
            <div style="background:rgba(0,255,102,0.1); border:1px solid #00ff66; color:#00ff66; font-size:12px; font-weight:800; padding:6px 16px; border-radius:30px; display:inline-block; margin-bottom:20px;">[SECURE PORTAL ACTIVE]</div>
            <h1 style='color: #ffffff; font-weight: 800; font-size: 36px; margin: 0 0 10px 0;'>VIP PORTAL</h1>
            <p style='color: #94a3b8; font-size: 15px;'>Sistemul necesita autorizare oficiala pentru deblocarea datelor.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="User de acces...", key="lux_user_v7")
        parola = st.text_input("PAROLA SECURIZATA", placeholder="••••••••", type="password", key="lux_pass_v7")
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE", key="btn_lux_submit_v7"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False
                if utilizator == "admin":
                    st.session_state.admin = True
                st.success("Acces Permis!")
                st.rerun()
            else:
                st.error("Date invalide!")
        if c_b2.button("INAPOI", key="btn_lux_back_v7"):
            st.session_state.ecran_login = False
            st.rerun()

else:
    if st.session_state.admin:
        st.markdown("<h2 style='color: #00ff66; font-weight: 800;'>PANOU ADMINISTRATOR</h2>", unsafe_allow_html=True)
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
                c_u.write(f"Cont: {user_nume}")
                if user_nume != "admin" and c_b.button("Sterge", key=f"del_{user_nume}"):
                    del st.session_state.lista_membri[user_nume]
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        st.write("---")

    col_stinga, col_abonamente = st.columns([1.9, 1.1])

    with col_stinga:
        st.markdown('<h3 style="color: #00ff66; font-weight:800; margin-bottom:15px;">SCORURI LIVE & VIDEOCLIPURI SCOREBAT</h3>', unsafe_allow_html=True)
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
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            
            pachet_selectat = st.selectbox(
                "ABONAMENTE VIP DISPONIBILE:",
                ["PACHET LOW", "PACHET MEDIUM", "HIGH VIP ELITE"],
                key="selector_preturi_v7"
            )
            
            link_stripe = "https://stripe.com"

            if pachet_selectat == "PACHET LOW":
                st.markdown(f"""
                <div class="pricing-card-lux pricing-border-low">
                    <h4 style="color:#00ff66; margin:0; font-weight:800;">PACHET LOW</h4>
                    <h2 style="margin:10px 0 20px 0; font-size:32px; color:#ffffff;">40 RON <span style="font-size:14px; color:#94a3b8; font-weight:600;">/ luna</span></h2>
                    <p style="margin:8px 0; color:#cbd5e1;">3 Bilete complet analizate pe saptamana</p>
                    <p style="margin:8px 0; color:#cbd5e1;">Selectie exclusiva din ligile mari europene</p>
                    <a class="stripe-luxury-btn stripe-low-med" href="{link_stripe}" target="_blank">CUMPARA ACCES LOW</a>
                </div>
                """, unsafe_allow_html=True)

            elif pachet_selectat == "PACHET MEDIUM":
                st.markdown(f"""
                <div class="pricing-card-lux pricing-border-medium">
                    <h4 style="color:#ffcc00; margin:0; font-weight:800;">PACHET MEDIUM</h4>
                    <h2 style="margin:10px 0 20px 0; font-size:32px; color:#ffffff;">70 RON <span style="font-size:14px; color:#94a3b8; font-weight:600;">/ luna</span></h2>
                    <p style="margin:8px 0; color:#cbd5e1;">1 Bilet Premium in fiecare zi calendaristica</p>
                    <p style="margin:8px 0; color:#cbd5e1;">Algoritm avansat pentru probabilitati live</p>
                    <a class="stripe-luxury-btn stripe-low-med" href="{link_stripe}" target="_blank">CUMPARA ACCES MEDIUM</a>
                </div>
                """, unsafe_allow_html=True)

            elif pachet_selectat == "HIGH VIP ELITE":
                st.markdown(f"""
                <div class="pricing-card-lux pricing-border-high">
                    <h4 style="color:#ff0055; margin:0; font-weight:800;">HIGH VIP ELITE</h4>
                    <h2 style="margin:10px 0 20px 0; font-size:32px; color:#ffffff;">120 RON <span style="font-size:14px; color:#94a3b8; font-weight:600;">/ luna</span></h2>
                    <p style="margin:8px 0; color:#cbd5e1;">Cota 2 VIP zilnica + Proiect Dublare</p>
                    <p style="margin:8px 0; color:#cbd5e1;">Monitorizare live non-stop pe sisteme</p>
                    <a class="stripe-luxury-btn stripe-high" href="{link_stripe}" target="_blank">DEBLOCHEAZA ACCES HIGH</a>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<div style='margin-top: 25px; text-align:center;'>", unsafe_allow_html=True)
            if st.button("ACCESEAZA CONT DETINUT", key="btn_trigger_final_v7"):
                st.session_state.ecran_login = True
                st.rerun()
        else:
            st.markdown(f"""
                <div class="vip-card-box" style="text-align: center; border: 1px solid #00ff66 !important; margin-top:25px;">
                    <h4 style="color:#00ff66; margin:0; font-weight:800;">CONEXIUNE SECURIZATA</h4>
                    <p style="color:#ffffff; margin:8px 0 0 0; font-size:16px;">Sesiune complet autorizata in sistem</p>
                </div>
            """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #475569; font-size: 14px; font-weight:600;'>&copy; 2026 PariuriGO World Live Center. Toate drepturile rezervate. Pariază responsabil.</p>", unsafe_allow_html=True)
