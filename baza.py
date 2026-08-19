import streamlit as st

def aplica_stiluri_landing_premium():
    st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Fundal Carbon profund, exact ca in imagine */
        .stApp {
            background-color: #050508 !important;
            color: #ffffff !important;
            font-family: 'Rajdhani', sans-serif !important;
        }
        
        h1, h2, h3, h4, p, span, label {
            font-family: 'Rajdhani', sans-serif !important;
            color: #ffffff !important;
        }

        /* Containerul central pentru titlul principal */
        .hero-title-container {
            text-align: center;
            padding-top: 40px;
            padding-bottom: 10px;
        }
        
        /* Imaginile cu telefoanele din centru */
        .mockup-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }

        /* Butoanele de App Store si Google Play stilizate in linie */
        .store-buttons-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
            margin-bottom: 40px;
        }
        
        .store-btn {
            background: #000000;
            border: 1px solid rgba(176, 66, 255, 0.4);
            border-radius: 8px;
            padding: 10px 24px;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            box-shadow: 0 4px 15px rgba(157, 0, 255, 0.1);
        }
        
        .store-btn:hover {
            border-color: #b042ff;
            box-shadow: 0 0 20px rgba(176, 66, 255, 0.4);
            transform: scale(1.02);
        }

        /* Meniul Premium de Jos (Navigation Bar din imagine) */
        .navbar-bottom-container {
            background: rgba(10, 10, 18, 0.9) !important;
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(176, 66, 255, 0.2);
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 50px;
            border-radius: 12px;
        }
        
        /* Căsuțele cu procente din aplicație - Mov Neon */
        .mov-badge-premium {
            background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important;
            color: #ffffff !important;
            padding: 6px 18px;
            border-radius: 6px;
            font-size: 15px;
            font-weight: 800;
            display: inline-block;
            box-shadow: 0 2px 10px rgba(157, 0, 255, 0.3);
        }

        /* Barele de progres rotunjite */
        .bar-container-premium {
            width: 100%;
            background: #111116;
            border-radius: 20px;
            height: 20px;
            overflow: hidden;
            border: 1px solid #222230;
        }
        
        .bar-fill-premium {
            height: 100%;
            background: linear-gradient(90deg, #6c00d9 0%, #b042ff 100%) !important;
            border-radius: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

def preia_meciuri_comunitate():
    return {
        "Dynamo Kiev vs FC Salzburg": {
            "liga": "CHAMPIONS LEAGUE - PLAY-OFF", "g_gz": "17", "g_os": "19", "med_gz": "2.05", "med_os": "2.20", "gp_gz": "6", "gp_os": "5",
            "ht_gz": "89.10%", "ht_os": "91.30%", "st_gz": "86.40%", "st_os": "88.90%", "p15_gz": "94.00%", "p15_os": "95.20%",
            "p25_gz": "70.10%", "p25_os": "74.30%", "gg_gz": "75.00%", "gg_os": "78.40%",
            "w_p15": "93%", "w_p25": "72%", "w_p05r1": "89%", "w_gg": "76%"
        },
        "LASK Linz vs FCSB": {
            "liga": "UEFA EUROPA LEAGUE", "g_gz": "16", "g_os": "14", "med_gz": "1.85", "med_os": "1.55", "gp_gz": "5", "gp_os": "7",
            "ht_gz": "84.10%", "ht_os": "78.30%", "st_gz": "86.20%", "st_os": "81.00%", "p15_gz": "91.00%", "p15_os": "85.20%",
            "p25_gz": "62.40%", "p25_os": "54.30%", "gg_gz": "68.00%", "gg_os": "61.40%",
            "w_p15": "90%", "w_p25": "58%", "w_p05r1": "84%", "w_gg": "64%"
        }
    }
