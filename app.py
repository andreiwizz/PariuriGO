import streamlit as st
import base64
from datetime import datetime

# ==============================================================================
# 1. CONFIGURARE INTERFAȚĂ ȘI DATA CURENTĂ (MANDATORIU PRIMA LINIE)
# ==============================================================================
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

# ==============================================================================
# 2. CITIRE ȘI DECORARE FOND PREMIUM (TEREN.JPG)
# ==============================================================================
def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.95), rgba(2, 6, 4, 0.97)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #030a05 !important;"

# ==============================================================================
# 3. STILIZARE CSS PREMIUM (HOLOGRAPHIC CYBERPUNK - GLASSMORPHISM)
# ==============================================================================
st.markdown(f"""
<style>
    @import url('https://googleapis.com');
    
    .stApp {{
        {bg_style}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    
    h1, h2, h3, h4, p, span, label, th, td {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    
    /* Fix premium pentru butoanele de control din aplicatie */
    div.stButton > button {{
        background: linear-gradient(135deg, rgba(0, 255, 102, 0.15) 0%, rgba(0, 92, 32, 0.05) 100%) !important;
        color: #00ff66 !important;
        border: 1px solid #00ff66 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        border-radius: 12px !important;
        padding: 16px 30px !important;
        width: 100% !important;
        display: block !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 4px 15px rgba(0, 255, 102, 0.1) !important;
    }}

    div.stButton > button:hover {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(0, 255, 102, 0.6) !important;
        transform: translateY(-3px);
    }}
    
    div.stButton > button div {{
        font-size: 15px !important;
    }}
    
    .pricing-card-lux {{
        background: linear-gradient(135deg, rgba(6, 24, 14, 0.85) 0%, rgba(2, 10, 5, 0.95) 100%) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin-top: 10px;
    }}
    
    .pricing-border-low {{ border: 1px solid rgba(0, 255, 102, 0.3) !important; }}
    .pricing-border-medium {{ border: 1px solid rgba(255, 204, 0, 0.3) !important; }}
    .pricing-border-high {{ border: 1px solid rgba(255, 0, 85, 0.4) !important; }}

    .stripe-luxury-btn {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 20px !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        text-decoration: none !important;
        margin-top: 25px;
    }}
    
    .stripe-low-med {{ background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important; color: #000000 !important; }}
    .stripe-high {{ background: linear-gradient(135deg, #ff0055 0%, #b3003b 100%) !important; color: #ffffff !important; }}

    .stTextInput input {{
        background: rgba(0, 0, 0, 0.6) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 14px !important;
    }}

    .full-screen-login-card {{
        background: linear-gradient(135deg, rgba(6, 26, 14, 0.95) 0%, rgba(2, 12, 6, 0.99) 100%) !important;
        backdrop-filter: blur(25px) !important;
        border: 2px solid rgba(0, 255, 102, 0.4) !important;
        border-radius: 24px !important;
        padding: 45px !important;
        max-width: 500px;
        margin: 40px auto !important;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9) !important;
    }}

    @keyframes neonDanger {{
        0% {{ box-shadow: 0 0 10px rgba(255, 0, 85, 0.2); border-color: rgba(255, 0, 85, 0.4); }}
        50% {{ box-shadow: 0 0 25px rgba(255, 0, 85, 0.8); border-color: #ff0055; transform: scale(1.01); }}
        100% {{ box-shadow: 0 0 10px rgba(255, 0, 85, 0.2); border-color: rgba(255, 0, 85, 0.4); }}
    }}

    .flame-card-active {{
        background: linear-gradient(135deg, rgba(20, 4, 10, 0.9) 0%, rgba(5, 1, 2, 0.98) 100%) !important;
        border-radius: 20px !important;
        padding: 25px !important;
        margin-top: 20px;
        animation: neonDanger 2s infinite ease-in-out;
    }}

    @keyframes textGlow {{
        0% {{ opacity: 0.8; text-shadow: 0 0 5px #ff0055; }}
        50% {{ opacity: 1; text-shadow: 0 0 20px #ff0055, 0 0 30px #ff0055; }}
        100% {{ opacity: 0.8; text-shadow: 0 0 5px #ff0055; }}
    }}

    .live-alert-text {{
        color: #ff0055;
        font-weight: 800;
        font-size: 14px;
        letter-spacing: 2px;
        text-transform: uppercase;
        animation: textGlow 1.5s infinite ease-in-out;
    }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)
st.write("---")
# ==============================================================================
# 4. INITIALIZARE MEMORIE ȘI CONTROL AUTOMAT CALENDAR
# ==============================================================================
if "lista_membri" not in st.session_state:
    st.session_state.lista_membri = {"admin": "pariurigo"}

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

if "ecran_login" not in st.session_state:
    st.session_state.ecran_login = False

# Generator dinamic bazat pe algoritm de dată
def genereaza_meciuri_dupa_data(data_string):
    zi_num = sum(ord(c) for c in data_string)
    elite_gazde = ["Real Madrid", "Barcelona", "Manchester Utd", "FCSB", "Bayern Munchen", "Inter Milano", "Liverpool", "Juventus"]
    elite_oaspeti = ["Man City", "Arsenal", "Rapid Bucuresti", "Chelsea", "Dortmund", "AC Milan", "Atletico Madrid", "PSG"]
    
    meciuri_generate = []
    for i in range(4):
        index_gz = (zi_num + i * 2) % len(elite_gazde)
        index_os = (zi_num + i * 3) % len(elite_oaspeti)
        if elite_gazde[index_gz] == elite_oaspeti[index_os]:
            index_os = (index_os + 1) % len(elite_oaspeti)
        meciuri_generate.append(elite_gazde[index_gz] + " vs " + elite_oaspeti[index_os])
    return meciuri_generate

partide_reale_zi = genereaza_meciuri_dupa_data(data_azi)
meciuri_analiza_zi = {}
seed_zi = sum(ord(c) for c in data_azi)

for i, partida in enumerate(partide_reale_zi):
    hash_meci = sum(ord(c) for c in partida) + seed_zi
    g_gz = str((hash_meci + i * 3) % 6 + 12)
    g_os = str((hash_meci + i * 5) % 6 + 10)
    med_gz = f"{round(1.8 + (hash_meci % 5) / 10, 1)}"
    meciuri_analiza_zi[partida] = {
        "liga": "Meciuri Oficiale Zi Curenta", "g_gz": g_gz, "g_os": g_os, "med_gz": med_gz, "med_os": f"{round(1.3 + (i % 4) / 10, 1)}", 
        "gp_gz": str((hash_meci) % 4 + 4), "gp_os": str((hash_meci + i) % 4 + 5),
        "ht_gz": f"{65 + (hash_meci % 15)}%", "st_gz": f"{70 + (i * 3) % 15}%", 
        "p15_gz": f"{82 + (hash_meci % 10)}%", "p25_gz": f"{55 + (i * 5) % 20}%", "gg_gz": f"{52 + (hash_meci % 25)}%",
        "w_p15": f"{82 + (hash_meci % 10)}%", "w_p25": f"{55 + (i * 5) % 20}%", 
        "w_p05r1": f"{65 + (hash_meci % 15)}%", "w_gg": f"{52 + (hash_meci % 25)}%"
    }
# ==============================================================================
# 5. CONTROL RENDERARE INTERFAȚĂ DINAMICĂ (LOGIN VS PLATFORMĂ)
# ==============================================================================
if st.session_state.ecran_login and not st.session_state.vip:
    st.markdown('<div class="full-screen-login-card" style="text-align: center;"><div style="background:rgba(0,255,102,0.1); border:1px solid #00ff66; color:#00ff66; font-size:12px; font-weight:800; padding:6px 16px; border-radius:30px; display:inline-block; margin-bottom:20px;">[SECURE PORTAL ACTIVE]</div><h1 style="color: #ffffff; font-weight: 800; font-size: 36px; margin: 0 0 10px 0;">VIP PORTAL</h1><p style="color: #94a3b8; font-size: 15px;">Sistemul necesita autorizare oficiala pentru deblocarea datelor.</p></div>', unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        utilizator = st.text_input("NUME UTILIZATOR", placeholder="User de acces...", key="lux_user_final_matrix")
        parola = st.text_input("PAROLA SECURIZATA", placeholder="••••••••", type="password", key="lux_pass_final_matrix")
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("CONECTARE", key="btn_lux_submit_final_matrix"):
            if utilizator in st.session_state.lista_membri and st.session_state.lista_membri[utilizator] == parola:
                st.session_state.vip = True
                st.session_state.ecran_login = False
                if utilizator == "admin":
                    st.session_state.admin = True
                st.success("Acces Permis!")
                st.rerun()
            else:
                st.error("Date invalide!")
        if c_b2.button("INAPOI", key="btn_lux_back_final_matrix"):
            st.session_state.ecran_login = False
            st.rerun()

else:
    if st.session_state.admin:
        st.markdown("<h3>🛠 PANOU ADMINISTRATOR</h3>", unsafe_allow_html=True)
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            nume = st.text_input("Nume Utilizator nou:", key="add_user_input")
            passw = st.text_input("Parola noua:", type="password", key="add_pass_input")
            if st.button("ACORDA PRIVILEGII VIP", key="btn_add_member"):
                if nume and passw:
                    st.session_state.lista_membri[nume] = passw
                    st.success("Membru activat!")
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col_adm2:
            st.markdown('<div class="admin-box">', unsafe_allow_html=True)
            for user_nume in list(st.session_state.lista_membri.keys()):
                c_u, c_b = st.columns([2.5, 1.5])
                c_u.write(f"👤 Cont: {user_nume}")
                if user_nume != "admin" and c_b.button("Sterge", key=f"del_{user_nume}"):
                    del st.session_state.lista_membri[user_nume]
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        st.write("---")
        # 3. PREDICTOR DINAMIC CU LINII ȘI PROCENTE NEON
        st.write("---")
        st.markdown('<h3 style="color: #00ff66; margin-bottom:15px;">📊 PROCENTE ANALIZĂ ALGORITM INTELIGENT</h3>', unsafe_allow_html=True)
        meci_ales_real = st.selectbox("🎯 Selecteaza meciul de azi pentru detalii procentuale:", partide_reale_zi, key="sel_meci_real_final_v11")
        mr = meciuri_analiza_zi[meci_ales_real]

        html_curat = '<div class="pricing-card-lux pricing-border-low">'
        html_curat += '<h4 style="color:#00ff66; margin:0; font-weight:800; letter-spacing:1px;">SISTEM PARIURIGO • DETALII LIVE</h4>'
        html_curat += '<h2 style="margin:8px 0 5px 0; font-size:30px; color:#ffffff;">' + meci_ales_real + '</h2>'
        html_curat += '<p style="color:#94a3b8; font-size:14px; text-transform:uppercase; margin-bottom:25px;">🏆 ' + mr['liga'] + ' • ' + data_azi + '</p>'
        
        html_curat += '<table style="width:100%; text-align:center; margin:20px 0; border-collapse:collapse; color:#fff;"><tr>'
        html_curat += '<td style="background:rgba(255,255,255,0.03); padding:12px; border-radius:10px; width:33%;"><div style="font-size:24px; font-weight:800; color:#00ff66;">' + mr['g_gz'] + '</div><div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Goluri Gazde</div></td>'
        html_curat += '<td style="background:rgba(255,255,255,0.03); padding:12px; border-radius:10px; width:33%;"><div style="font-size:24px; font-weight:800; color:#ffffff;">' + mr['med_gz'] + ' : ' + mr['med_os'] + '</div><div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Medie Goluri</div></td>'
        html_curat += '<td style="background:rgba(255,255,255,0.03); padding:12px; border-radius:10px; width:33%;"><div style="font-size:24px; font-weight:800; color:#00ff66;">' + mr['g_os'] + '</div><div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Goluri Oaspeți</div></td>'
        html_curat += '</tr><tr style="height:10px;"></tr><tr>'
        html_curat += '<td style="background:rgba(255,255,255,0.03); padding:12px; border-radius:10px;"><div style="font-size:24px; font-weight:800; color:#00ff66;">' + mr['gp_gz'] + '</div><div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Primite Gz</div></td>'
        html_curat += '<td style="background:rgba(255,255,255,0.03); padding:12px; border-radius:10px;"><div style="font-size:24px; font-weight:800; color:#475569;">VS</div><div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Status</div></td>'
        html_curat += '<td style="background:rgba(255,255,255,0.03); padding:12px; border-radius:10px;"><div style="font-size:24px; font-weight:800; color:#00ff66;">' + mr['gp_os'] + '</div><div style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Primite Os</div></td>'
        html_curat += '</tr></table>'
        
        html_curat += '<h4 style="color:#ffffff; margin-top:25px; font-weight:800;">📋 Probabilitati Evenimente (HT/ST):</h4>'
        html_curat += '<div style="display:flex; background:rgba(0,255,102,0.02); border-left:4px solid #00ff66; padding:10px 14px; margin:8px 0;"><span>Peste 0.5 HT (Prima Repriza)</span><span style="background:#00ff66; color:#000; font-weight:800; padding:2px 10px; border-radius:5px; margin-left:auto;">' + mr['ht_gz'] + '</span></div>'
        html_curat += '<div style="display:flex; background:rgba(0,255,102,0.02); border-left:4px solid #00ff66; padding:10px 14px; margin:8px 0;"><span>Peste 0.5 ST (A doua Repriza)</span><span style="background:#00ff66; color:#000; font-weight:800; padding:2px 10px; border-radius:5px; margin-left:auto;">' + mr['st_gz'] + '</span></div>'
        html_curat += '<div style="display:flex; background:rgba(0,255,102,0.02); border-left:4px solid #00ff66; padding:10px 14px; margin:8px 0;"><span>Peste 1.5 Goluri Finale</span><span style="background:#00ff66; color:#000; font-weight:800; padding:2px 10px; border-radius:5px; margin-left:auto;">' + mr['p15_gz'] + '</span></div>'
        html_curat += '<div style="display:flex; background:rgba(0,255,102,0.02); border-left:4px solid #00ff66; padding:10px 14px; margin:8px 0;"><span>Peste 2.5 Goluri Finale</span><span style="background:#00ff66; color:#000; font-weight:800; padding:2px 10px; border-radius:5px; margin-left:auto;">' + mr['p25_gz'] + '</span></div>'
        html_curat += '<div style="display:flex; background:rgba(0,255,102,0.02); border-left:4px solid #00ff66; padding:10px 14px; margin:8px 0;"><span>Ambele echipe marcheaza (GG)</span><span style="background:#00ff66; color:#000; font-weight:800; padding:2px 10px; border-radius:5px; margin-left:auto;">' + mr['gg_gz'] + '</span></div>'
        
        html_curat += '<h4 style="color:#ffffff; margin-top:25px; font-weight:800;">📈 Bare Evolutie Forta Algoritm:</h4>'
        html_curat += '<div style="margin: 12px 0;"><div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:4px;"><span>🔥 Probabilitate Peste 1.5 Goluri</span><span>' + mr['w_p15'] + '</span></div><div style="width:100%; background:rgba(255,255,255,0.06); border-radius:20px; height:12px; overflow:hidden;"><div style="height:100%; background:#00ff66; width:' + mr['w_p15'] + '; border-radius:20px;"></div></div></div>'
        html_curat += '<div style="margin: 12px 0;"><div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:4px;"><span>🔥 Probabilitate Peste 2.5 Goluri</span><span>' + mr['w_p25'] + '</span></div><div style="width:100%; background:rgba(255,255,255,0.06); border-radius:20px; height:12px; overflow:hidden;"><div style="height:100%; background:#00ff66; width:' + mr['w_p25'] + '; border-radius:20px;"></div></div></div>'
        html_curat += '<div style="margin: 12px 0;"><div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:4px;"><span>⚡ Sanse Gol in Prima Repriza (R1)</span><span>' + mr['w_p05r1'] + '</span></div><div style="width:100%; background:rgba(255,255,255,0.06); border-radius:20px; height:12px; overflow:hidden;"><div style="height:100%; background:#00ff66; width:' + mr['w_p05r1'] + '; border-radius:20px;"></div></div></div>'
        html_curat += '<div style="margin: 12px 0;"><div style="display:flex; justify-content:space-between; font-weight:700; margin-bottom:4px;"><span>⚡ Sanse Ambele Marcheaza (GG)</span><span>' + mr['w_gg'] + '</span></div><div style="width:100%; background:rgba(255,255,255,0.06); border-radius:20px; height:12px; overflow:hidden;"><div style="height:100%; background:#00ff66; width:' + mr['w_gg'] + '; border-radius:20px;"></div></div></div>'
        html_curat += '</div>'
        st.markdown(html_curat, unsafe_allow_html=True)

    # ==============================================================================
    # COLOANA DREAPTĂ: SELECTIE PACHETE VIP
    # ==============================================================================
    with col_abonamente:
        if not st.session_state.vip:
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            pachet_selectat = st.selectbox("ABONAMENTE VIP DISPONIBILE:", ["PACHET LOW", "PACHET MEDIUM", "HIGH VIP ELITE"], key="selector_preturi_final_v11")
            link_stripe = "https://stripe.com"

            if pachet_selectat == "PACHET LOW":
                st.markdown(f'<div class="pricing-card-lux pricing-border-low"><h4 style="color:#00ff66; margin:0;">PACHET LOW</h4><h2 style="margin:10px 0 20px 0; font-size:32px;">40 RON <span style="font-size:14px; color:#94a3b8; font-weight:600;">/ luna</span></h2><p>✅ 3 Bilete complet analizate pe saptamana</p><p>✅ Selectie exclusiva din ligile mari europene</p><a class="stripe-luxury-btn stripe-low-med" href="{link_stripe}" target="_blank">CUMPARA ACCES LOW</a></div>', unsafe_allow_html=True)
            elif pachet_selectat == "PACHET MEDIUM":
                st.markdown(f'<div class="pricing-card-lux pricing-border-medium"><h4 style="color:#ffcc00; margin:0;">PACHET MEDIUM</h4><h2 style="margin:10px 0 20px 0; font-size:32px;">70 RON <span style="font-size:14px; color:#94a3b8; font-weight:600;">/ luna</span></h2><p>✅ 1 Bilet Premium in fiecare zi calendaristica</p><p>✅ Algoritm avansat pentru probabilitati live</p><a class="stripe-luxury-btn stripe-low-med" href="{link_stripe}" target="_blank">CUMPARA ACCES MEDIUM</a></div>', unsafe_allow_html=True)
            elif pachet_selectat == "HIGH VIP ELITE":
                st.markdown(f'<div class="pricing-card-lux pricing-border-high"><h4 style="color:#ff0055; margin:0;">HIGH VIP ELITE</h4><h2 style="margin:10px 0 20px 0; font-size:32px;">120 RON <span style="font-size:14px; color:#94a3b8; font-weight:600;">/ luna</span></h2><p>✅ Cota 2 VIP zilnica + Proiect Dublare</p><p>✅ Monitorizare live non-stop pe sisteme</p><a class="stripe-luxury-btn stripe-high" href="{link_stripe}" target="_blank">DEBLOCHEAZA ACCES HIGH</a></div>', unsafe_allow_html=True)

            st.markdown("<div style='margin-top: 25px; text-align:center;'>", unsafe_allow_html=True)
            if st.button("ACCESEAZA CONT DETINUT", key="btn_trigger_final_secure_v11"):
                st.session_state.ecran_login = True
                st.rerun()
        else:
            st.markdown('<div class="vip-card-box" style="text-align: center; border: 1px solid #00ff66 !important; margin-top:25px;"><h4 style="color:#00ff66; margin:0; font-weight:800;">CONEXIUNE SECURIZATA</h4><p style="color:#ffffff; margin:8px 0 0 0; font-size:16px;">Sesiune complet autorizata in sistem</p></div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #475569; font-size: 14px; font-weight:600;'>&copy; 2026 PariuriGO World Live Center. Toate drepturile rezervate. Pariază responsabil.</p>", unsafe_allow_html=True)
