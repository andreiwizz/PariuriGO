import streamlit as st
import base64

# 1. Configurare Pagină principală (Trebuie să fie obligatoriu prima linie din cod)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Funcție pentru citirea imaginii locale de fundal (teren.jpg)
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")

# 3. Stabilirea stilului de fundal (cu tentă întunecată premium peste imagine)
if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.95), rgba(2, 6, 4, 0.97)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #030a05 !important;"

# 4. Injectarea stilului CSS de bază pentru fundal și fonturi
st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    
    .stApp {{
        {bg_style}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
</style>
""", unsafe_allow_html=True)

# 5. Titlu de test pentru a verifica că totul se încarcă corect
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800;'>⚽ PARIURIGO LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")
# 6. Adăugare stiluri CSS suplimentare pentru casetele VIP și butoane
st.markdown("""
<style>
    h3, h4, h2, p, span, a { font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important; }
    
    /* Caseta Premium cu efect de sticlă (Glassmorphism) */
    .vip-card-box {
        background: linear-gradient(135deg, rgba(6, 20, 13, 0.75) 0%, rgba(3, 10, 6, 0.9) 100%) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border-radius: 18px !important;
        padding: 26px !important;
        margin-bottom: 25px !important;
        transition: all 0.4s ease;
    }
    
    /* Borduri și umbre neon dedicate pentru fiecare pachet în funcție de selectie */
    .border-low { border: 1px solid rgba(0, 255, 102, 0.25) !important; box-shadow: 0 10px 30px rgba(0, 255, 102, 0.03) !important; }
    .border-medium { border: 1px solid rgba(255, 204, 0, 0.25) !important; box-shadow: 0 10px 30px rgba(255, 204, 0, 0.03) !important; }
    .border-high { border: 1px solid rgba(255, 0, 85, 0.35) !important; box-shadow: 0 12px 35px rgba(255, 0, 85, 0.06) !important; }

    /* Butoane premium animate */
    .stripe-btn {
        font-weight: 800 !important;
        font-size: 15px !important;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 20px !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        text-decoration: none !important;
        margin-top: 20px;
        transition: all 0.3s ease !important;
    }
    .btn-green { background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important; color: #000000 !important; box-shadow: 0 4px 20px rgba(0, 255, 102, 0.3) !important; }
    .btn-red { background: linear-gradient(135deg, #ff0055 0%, #b3003b 100%) !important; color: #ffffff !important; box-shadow: 0 4px 25px rgba(255, 0, 85, 0.4) !important; }
</style>
""", unsafe_allow_html=True)

# 7. Crearea structurii pe coloane (Stânga rămâne liberă momentan)
col_stinga, col_abonamente = st.columns([1.8, 1.2])

with col_abonamente:
    st.markdown('<h3 style="color: #ffffff; font-weight:800; margin-bottom:15px;">🏆 SELECȚIE ACCES VIP</h3>', unsafe_allow_html=True)
    
    # Selectorul interactiv
    pachet_ales = st.selectbox(
        "Alege tipul de abonament:",
        ["🟢 PACHET LOW", "🟡 PACHET MEDIUM", "🔥 HIGH VIP ELITE"],
        key="selector_pachet_vip"
    )
    
    link_stripe = "https://stripe.com" # Modifică cu link-ul tău real când vrei

    # Randare dinamică în funcție de ce pachet este ales în meniu
    if pachet_ales == "🟢 PACHET LOW":
        st.markdown(f"""
        <div class="vip-card-box border-low">
            <h4 style="color:#00ff66; margin:0 0 5px 0;">🟢 PACHET LOW</h4>
            <h2 style="margin:0 0 15px 0; font-size:28px;">40 RON <span style="font-size:14px; color:#94a3b8;">/ lună</span></h2>
            <p style="margin:6px 0;">✅ 3 Bilete complet analizate pe săptămână</p>
            <p style="margin:6px 0;">✅ Selecție exclusivă din ligile mari europene</p>
            <a class="stripe-btn btn-green" href="{link_stripe}" target="_blank">CUMPĂRĂ ACCES LOW 🚀</a>
        </div>
        """, unsafe_allow_html=True)

    elif pachet_ales == "🟡 PACHET MEDIUM":
        st.markdown(f"""
        <div class="vip-card-box border-medium">
            <h4 style="color:#ffcc00; margin:0 0 5px 0;">🟡 PACHET MEDIUM</h4>
            <h2 style="margin:0 0 15px 0; font-size:28px;">70 RON <span style="font-size:14px; color:#94a3b8;">/ lună</span></h2>
            <p style="margin:6px 0;">✅ 1 Bilet Premium în fiecare zi calendaristică</p>
            <p style="margin:6px 0;">✅ Algoritm avansat pentru probabilități live</p>
            <a class="stripe-btn btn-green" href="{link_stripe}" target="_blank">CUMPĂRĂ ACCES MEDIUM 🟡</a>
        </div>
        """, unsafe_allow_html=True)

    elif pachet_ales == "🔥 HIGH VIP ELITE":
        st.markdown(f"""
        <div class="vip-card-box border-high">
            <h4 style="color:#ff0055; margin:0 0 5px 0;">🔥 HIGH VIP ELITE</h4>
            <h2 style="margin:0 0 15px 0; font-size:28px;">120 RON <span style="font-size:14px; color:#94a3b8;">/ lună</span></h2>
            <p style="margin:6px 0;">✅ Cota 2 VIP zilnică + Proiect dedicat Dublare</p>
            <p style="margin:6px 0;">✅ Monitorizare live non-stop pe toate sistemele</p>
            <a class="stripe-btn btn-red" href="{link_stripe}" target="_blank">DEBLOCHEAZĂ ACCES HIGH 🔥</a>
        </div>
        """, unsafe_allow_html=True)
# ==============================================================================
# INITIALIZARE STĂRI SECURIZATE (DE LA LINIA 134)
# ==============================================================================
if "lista_membri" not in st.session_state:
    st.session_state.lista_membri = {"admin": "pariurigo"}

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

# Stare nouă pentru a controla dacă utilizatorul se află în ecranul de login full-screen
if "ecran_login" not in st.session_state:
    st.session_state.ecran_login = False

# Injectare stiluri CSS exclusive pentru ecranul de Login Full-Screen de înaltă clasă
st.markdown("""
<style>
    @keyframes cyberScan {
        0% { top: 0%; opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { top: 100%; opacity: 0; }
    }

    /* Caseta centrală mare pentru logarea Full Screen */
    .full-screen-login-card {
        position: relative;
        background: linear-gradient(135deg, rgba(6, 26, 14, 0.9) 0%, rgba(2, 12, 6, 0.98) 100%) !important;
        backdrop-filter: blur(25px) !important;
        -webkit-backdrop-filter: blur(25px) !important;
        border: 2px solid rgba(0, 255, 102, 0.4) !important;
        border-radius: 24px !important;
        padding: 45px !important;
        max-width: 500px;
        margin: 60px auto !important;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(0, 255, 102, 0.1) !important;
        overflow: hidden;
    }

    .full-screen-login-card::after {
        content: '';
        position: absolute;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, transparent, #00ff66, transparent);
        box-shadow: 0 0 20px #00ff66, 0 0 40px #00ff66;
        animation: cyberScan 3.5s infinite linear;
    }

    .status-badge-secure {
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
        text-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# LOGICĂ RENDERARE DINAMICĂ (ECRAN LOGIN SAU PLATFORMĂ)
# ==============================================================================

# SITUAȚIA A: Utilizatorul a cerut login-ul și NU este încă conectat (Ascunde tot ecranul)
if st.session_state.ecran_login and not st.session_state.vip:
    
    st.markdown("""
        <div class="full-screen-login-card" style="text-align: center;">
            <div class="status-badge-secure">🔒 SECURE ENCRYPTION ACTIVE</div>
            <h1 style='color: #ffffff; font-weight: 800; font-size: 36px; margin: 0 0 10px 0; letter-spacing:1px;'>VIP PORTAL</h1>
            <p style='color: #94a3b8; font-size: 15px; font-weight: 600; margin-bottom: 30px;'>Sistemul necesită autorizare oficială pentru a debloca datele live</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Inputuri centrate și aerisite pe mijlocul ecranului golit
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="Introdu user-ul...", key="lux_user")
        parola = st.text_input("PAROLĂ SECURIZATĂ", placeholder="••••••••", type="password", key="lux_pass")
        
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE ⚡", key="btn_lux_submit"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False # Închide ecranul de login
                if utilizator == "admin":
                    st.session_state.admin = True
                st.success("Acces granted!")
                st.rerun()
            else:
                st.error("Date invalide!")
                
        if c_b2.button("ÎNAPOI ↩️", key="btn_lux_back"):
            st.session_state.ecran_login = False
            st.rerun()

# SITUAȚIA B: Interfața principală normală (Apare când NU te loghezi sau ești deja Logat)
else:
    # Dacă utilizatorul NU este logat, îi punem butonul superb de login în bara de abonamente
    with col_abonamente:
        if not st.session_state.vip:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            if st.button("🔐 DEBLOCHEAZĂ PORTAL VIP", key="btn_trigger_fullscreen"):
                st.session_state.ecran_login = True
                st.rerun()
        else:
            # Dacă este deja logat, îi afișăm un status de lux în locul butonului de login
            st.markdown(f"""
                <div class="vip-card-box border-low" style="text-align: center; border-color: #00ff66 !important;">
                    <h4 style="color:#00ff66; margin:0; font-weight:800;">🟢 CONEXIUNE VALIDĂ</h4>
                    <p style="color:#ffffff; margin:8px 0 0 0; font-size:16px;">Sesiune activă: <b>{st.session_state.get('login_user', 'Membru')}</b></p>
                </div>
            """, unsafe_allow_html=True)

    # PANOU ADMINISTRATOR MATRIX EXECUTIVE (Apare în aplicație doar pentru admin după logare)
    if st.session_state.admin:
        st.write("---")
        st.markdown("<h2 style='color: #00ff66; font-weight: 800; letter-spacing: 1px;'>🛠 CORE PLATFORM ADMINISTRATION</h2>", unsafe_allow_html=True)
        
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            st.markdown("<h4 style='color: #ffffff; margin-top:0; font-weight:800; border-bottom: 1px solid rgba(0,255,102,0.15); padding-bottom: 8px;'>➕ ÎNREGISTRARE CLIENT NOU</h4>", unsafe_allow_html=True)
            nume = st.text_input("Nume Utilizator:", placeholder="Ex: marian_vip", key="add_user_input")
            passw = st.text_input("Parolă:", placeholder="Parolă cont...", type="password", key="add_pass_input")
            if st.button("ACORDĂ PRIVILEGII VIP 💎", key="btn_add_member"):
                if nume and passw:
                    st.session_state.lista_membri[nume] = passw
                    st.success(f"✔️ Utilizatorul '{nume}' a fost activat!")
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
                    
        with col_adm2:
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            st.markdown("<h4 style='color: #ffffff; margin-top:0; font-weight:800; border-bottom: 1px solid rgba(255,0,85,0.15); padding-bottom: 8px;'>👥 CONTROL ACCES MEMBRI</h4>", unsafe_allow_html=True)
            for user_nume in list(st.session_state.lista_membri.keys()):
                c_u, c_b = st.columns([2.5, 1.5])
                c_u.markdown(f"<p style='margin: 14px 0 0 0; color:#ffffff; font-size:16px;'>👤 Membru: <b style='color:#00ff66;'>{user_nume}</b></p>", unsafe_allow_html=True)
                if user_nume != "admin":
                    if c_b.button("REVOCĂ ACCES ❌", key=f"del_{user_nume}"):
                        del st.session_state.lista_membri[user_nume]
                        st.success("Eliminat!")
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        st.write("---")

    # Păstrează coloanele aliniate curat sub aplicație
    col_stinga, col_abonamente = st.columns([1.8, 1.2])

# ==============================================================================
col_stinga, col_abonamente = st.columns([1.8, 1.2])
# ==============================================================================
# INITIALIZARE STĂRI ȘI MEMBRI (DE LA LINIA 134 V4 - FIX SCOREBAT INTEGRAL)
# ==============================================================================
if "lista_membri" not in st.session_state:
    st.session_state.lista_membri = {"admin": "pariurigo"}

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

if "ecran_login" not in st.session_state:
    st.session_state.ecran_login = False

# Injectare stiluri CSS exclusive (Scanners, Grid și Bare Progres)
st.markdown("""
<style>
    @keyframes cyberScan {
        0% { top: 0%; opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { top: 100%; opacity: 0; }
    }

    .full-screen-login-card {
        position: relative;
        background: linear-gradient(135deg, rgba(6, 26, 14, 0.9) 0%, rgba(2, 12, 6, 0.98) 100%) !important;
        backdrop-filter: blur(25px) !important;
        border: 2px solid rgba(0, 255, 102, 0.4) !important;
        border-radius: 24px !important;
        padding: 45px !important;
        max-width: 500px;
        margin: 60px auto !important;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(0, 255, 102, 0.1) !important;
        overflow: hidden;
    }

    .full-screen-login-card::after {
        content: '';
        position: absolute;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, transparent, #00ff66, transparent);
        box-shadow: 0 0 20px #00ff66, 0 0 40px #00ff66;
        animation: cyberScan 3.5s infinite linear;
    }

    .status-badge-secure {
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
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# LOGICĂ RENDERING INTERFAȚĂ DINAMICĂ
# ==============================================================================
if st.session_state.ecran_login and not st.session_state.vip:
    # A. ECRAN LOGIN FULL-SCREEN
    st.markdown("""
        <div class="full-screen-login-card" style="text-align: center;">
            <div class="status-badge-secure">🔒 SECURE ENCRYPTION ACTIVE</div>
            <h1 style='color: #ffffff; font-weight: 800; font-size: 36px; margin: 0 0 10px 0;'>VIP PORTAL</h1>
            <p style='color: #94a3b8; font-size: 15px;'>Sistemul necesită autorizare oficială pentru deblocarea datelor.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="User de acces...", key="lux_user")
        parola = st.text_input("PAROLĂ SECURIZATĂ", placeholder="••••••••", type="password", key="lux_pass")
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE ⚡", key="btn_lux_submit"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False
                if utilizator == "admin":
                    st.session_state.admin = True
                st.success("Acces Permis!")
                st.rerun()
            else:
                st.error("Date invalide!")
        if c_b2.button("ÎNAPOI ↩️", key="btn_lux_back"):
            st.session_state.ecran_login = False
            st.rerun()

else:
    # B. RENDERING PLATFORMĂ NORMALĂ
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

    # CREARE CONTEXT COLOANE APLICAȚIE (Se rulează curat în bloc liniar)
    col_stinga, col_abonamente = st.columns([1.9, 1.1])

    # RENDERING WIDGET LIVE SCOREBAT REAL-TIME (În coloana din Stânga)
    with col_stinga:
        st.markdown('<h3 style="color: #00ff66; font-weight:800; margin-bottom:15px;">📊 SCORURI LIVE & VIDEOCLIPURI SCOREBAT</h3>', unsafe_allow_html=True)
        
        # Widget-ul oficial ScoreBat API gratuit, complet integrat fără erori de blocare cross-origin
        st.components.v1.html(
            """
            <div style="border: 2px solid rgba(0, 255, 102, 0.3); border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.8); background: #111;">
                <iframe 
                    src="https://scorebat.com" 
                    style="width: 100%; height: 750px; border: none; background: #111;"
                    allow="autoplay; fullscreen"
                    loading="lazy">
                </iframe>
            </div>
            """,
            height=770,
            scrolling=False
        )

    # RENDERING ELEMENTE ÎN COLOANA DIN DREAPTA
    with col_abonamente:
        if not st.session_state.vip:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
              # ==============================================================================
    # RENDERING ELEMENTE IN COLOANA DIN DREAPTA (ALINIAT PERFECT)
    # ==============================================================================
    with col_abonamente:
        if not st.session_state.vip:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            if st.button("🔐 DEBLOCHEAZĂ PORTAL VIP", key="btn_trigger_fullscreen_final"):
                st.session_state.ecran_login = True
                st.rerun()
        else:
            st.markdown(f"""
                <div class="vip-card-box border-low" style="text-align: center; border-color: #00ff66 !important; margin-top:25px;">
                    <h4 style="color:#00ff66; margin:0; font-weight:800;">🟢 CONEXIUNE VALIDĂ</h4>
                    <p style="color:#ffffff; margin:8px 0 0 0; font-size:16px;">Sesiune complet autorizată</p>
                </div>
            """, unsafe_allow_html=True)
