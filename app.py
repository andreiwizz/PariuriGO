import streamlit as st
import base64

# 1. Configurare Pagină principală
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Fundal Premium (Imagine locală sau culoare fallback)
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.95), rgba(2, 6, 4, 0.97)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #030a05 !important;"

# 3. CSS Stiluri Pachete și Layout
st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    .stApp {{ {bg_style} color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; }}
    h3, h4, h2, p, span, a {{ font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important; }}
    
    .vip-card-box {{
        background: linear-gradient(145deg, rgba(12, 34, 22, 0.9), rgba(6, 18, 12, 0.95)) !important;
        border: 1px solid rgba(0, 255, 102, 0.3) !important;
        border-radius: 18px !important;
        padding: 24px !important;
        margin-bottom: 25px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.7) !important;
    }}
    .stripe-btn {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 20px !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        text-decoration: none !important;
        margin-top: 15px;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800;'>⚽ PARIURIGO LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")

# 4. Layout Coloane (Stânga liberă pentru algoritm, Dreapta pentru Pachete)
col_stinga, col_abonamente = st.columns([1.8, 1.2])

with col_abonamente:
    st.markdown('<h3 style="color: #ffffff; font-weight:800; margin-bottom:15px;">🏆 PACHETE ACCES VIP</h3>', unsafe_allow_html=True)
    link_stripe = "https://stripe.com"
    
    # Pachet LOW
    st.markdown(f"""<div class="vip-card-box">
        <h4 style="color:#00ff66; margin:0 0 5px 0;">🟢 PACHET LOW</h4>
        <h2 style="margin:0 0 15px 0; font-size:28px;">40 RON <span style="font-size:14px; color:#94a3b8;">/ lună</span></h2>
        <p style="margin:6px 0;">✅ 3 Bilete complet analizate pe săptămână</p>
        <p style="margin:6px 0;">✅ Selecție exclusivă din ligile mari europene</p>
        <a class="stripe-btn" href="{link_stripe}" target="_blank">CUMPĂRĂ ACCES LOW 🚀</a>
    </div>""", unsafe_allow_html=True)

    # Pachet MEDIUM
    st.markdown(f"""<div class="vip-card-box">
        <h4 style="color:#ffcc00; margin:0 0 5px 0;">🟡 PACHET MEDIUM</h4>
        <h2 style="margin:0 0 15px 0; font-size:28px;">70 RON <span style="font-size:14px; color:#94a3b8;">/ lună</span></h2>
        <p style="margin:6px 0;">✅ 1 Bilet Premium în fiecare zi calendaristică</p>
        <p style="margin:6px 0;">✅ Algoritm avansat pentru probabilități live</p>
        <a class="stripe-btn" href="{link_stripe}" target="_blank">CUMPĂRĂ ACCES MEDIUM 🟡</a>
    </div>""", unsafe_allow_html=True)

    # Pachet HIGH
    st.markdown(f"""<div class="vip-card-box" style="border: 1px solid rgba(255, 0, 85, 0.45) !important;">
        <h4 style="color:#ff0055; margin:0 0 5px 0;">🔥 HIGH VIP ELITE</h4>
        <h2 style="margin:0 0 15px 0; font-size:28px;">120 RON <span style="font-size:14px; color:#94a3b8;">/ lună</span></h2>
        <p style="margin:6px 0;">✅ Cota 2 VIP zilnică + Proiect dedicat Dublare</p>
        <p style="margin:6px 0;">✅ Monitorizare live non-stop pe toate sistemele</p>
        <a class="stripe-btn" href="{link_stripe}" style="background: linear-gradient(135deg, #ff0055 0%, #990033 100%) !important; color:#ffffff !important;" target="_blank">DEBLOCHEAZĂ ACCES HIGH 🔥</a>
    </div>""", unsafe_allow_html=True)
