import streamlit as st
import pandas as pd
import time

# --- 1. 頂級視覺 CSS (星際噴發與發光浮水印) ---
st.set_page_config(page_title="ZPIM 2026 巔峰導航儀", layout="wide")
st.markdown("""
    <style>
    .stApp {
        background-color: #000c14;
        background-image: radial-gradient(circle at 2px 2px, #00ffcc 1px, transparent 0),
                          linear-gradient(45deg, rgba(0, 20, 40, 0.5) 0%, rgba(0, 5, 10, 0.9) 100%);
        background-size: 50px 50px, cover;
        animation: star_glow 12s infinite alternate;
    }
    @keyframes star_glow { from { opacity: 0.8; } to { opacity: 1; } }
    .main-box {
        border: 2px solid #00ffcc; padding: 25px; border-radius: 12px;
        background: rgba(0, 15, 25, 0.85); box-shadow: 0 0 25px rgba(0, 255, 204, 0.4);
    }
    .watermark {
        position: fixed; top: 40%; left: 50%; transform: translate(-50%, -50%) rotate(-25deg);
        color: #00ffcc; opacity: 0.08; font-size: 85px; pointer-events: none; z-index: 999;
    }
    </style>
    <div class="watermark">ZPIM 2026 EXCLUSIVE</div>
    """, unsafe_allow_html=True)

# --- 2. 門禁授權庫 (計次熔斷) ---
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {"1-1":3, "1-2":3, "1-3":3, "1-5":3, "a-1":5, "a-2":5, "a-3":5}

if "auth" not in st.session_state: st.session_state["auth"] = False

# --- 3. 門禁介面 (電路板風格) ---
if not st.session_state["auth"]:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.title("🛡️ ZPIM 2026 戰略授權節點")
    pwd = st.text_input("輸入授權代碼", type="password")
    if st.button("🚀 啟動驗證"):
        if pwd.isdigit() and int(pwd) >= 999:
            st.session_state["auth"] = True; st.session_state["lvl"] = "MASTER"; st.rerun()
        elif pwd in st.session_state["auth_db"] and st.session_state["auth_db"][pwd] > 0:
            st.session_state["auth_db"][pwd] -= 1
            st.session_state["auth"] = True; st.session_state["lvl"] = "GUEST"; st.rerun()
        else: st.error("🚫 授權無效或已過期")
    st.markdown('</div>', unsafe_allow_html=True); st.stop()

# --- 4. 核心系統：星空、紅柱、說明、證書 ---
st.sidebar.title("📊 戰略參數對位")
q1 = st.sidebar.slider("Q1 實體實相 (資產/基礎) %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯實相 (專利/算法) %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務實相 (利潤/閉環) %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運實相 (主權/團隊) %", 0, 100, 100)

st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
if st.sidebar.button("🚀 啟動完整診斷"):
    # 紅色柱圖
    data = pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '百分比':[q1,q2,q3,q4]})
    st.bar_chart(data.set_index('維度'), color="#FF0000")
    
    # 4Q 深度鑑定結論 (取代無意義數字)
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("📜 首席顧問 鑑定結論：")
    cols = st.columns(2)
    with cols[0]:
        st.write(f"✅ **Q1 實體** ({q1}%): 資產底蘊深厚。")
        st.write(f"✅ **Q2 邏輯** ({q2}%): 運算邏輯清晰。")
    with cols[1]:
        st.write(f"✅ **Q3 財務** ({q3}%): 財務實相已閉環。")
        st.write(f"✅ **Q4 營運** ({q4}%): SOP 運作完美。")
    
    st.info("💡 **顧問核心建議**：結構穩固，主權定格。請維持 Q1 實體資產與 Q3 財務流之連動純度。")
    
    # 官方鑑定書
    st.markdown(f"""
        <hr style="border-top: 2px dashed #00ffcc;">
        <h2 style="color: #00ffcc; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center; color: white;"><b>總評級：S 級 (戰略領航者) | ID: ZPIM-{int(time.time())}</b></p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
