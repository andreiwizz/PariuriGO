import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • Core VIP",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru injectarea imaginii teren.jpg cu opacitate perfect echilibrată
def aplica_fundal_teren_calibrat(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            /* Am setat opacitatea la 0.82 ca să fie o idee mai vizibil și mai clar terenul */
            .stApp {
                background: linear-gradient(rgba(4, 3, 8, 0.82), rgba(6, 4, 15, 0.86)), 
                            url("data:image/jpeg;base64,""" + b64_img + """") !important;
                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }
            
            /* Ascundem complet meniurile de fundal Streamlit */
            #MainMenu, footer, header { display: none !important; }
            div[data-testid="stToolbar"] { display: none !important; }
        </style>
        """, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp { background-color: #040308 !important; }</style>", unsafe_allow_html=True)

# Activăm imaginea cu terenul în varianta perfect vizibilă, dar profesională
aplica_fundal_teren_calibrat("teren.jpg")
