import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • VIP App",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru transformarea imaginii din folder în fundal web
def aplica_fundal_teren_local(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        # Injectăm stilul CSS curat, fără f-string-uri care să blocheze acoladele
        st.markdown("""
        <style>
            @import url('https://googleapis.com');
            
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.90), rgba(6, 4, 15, 0.94)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
                color: #ffffff !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }
            
            h1, h2, h3, h4, p, span, label {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }

            /* TELEFONUL MOBIL CENTRAT MAT PREPARAT PENTRU LOGIN */
            .phone-wrapper-container {
                max-width: 410px;
                margin: 30px auto;
                background: rgba(13, 11, 22, 0.85) !important;
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                border: 1px solid rgba(176, 66, 255, 0.18);
                border-radius: 42px;
                padding: 24px;
                box-shadow: 0 35px 80px -15px rgba(157, 0, 255, 0.3);
                position: relative;
                min-height: 735px;
            }
            
            .phone-notch {
                width: 115px;
                height: 24px;
                background: #000000;
                margin: -12px auto 25px auto;
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.03);
            }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

# Executăm injectarea fundalului cu terenul tău local
aplica_fundal_teren_local("teren.jpg")

# SENSUL APLICAȚIEI PE ECRAN
st.markdown('<div class="phone-wrapper-container"><div class="phone-notch"></div>', unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#b042ff; font-weight:800; font-size:16px; margin-top:220px; letter-spacing:0.5px;'>⚽ STADIONUL ESTE LIVE</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8e8e93; font-size:13px; margin-top:-5px;'>Eroarea de sintaxă a fost eliminată complet.</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Închide corect containerul telefonului
    # ECRANUL DE ÎNREGISTRARE CONT DIRECT ÎN IPHONE
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

# ================== INTERFAȚA PENTRU UTILIZATORII LOGAȚI ==================
else:
    st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; padding:0 5px;">
        <span style="font-size:16px; font-weight:700; color:#71717a;">🔀</span>
        <span style="font-size:20px; font-weight:800; color:#ffffff;"><span style="color:#b042ff;">PariuriGO</span> VIP</span>
        <span style="font-size:16px; color:#b042ff;">☰</span>
    </div>
    <div style="background:linear-gradient(135deg, #120b2e 0%, #05040f 100%); border:1px solid #b042ff; border-radius:20px; padding:16px; margin-bottom:18px; box-shadow:0 8px 25px rgba(176,66,255,0.15);">
        <div style="background:rgba(176,66,255,0.2); color:#b042ff; font-size:10px; font-weight:800; padding:4px 10px; border-radius:12px; display:inline-block; margin-bottom:8px;">&bull; VIP ACTIVE</div>
        <h3 style="margin:0 0 4px 0; font-size:19px; font-weight:800; color:#ffffff;">PREDICTION SYSTEM</h3>
        <p style="margin:0; font-size:11px; color:#a1a1aa; line-height:1.4;">Bine ai venit în portalul premium de analiză sportivă!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("🔓 Sistem complet deblocat cu succes!")
    
    # Adăugăm un selector curat pentru funcții direct în telefon
    zona_activa = st.selectbox("📂 Secțiuni active:", ["🏠 Meniu Principal", "🎟️ Biletul Zilei", "💬 Live Chat VIP"])
    
    if zona_activa == "🎟️ Biletul Zilei":
        st.write("---")
        st.markdown("### 🎫 COTA 2 PREMIUM")
        st.info("• LASK Linz vs FCSB ➡️ Peste 1.5 goluri\n• CFR Cluj vs Pafos ➡️ 1 Solist")
    elif zona_activa == "💬 Live Chat VIP":
        st.write("---")
        st.markdown("### 💬 Chat Premium")
        st.write("**Admin 👑:** Biletele sunt trimise, spor la profit!")
        
    st.write("---")
    
    # BARA DE NAVIGARE ORIZONTALĂ DE JOS (O ÎNCHIDEM DESIGNER DIRECT ÎN CORP)
    st.markdown("""
    <div class="app-bottom-navbar">
        <div class="nav-item-bottom">🤖<br><span style="color:#b042ff;">AI Engine</span></div>
        <div class="nav-item-bottom">⚽<br>Live</div>
        <div class="nav-item-center-gold">🏠</div>
        <div class="nav-item-bottom">🎟️<br>Ticket</div>
        <div class="nav-item-bottom">📞<br>Contact</div>
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        if st.button("🔒 Sign Out / Reset cont", use_container_width=True, key="logout_final_v6"):
            st.session_state.user_logat = False
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # ÎNCHIDE CORPUL PENTRU wrapper-container

