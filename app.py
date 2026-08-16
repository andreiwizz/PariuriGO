import streamlit as st
import base64

# 1. Configurare Pagină principală (MANDATORIU SĂ FIE PRIMA FUNCȚIE)
st.set_page_config(
    page_title="PariuriGO Live Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție pentru citirea imaginii locale de pe GitHub
def incarcă_teren_fotbal(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

img_data = incarcă_teren_fotbal("teren.png")

# Structură curată de CSS inline pentru a evita orice eroare de sintaxă string
css_stiluri = """
<style>
    @import url('https://googleapis.com');

    .stApp {
        background: linear-gradient(rgba(4, 12, 8, 0.9), rgba(4, 12, 8, 0.9)) !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }
"""

if img_data:
    css_stiluri = css_stiluri.replace(
        "background: linear-gradient(rgba(4, 12, 8, 0.9), rgba(4, 12, 8, 0.9)) !important;",
        f"background: linear-gradient(rgba(4, 12, 8, 0.9), rgba(4, 12, 8, 0.9)), url('data:image/png;base64,{img_data}') !important;"
    )

css_stiluri += """
    h1, h2, h3, h4, p, span, div, button {
        font-family: 'Rajdhani', sans-serif !important;
    }

    .nav-bar {
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(10px);
        padding: 15px 30px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.05);
    }

    .premium-card {
        background: rgba(13, 31, 23, 0.65);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 255, 102, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.7);
    }
    
    .live-badge {
        background: #ef4444;
        color: white;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 14px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .scor-display {
        font-size: 36px !important;
        font-weight: 800;
        color: #ffcc00;
        text-align: center;
        letter-spacing: 2px;
        margin: 15px 0;
    }

    .stat-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 10px 0;
        font-size: 17px;
        font-weight: 600;
    }
    .stat-label {
        color: #94a3b8;
        text-transform: uppercase;
        font-size: 13px;
    }
    .stat-val {
        color: #ffffff;
        font-size: 19px;
        font-weight: 700;
    }

    .cota-box {
        background: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(0, 255, 102, 0.2);
        border-radius: 8px;
        padding: 10px;
        text-align: center;
    }

    .stButton > button {
        background: linear-gradient(135deg, #00ff66 0%, #00ea53 100%) !important;
        color: #040c08 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 4px 20px rgba(0, 255, 102, 0.4) !important;
        width: 100%;
    }
</style>
"""

st.markdown(css_stiluri, unsafe_allow_html=True)

# 2. Bara de Navigare de Sus
st.markdown("""
<div class="nav-bar">
    <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 26px; font-weight: 800; color: #00ff66; letter-spacing: 1px;">PARIURIGO</span>
    </div>
    <div style="font-size: 15px; font-weight: 600; color: #94a3b8;">
        🔴 LIVE CENTER &bull; DASHBOARD SPORTIV PREMIUM
    </div>
</div>
""", unsafe_allow_html=True)

col_stanga, col_dreapta = st.columns([1.2, 0.8])

# 3. PANOU LIVE (Stânga)
with col_stanga:
    st.markdown("### 🏟️ MECIURI ÎN DESFĂȘURARE")
    
    st.markdown("""
    <div class="premium-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="live-badge">LIVE &bull; MIN 76</span>
            <span style="color: #94a3b8; font-weight: bold;">LALIGA</span>
        </div>
        
        <div class="scor-display">
            REAL MADRID <span style="color:white; font-size:40px;">2 - 1</span> BARCELONA
        </div>
        
        <hr style="border-color: rgba(255,255,255,0.08);">
        
        <div class="stat-row">
            <span class="stat-val">52%</span>
            <span class="stat-label">Posesie Mingi %</span>
            <span class="stat-val">48%</span>
        </div>
        <div class="stat-row">
            <span class="stat-val" style="color: #00ff66;">7</span>
            <span class="stat-label">Șuturi pe Poartă</span>
            <span class="stat-val" style="color: #ef4444;">4</span>
        </div>
        <div class="stat-row">
            <span class="stat-val">12</span>
            <span class="stat-label">Faulturi Comise</span>
            <span class="stat-val">14</span>
        </div>
        <div class="stat-row">
            <span class="stat-val" style="color: #eab308;">🟨 2</span>
            <span class="stat-label">Cartonașe Primite</span>
            <span class="stat-val" style="color: #eab308;">🟨 3</span>
        </div>
        
        <hr style="border-color: rgba(255,255,255,0.08);">
        
        <div style="font-size: 15px; font-weight: bold; color: #94a3b8; margin-bottom: 8px;">SUGESTIE ANALIST:</div>
        <div style="background: rgba(0,255,102,0.05); padding: 12px; border-radius: 8px; border-left: 4px solid #00ff66; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <span style="font-weight: 800; font-size: 18px; color: white;">Ambele marchează (GG)</span>
            </div>
            <div style="font-size: 22px; font-weight: 800; color: #00ff66;">Cotă 1.72</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="premium-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="live-badge" style="background: #22c55e;">PRE-MECI &bull; 22:00</span>
            <span style="color: #94a3b8; font-weight: bold;">PREMIER LEAGUE</span>
        </div>
        
        <div class="scor-display" style="color: white; font-size: 28px;">
            MANCHESTER CITY <span style="color:#ffcc00; font-size:26px;">vs</span> LIVERPOOL
        </div>
        
        <hr style="border-color: rgba(255,255,255,0.08);">
        
        <div style="display: flex; gap: 15px; margin-bottom: 15px;">
            <div style="flex:1;" class="cota-box"><span style="color:#94a3b8; font-size:13px;">1</span><br><strong style="font-size:17px;">2.15</strong></div>
            <div style="flex:1;" class="cota-box"><span style="color:#94a3b8; font-size:13px;">X</span><br><strong style="font-size:17px;">3.60</strong></div>
            <div style="flex:1;" class="cota-box"><span style="color:#94a3b8; font-size:13px;">2</span><br><strong style="font-size:17px;">3.20</strong></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. PANOU ABONAMENTE (Dreapta)
with col_dreapta:
    st.markdown("### 🏆 DEBLOCHEAZĂ ACCES VIP")
    
    opțiune_pachet = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with opțiune_pachet[0]:
        st.markdown("""
        <div class="premium-card" style="border-color: rgba(34, 197, 94, 0.4);">
            <p style="font-size: 22px; font-weight: 800; color: #22c55e; text-align:center; margin:0;">PACHET STANDARD LOW</p>
            <h1 style="text-align: center; color: white; margin: 10px 0; font-size: 38px;">19 RON <span style='font-size:15px; color:#94a3b8;'>/ lună</span></h1>
            <hr style="border-color: rgba(255,255,255,0.08);">
            <p>✅ 3 Bilete gata analizate pe săptămână</p>
            <p>✅ Cote sigure cu probabilitate mare</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Cumpără LOW", key="b_low")

    with opțiune_pachet[1]:
        st.markdown("""
        <div class="premium-card" style="border-color: rgba(234, 179, 8, 0.4);">
            <p style="font-size: 22px; font-weight: 800; color: #eab308; text-align:center; margin:0;">PACHET GOLD MEDIUM</p>
            <h1 style="text-align: center; color: white; margin: 10px 0; font-size: 38px;">49 RON <span style='font-size:15px; color:#94a3b8;'>/ lună</span></h1>
            <hr style="border-color: rgba(255,255,255,0.08);">
            <p>✅ 1 Bilet Premium în fiecare zi</p>
            <p>✅ Notificări instant pe Telegram Bot</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Cumpără GOLD", key="b_med")

    with opțiune_pachet[2]:
        st.markdown("""
        <div class="premium-card" style="border-color: rgba(239, 68, 68, 0.4);">
            <p style="font-size: 22px; font-weight: 800; color: #ef4444; text-align:center; margin:0;">🔥 HIGH VIP ELITE</p>
            <h1 style="text-align: center; color: white; margin: 10px 0; font-size: 38px;">99 RON <span style='font-size:15px; color:#94a3b8;'>/ lună</span></h1>
            <hr style="border-color: rgba(255,255,255,0.08);">
            <p>✅ Acces total la Proiect Dublare</p>
            <p>✅ Cota 2 VIP zilnică & Suport privat 1-la-1</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Cumpără VIP ELITE", key="b_high")
