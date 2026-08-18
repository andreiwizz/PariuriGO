import streamlit as st

def setari_estetice(bg_style):
    st.markdown(f"""
    <style>
        @import url('https://googleapis.com');
        .stApp {{ background-color: #030805 !important; color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; }}
        h1, h2, h3, h4, p, span, label {{ font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important; }}
        div[data-testid="column"]:nth-of-type(1) {{
            background-color: #06140c !important; border-right: 2px solid rgba(0, 255, 102, 0.2) !important;
            padding: 30px 25px !important; border-radius: 20px 0 0 20px !important; box-shadow: inset -10px 0 30px rgba(0,0,0,0.5) !important;
        }}
        div[data-testid="column"]:nth-of-type(2) {{
            background-color: #0d0d0d !important; padding: 30px 25px !important;
            border-radius: 0 20px 20px 0 !important; box-shadow: inset 10px 0 30px rgba(0,0,0,0.8) !important;
        }}
        button div {{ font-size: 0px !important; }} button div:before {{ font-size: 16px !important; }}
        .inner-cyber-card {{ background: rgba(0, 0, 0, 0.4) !important; border: 1px solid rgba(0, 255, 102, 0.15) !important; border-radius: 14px !important; padding: 20px !important; margin-bottom: 20px !important; }}
        .vip-card-box {{ background: #121212 !important; border-left: 4px solid #00ff66 !important; border-radius: 8px !important; padding: 22px !important; margin-bottom: 22px !important; }}
        div[data-testid="stSelectbox"] div[data-baseweb="select"] {{ background-color: #020503 !important; border: 1px solid #00ff66 !important; color: #ffffff !important; border-radius: 8px !important; }}
        .cyber-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; text-align: center; margin: 20px 0; }}
        .cyber-grid-item {{ background: rgba(0, 255, 102, 0.02); border: 1px solid rgba(0, 255, 102, 0.08); border-radius: 10px; padding: 14px 10px; }}
        .cyber-num {{ font-size: 26px; font-weight: 800; color: #00ff66; }}
        .cyber-label {{ font-size: 13px; color: #94a3b8; text-transform: uppercase; }}
        .proc-row {{ display: flex; justify-content: space-between; align-items: center; background: rgba(0, 255, 102, 0.03); border-left: 3px solid #00ff66; padding: 12px 16px; margin: 10px 0; }}
        .proc-badge {{ background: #00ff66; color: #000000; font-weight: 800; padding: 4px 10px; border-radius: 4px; }}
        .bar-wrapper {{ margin: 16px 0; }} .bar-title-flex {{ display: flex; justify-content: space-between; font-size: 15px; }}
        .bar-container-custom {{ width: 100%; background: rgba(255, 255, 255, 0.04); border-radius: 10px; height: 16px; overflow: hidden; }}
        .bar-fill-neon-custom {{ height: 100%; background: linear-gradient(90deg, #005c20 0%, #00ff66 100%); border-radius: 10px; }}
        div[data-testid="stLinkButton"] a {{
            background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important; color: #000000 !important;
            font-weight: 800 !important; font-size: 18px !important; border-radius: 8px !important; padding: 14px 20px !important;
            display: block !important; text-align: center !important; text-decoration: none !important;
            box-shadow: 0 4px 20px rgba(0, 255, 102, 0.3) !important; animation: glowPulseAnimate 2s infinite ease-in-out !important;
        }}
        @keyframes glowPulseAnimate {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.02); }} 100% {{ transform: scale(1); }} }}
    </style>
    """, unsafe_allow_html=True)

def preia_meciuri():
    return {
        "FCSB vs Rapid București": {
            "liga": "ROMÂNIA SUPERLIGA", "g_gz": "14", "g_os": "11", "med_gz": "1.75", "med_os": "1.37", "gp_gz": "5", "gp_os": "9",
            "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%", "p15_gz": "91.20%", "p25_gz": "64.29%", "gg_gz": "71.43%",
            "w_p15": "85%", "w_p25": "64%", "w_p05r1": "85%", "w_gg": "71%"
        },
        "CFR Cluj vs Universitatea Craiova": {
            "liga": "ROMÂNIA SUPERLIGA", "g_gz": "11", "g_os": "13", "med_gz": "1.37", "med_os": "1.62", "gp_gz": "7", "gp_os": "6",
            "ht_gz": "75.00%", "ht_os": "62.50%", "st_gz": "87.50%", "st_os": "75.00%", "p15_gz": "87.50%", "p25_gz": "50.00%", "gg_gz": "62.50%",
            "w_p15": "81%", "w_p25": "56%", "w_p05r1": "68%", "w_gg": "62%"
        }
    }
