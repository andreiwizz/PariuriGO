import streamlit as st
import base64
from datetime import datetime

# 1. Configurare Pagină principală (MANDATORIU PRIMA LINIE)
st.set_page_config(
    page_title="PariuriGO World Live Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

data_azi = datetime.now().strftime("%d.%m.%Y")

def incarc_imagine_locala(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

teren_base64 = incarc_imagine_locala("teren.jpg")
logo_base64 = incarc_imagine_locala("logo.png")

if teren_base64:
    bg_style = f"background: linear-gradient(rgba(4, 14, 8, 0.94), rgba(2, 6, 4, 0.96)), url('data:image/jpeg;base64,{teren_base64}') !important; background-size: cover !important; background-position: center !important; background-repeat: no-repeat !important; background-attachment: fixed !important;"
else:
    bg_style = "background-color: #040e08 !important;"

st.markdown(f"""
<style>
    .stApp {{
        {bg_style}
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif !important;
    }}
    h1, h2, h3, h4, p, span, label {{
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
    }}
    .glass-box-container {{
        background: rgba(8, 20, 14, 0.88) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 255, 102, 0.2) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 12px 40px 0 rgba(0,0,0,0.7) !important;
        margin-bottom: 25px !important;
    }}
    .vip-card-box {{
        background: rgba(10, 25, 18, 0.9) !important;
        border: 1px solid rgba(0, 255, 102, 0.3) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.6) !important;
    }}
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
        background-color: rgba(10, 30, 18, 0.9) !important;
        border: 1px solid #00ff66 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }}
    .stat-container {{ width: 100%; margin: 0 auto; }}
    .stat-row {{ display: flex; justify-content: space-between; align-items: center; margin: 12px 0; text-align: center; }}
    .stat-left-val, .stat-right-val {{ width: 20%; font-size: 22px; font-weight: 800; color: #ffffff; text-align: center; }}
    .stat-center-label {{ width: 60%; font-size: 16px; font-weight: 700; color: #a0aec0; text-transform: uppercase; letter-spacing: 0.5px; }}
    .green-badge {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%);
        color: #000000 !important;
        padding: 5px 18px;
        border-radius: 6px;
        font-size: 16px;
        font-weight: 800;
        display: inline-block;
        box-shadow: 0 2px 12px rgba(0, 255, 102, 0.3);
    }}
    .bar-wrapper {{ display: flex; align-items: center; margin: 14px 0; }}
    .bar-label {{ width: 28%; font-size: 16px; font-weight: 700; color: #ffffff; }}
    .bar-container {{ width: 72%; background: rgba(255, 255, 255, 0.05); border-radius: 12px; overflow: hidden; height: 26px; position: relative; border: 1px solid rgba(255,255,255,0.05); }}
    .bar-fill-neon {{
        height: 100%;
        background: linear-gradient(90deg, #006622 0%, #00ff66 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 12px;
        font-size: 13px;
        font-weight: 800;
        color: #000000;
    }}
    .bar-fill-soft {{
        height: 100%;
        background: linear-gradient(90deg, #013a16 0%, #00bc43 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 12px;
        font-size: 13px;
        font-weight: 800;
        color: #ffffff;
    }}
    .green-footer-box {{ background: rgba(0, 255, 102, 0.05); border: 1px solid rgba(0, 255, 102, 0.18); border-radius: 10px; padding: 12px 20px; margin-top: 20px; display: flex; align-items: center; gap: 12px; }}
    div[data-testid="stLinkButton"] a {{
        background: linear-gradient(135deg, #00ff66 0%, #00bc43 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        text-decoration: none !important;
        box-shadow: 0 0 12px rgba(0, 255, 102, 0.4) !important;
        animation: pulsareGlow 1.8s infinite ease-in-out !important;
    }}
    @keyframes pulsareGlow {{
        0% {{ transform: scale(1); box-shadow: 0 0 12px rgba(0, 255, 102, 0.4); }}
        50% {{ transform: scale(1.02); box-shadow: 0 0 25px rgba(0, 255, 102, 0.7); }}
        100% {{ transform: scale(1); box-shadow: 0 0 12px rgba(0, 255, 102, 0.4); }}
    }}
</style>
""", unsafe_allow_html=True)

if logo_base64:
    st.markdown(f'<div style="text-align: center; margin-bottom: 15px;"><img src="data:image/png;base64,{logo_base64}" width="280"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff;'>⚽ PARIURIGO &bull; WORLD LIVE CENTER</h1>", unsafe_allow_html=True)

st.write("---")

col_meciuri, col_abonamente = st.columns([1.3, 0.7], gap="large")

meciuri_date = {
    "FCSB vs Rapid București": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": "14", "g_os": "11", "med_gz": "1.75", "med_os": "1.37", "gp_gz": "5", "gp_os": "9",
        "ht_gz": "85.71%", "ht_os": "71.43%", "st_gz": "78.50%", "st_os": "64.25%",
        "p15_gz": "91.20%", "p15_os": "78.50%", "p25_gz": "64.29%", "p25_os": "50.00%",
        "gg_gz": "71.43%", "gg_os": "57.14%", "c_gz": "14.29%", "c_os": "28.57%",
        "cor_gz": "-", "cor_os": "14.29%",
        "w_p15": "85.00%", "w_p25": "64.29%", "w_p05r1": "85.71%", "w_p05r2": "78.50%", "w_gg": "71.43%", "w_c35": "21.43%", "w_cor95": "14.29%"
    },
    "CFR Cluj vs Universitatea Craiova": {
        "liga": "ROMÂNIA SUPERLIGA",
        "g_gz": "11", "g_os": "13", "med_gz": "1.37", "med_os": "1.62", "gp_gz": "7", "gp_os": "6",
        "ht_gz": "75.00%", "ht_os": "62.50%", "st_gz": "87.50%", "st_os": "75.00%",
        "p15_gz": "87.50%", "p15_os": "75.00%", "p25_gz": "50.00%", "p25_os": "62.50%",
        "gg_gz": "62.50%", "gg_os": "62.50%", "c_gz": "25.00%", "c_os": "37.50%",
        "cor_gz": "12.50%", "cor_os": "25.00%",
        "w_p15": "81.00%", "w_p25": "56.00%", "w_p05r1": "68.00%", "w_p05r2": "81.00%", "w_gg": "62.00%", "w_c35": "31.00%", "w_cor95": "18.00%"
    },
    "Bașakșehir vs Kocaelispor": {
        "liga": "SUPER LIG &bull; TURKEY",
        "g_gz": "7", "g_os": "3", "med_gz": "1.00", "med_os": "0.43", "gp_gz": "8", "gp_os": "6",
        "ht_gz": "71.43%", "ht_os": "57.14%", "st_gz": "71.43%", "st_os": "57.14%",
        "p15_gz": "85.71%", "p15_os": "42.86%", "p25_gz": "28.57%", "p25_os": "42.86%",
        "gg_gz": "57.14%", "gg_os": "42.86%", "c_gz": "14.29%", "c_os": "28.57%",
        "cor_gz": "-", "cor_os": "14.29%",
        "w_p15": "64.29%", "w_p25": "14.29%", "w_p05r1": "64.29%", "w_p05r2": "64.29%", "w_gg": "50.00%", "w_c35": "21.43%", "w_cor95": "7.14%"
    }
}

with col_meciuri:
    st.subheader("🌍 Meciuri Live din Toate Ligile Lumii")

    st.markdown("""
        <div style="width:100%; height:420px; overflow:auto; background:rgba(5,15,10,0.9); border-radius:12px; border:1px solid rgba(0,255,102,0.2); padding:10px; margin-bottom: 25px;">
            <iframe src="https://scorebat.com" frameborder="0" width="100%" height="390px" allowfullscreen allow="autoplay; fullscreen"></iframe>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("📊 Modul Algoritm & Probabilități (Meci de Top)")

    meci_ales = st.selectbox("🎯 Schimbă meciul din ziua respectivă:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]

    st.markdown('<div class="glass-box-container">', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8; margin:0;'>MECI RECOMANDAT &bull; DATE LA ZI " + data_azi + "</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#00ff66; margin: 5px 0;'>" + meci_ales + "</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8; font-size:14px; margin-top:2px;'>" + m['liga'] + "</p>", unsafe_allow_html=True)
    st.markdown('<hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">', unsafe_allow_html=True)

    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["g_gz"] + '</div><div class="stat-center-label">Total goluri marcate</div><div class="stat-right-val">' + m["g_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["med_gz"] + '</div><div class="stat-center-label">Medie goluri</div><div class="stat-right-val">' + m["med_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["gp_gz"] + '</div><div class="stat-center-label">Goluri primite</div><div class="stat-right-val">' + m["gp_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">', unsafe_allow_html=True)

    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["ht_gz"] + '</div><div class="stat-center-label">Peste 0.5 HT</div><div class="stat-right-val">' + m["ht_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["st_gz"] + '</div><div class="stat-center-label">Peste 0.5 ST</div><div class="stat-right-val">' + m["st_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["p15_gz"] + '</div><div class="stat-center-label">Peste 1.5 goluri</div><div class="stat-right-val">' + m["p15_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["p25_gz"] + '</div><div class="stat-center-label">Peste 2.5 goluri</div><div class="stat-right-val">' + m["p25_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["gg_gz"] + '</div><div class="stat-center-label">Ambele marchează</div><div class="stat-right-val">' + m["gg_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["c_gz"] + '</div><div class="stat-center-label">Peste 3.5 cartonașe</div><div class="stat-right-val">' + m["c_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["cor_gz"] + '</div><div class="stat-center-label">Peste 9.5 cornere</div><div class="stat-right-val">' + m["cor_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr style="border-color: rgba(255,255,255,0.05); margin: 15px 0;">', unsafe_allow_html=True)
    st.markdown("<p style='color:#00ff66; font-weight:800; margin-bottom:10px;'>📈 BARE EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:</p>", unsafe_allow_html=True)

    def bara(eticheta, procent, tip="neon"):
        clasa = "bar-fill-neon" if tip == "neon" else "bar-fill-soft"
        st.markdown(
            '<div class="bar-wrapper"><div class="bar-label">' + eticheta + '</div>'
            '<div class="bar-container"><div class="' + clasa + '" style="width:' + procent + ';">' + procent + '</div></div></div>',
            unsafe_allow_html=True
        )

    bara("Peste 1.5:", m["w_p15"], "neon")
    bara("Peste 2.5:", m["w_p25"], "soft")
    bara("Peste 0.5 R1:", m["w_p05r1"], "neon")
    bara("Peste 0.5 R2:", m["w_p05r2"], "neon")
    bara("Ambele marchează:", m["w_gg"], "neon")
    bara("+ 3.5 Cartonașe:", m["w_c35"], "soft")
    bara("+ 9.5 Cornere:", m["w_cor95"], "soft")

    st.markdown(
        '<div class="green-footer-box">🔸 Sistem Algoritm Automat PariuriGO — '
        'Toate procentele sunt calculate pe baza istoricului de meciuri din data de ' + data_azi + '</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)  # inchide glass-box-container

# 4. SECȚIUNE ABONAMENTE VIP — INTEGRAT LINK-UL STRIPE DE TEST
with col_abonamente:
    st.subheader("🏆 Toate Abonamentele VIP")

    # Linkul oficial generat de tine în Stripe Sandbox (mod test)
    link_stripe_test_low = "https://buy.stripe.com/test_5kQfZjgBrakW0YLbVMfjG00"
    # Momentan MEDIUM si HIGH sunt pe acelasi link de test.
    # Inlocuieste-le cu linkurile lor proprii cand le generezi in Stripe.
    link_stripe_test_medium = link_stripe_test_low
    link_stripe_test_high = link_stripe_test_low

    # 1. LOW
    st.markdown('<div class="vip-card-box">', unsafe_allow_html=True)
    st.markdown("<h3>🟢 PACHET LOW</h3>", unsafe_allow_html=True)
    st.markdown("<span class='green-badge'>40 RON / lună</span>", unsafe_allow_html=True)
    st.write("📋 Beneficii incluse:")
    st.write("• 3 Bilete gata analizate pe săptămână")
    st.write("• Cote sigure selectate din ligile mari")
    st.write("• Acces grup comunitate chat")
    st.write("")
    st.link_button("Abonare LOW 🚀", link_stripe_test_low, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. MEDIUM
    st.markdown('<div class="vip-card-box">', unsafe_allow_html=True)
    st.markdown("<h3>🟡 PACHET MEDIUM</h3>", unsafe_allow_html=True)
    st.markdown("<span class='green-badge'>70 RON / lună</span>", unsafe_allow_html=True)
    st.write("📋 Beneficii incluse:")
    st.write("• 1 Bilet Premium în fiecare zi")
    st.write("• Procente și probabilități avansate live")
    st.write("• Notificări instant pe Telegram")
    st.write("")
    st.link_button("Abonare MEDIUM 🟡", link_stripe_test_medium, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. HIGH
    st.markdown('<div class="vip-card-box">', unsafe_allow_html=True)
    st.markdown("<h3>🔥 HIGH VIP ELITE</h3>", unsafe_allow_html=True)
    st.markdown("<span class='green-badge'>120 RON / lună</span>", unsafe_allow_html=True)
    st.write("📋 Beneficii incluse:")
    st.write("• Cota 2 VIP zilnică + Proiect Dublare")
    st.write("• Acces total la toate sistemele noastre")
    st.write("• Suport privat 1-la-1 direct cu tipsterul")
    st.write("")
    st.link_button("Deblochează HIGH 🔥", link_stripe_test_high, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    import sqlite3

# ================== BAZA MEMBRI ==================
import sqlite3

# Ascundem textul urât de săgeată care apare deasupra meniului în noile versiuni de Streamlit
st.markdown("""
<style>
    /* Ascunde textul brut de iconițe care buguiește sidebar-ul */
    button div {
        font-size: 0px !important;
    }
    button div:before {
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

conn = sqlite3.connect("membri.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS membri(
    user TEXT PRIMARY KEY,
    parola TEXT
)
""")
conn.commit()

# cont admin
c.execute("INSERT OR IGNORE INTO membri VALUES (?,?)", ("admin","pariurigo"))
conn.commit()

if "vip" not in st.session_state:
    st.session_state.vip = False

if "admin" not in st.session_state:
    st.session_state.admin = False

st.write("---")

# ================== LOGIN ==================
with st.sidebar:
    st.title("🔐 LOGIN")

    utilizator = st.text_input("Utilizator")
    parola = st.text_input("Parolă", type="password")

    if st.button("Conectare"):
        c.execute(
            "SELECT * FROM membri WHERE user=? AND parola=?",
            (utilizator, parola)
        )

        if c.fetchone():
            st.session_state.vip = True
            if utilizator == "admin":
                st.session_state.admin = True
            st.success("Conectat cu succes!")
            st.rerun()
        else:
            st.error("Date greșite!")

vip = st.session_state.vip
admin = st.session_state.admin

# ================== ADMIN PANEL ==================
if admin:
    st.write("---")
    st.header("🛠 ADMIN PANEL")

    nume = st.text_input("Nume membru")
    passw = st.text_input("Parolă membru")

    if st.button("➕ Adaugă membru"):
        c.execute(
            "INSERT OR REPLACE INTO membri VALUES (?,?)",
            (nume, passw)
        )
        conn.commit()
        st.success("Membru adăugat!")
        st.rerun()

    st.subheader("👥 Lista membrilor")

    c.execute("SELECT user FROM membri")
    membri = c.fetchall()

    for m in membri:
        col1, col2 = st.columns([3, 1])
        col1.write("👤 " + m[0])

        if m[0] != "admin":
            if col2.button("Șterge", key=m[0]):
                c.execute(
                    "DELETE FROM membri WHERE user=?",
                    (m[0],)
                )
                conn.commit()
                st.success("Membru șters!")
                st.rerun()
)
