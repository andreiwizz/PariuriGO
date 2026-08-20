import streamlit as st
import base64

# 1. Configurare Pagina Full-Screen Nativa
st.set_page_config(
    page_title="PariuriGO • VIP App",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Functie securizata pentru transformarea imaginii din folder in fundal web
def aplica_fundal_teren_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            @import url('https://googleapis.com');
            
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.92), rgba(6, 4, 15, 0.95)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
                color: #ffffff !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }
            
            h1, h2, h3, h4, p, span, label { font-family: 'Plus Jakarta Sans', sans-serif !important; }

            /* TELEFONUL MOBIL CENTRAT MAT DIN SENSUL TRIMIS */
            .phone-wrapper-container {
                max-width: 410px;
                margin: 40px auto;
                background: rgba(13, 11, 22, 0.88) !important;
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                border: 1px solid rgba(176, 66, 255, 0.22);
                border-radius: 42px;
                padding: 24px;
                box-shadow: 0 35px 80px -15px rgba(157, 0, 255, 0.35);
                position: relative;
                min-height: 735px;
            }
            
            .phone-notch {
                width: 115px; height: 24px; background: #000000;
                margin: -12px auto 25px auto; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.03);
            }

            .stTextInput div[data-baseweb="input"] {
                background-color: rgba(255, 255, 255, 0.03) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                border-radius: 14px !important;
            }
            .stTextInput input { color: #ffffff !important; font-size: 15px; }

            div.stButton > button {
                background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%) !important;
                color: #ffffff !important;
                font-weight: 700 !important;
                font-size: 15px !important;
                border: none !important;
                width: 100% !important;
                border-radius: 14px !important;
                padding: 12px !important;
                box-shadow: 0 8px 20px rgba(176, 66, 255, 0.25) !important;
            }
            div.stButton > button:hover { transform: translateY(-1px) !important; box-shadow: 0 10px 25px rgba(176, 66, 255, 0.4) !important; }

            .app-bottom-navbar {
                display: flex; justify-content: space-around; align-items: center;
                background: #141419; border-top: 1px solid #27272a; padding: 12px 5px; margin-top: 25px; border-radius: 0 0 24px 24px;
            }
            .nav-item-bottom { text-align: center; font-size: 11px; color: #a1a1aa; font-weight: 700; }
            .nav-item-center-gold {
                background: linear-gradient(135deg, #b042ff 0%, #7900f2 100%);
                width: 44px; height: 44px; border-radius: 50%;
                display: flex; align-items: center; justify-content: center; font-size: 20px;
                margin-top: -24px; box-shadow: 0 4px 15px rgba(176, 66, 255, 0.4);
            }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

aplica_fundal_teren_local("teren.jpg")

if "user_logat" not in st.session_state: st.session_state.user_logat = False
if "baza_date_utilizatori" not in st.session_state: st.session_state.baza_date_utilizatori = {"admin": "pariurigo", "andreiwizz": "Parola123parola"}
if "mod_ecran_autentificare" not in st.session_state: st.session_state.mod_ecran_autentificare = "login"

st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)
if not st.session_state.user_logat:
    if st.session_state.mod_ecran_autentificare == "login":
        st.markdown("<h1 style='text-align:center; font-size:36px; font-weight:800; background: linear-gradient(135deg, #ffffff 0%, #b042ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom:5px;'>PariuriGO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:30px; font-weight:500;'>Sign in to deblock the premium center</p>", unsafe_allow_html=True)
        
        username = st.text_input("USER IDENTITY", placeholder="Username...", key="user_login_premium")
        password = st.text_input("SECURE KEY", type="password", placeholder="Password...", key="pass_login_premium")
        
        st.write("")
        if st.button("👉 SIGN IN TO APPLICATION", key="btn_exec_login_v6"):
            if username in st.session_state.baza_date_utilizatori and st.session_state.baza_date_utilizatori[username] == password:
                st.session_state.user_logat = True
                st.rerun()
            else: st.error("Access Denied! Wrong data.")
                
        st.write("---")
        st.markdown("<p style='text-align:center; font-size:13px; color:#8e8e93;'>New to our network?</p>", unsafe_allow_html=True)
        if st.button("➕ CREATE PROFILE ACCOUNT 🚀", key="btn_go_to_reg_v6"):
            st.session_state.mod_ecran_autentificare = "register"
            st.rerun()

    elif st.session_state.mod_ecran_autentificare == "register":
        st.markdown("<h1 style='text-align:center; font-size:28px; font-weight:800; color:#b042ff; margin-bottom:5px;'>Sign Up</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:0; margin-bottom:25px;'>Create a permanent member profile</p>", unsafe_allow_html=True)
        
        new_user = st.text_input("CHOOSE USERNAME", placeholder="Username...", key="reg_user_v6")
        new_pass = st.text_input("CHOOSE SECURE KEY", type="password", placeholder="Password...", key="reg_pass_v6")
        confirm_pass = st.text_input("CONFIRM SECURE KEY", type="password", placeholder="Repeat password...", key="reg_pass_conf_v6")
        
        st.write("")
        if st.button("✨ REGISTER PROFILE NOW", key="btn_exec_reg_v6"):
            if not new_user or not new_pass: st.error("All areas required!")
            elif new_user in st.session_state.baza_date_utilizatori: st.error("Username taken!")
            elif new_pass != confirm_pass: st.error("Keys mismatch!")
            else:
                st.session_state.baza_date_utilizatori[new_user] = new_pass
                st.success("Account created!")
                st.session_state.mod_ecran_autentificare = "login"
                st.rerun()
        st.write("---")
        if st.button("⬅️ BACK TO LOG IN", key="btn_back_v6"):
            st.session_state.mod_ecran_autentificare = "login"
            st.rerun()
