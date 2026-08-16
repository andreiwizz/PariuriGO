import streamlit as st

# Configurare pagină
st.set_page_config(page_title="Pachete PariuriGO", layout="wide")

# Font personalizat pentru titlu (Low, Medium, High) folosind HTML/CSS
st.markdown("""
<style>
    .pachet-titlu {
        font-size: 24px !important;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 10px;
    }
    .pachet-pret {
        font-size: 20px !important;
        font-weight: bold;
        text-align: center;
        color: #2E7D32;
    }
</style>
""", unsafe_allow_html=True)

st.title("Alege Pachetul Tău PariuriGO")
st.write("Selectează nivelul de acces care ți se potrivește cel mai bine:")

# Crearea celor 3 coloane pentru pachete
col1, col2, col3 = st.columns(3)

# 1. PACHETUL LOW
with col1:
    # Imagine mică (înlocuiește link-ul cu imaginea ta dacă dorești)
    st.image("https://flaticon.com", width=70)
    st.markdown('<p class="pachet-titlu">Pachet LOW</p>', unsafe_allow_html=True)
    st.markdown('<p class="pachet-pret">19 RON / lună</p>', unsafe_allow_html=True)
    st.write("- 3 ponturi pe zi")
    st.write("- Cote între 1.50 - 2.00")
    st.write("- Suport de bază")
    if st.button("Cumpără LOW", key="low"):
        st.success("Ai ales pachetul Low! Redirecționare către plată...")

# 2. PACHETUL MEDIUM
with col2:
    st.image("https://flaticon.com", width=70)
    st.markdown('<p class="pachet-titlu">Pachet MEDIUM</p>', unsafe_allow_html=True)
    st.markdown('<p class="pachet-pret">49 RON / lună</p>', unsafe_allow_html=True)
    st.write("- 7 ponturi pe zi")
    st.write("- Cote între 2.00 - 5.00")
    st.write("- Acces la grupul de chat")
    if st.button("Cumpără MEDIUM", key="medium"):
        st.success("Ai ales pachetul Medium! Redirecționare către plată...")

# 3. PACHETUL HIGH
with col3:
    st.image("https://flaticon.com", width=70)
    st.markdown('<p class="pachet-titlu">Pachet HIGH</p>', unsafe_allow_html=True)
    st.markdown('<p class="pachet-pret">99 RON / lună</p>', unsafe_allow_html=True)
    st.write("- Toate ponturile incluse")
    st.write("- Cote VIP (peste 5.00)")
    st.write("- Suport dedicat 24/7")
    if st.button("Cumpără HIGH", key="high"):
        st.success("Ai ales pachetul High! Redirecționare către plată...")
