import streamlit as st
import base64

# 1. Configurare Pagină Full-Screen Nativă
st.set_page_config(
    page_title="PariuriGO • Core VIP",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funcție securizată pentru injectarea imaginii teren.jpg ca fundal transparent/întunecat
def aplica_fundal_teren_transparent(cale_imagine):
    try:
        with open(cale_imagine, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        st.markdown("""
        <style>
            /* Adăugăm un gradient negru intens de 94% opacitate peste teren */
            .stApp {
                background: linear-gradient(rgba(3, 3, 5, 0.94), rgba(4, 4, 7, 0.96)), 
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
        st.markdown("<style>.stApp { background-color: #030305 !important; }</style>", unsafe_allow_html=True)

# Activăm imaginea cu terenul în variantă transparentă / discretă
aplica_fundal_teren_transparent("teren.jpg")
