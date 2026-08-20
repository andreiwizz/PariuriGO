import streamlit as st

def aplica_stiluri_aplicatie_elita():
    st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        .stApp {
            background-color: #030305 !important;
            color: #ffffff !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        h1, h2, h3, h4, p, span, label {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #ffffff !important;
        }

        /* STRUCTURA DE TELEFON MOBIL CENTRATĂ (GLASSMORPHISM) */
        .phone-wrapper-container {
            max-width: 410px;
            margin: 40px auto;
            background: rgba(18, 18, 24, 0.8) !important;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 40px;
            padding: 24px;
            box-shadow: 0 25px 50px -12px rgba(157, 0, 255, 0.2);
        }
        
        /* Dynamic Island / Notch elegant pe iPhone */
        .phone-notch {
            width: 110px;
            height: 25px;
            background: #000000;
            margin: -12px auto 25px auto;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        /* Intrări de text moderne */
        .stTextInput div[data-baseweb="input"] {
            background-color: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 14px !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        .stTextInput div[data-baseweb="input"]:focus-within {
            border-color: #a855f7 !important;
            box-shadow: 0 0 12px rgba(168, 85, 247, 0.2) !important;
            background-color: rgba(255, 255, 255, 0.05) !important;
        }
        
        .stTextInput input {
            color: #ffffff !important;
            font-size: 15px !important;
            font-weight: 500 !important;
        }

        /* Butonul Premium cu gradient fin și reflexii */
        div.stButton > button {
            background: linear-gradient(135deg, #a855f7 0%, #6366f1 100%) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            font-size: 15px !important;
            letter-spacing: 0.3px !important;
            border: none !important;
            width: 100% !important;
            border-radius: 14px !important;
            padding: 12px !important;
            box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4) !important;
            transition: all 0.2s ease !important;
        }
        
        div.stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 12px 25px -5px rgba(168, 85, 247, 0.5) !important;
        }

        /* Stilul cardurilor de sport din interior */
        .premium-sport-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 18px;
            padding: 16px;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .sport-left-section { display: flex; align-items: center; gap: 14px; }
        .sport-icon-box { background: rgba(255, 255, 255, 0.04); width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 20px; border: 1px solid rgba(255, 255, 255, 0.05); }
        .card-main-title { font-size: 16px; font-weight: 700; margin: 0; }
        .card-sub-desc { font-size: 12px; color: #8e8e93; margin: 2px 0 0 0; }
        .tag-active { background: rgba(52, 211, 153, 0.1); color: #34d399 !important; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
        .tag-upcoming { background: rgba(255, 255, 255, 0.03); color: #8e8e93 !important; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)
