import streamlit as st
import base64
import os

# 1. Configurare pagină (Full Screen)
st.set_page_config(page_title="PariuriGo • Live Center", page_icon="⚽", layout="wide")

# Funcție pentru imaginea de fundal
def adauga_imagine_fundal(nume_fisier):
    if os.path.exists(nume_fisier):
        with open(nume_fisier, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(5, 11, 14, 0.90), rgba(5, 11, 14, 0.90)), url("data:image/jpg;base64,{encoded_string}");
                background-size: cover; background-position: center; background-attachment: fixed;
                color: #ffffff; font-family: 'Segoe UI', sans-serif;
            }}
            </style>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown("<style>.stApp { background-color: #0b0f17; color: #ffffff; }</style>", unsafe_allow_html=True)

# Activare fundal
adauga_imagine_fundal("fundal.jpg")

# 2. Injectare CSS pentru noul stil cu bare aurii/portocalii (Stil Gold/Orange Pro)
st.markdown("""
    <style>
    /* Containere principale meci */
    .pro-match-container { background-color: rgba(14, 20, 32, 0.85); border: 1px solid #1f2c47; border-radius: 12px; padding: 25px; margin-bottom: 25px; }
    
    /* Header echipe */
    .league-title { color: #f59e0b; font-size: 12px; font-weight: bold; text-align: center; text-transform: uppercase; margin-bottom: 20px; }
    .teams-header { display: flex; justify-content: space-around; align-items: center; text-align: center; margin-bottom: 30px; }
    .team-box { font-size: 20px; font-weight: bold; letter-spacing: 0.5px; }
    .vs-circle { background-color: #1f2c47; padding: 8px 12px; border-radius: 50%; font-size: 12px; color: #8a9da8; }
    
    /* Tabelul de statistici pe linii */
    .stat-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
    .stat-pct-left { background-color: #d97706; color: white; padding: 5px 15px; border-radius: 6px; font-weight: bold; font-size: 13px; width: 70px; text-align: center; }
    .stat-pct-right { background-color: #d97706; color: white; padding: 5px 15px; border-radius: 6px; font-weight: bold; font-size: 13px; width: 70px; text-align: center; }
    .stat-name-center { color: #ffffff; font-size: 13px; font-weight: 500; text-align: center; flex-grow: 1; }
    .stat-value-simple { color: #8a9da8; font-size: 14px; font-weight: bold; width: 70px; text-align: center; }
    
    /* Secțiunea de bare de progres inferioare */
    .progress-section { margin-top: 30px; padding-top: 20px; border-top: 1px solid #1f2c47; }
    .progress-label-row { display: flex; justify-content: space-between; font-size: 12px; color: #ffffff; font-weight: 500; margin-bottom: 4px; }
    .custom-progress-bar { background-color: #111827; border-radius: 10px; height: 12px; width: 100%; margin-bottom: 15px; overflow: hidden; }
    .custom-progress-fill { background: linear-gradient(90deg, #d97706, #f59e0b); height: 100%; border-radius: 10px; }
    
    /* Arbitru box */
    .referee-box { background-color: #111827; border: 1px solid #1f2c47; border-radius: 8px; padding: 12px; margin-top: 20px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; }
    
    /* Card VIP Dreapta */
    .vip-card-pro { background-color: rgba(14, 20, 32, 0.9); border: 1px solid #d97706; border-radius: 12px; padding: 25px; text-align: center; }
    .vip-title-gold { color: #f59e0b; font-size: 20px; font-weight: bold; text-transform: uppercase; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# 3. Structura Layout
st.markdown('<h2 style="margin-bottom: 20px;">⚽ PARIURIGO • LIVE ADVANCED CENTER</h2>', unsafe_allow_html=True)

col_stanga, col_dreapta = st.columns([0.7, 0.3])

with col_stanga:
    # ÎNCEPUT CONTAINER MECI EXACT CA ÎN IMAGINE
    st.markdown("""
    <div class="pro-match-container">
        <div class="league-title">🏆 Super Lig (Turkey)</div>
        
        <div class="teams-header">
            <div class="team-box">⚫ BAȘAKȘEHIR</div>
            <div class="vs-circle">VS</div>
            <div class="team-box">🟢 KOCAELISPOR</div>
        </div>
        
        <!-- Linii Statistici Clasice -->
        <div class="stat-row">
            <div class="stat-value-simple">7</div>
            <div class="stat-name-center">Total goluri marcate</div>
            <div class="stat-value-simple">3</div>
        </div>
        <div class="stat-row">
            <div class="stat-value-simple">1.00</div>
            <div class="stat-name-center">Medie goluri</div>
            <div class="stat-value-simple">0.43</div>
        </div>
        <div class="stat-row">
            <div class="stat-value-simple">8</div>
            <div class="stat-name-center">Goluri primite</div>
            <div class="stat-value-simple">6</div>
        </div>
        
        <hr style="border-color: #1f2c47; margin: 20px 0;">
        
        <!-- Linii Statistici cu Procente (Casete Portocalii) -->
        <div class="stat-row">
            <div class="stat-pct-left">71.43%</div>
            <div class="stat-name-center">Peste 0.5 HT</div>
            <div class="stat-pct-right">57.14%</div>
        </div>
        
        <div class="stat-row">
            <div class="stat-pct-left">71.43%</div>
            <div class="stat-name-center">Peste 0.5 ST</div>
            <div class="stat-pct-right">57.14%</div>
        </div>
        
        <div class="stat-row">
            <div class="stat-pct-left">85.71%</div>
            <div class="stat-name-center">Peste 1.5 goluri</div>
            <div class="stat-pct-right">42.86%</div>
        </div>
        
        <div class="stat-row">
            <div class="stat-pct-left">28.57%</div>
            <div class="stat-name-center">Peste 2.5 goluri</div>
            <div class="stat-pct-right">0.00%</div>
        </div>
        
        <div class="stat-row">
            <div class="stat-pct-left">57.14%</div>
            <div class="stat-name-center">Ambele marchează (GG)</div>
            <div class="stat-pct-right">42.86%</div>
        </div>
        
        <div class="stat-row">
            <div class="stat-pct-left">14.29%</div>
            <div class="stat-name-center">Peste 3.5 cartonașe</div>
            <div class="stat-pct-right">28.57%</div>
        </div>

        <!-- SECTIUNEA JOS: BARE ORIZONTALE DE PROGRES -->
        <div class="progress-section">
            
            <!-- Bara Peste 1.5 -->
            <div class="progress-label-row"><span>Peste 1.5:</span> <span>64.29%</span></div>
            <div class="custom-progress-bar"><div class="custom-progress-fill" style="width: 64.29%;"></div></div>
            
            <!-- Bara Peste 2.5 -->
            <div class="progress-label-row"><span>Peste 2.5:</span> <span>14.29%</span></div>
            <div class="custom-progress-bar"><div class="custom-progress-fill" style="width: 14.29%;"></div></div>
            
            <!-- Bara Ambele marchează -->
            <div class="progress-label-row"><span>Ambele marchează:</span> <span>50.00%</span></div>
            <div class="custom-progress-bar"><div class="custom-progress-fill" style="width: 50.00%;"></div></div>
            
            <!-- Bara Peste 3.5 Cartonașe -->
            <div class="progress-label-row"><span>+ 3.5 Cartonașe:</span> <span>21.43%</span></div>
            <div class="custom-progress-bar"><div class="custom-progress-fill" style="width: 21.43%;"></div></div>
        </div>
        
        <!-- Caseta Arbitru din Subsol -->
        <div class="referee-box">
            <span>🔸 <b>Stats arbitru • probabilitate matematică</b><br><small style="color:#8a9da8;">M. Turkmen • 7/7 meciuri din ligă</small></span>
            <span style="color:#f59e0b; font-weight:bold;">▼</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_dreapta:
    # PANOU VIP COORDONAT
    st.markdown("""
    <div class="vip-card-pro">
        <div class="vip-title-gold">👑 PARIURIGO VIP</div>
        <p style="font-size: 24px; font-weight: bold; color: #ffffff; margin-bottom: 5px;">29 RON <span style="font-size:13px; color:#8a9da8;">/ lună</span></p>
        <p style="color: #8a9da8; font-size: 13px; margin-bottom: 20px;">Deblochează procentajele complete generate de IA pentru toate meciurile live din Europa.</p>
        <div style="text-align: left; font-size: 13px; line-height: 2; margin-bottom: 25px;">
            🔸 Acces complet la algoritmii avansați<br>
            🔸 Statistici detaliate arbitri și cornere<br>
            🔸 Alerte instant pe Telegram / WhatsApp
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Activează Pachetul Inteligent"):
        st.success("Se încarcă modulul de securitate plată...")
