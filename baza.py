import streamlit as st

def setari_stil_mov(bg_style):
    st.markdown(f"""
    <style>
        @import url('https://googleapis.com');
        .stApp {{ {bg_style} color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; }}
        h1, h2, h3, h4, p, span, label {{ color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important; }}
        button div {{ font-size: 0px !important; }} button div:before {{ font-size: 16px !important; }}
        section[data-testid="stSidebar"] {{ background-color: #0b071e !important; border-right: 1px solid rgba(157, 0, 255, 0.3) !important; }}
        .glass-box-container {{ background: #000000 !important; border: 1px solid #1a0f30 !important; border-radius: 16px !important; padding: 24px !important; box-shadow: 0 20px 40px rgba(157, 0, 255, 0.15) !important; margin-bottom: 25px !important; }}
        .vip-card-box {{ background: #090615 !important; border: 1px solid #9d00ff !important; border-radius: 14px !important; padding: 22px !important; margin-bottom: 22px !important; }}
        div[data-testid="stSelectbox"] div[data-baseweb="select"] {{ background-color: #0c081f !important; border: 1px solid #9d00ff !important; color: #ffffff !important; }}
        .stat-container {{ width: 100%; }} .stat-row {{ display: flex; justify-content: space-between; align-items: center; margin: 14px 0; text-align: center; }}
        .stat-left-val, .stat-right-val {{ width: 20%; font-size: 20px; font-weight: 800; color: #ffffff; }}
        .stat-center-label {{ width: 60%; font-size: 15px; font-weight: 700; color: #cbd5e1; text-transform: uppercase; }}
        .mov-badge-tiktok {{ background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important; color: #ffffff !important; padding: 5px 20px; border-radius: 6px; font-size: 16px; font-weight: 800; display: inline-block; }}
        .bar-wrapper {{ margin: 14px 0; }} .bar-container-custom {{ width: 100%; background: #130d24; border-radius: 20px; height: 22px; overflow: hidden; border: 1px solid #281947; }}
        .bar-fill-mov-tiktok {{ height: 100%; background: linear-gradient(90deg, #6c00d9 0%, #b042ff 100%) !important; border-radius: 20px; display: flex; align-items: center; justify-content: flex-end; padding-right: 12px; font-size: 13px; font-weight: 800; color: #ffffff; }}
        div[data-testid="stLinkButton"] a {{ background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important; color: #ffffff !important; font-weight: 800 !important; font-size: 17px !important; border-radius: 8px !important; padding: 13px 20px !important; display: block !important; text-align: center !important; text-decoration: none !important; }}
        .green-footer-box {{ background: rgba(157, 0, 255, 0.05); border: 1px solid rgba(157, 0, 255, 0.2); border-radius: 10px; padding: 12px 15px; margin-top: 20px; display: flex; align-items: center; gap: 10px; }}
    </style>
    """, unsafe_allow_html=True)

def dictionar_meciuri():
    return {
        "Bașakșehir vs Kocaelispor": {
            "liga": "SUPER LIG (TURKEY)", "g_gz": "7", "g_os": "3", "med_gz": "1.00", "med_os": "0.43", "gp_gz": "8", "gp_os": "6",
            "ht_gz": "71.43%", "ht_os": "57.14%", "st_gz": "71.43%", "st_os": "57.14%", "p15_gz": "85.71%", "p15_os": "42.86%",
            "p25_gz": "28.57%", "p25_os": "42.86%", "gg_gz": "57.14%", "gg_os": "42.86%", "c_gz": "14.29%", "c_os": "28.57%", "cor_gz": "14.29%", "cor_os": "14.29%",
            "w_p15": "64.29%", "w_p25": "14.29%", "w_p05r1": "64.29%", "w_p05r2": "64.29%", "w_gg": "50.00%", "w_c35": "21.43%", "w_cor95": "14.29%"
        },
        "FCSB vs Rapid București": {
            "liga": "ROMÂNIA SUPERLIGA", "g_gz": "14", "g_os": "11", "med_gz": "1.75", "med_os": "1.37", "gp_gz": "5", "gp_os": "9",
            "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%", "p15_gz": "91.20%", "p15_os": "78.50%",
            "p25_gz": "64.29%", "p25_os": "50.00%", "gg_gz": "71.43%", "gg_os": "57.14%", "c_gz": "14.29%", "c_os": "28.57%", "cor_gz": "-", "cor_os": "14.29%",
            "w_p15": "85.00%", "w_p25": "64.29%", "w_p05r1": "85.71%", "w_p05r2": "78.50%", "w_gg": "71.43%", "w_c35": "21.43%", "w_cor95": "14.29%"
        }
    }
