import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • VIP App",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru transformarea imaginii din folder în fundal web
def aplica_fundal_teren_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        # Injectăm stilul CSS curat, fără f-string-uri care să blocheze acoladele
        st.markdown("""
        <style>
            @import url('https://googleapis.com');
            
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.90), rgba(6, 4, 15, 0.94)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
                color: #ffffff !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }
            
            h1, h2, h3, h4, p, span, label {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }

            /* TELEFONUL MOBIL CENTRAT MAT PREPARAT PENTRU LOGIN */
            .phone-wrapper-container {
                max-width: 410px;
                margin: 30px auto;
                background: rgba(13, 11, 22, 0.85) !important;
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                border: 1px solid rgba(176, 66, 255, 0.18);
                border-radius: 42px;
                padding: 24px;
                box-shadow: 0 35px 80px -15px rgba(157, 0, 255, 0.3);
                position: relative;
                min-height: 735px;
            }
            
            .phone-notch {
                width: 115px;
                height: 24px;
                background: #000000;
                margin: -12px auto 25px auto;
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.03);
            }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

# Executăm injectarea fundalului cu terenul tău local
aplica_fundal_teren_local("teren.jpg")

# SENSUL APLICAȚIEI PE ECRAN
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#b042ff; font-weight:800; font-size:16px; margin-top:220px; letter-spacing:0.5px;'>⚽ STADIONUL ESTE LIVE</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:-5px;'>Eroarea de sintaxă a fost eliminată complet.</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Închide corect containerul telefonului
