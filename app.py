import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • VIP App",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție de securitate pentru citirea și injectarea imaginii locale cu terenul
def incarca_fundal_teren_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

teren_base64 = incarca_fundal_teren_local("teren.jpg")

# 2. MOTORUL GRAFIC - STILUL VIZUAL PENTRU TERENUL DE FUNDAL ȘI GHIDUL DE IPHONE
if teren_base64:
    st.markdown(f"""
    <style>
        @import url('https://googleapis.com');
        
        /* Injectăm terenul tău local pe fundal cu overlay întunecat pentru contrast maxim */
        .stApp {{
            background: linear-gradient(rgba(4, 3, 8, 0.90), rgba(6, 4, 15, 0.94)), 
                        url("data:image/jpeg;base64,{teren_base64}") !important;
            background-size: cover !important;
            background-position: center center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
            color: #ffffff !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        h1, h2, h3, h4, p, span, label {{
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* TELEFONUL MOBIL CENTRAT - EFECT DE STICLĂ TRIDIMENSIONALĂ */
        .phone-wrapper-container {{
            max-width: 410px;
            margin: 30px auto;
            background: rgba(13, 11, 22, 0.82) !important;
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 1px solid rgba(176, 66, 255, 0.18);
            border-radius: 42px;
            padding: 24px;
            box-shadow: 0 35px 80px -15px rgba(157, 0, 255, 0.3);
            position: relative;
            min-height: 735px;
        }
        
        /* Dynamic Island / Notch pe mijlocul ecranului */
        .phone-notch {{
            width: 115px;
            height: 24px;
            background: #000000;
            margin: -12px auto 25px auto;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }
    </style>
    """, unsafe_allow_html=True)
else:
    # Soluție de rezervă (Fallback) în caz că imaginea lipsește din folder
    st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #040308 !important; color: #ffffff !important; font-family: 'Plus Jakarta Sans', sans-serif !important; }
        .phone-wrapper-container { max-width: 410px; margin: 30px auto; background: #0d0b16 !important; border: 1px solid rgba(176,66,255,0.2); border-radius: 42px; padding: 24px; min-height: 735px; position: relative; }
        .phone-notch { width: 115px; height: 24px; background: #000000; margin: -12px auto 25px auto; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# SENSUL APLICAȚIEI PE ECRAN
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#b042ff; font-weight:800; font-size:16px; margin-top:220px; letter-spacing:0.5px;'>⚽ STADIONUL DE FUNDAL ESTE LIVE</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:-5px;'>Terenul se randează corect în spatele iPhone-ului mat.</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Închide corect containerul telefonului
