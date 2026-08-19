import streamlit as st

def aplica_stiluri_landing_premium():
    st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        .stApp {
            background-color: #050508 !important;
            color: #ffffff !important;
            font-family: 'Rajdhani', sans-serif !important;
        }
        
        h1, h2, h3, h4, p, span, label {
            font-family: 'Rajdhani', sans-serif !important;
            color: #ffffff !important;
        }

        .hero-title-container { text-align: center; padding-top: 25px; padding-bottom: 5px; }
        .mockup-wrapper { display: flex; justify-content: center; align-items: center; margin: 15px 0; }
        .store-buttons-container { display: flex; justify-content: center; gap: 20px; margin-top: 15px; margin-bottom: 35px; }
        
        .store-btn {
            background: #000000; border: 1px solid rgba(176, 66, 255, 0.4); border-radius: 8px;
            padding: 8px 20px; display: flex; align-items: center; gap: 10px; text-decoration: none;
        }
        .store-btn:hover { border-color: #b042ff; box-shadow: 0 0 20px rgba(176, 66, 255, 0.4); }

        /* Stil pentru rândurile de tabel din interiorul sportului */
        .phone-table { width: 100%; margin-top: 10px; }
        .phone-row { display: flex; justify-content: space-between; padding: 8px 5px; border-bottom: 1px solid #1a103c; }
        .phone-label { color: #cbd5e1; font-size: 13px; text-transform: uppercase; }
        .phone-val { color: #ffffff; font-weight: 800; font-size: 15px; }

        .mov-badge-premium {
            background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important;
            color: #ffffff !important; padding: 3px 10px; border-radius: 6px; font-size: 13px; font-weight: 800;
        }
        
        .bar-wrapper { margin: 10px 0; }
        .bar-container-premium { width: 100%; background: #130d24; border-radius: 20px; height: 16px; overflow: hidden; border: 1px solid #281947; }
        .bar-fill-mov-tiktok { height: 100%; background: linear-gradient(90deg, #6c00d9 0%, #b042ff 100%) !important; border-radius: 20px; }

        /* Forțăm butoanele-carduri de sport să arate ca în imaginea ta din TikTok */
        div.stButton > button {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            padding: 15px !important;
            width: 100% !important;
            text-align: left !important;
            display: block !important;
            margin-bottom: -10px !important;
        }
        div.stButton > button:hover {
            border-color: #b042ff !important;
            background: rgba(176, 66, 255, 0.05) !important;
        }
    </style>
    """, unsafe_allow_html=True)

def date_fotbal_real():
    return {
        "LASK Linz vs FCSB": {
            "liga": "UEFA EUROPA LEAGUE", "g_gz": "16", "g_os": "14", "med_gz": "1.85", "med_os": "1.55", "ht_gz": "84.10%", "p15_gz": "91.00%", "w_p15": "90%", "w_gg": "64%"
        },
        "CFR Cluj vs Pafos FC": {
            "liga": "UEFA CONFERENCE LEAGUE", "g_gz": "15", "g_os": "11", "med_gz": "1.65", "med_os": "1.28", "ht_gz": "81.00%", "p15_gz": "87.50%", "w_p15": "85%", "w_gg": "58%"
        }
    }

def date_cs2_real():
    return {
        "Natus Vincere vs FaZe Clan": {
            "liga": "PGL MAJOR COLOGNE", "g_gz": "2", "g_os": "1", "med_gz": "13.4", "med_os": "11.2", "ht_gz": "78.00%", "p15_gz": "85.00%", "w_p15": "88%", "w_gg": "72%"
        },
        "G2 Esports vs Team Vitality": {
            "liga": "BLAST PREMIER FINALS", "g_gz": "1", "g_os": "2", "med_gz": "10.8", "med_os": "12.6", "ht_gz": "69.00%", "p15_gz": "81.00%", "w_p15": "79%", "w_gg": "65%"
        }
    }
