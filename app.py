import streamlit as st
import base64

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO Live Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție pentru citirea imaginii locale JPG de pe GitHub și transformarea ei în fundal
def decodifica_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# Citim terenul de fotbal și logo-ul din proiectul tău GitHub
teren_base64 = decodifica_imagine_locala("teren.jpg")
logo_base64 = decodifica_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"""
        background: linear-gradient(rgba(4, 12, 8, 0.94), rgba(2, 6, 4, 0.96)), 
                    url('data:image/jpeg;base64,{teren_base64}') !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    """
else:
    bg_style = "background: radial-gradient(circle at center, #06140d 0%, #020805 100%) !important;"

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
    
    /* Carduri tip sticlă mată în nuanțe verzi închise */
    div[data-testid="stVerticalBlockBorder"] {{
        background: rgba(8, 20, 14, 0.88) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.7) !important;
        margin-bottom: 20px !important;
    }}

    /* DESIGN INTEGRAT ÎN TENTĂ VERDE PENTRU GRAFIC */
    .stat-container {{
        width: 100%;
        margin: 0 auto;
    }}
    
    .stat-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 10px 0;
        text-align: center;
    }}
    
    .stat-left-val {{
        width: 20%;
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
    }}
    
    .stat-right-val {{
        width: 20%;
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
    }}
    
    .stat-center-label {{
        width: 60%;
        font-size: 16px;
        font-weight: 700;
        color: #a0aec0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    /* MODIFICAT: Insigne verzi neon cu procente */
    .green-badge {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%);
        color: #000000 !important;
        padding: 4px 15px;
        border-radius: 6px;
        font-size: 16px;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 2px 10px rgba(0, 255, 102, 0.25);
    }}
    
    /* Structură pentru barele mari din a doua parte a pozei */
    .bar-wrapper {{
        display: flex;
        align-items: center;
        margin: 12px 0;
    }}
    
    .bar-label {{
        width: 25%;
        font-size: 16px;
        font-weight: 700;
        color: #ffffff;
    }}
    
    .bar-container {{
        width: 75%;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        overflow: hidden;
        height: 24px;
        position: relative;
        border: 1px solid rgba(255,255,255,0.05);
    }}
    
    /* MODIFICAT: Degraduri de verde intens pentru bare */
    .bar-fill-intense-green {{
        height: 100%;
        background: linear-gradient(90deg, #008f33 0%, #00ff66 100%);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10px;
        font-size: 13px;
        font-weight: 800;
        color: #000000;
    }}
    
    .bar-fill-soft-green {{
        height: 100%;
        background: linear-gradient(90deg, #024c1c 0%, #00bc43 100%);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10px;
        font-size: 13px;
        font-weight: 800;
        color: #ffffff;
    }}
    
    /* MODIFICAT: Căsuța de jos în nuanță verde sticlă */
    .green-footer-box {{
        background: rgba(0, 255, 102, 0.05);
        border: 1px solid rgba(0, 255, 102, 0.18);
        border-radius: 10px;
        padding: 12px 20px;
        margin-top: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }}
</style>
""", unsafe_allow_html=True)

# 2. Header-ul principal al aplicației cu Logo
if logo_base64:
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <img src="data:image/png;base64,{logo_base64}" width="280">
        </div>
        """, 
        unsafe_allow_html=True
    )
else:
    st.markdown("<h1 style='text-align: center; color: #00ff66;'>⚽ PARIURIGO &bull; DASHBOARD</h1>", unsafe_allow_html=True)

st.write("---")

# Împărțirea ecranului: Graficul cu Statistici (Stânga) și Abonamente VIP (Dreapta)
col_grafic, col_abonamente = st.columns([1.3, 0.7], gap="large")

# 3. SECȚIUNEA DIN STÂNGA: GRAFICUL VIZUAL ÎN TENTĂ VERDE
with col_grafic:
    st.subheader("📊 Modul Algoritm & Probabilități")
    
    with st.container(border=True):
        st.markdown("<p style='text-align:center; color:#94a3b8; margin:0;'>SUPER LIG &bull; TURKEY</p>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>BAȘAKȘEHIR vs KOCAELISPOR</h2>", unsafe_allow_html=True)
        st.write("---")
        
        # PARTEA 1 A GRAFICULUI: Simetrie cu etichete centrale și insigne verzi
        st.markdown("""
        <div class="stat-container">
            <div class="stat-row">
                <div class="stat-left-val">7</div>
                <div class="stat-center-label">Total goluri marcate</div>
                <div class="stat-right-val">3</div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val">1.00</div>
                <div class="stat-center-label">Medie goluri</div>
                <div class="stat-right-val">0.43</div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val">8</div>
                <div class="stat-center-label">Goluri primite</div>
                <div class="stat-right-val">6</div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">
            <div class="stat-row">
                <div class="stat-left-val"><span class="green-badge">71.43%</span></div>
                <div class="stat-center-label">Peste 0.5 HT</div>
                <div class="stat-right-val"><span class="green-badge">57.14%</span></div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val"><span class="green-badge">71.43%</span></div>
                <div class="stat-center-label">Peste 0.5 ST</div>
                <div class="stat-right-val"><span class="green-badge">57.14%</span></div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val"><span class="green-badge">85.71%</span></div>
                <div class="stat-center-label">Peste 1.5 goluri</div>
                <div class="stat-right-val"><span class="green-badge">42.86%</span></div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val" style="color:#00ff66;">28.57%</div>
                <div class="stat-center-label">Peste 2.5 goluri</div>
                <div class="stat-right-val" style="color:#00ff66;">42.86%</div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val" style="color:#00ff66;">57.14%</div>
                <div class="stat-center-label">Ambele marchează</div>
                <div class="stat-right-val" style="color:#00ff66;">42.86%</div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val" style="font-size:14px; color:#a0aec0;">14.29%</div>
                <div class="stat-center-label">Peste 3.5 cartonașe</div>
                <div class="stat-right-val" style="font-size:14px; color:#a0aec0;">28.57%</div>
            </div>
            <div class="stat-row">
                <div class="stat-left-val" style="font-size:12px; color:#a0aec0;">-</div>
                <div class="stat-center-label">Peste 9.5 cornere</div>
                <div class="stat-right-val" style="font-size:14px; color:#00ff66;">14.29%</div>
            </div>
        </div>
        <hr style="border-color: rgba(255,255,255,0.05); margin: 20px 0;">
        """, unsafe_allow_html=True)
        
        # PARTEA 2 A GRAFICULUI: Barele orizontale în nuanțe de verde
        st.write("**📈 EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:**")
        
        st.markdown("""
        <div class="bar-wrapper">
            <div class="bar-label">Peste 1.5:</div>
            <div class="bar-container"><div class="bar-fill-intense-green" style="width: 64.29%;">64.29%</div></div>
        </div>
        <div class="bar-wrapper">
            <div class="bar-label">Peste 2.5:</div>
            <div class="bar-container"><div class="bar-fill-soft-green" style="width: 14.29%;">14.29%</div></div>
        </div>
        <div class="bar-wrapper">
            <div class="bar-label">Peste 0.5 R1:</div>
