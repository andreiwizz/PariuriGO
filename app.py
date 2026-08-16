st.markdown("""
<style>

/* ===== TABURI REPARATE ===== */

.stTabs [data-baseweb="tab-list"]{
    gap: 8px;
    background: transparent;
    border-bottom: 1px solid rgba(0,255,102,.25);
}

.stTabs [data-baseweb="tab"]{
    height: 50px;
    padding: 0 18px;
    background: rgba(8,22,15,.88);
    color: #cbd5e1 !important;
    border: 1px solid rgba(0,255,102,.18);
    border-radius: 10px 10px 0 0;
    font-weight: 700;
}

.stTabs [aria-selected="true"]{
    background: rgba(0,255,102,.12) !important;
    color: #00ff66 !important;
    border-color: #00ff66 !important;
}

.stTabs [data-baseweb="tab"]:hover{
    color: white !important;
    border-color: #00ff66;
}

button[kind="tab"]{
    color: inherit !important;
}

</style>
""", unsafe_allow_html=True)
