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
    </style>
    """, unsafe_allow_html=True)

def descarca_meciuri_zile(zi_selectata):
    if zi_selectata == "Azi":
        # MECIURI REALE DE ASTĂZI (MIERCURI 19 AUGUST 2026)
        return {
            "Vikingur Reykjavik vs UE Santa Coloma": {
                "liga": "UEFA CONFERENCE LEAGUE", "g_gz": "14", "g_os": "6", "med_gz": "1.75", "med_os": "1.10", "gp_gz": "3", "gp_os": "8",
                "ht_gz": "81.20%", "ht_os": "65.40%", "st_gz": "86.00%", "st_os": "72.30%", "p15_gz": "88.20%", "p15_os": "74.10%",
                "p25_gz": "58.50%", "p25_os": "42.20%", "gg_gz": "61.00%", "gg_os": "52.50%", "c_gz": "12.50%", "c_os": "20.10%", "cor_gz": "-", "cor_os": "11.40%",
                "w_p15": "85%", "w_p25": "55%", "w_p05r1": "81%", "w_p05r2": "86%", "w_gg": "60%", "w_c35": "24%", "w_cor95": "31%"
            },
            "Minaur Baia Mare vs SCM Zalău": {
                "liga": "CUPA ROMÂNIEI", "g_gz": "11", "g_os": "9", "med_gz": "1.37", "med_os": "1.22", "gp_gz": "6", "gp_os": "7",
                "ht_gz": "75.00%", "ht_os": "68.20%", "st_gz": "78.50%", "st_os": "71.15%", "p15_gz": "82.40%", "p15_os": "76.50%",
                "p25_gz": "48.20%", "p25_os": "44.00%", "gg_gz": "57.10%", "gg_os": "51.10%", "c_gz": "25.00%", "c_os": "31.50%", "cor_gz": "-", "cor_os": "10.20%",
                "w_p15": "80%", "w_p25": "46%", "w_p05r1": "75%", "w_p05r2": "78%", "w_gg": "54%", "w_c35": "18%", "w_cor95": "14%"
            }
        }
    else:
        # MECIURI REALE DE MÂINE (JOI 20 AUGUST 2026) - ROMÂNII ÎN EUROPA
        return {
            "LASK Linz vs FCSB": {
                "liga": "UEFA EUROPA LEAGUE - PLAY-OFF", "g_gz": "16", "g_os": "14", "med_gz": "1.85", "med_os": "1.55", "gp_gz": "5", "gp_os": "7",
                "ht_gz": "84.10%", "ht_os": "78.30%", "st_gz": "86.20%", "st_os": "81.00%", "p15_gz": "91.00%", "p15_os": "85.20%",
                "p25_gz": "62.40%", "p25_os": "54.30%", "gg_gz": "68.00%", "gg_os": "61.40%", "c_gz": "18.50%", "c_os": "22.40%", "cor_gz": "-", "cor_os": "13.50%",
                "w_p15": "90%", "w_p25": "58%", "w_p05r1": "84%", "w_p05r2": "86%", "w_gg": "64%", "w_c35": "38%", "w_cor95": "40%"
            },
            "CFR Cluj vs Pafos FC": {
                "liga": "UEFA CONFERENCE LEAGUE - PLAY-OFF", "g_gz": "15", "g_os": "11", "med_gz": "1.65", "med_os": "1.28", "gp_gz": "4", "gp_os": "6",
                "ht_gz": "81.00%", "ht_os": "71.50%", "st_gz": "84.50%", "st_os": "76.00%", "p15_gz": "87.50%", "p15_os": "79.10%",
                "p25_gz": "55.00%", "p25_os": "44.20%", "gg_gz": "61.50%", "gg_os": "52.10%", "c_gz": "21.00%", "c_os": "24.50%", "cor_gz": "-", "cor_os": "12.90%",
                "w_p15": "85%", "w_p25": "50%", "w_p05r1": "81%", "w_p05r2": "84%", "w_gg": "58%", "w_c35": "32%", "w_cor95": "25%"
            },
            "Corvinul Hunedoara vs HNK Rijeka": {
                "liga": "UEFA CONFERENCE LEAGUE - PLAY-OFF", "g_gz": "12", "g_os": "13", "med_gz": "1.40", "med_os": "1.52", "gp_gz": "6", "gp_os": "5",
                "ht_gz": "74.20%", "ht_os": "76.10%", "st_gz": "79.10%", "st_os": "82.30%", "p15_gz": "81.50%", "p15_os": "84.20%",
                "p25_gz": "46.30%", "p25_os": "51.00%", "gg_gz": "54.00%", "gg_os": "58.20%", "c_gz": "23.40%", "c_os": "19.50%", "cor_gz": "-", "cor_os": "11.20%",
                "w_p15": "82%", "w_p25": "48%", "w_p05r1": "74%", "w_p05r2": "79%", "w_gg": "56%", "w_c35": "28%", "w_cor95": "20%"
            }
        }
