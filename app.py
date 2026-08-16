import streamlit as st
import base64

# 1. Configurare Pagină principală
st.set_page_config(
    page_title="PariuriGO Live Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție pentru a citi imaginea locală de pe GitHub și a o converti pentru CSS
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

img_base64 = get_base64_image("teren.png")
overlay_color = "rgba(4, 12, 8, 0.88)"
text_principal = "#ffffff"
text_secundar = "#94a3b8"
glass_bg = "rgba(13, 31, 23, 0.6)"
glass_border = "rgba(0, 255, 102, 0.2)"
glass_shadow = "rgba(0, 0, 0, 0.7)"

if img_base64:
    bg_style = f"background: linear-gradient({overlay_color}, {overlay_color}), url('data:image/png;base64,{img_base64}') !important;"
else:
    bg_style = f"background: {overlay_color} !important;"

# Injectare stiluri CSS cu fontul sportiv "Rajdhani" și elemente grafice avansate
st.markdown(f"""
<style>
    @import url('https://googleapis.com');

    /* Aplicare font și fundal */
    .stApp {{
        {bg_style}
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: {text_principal} !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    
    h1, h2, h3, h4, p, span, div {{
        font-family: 'Rajdhani', sans-serif !important;
    }}

    /* Bara de Navigare de Sus */
    .nav-bar {{
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        padding: 10px 30px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.05);
    }}

    /* Cardurile Premium Glassmorphism */
    .premium-card {{
        background: {glass_bg};
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid {glass_border};
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 12px 40px 0 {glass_shadow};
    }}
    
    /* Ecran Scor și Minute */
    .live-badge {{
        background: #ef4444;
        color: white;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 14px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        animation: blinker 1.5s linear infinite;
    }}
    @keyframes blinker {{
        50% {{ opacity: 0.5; }}
    }}

    .scor-display {{
        font-size: 38px !important;
        font-weight: 800;
        color: #ffcc00;
        text-align: center;
        letter-spacing: 2px;
        margin: 10px 0;
    }}

    /* Statistici Meci (Bare de progres și detalii) */
    .stat-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 8px 0;
        font-size: 16px;
        font-weight: 600;
    }}
    .stat-label {{
        color: #94a3b8;
        text-transform: uppercase;
        font-size: 14px;
    }}
    .stat-val {{
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
    }}

    /* Cote și Butoane */
    .cota-box {{
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(0, 255, 102, 0.3);
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        transition: all 0.2s;
    }}
    .cota-box:hover {{
        border-color: #00ff66;
        background: rgba(0, 255, 102, 0.1);
    }}

    /* Suprascriere Butoane Streamlit */
    .stButton > button {{
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
        transition: all 0.3s ease !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 25px rgba(0, 255, 102, 0.6) !important;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Bara de Navigare Superioară
st.markdown("""
<div class="nav-bar">
    <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 28px;">⚽</span>
        <span style="font-size: 26px; font-weight: 800; color: #00ff66; letter-spacing: 1px;">PARIURIGO</span>
    </div>
    <div style="font-size: 16px; font-weight: 600; color: #94a3b8;">
        🔴 LIVE CENTER &bull; PLATFORMA PREMIUM v2.0
    </div>
</div>
""", unsafe_allow_html=True)

col_stanga, col_dreapta = st.columns([1.2, 0.8])

# 3. SECȚIUNEA MECIURI LIVE (Stânga)
with col_stanga:
    st.markdown("<h2 style='color: #ffffff; font-weight: 800; margin-bottom:15px;'>🏟️ CENTRUL DE MECIURI LIVE</h2>", unsafe_allow_html=True)
    
    # MECIUL 1: REAL MADRID vs BARCELONA
    st.markdown("""
    <div class="premium-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="live-badge">LIVE &bull; MIN 76</span>
            <span style="color: #94a3b8; font-weight: bold;">LALIGA EA SPORTS</span>
        </div>
        
        <div class="scor-display">
            REAL MADRID <span style="color:white; font-size:44px; margin: 0 15px;">2 - 1</span> BARCELONA
        </div>
        
        <hr style="border-color: rgba(255,255,255,0.08); margin: 15px 0;">
        
        <!-- Statistici Live detaliate -->
        <div class="stat-row">
            <span class="stat-val">52%</span>
            <span class="stat-label">Posesie %</span>
            <span class="stat-val">48%</span>
        </div>
        <div class="stat-row">
            <span class="stat-val" style="color: #00ff66;">7</span>
            <span class="stat-label">Șuturi pe poartă</span>
            <span class="stat-val" style="color: #ff3333;">4</span>
        </div>
        <div class="stat-row">
            <span class="stat-val">12</span>
            <span class="stat-label">Faulturi Comise</span>
            <span class="stat-val">14</span>
        </div>
        <div class="stat-row">
            <span class="stat-val" style="color: #eab308;">🟨 2</span>
            <span class="stat-label">Cartonașe</span>
            <span class="stat-val" style="color: #eab308;">🟨 3 &bull; 🟥 0</span>
        </div>
        
        <hr style="border-color: rgba(255,255,255,0.08); margin: 15px 0;">
        
        <div style="font-size: 16px; font-weight: bold; color: #94a3b8; margin-bottom: 10px;">PONT RECOMANDAT DE ALGORITM:</div>
        <div style="background: rgba(0,255,102,0.05); padding: 12px; border-radius: 8px; border-left: 4px solid #00ff66; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <span style="font-weight: 800; font-size: 18px; color: white;">Ambele echipe marchează (GG)</span><br>
                <span style="color: #94a3b8; font-size: 14px;">Stare: În desfășurare (Așteptăm gol Barcelona)</span>
            </div>
            <div style="font-size: 24px; font-weight: 800; color: #00ff66;">Cota: 1.72</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # MECIUL 2: MANCHESTER CITY vs LIVERPOOL
    st.markdown("""
    <div class="premium-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="live-badge" style="background: #22c55e;">PRE-MECI &bull; 22:00</span>
            <span style="color: #94a3b8; font-weight: bold;">PREMIER LEAGUE</span>
        </div>
        
        <div class="scor-display" style="color: white; font-size: 30px;">
            MANCHESTER CITY <span style="color:#ffcc00; font-size:32px; margin: 0 10px;">vs</span> LIVERPOOL
        </div>
        
        <hr style="border-color: rgba(255,255,255,0.08); margin: 15px 0;">
        
        <div style="display: flex; gap: 15px; margin-bottom: 15px;">
            <div style="flex:1;" class="cota-box"><span style="color:#94a3b8; font-size:14px;">1</span><br><strong style="font-size:18px;">2.15</strong></div>
            <div style="flex:1;" class="cota-box"><span style="color:#94a3b8; font-size:14px;">X</span><br><strong style="font-size:18px;">3.60</strong></div>
            <div style="flex:1;" class="cota-box"><span style="color:#94a3b8; font-size:14px;">2</span><br><strong style="font-size:18px;">3.20</strong></div>
        </div>
        
        <div style="background: rgba(0,255,102,0.05); padding: 12px; border-radius: 8px; border-left: 4px solid #ffcc00; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <span style="font-weight: 800; font-size: 18px; color: white;">Peste 2.5 Goluri în Meci</span><br>
                <span style="color: #94a3b8; font-size: 14px;">Analiză: Ultimele 5 meciuri directe au fost de peste 3 goluri.</span>
            </div>
            <div style="font-size: 24px; font-weight: 800; color: #ffcc00;">Cota: 1.85</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SECȚIUNEA ABONAMENTE & BILETE VIP (Dreapta)
with col_dreapta:
    st.markdown("<h2 style='color: #ffffff; font-weight: 800; margin-bottom:15px;'>🏆 ACCES VIP PREMIUM</h2>", unsafe_allow_html=True)
    
    tab_low, tab_med, tab_high = st.tabs(["🟢 LOW", "🟡 MEDIUM", "🔥 HIGH"])
    
    with tab_low:
        st.markdown("""
        <div class="premium-card" style="border-color: rgba(34, 197, 94, 0.4);">
            <p style="font-size: 24px; font-weight: 800; color: #22c55e; margin: 0; text-align:center;">PACHET STANDARD LOW</p>
