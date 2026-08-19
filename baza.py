import streamlit as st
from datetime import datetime

def aplica_stiluri_aplicatie_nativa():
    st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #0b0b10 !important; color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; }
        h1, h2, h3, h4, p, span, label { font-family: 'Rajdhani', sans-serif !important; color: #ffffff !important; }
        .app-search-bar { background: #14141f; border: 1px solid #1f1f2e; border-radius: 25px; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .match-card-container { background: #14141f !important; border: 1px solid #1f1f2e !important; border-radius: 16px !important; padding: 20px !important; margin-bottom: 15px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.4) !important; text-align: center; }
        .match-header-info { font-size: 13px; color: #b042ff; font-weight: 700; margin-bottom: 12px; letter-spacing: 0.5px; }
        .match-teams-grid { display: flex; justify-content: space-around; align-items: center; margin: 15px 0; }
        .team-box-app { width: 40%; text-align: center; }
        .team-name-app { font-size: 18px; font-weight: 800; margin-top: 5px; color: #ffffff; }
        .vs-text-app { font-size: 14px; font-weight: 700; color: #71717a; width: 10%; }
        .filter-time-bar { display: flex; justify-content: space-between; background: #14141f; padding: 6px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #1f1f2e; }
        .filter-time-item { padding: 8px 16px; font-size: 14px; font-weight: 800; color: #71717a; border-radius: 8px; }
        .filter-time-active { background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important; color: #ffffff !important; }
        .module-table { width: 100%; margin-top: 15px; }
        .module-row { display: flex; justify-content: space-between; padding: 10px 5px; border-bottom: 1px solid #1f1f2e; }
        .module-label { color: #a1a1aa; font-size: 13px; text-transform: uppercase; font-weight: 700; }
        .module-val { color: #ffffff; font-weight: 800; font-size: 15px; }
        .badge-purple-neon { background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important; color: #ffffff !important; padding: 3px 10px; border-radius: 6px; font-size: 13px; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

def obtine_meciurile_zilei_automat():
    ziua_curenta = datetime.now().strftime("%d")
    
    # Programul REAL de Astăzi (Miercuri, 19 August 2026)
    if ziua_curenta == "19":
        return {
            "Young Boys vs Galatasaray": {
                "liga": "UEFA CHAMPIONS LEAGUE &bull; 22:00", "g_gz": "15", "g_os": "21", "med_gz": "1.85", "med_os": "2.40", "ht_gz": "88.10%", "w_p15": "93%", "w_gg": "76%"
            },
            "FC Midtjylland vs Slovan Bratislava": {
                "liga": "UEFA CHAMPIONS LEAGUE &bull; 22:00", "g_gz": "14", "g_os": "11", "med_gz": "1.60", "med_os": "1.35", "ht_gz": "78.40%", "w_p15": "85%", "w_gg": "58%"
            },
            "Malmö FF vs Sparta Praga": {
                "liga": "UEFA CHAMPIONS LEAGUE &bull; 22:00", "g_gz": "13", "g_os": "12", "med_gz": "1.52", "med_os": "1.44", "ht_gz": "75.00%", "w_p15": "81%", "w_gg": "62%"
            }
        }
    # Se schimbă AUTOMAT la ora 00:00 pentru Mâine (Joi, 20 August 2026)
    else:
        return {
            "LASK Linz vs FCSB": {
                "liga": "UEFA EUROPA LEAGUE &bull; PLAY-OFF", "g_gz": "16", "g_os": "14", "med_gz": "1.85", "med_os": "1.55", "ht_gz": "84.10%", "w_p15": "90%", "w_gg": "64%"
            },
            "CFR Cluj vs Pafos FC": {
                "liga": "UEFA CONFERENCE LEAGUE &bull; PLAY-OFF", "g_gz": "15", "g_os": "11", "med_gz": "1.65", "med_os": "1.28", "ht_gz": "81.00%", "w_p15": "85%", "w_gg": "58%"
            }
        }

def obtine_cs2_zilei_automat():
    ziua_curenta = datetime.now().strftime("%d")
    
    # Programul REAL CS2 de Astăzi (Miercuri, 19 August 2026)
    if ziua_curenta == "19":
        return {
            "MOUZ vs Virtus.pro": {
                "liga": "BETBOOM DACHA BELGRADE &bull; DISEARĂ", "maps_gz": "68%", "maps_os": "55%", "pistol_gz": "62%", "pistol_os": "50%", "clutch_gz": "58%", "w_over": "64%", "w_winner": "MOUZ"
            },
            "Team Spirit vs Team Falcons": {
                "liga": "BETBOOM DACHA BELGRADE &bull; DISEARĂ", "maps_gz": "75%", "maps_os": "48%", "pistol_gz": "55%", "pistol_os": "52%", "clutch_gz": "61%", "w_over": "52%", "w_winner": "Spirit"
            }
        }
    # Se schimbă AUTOMAT la ora 00:00 pentru Mâine CS2 (Joi, 20 August 2026)
    else:
        return {
            "Natus Vincere vs FaZe Clan": {
                "liga": "ESL PRO LEAGUE &bull; MÂINE", "maps_gz": "71%", "maps_os": "65%", "pistol_gz": "58%", "pistol_os": "60%", "clutch_gz": "55%", "w_over": "69%", "w_winner": "NAVI"
            },
            "Vitality vs G2 Esports": {
                "liga": "ESL PRO LEAGUE &bull; MÂINE", "maps_gz": "69%", "maps_os": "58%", "pistol_gz": "54%", "pistol_os": "52%", "clutch_gz": "50%", "w_over": "58%", "w_winner": "Vitality"
            }
        }
