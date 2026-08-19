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
            margin-bottom: 35px;
        }
        
        .store-btn {
            background: #000000;
            border: 1px solid rgba(176, 66, 255, 0.4);
            border-radius: 8px;
            padding: 8px 20px;
            display: flex;
            vertical-align: center;
            gap: 10px;
            text-decoration: none;
            box-shadow: 0 4px 15px rgba(157, 0, 255, 0.1);
        }
        
        .store-btn:hover {
            border-color: #b042ff;
            box-shadow: 0 0 20px rgba(176, 66, 255, 0.4);
        }

        /* CARDURILE PREMIUM TIP APLICAȚIE - COPIE DUPĂ FILMETUL TĂU */
        .sport-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 12px 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .sport-info {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .sport-title {
            font-size: 16px;
            font-weight: 800;
            margin: 0;
        }
        
        .sport-desc {
            font-size: 11px;
            color: #a0aec0;
            margin: 0;
        }
        
        /* Insignele verzi cu AVAILABLE ca in imaginea ta */
        .badge-available {
            background: rgba(0, 255, 102, 0.1);
            color: #00ff66 !important;
            border: 1px solid #00ff66;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.5px;
        }
        
        /* Insignele gri cu SOON */
        .badge-soon {
            background: rgba(255, 255, 255, 0.05);
            color: #a0aec0 !important;
            border: 1px solid #4a5568;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 800;
        }
    </style>
    """, unsafe_allow_html=True)
