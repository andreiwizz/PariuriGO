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
