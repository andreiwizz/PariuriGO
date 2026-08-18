import streamlit as st

st.set_page_config(page_title="Pariuri GO", page_icon="⚽", layout="centered")

# ---------- CSS tema GitHub dark ----------
st.markdown("""
<style>
.stApp {
    background-color: #0d1117;
}
.pgo-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 2px;
}
.pgo-title {
    color: #e6edf3;
    font-size: 22px;
    font-weight: 600;
    font-family: -apple-system, sans-serif;
}
.pgo-subtitle {
    color: #8b949e;
    font-size: 13px;
    font-family: 'Courier New', monospace;
    margin-bottom: 24px;
}
.pgo-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 14px;
    transition: border-color 0.2s ease;
}
.pgo-card:hover {
    border-color: #58a6ff;
}
.pgo-card-featured {
    background: #161b22;
    border: 2px solid #58a6ff;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 14px;
    position: relative;
}
.pgo-badge-popular {
    position: absolute;
    top: -10px;
    left: 16px;
    background: #0d1117;
    color: #58a6ff;
    font-size: 11px;
    padding: 0 8px;
    font-family: 'Courier New', monospace;
}
.pgo-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.pgo-name {
    color: #e6edf3;
    font-size: 16px;
    font-weight: 600;
}
.pgo-tag {
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 12px;
    font-family: 'Courier New', monospace;
}
.pgo-tag-low { background: #0d2818; color: #7ee787; }
.pgo-tag-medium { background: #0c2d4a; color: #79c0ff; }
.pgo-tag-high { background: #2d1f47; color: #d2a8ff; }
.pgo-desc {
    color: #8b949e;
    font-size: 13px;
    margin-top: 8px;
}
.pgo-price {
    color: #e6edf3;
    font-size: 14px;
    font-weight: 600;
    margin-top: 10px;
    font-family: 'Courier New', monospace;
}
</style>
""", unsafe_allow_html=True)

# ---------- definitia pachetelor ----------
# link-urile de Telegram / Stripe le pui pe ale tale
PACHETE = {
    "low": {
        "nume": "Low",
        "icon": "🔓",
        "tag_class": "pgo-tag-low",
        "tag_text": "basic",
        "descriere": "1-2 ponturi pe zi, cote medii",
        "pret": "29 RON / luna",
        "stripe_link": "https://buy.stripe.com/xxxxx_low",
        "telegram_link": "https://t.me/+xxxxx_low",
    },
    "medium": {
        "nume": "Medium",
        "icon": "⚡",
        "tag_class": "pgo-tag-medium",
        "tag_text": "plus",
        "descriere": "3-4 ponturi pe zi, analiza detaliata",
        "pret": "59 RON / luna",
        "stripe_link": "https://buy.stripe.com/xxxxx_medium",
        "telegram_link": "https://t.me/+xxxxx_medium",
        "featured": True,
    },
    "high": {
        "nume": "High",
        "icon": "👑",
        "tag_class": "pgo-tag-high",
        "tag_text": "vip",
        "descriere": "ponturi nelimitate, banca zilei",
        "pret": "99 RON / luna",
        "stripe_link": "https://buy.stripe.com/xxxxx_high",
        "telegram_link": "https://t.me/+xxxxx_high",
    },
}

# ---------- header ----------
st.markdown("""
<div class="pgo-header">
    <span style="font-size:22px;">📊</span>
    <span class="pgo-title">Pariuri GO</span>
</div>
<div class="pgo-subtitle"># deblocheaza ponturile • alege un pachet</div>
""", unsafe_allow_html=True)

# ---------- carduri pachete ----------
for cheie, pachet in PACHETE.items():
    card_class = "pgo-card-featured" if pachet.get("featured") else "pgo-card"

    badge_html = '<div class="pgo-badge-popular">popular</div>' if pachet.get("featured") else ""

    st.markdown(f"""
    <div class="{card_class}">
        {badge_html}
        <div class="pgo-row">
            <span class="pgo-name">{pachet['icon']} {pachet['nume']}</span>
            <span class="pgo-tag {pachet['tag_class']}">{pachet['tag_text']}</span>
        </div>
        <div class="pgo-desc">{pachet['descriere']}</div>
        <div class="pgo-price">{pachet['pret']}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.link_button(f"Plateste ({pachet['nume']})", pachet["stripe_link"], use_container_width=True)
    with col2:
        st.link_button("Telegram", pachet["telegram_link"], use_container_width=True)
