import streamlit as st

def aplica_stiluri_champions():
    bg_url = "https://unsplash.com"
    st.markdown(f"""
    <style>
        @import url('https://googleapis.com');
        .stApp {{ background: linear-gradient(rgba(10, 5, 28, 0.93), rgba(4, 2, 15, 0.96)), url('{bg_url}') !important; background-size: cover !important; background-position: center !important; background-repeat: no-repeat !important; background-attachment: fixed !important; color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; }}
        h1, h2, h3, h4, p, span, label {{ color: #ffffff !important; font-family: 'Rajdhani', sans-serif !important; font-weight: 700 !important; }}
        button div {{ font-size: 0px !important; }} button div:before {{ font-size: 16px !important; }}
        section[data-testid="stSidebar"] {{ background-color: #0b071e !important; border-right: 1px solid rgba(157, 0, 255, 0.3) !important; }}
        .glass-box-container {{ background: #000000 !important; border: 1px solid #1a0f30 !important; border-radius: 16px !important; padding: 24px !important; box-shadow: 0 20px 40px rgba(157, 0, 255, 0.15) !important; margin-bottom: 25px !important; }}
        .vip-card-box {{ background: #090615 !important; border: 1px solid #9d00ff !important; border-radius: 14px !important; padding: 22px !important; margin-bottom: 22px !important; }}
        div[data-testid="stSelectbox"] div[data-baseweb="select"] {{ background-color: #0c081f !important; border: 1px solid #9d00ff !important; color: #ffffff !important; border-radius: 8px !important; }}
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

def descarca_meciuri_zile(zi_selectata):
    if zi_selectata == "Azi":
        return {
            "Bodø/Glimt vs Crvena Zvezda": {
                "liga": "CHAMPIONS LEAGUE - PLAY-OFF", "g_gz": "16", "g_os": "11", "med_gz": "1.90", "med_os": "1.45", "gp_gz": "4", "gp_os": "5",
                "ht_gz": "82.50%", "ht_os": "74.10%", "st_gz": "88.00%", "st_os": "81.30%", "p15_gz": "91.20%", "p15_os": "84.10%",
                "p25_gz": "65.50%", "p25_os": "52.20%", "gg_gz": "71.00%", "gg_os": "61.50%", "c_gz": "14.20%", "c_os": "22.10%", "cor_gz": "-", "cor_os": "12.40%",
                "w_p15": "88%", "w_p25": "62%", "w_p05r1": "82%", "w_p05r2": "88%", "w_gg": "71%", "w_c35": "24%", "w_cor95": "35%"
            },
            "Dinamo Zagreb vs Qarabağ FK": {
                "liga": "CHAMPIONS LEAGUE - PLAY-OFF", "g_gz": "15", "g_os": "13", "med_gz": "1.80", "med_os": "1.65", "gp_gz": "5", "gp_os": "6",
                "ht_gz": "85.00%", "ht_os": "78.40%", "st_gz": "84.50%", "st_os": "82.10%", "p15_gz": "89.40%", "p15_os": "86.20%",
                "p25_gz": "61.20%", "p25_os": "55.00%", "gg_gz": "68.30%", "gg_os": "64.00%", "c_gz": "18.00%", "c_os": "24.50%", "cor_gz": "-", "cor_os": "14.10%",
                "w_p15": "89%", "w_p25": "58%", "w_p05r1": "85%", "w_p05r2": "84%", "w_gg": "66%", "w_c35": "28%", "w_cor95": "31%"
            },
            "Lille OSC vs Slavia Praga": {
                "liga": "CHAMPIONS LEAGUE - PLAY-OFF", "g_gz": "12", "g_os": "9", "med_gz": "1.45", "med_os": "1.20", "gp_gz": "3", "gp_os": "4",
                "ht_gz": "72.10%", "ht_os": "65.30%", "st_gz": "79.00%", "st_os": "71.20%", "p15_gz": "82.00%", "p15_os": "76.40%",
                "p25_gz": "48.00%", "p25_os": "41.50%", "gg_gz": "55.00%", "gg_os": "49.00%", "c_gz": "16.10%", "c_os": "19.30%", "cor_gz": "-", "cor_os": "11.50%",
                "w_p15": "79%", "w_p25": "45%", "w_p05r1": "72%", "w_p05r2": "79%", "w_gg": "52%", "w_c35": "33%", "w_cor95": "21%"
            }
        }
    else:
        return {
            "Dynamo Kiev vs FC Salzburg": {
                "liga": "CHAMPIONS LEAGUE - PLAY-OFF (MÂINE)", "g_gz": "17", "g_os": "19", "med_gz": "2.05", "med_os": "2.20", "gp_gz": "6", "gp_os": "5",
                "ht_gz": "89.10%", "ht_os": "91.30%", "st_gz": "86.40%", "st_os": "88.90%", "p15_gz": "94.00%", "p15_os": "95.20%",
                "p25_gz": "70.10%", "p25_os": "74.30%", "gg_gz": "75.00%", "gg_os": "78.40%", "c_gz": "20.50%", "c_os": "18.20%", "cor_gz": "-", "cor_os": "16.50%",
                "w_p15": "93%", "w_p25": "72%", "w_p05r1": "89%", "w_p05r2": "86%", "w_gg": "76%", "w_c35": "41%", "w_cor95": "45%"
            },
            "Malmö FF vs Sparta Praga": {
                "liga": "CHAMPIONS LEAGUE - PLAY-OFF (MÂINE)", "g_gz": "14", "g_os": "15", "med_gz": "1.65", "med_os": "1.78", "gp_gz": "5", "gp_os": "6",
                "ht_gz": "81.00%", "ht_os": "83.50%", "st_gz": "84.20%", "st_os": "85.00%", "p15_gz": "88.50%", "p15_os": "89.10%",
                "p25_gz": "58.00%", "p25_os": "61.20%", "gg_gz": "64.50%", "gg_os": "67.10%", "c_gz": "23.00%", "c_os": "21.40%", "cor_gz": "-", "cor_os": "13.90%",
                "w_p15": "88%", "w_p25": "59%", "w_p05r1": "81%", "w_p05r2": "84%", "w_gg": "65%", "w_c35": "36%", "w_cor95": "28%"
            },
            "FC Midtjylland vs Slovan Bratislava": {
                "liga": "CHAMPIONS LEAGUE - PLAY-OFF (MÂINE)", "g_gz": "13", "g_os": "10", "med_gz": "1.55", "med_os": "1.30", "gp_gz": "4", "gp_os": "5",
                "ht_gz": "76.30%", "ht_os": "69.10%", "st_gz": "81.20%", "st_os": "74.50%", "p15_gz": "85.00%", "p15_os": "79.80%",
                "p25_gz": "52.00%", "p25_os": "46.30%", "gg_gz": "59.00%", "gg_os": "53.20%", "c_gz": "17.40%", "c_os": "22.80%", "cor_gz": "-", "cor_os": "12.10%",
                "w_p15": "82%", "w_p25": "49%", "w_p05r1": "76%", "w_p05r2": "81%", "w_gg": "56%", "w_c35": "30%", "w_cor95": "23%"
            }
        }
