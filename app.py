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
# INITIALIZARE STATE SECURIZAT ȘI MEMBRI
# ==============================================================================
if "lista_membri" not in st.session_state:
    st.session_state.lista_membri = {"admin": "pariurigo"}

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

# ==============================================================================
# SIDEBAR LOGIN ACCES
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #00ff66; margin-top:0;'>🔐 LOGIN ACCES</h2>", unsafe_allow_html=True)
    utilizator = st.text_input("Utilizator", key="login_user")
    parola = st.text_input("Parolă", type="password", key="login_pass")

    if st.button("Conectare"):
        if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
            st.session_state.vip = True
            if utilizator == "admin":
                st.session_state.admin = True
            st.success("Conectat cu succes!")
            st.rerun()
        else:
            st.error("Date de identificare incorecte!")

# ==============================================================================
# PANOU ADMINISTRATOR (Apare doar pentru userul 'admin')
# ==============================================================================
if st.session_state.admin:
    st.write("---")
    st.markdown("<h2 style='color: #00ff66; font-weight: 800;'>🛠 PANOU ADMINISTRATOR</h2>", unsafe_allow_html=True)
    
    col_adm1, col_adm2 = st.columns(2)
    
    with col_adm1:
        st.markdown('<div class="admin-box">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #ffffff; margin-top:0;'>➕ Înregistrare Membru Nou</h4>", unsafe_allow_html=True)
        nume = st.text_input("Utilizator nou:", key="add_user_input")
        passw = st.text_input("Parolă nouă:", type="password", key="add_pass_input")
        if st.button("Salvează în bază", key="btn_add_member"):
            if nume and passw:
                st.session_state.lista_membri[nume] = passw
                st.success(f"✔️ Membrul '{nume}' a fost adăugat!")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
                
    with col_adm2:
        st.markdown('<div class="admin-box">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #ffffff; margin-top:0;'>👥 Listă Membri Activi</h4>", unsafe_allow_html=True)
        for user_nume in list(st.session_state.lista_membri.keys()):
            c_u, c_b = st.columns()
            c_u.markdown(f"<p style='margin: 10px 0; color:#cbd5e1;'>👤 <b>{user_nume}</b></p>", unsafe_allow_html=True)
            if user_nume != "admin":
                if c_b.button("Șterge", key=f"del_{user_nume}"):
                    del st.session_state.lista_membri[user_nume]
                    st.success("Eliminat!")
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.write("---")

