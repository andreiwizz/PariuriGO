import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • Core Center",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru injectarea imaginii teren.jpg direct ca fundal full-screen
def aplica_doar_fundal_teren(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            /* Ștergem toate marginile și forțăm imaginea pe tot ecranul */
            .stApp {
                background: url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }
            
            /* Ascundem elementele native de Streamlit care ar putea încurca */
            #MainMenu, footer, header { display: none !important; }
            div[data-testid="stToolbar"] { display: none !important; }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

# Activăm exclusiv imaginea ta cu terenul de fotbal
aplica_doar_fundal_teren("teren.jpg")
