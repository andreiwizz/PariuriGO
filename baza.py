import streamlit as st

def aplica_stiluri_aplicatie_nativa():
    st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Aplicatie Full-Screen pe fundal inchis, fara elemente de site */
        .stApp {
            background-color: #0d0d11 !important;
            color: #ffffff !important;
            font-family: 'Rajdhani', sans-serif !important;
        }
        
        h1, h2, h3, h4, p, span, label {
            font-family: 'Rajdhani', sans-serif !important;
            color: #ffffff !important;
        }
        
        /* Header-ul de cautare de sus ca in TikTok */
        .app-search-bar {
            background: #16161f;
            border: 1px solid #222230;
            border-radius: 25px;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        /* Cardurile mari de sport stilizate exact ca in imagine */
        .native-card {
            background: #16161f !important;
            border: 1px solid #222230 !important;
            border-radius: 16px !important;
            padding: 18px !important;
            margin-bottom: 12px !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        }

        .native-flex {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .native-left {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .native-title {
            font-size: 18px;
            font-weight: 800;
            margin: 0;
            color: #ffffff;
        }

        .native-desc {
            font-size: 13px;
            color: #71717a;
            margin: 2px 0 0 0;
        }

        /* Insignele verzi cu AVAILABLE Mov din imaginea ta */
        .status-available {
            background: rgba(176, 66, 255, 0.1) !important;
            color: #b042ff !important;
            border: 1px solid #b042ff !important;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.5px;
        }

        .status-soon {
            background: rgba(255, 255, 255, 0.02) !important;
            color: #71717a !important;
            border: 1px solid #27272a !important;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 800;
        }

        /* Stil tabel interior module sport */
        .module-table {
            width: 100%;
            margin-top: 15px;
        }

        .module-row {
            display: flex;
            justify-content: space-between;
            padding: 12px 8px;
            border-bottom: 1px solid #222230;
        }

        .module-label {
            color: #a1a1aa;
            font-size: 14px;
            text-transform: uppercase;
            font-weight: 700;
        }

        .module-val {
            color: #ffffff;
            font-weight: 800;
            font-size: 16px;
        }

        .badge-purple-neon {
            background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important;
            color: #ffffff !important;
            padding: 4px 14px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 800;
        }

        /* Stil special pentru butoanele invizibile de click pe carduri */
        div.stButton > button {
            background: transparent !important;
            border: none !important;
            color: transparent !important;
            padding: 0 !important;
            height: 0px !important;
            margin: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

def date_fotbal_interactiv():
    return {
        "FCSB vs Rapid București": {
            "liga": "ROMÂNIA SUPERLIGA", "g_gz": "14", "g_os": "11", "med_gz": "1.75", "med_os": "1.37", "ht_gz": "85.71%", "p15_gz": "91.20%", "w_p15": "85%", "w_gg": "71%"
        },
        "LASK Linz vs FCSB": {
            "liga": "UEFA EUROPA LEAGUE", "g_gz": "16", "g_os": "14", "med_gz": "1.85", "med_os": "1.55", "ht_gz": "84.10%", "p15_gz": "91.00%", "w_p15": "90%", "w_gg": "64%"
        }
    }

def date_cs2_interactiv():
    return {
        "FaZe Clan vs Natus Vincere": {
            "liga": "PGL MAJOR COLOGNE", "maps_gz": "64%", "maps_os": "72%", "pistol_gz": "58%", "pistol_os": "61%", "clutch_gz": "54%", "w_over": "68%", "w_winner": "FaZe"
        },
        "G2 Esports vs Team Vitality": {
            "liga": "BLAST PREMIER FINALS", "maps_gz": "55%", "maps_os": "68%", "pistol_gz": "50%", "pistol_os": "55%", "clutch_gz": "48%", "w_over": "59%", "w_winner": "Vitality"
        }
    }
