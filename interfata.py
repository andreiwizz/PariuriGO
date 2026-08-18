import streamlit as st

def randeaza_sectiune_meciuri(meciuri_date, data_azi):
    st.subheader("🌍 Toate Meciurile Live din Lume")
    st.markdown('<div style="width:100%; height:420px; overflow:auto; background:rgba(0,0,0,0.8); border-radius:12px; border:1px solid #1a0f30; padding:10px; margin-bottom: 25px;"><iframe src="https://scorebat.com" frameborder="0" width="100%" height="390px" allowfullscreen allow="autoplay; fullscreen"></iframe></div>', unsafe_allow_html=True)
    st.write("---")
    st.subheader("📊 Modul Algoritm & Probabilități")
    
    meci_ales = st.selectbox("🎯 Schimbă meciul:", list(meciuri_date.keys()))
    m = meciuri_date[meci_ales]
    
    st.markdown('<div class="glass-box-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#b042ff; margin: 5px 0; font-size:32px; font-weight:800; text-shadow: 0 0 10px rgba(176,66,255,0.4);'>" + meci_ales + "</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#cbd5e1; font-size:14px; font-weight:700;'>🏆 " + m['liga'] + " &bull; " + data_azi + "</p>", unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #221545;">', unsafe_allow_html=True)
    
    st.markdown('<div class="stat-container">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["g_gz"] + '</div><div class="stat-center-label">Total goluri marcate</div><div class="stat-right-val">' + m["g_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["med_gz"] + '</div><div class="stat-center-label">Medie goluri</div><div class="stat-right-val">' + m["med_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val">' + m["gp_gz"] + '</div><div class="stat-center-label">Goluri primite</div><div class="stat-right-val">' + m["gp_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #221545;">', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="mov-badge-tiktok">' + m["ht_gz"] + '</span></div><div class="stat-center-label">Peste 0.5 HT</div><div class="stat-right-val"><span class="mov-badge-tiktok">' + m["ht_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="mov-badge-tiktok">' + m["st_gz"] + '</span></div><div class="stat-center-label">Peste 0.5 ST</div><div class="stat-right-val"><span class="mov-badge-tiktok">' + m["st_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val"><span class="mov-badge-tiktok">' + m["p15_gz"] + '</span></div><div class="stat-center-label">Peste 1.5 goluri</div><div class="stat-right-val"><span class="mov-badge-tiktok">' + m["p15_os"] + '</span></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="color:#b042ff; font-size:20px;">' + m["p25_gz"] + '</div><div class="stat-center-label">Peste 2.5 goluri</div><div class="stat-right-val" style="color:#b042ff; font-size:20px;">' + m["p25_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="color:#b042ff; font-size:20px;">' + m["gg_gz"] + '</div><div class="stat-center-label">Ambele marchează</div><div class="stat-right-val" style="color:#b042ff; font-size:20px;">' + m["gg_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="font-size:14px; color:#a0aec0;">' + m["c_gz"] + '</div><div class="stat-center-label">Peste 3.5 cartonașe</div><div class="stat-right-val" style="font-size:14px; color:#a0aec0;">' + m["c_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="stat-row"><div class="stat-left-val" style="font-size:14px; color:#a0aec0;">' + m["cor_gz"] + '</div><div class="stat-center-label">Peste 9.5 cornere</div><div class="stat-right-val" style="font-size:14px; color:#b042ff;">' + m["cor_os"] + '</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-color: #221545; margin: 20px 0;">', unsafe_allow_html=True)
    st.markdown('<p style="font-weight:800; color:#b042ff;">📈 BARE EVOLUȚIE PROBABILITĂȚI GENERALE GLOBAL:</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="bar-wrapper"><div class="bar-title-flex"><span>Peste 1.5:</span></div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: ' + m["w_p15"] + ';">' + m["w_p15"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Peste 2.5:</div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: ' + m["w_p25"] + ';">' + m["w_p25"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Peste 0.5 R1:</div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: ' + m["w_p05r1"] + ';">' + m["w_p05r1"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Peste 0.5 R2:</div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: ' + m["w_p05r2"] + ';">' + m["w_p05r2"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">Ambele marchează:</div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: ' + m["w_gg"] + ';">' + m["w_gg"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">+ 3.5 Cartonașe:</div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: ' + m["w_c35"] + ';">' + m["w_c35"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="bar-wrapper"><div class="bar-label">+ 9.5 Cornere:</div><div class="bar-container-custom"><div class="bar-fill-mov-tiktok" style="width: ' + m["w_cor95"] + ';">' + m["w_cor95"] + '</div></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="green-footer-box"><div style="font-size:18px; color:#b042ff;">🏆</div><div><strong>Algoritm Automat PariuriGO VIP</strong></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
