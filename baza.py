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

        .hero-title-container {
            text-align: center;
            padding-top: 30px;
            padding-bottom: 5px;
        }
        
        .mockup-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 15px 0;
        }

        .store-buttons-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
            margin-bottom: 30px;
        }
        
        .store-btn {
            background: #000000;
            border: 1px solid rgba(176, 66, 255, 0.4);
            border-radius: 8px;
            padding: 8px 20px;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 4px 15px rgba(157, 0, 255, 0.1);
        }
        
        .store-btn:hover {
            border-color: #b042ff;
            box-shadow: 0 0 20px rgba(176, 66, 255, 0.4);
        }

        /* Tabelul de statistici din interiorul telefonului */
        .phone-table {
            width: 100%;
            margin-top: 15px;
            border-collapse: collapse;
        }
        
        .phone-row {
            display: flex;
            justify-content: space-between;
            padding: 10px 5px;
            border-bottom: 1px solid #1a103c;
        }
        
        .phone-label {
            color: #cbd5e1;
            font-size: 14px;
            text-transform: uppercase;
        }
        
        .phone-val {
            color: #ffffff;
            font-weight: 800;
            font-size: 16px;
        }

        .mov-badge-premium {
            background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important;
            color: #ffffff !important;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 800;
            box-shadow: 0 2px 10px rgba(157, 0, 255, 0.3);
        }
    </style>
    """, unsafe_allow_html=True)

def preia_meciuri_comunitate():
    return {
        "LASK Linz vs FCSB": {
            "liga": "UEFA EUROPA LEAGUE", "g_gz": "16", "g_os": "14", "med_gz": "1.85", "med_os": "1.55", "gp_gz": "5", "gp_os": "7",
            "ht_gz": "84.10%", "ht_os": "78.30%", "w_p15": "90%", "w_gg": "64%"
        },
        "CFR Cluj vs Pafos FC": {
            "liga": "UEFA CONFERENCE LEAGUE", "g_gz": "15", "g_os": "11", "med_gz": "1.65", "med_os": "1.28", "gp_gz": "4", "gp_os": "6",
            "ht_gz": "81.00%", "ht_os": "71.50%", "w_p15": "85%", "w_gg": "58%"
        }
    }
