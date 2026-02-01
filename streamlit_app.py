import streamlit as st
import pandas as pd
import time

# --- 1. 頂級視覺 CSS (強化 101 燈塔背景、發光文字、鑑定書格式) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #002222 0%, #000c14 100%);
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png");
        background-attachment: fixed;
    }
    
    /* 101 戰略燈塔 (貫穿始終，定格右側) */
    .stApp::after {
        content: "";
        position: fixed; bottom: 0; right: 5%; width: 220px; height: 650px;
        background: linear-gradient(to top, rgba(0, 255, 204, 0.25) 0%, transparent 100%);
        clip-path: polygon(45% 0, 55% 0, 62% 10%, 38% 10%, 38% 12%, 67% 12%, 78% 25%, 22% 25%, 22% 27%, 83% 27%, 92% 45%, 8% 45%, 8% 47%, 97% 47%, 100% 100%, 0 100%);
        z-index: -1;
        filter: drop-shadow(0 0 15px #00ffcc);
    }

    /* 左側側邊欄：字體亮度加強 200% */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 25, 35, 0.95) !important;
        border-right: 2px solid #00ffcc;
    }
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 1.15rem !important;
        text-shadow: 0 0 10px #00ffcc;
    }

    .main-box {
        border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;
        background: rgba(0, 15, 25, 0.9); box-shadow: 0 0 35px rgba(0, 255, 204, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 授權與門禁 (避 4 計次) ---
if "auth" not in st.session_state: st.session_state["auth"] = False
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {"1-1":3, "a-1":5, "zpim2026":999}

if not st.session_state["auth"]:
    st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.header("🔒 ZPIM 2026 系統鎖定")
        pwd = st.text_input("輸入授權代碼", type="password")
        if st.button("🚀 啟動驗證"):
            if pwd.isdigit() and int(pwd) >= 999:
                st.session_state["auth"] = True; st.session_state["lvl"] = "首席顧問"; st.rerun()
            elif pwd in st.session_state["auth_db"] and st.session_state["auth_db"][pwd] > 0:
                st.session_state["auth_db"][pwd] -= 1
                st.session_state["auth"] = True; st.session_state["lvl"] = "合作夥伴"; st.rerun()
            else: st.error("🚫 代碼無效")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 3. 戰略導航中心 ---
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.sidebar.markdown(f"🚩 **當前權限**：{st.session_state['lvl']}")

q1 = st.sidebar.slider("Q1 實體實相 %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯實相 %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務實相 %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運實相 %", 0, 100, 100)

if "started" not in st.session_state: st.session_state["started"] = False
if st.sidebar.button("🚀 啟動完整診斷"): st.session_state["started"] = True

if st.session_state["started"]:
    # 顯化紅色柱圖
    st.bar_chart(pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '值':[q1,q2,q3,q4]}).set_index('維度'), color="#FF0000")
    
    # 鑑定結論深度說明 (改善空洞問題)
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("📜 首席顧問 鑑定結論 (繁體巔峰版)")
    c1, c2 = st.columns(2)
    with c1:
        st.success(f"✅ **Q1 實體實相** ({q1}%): 資產底蘊定格穩定。")
        st.success(f"✅ **Q2 邏輯實相** ({q2}%): 運算邏輯純度極高。")
    with c2:
        st.success(f"✅ **Q3 財務實相** ({q3}%): 獲利實相已達成閉環。")
        st.success(f"✅ **Q4 營運實相** ({q4}%): 主權清晰，團隊執行精準。")
    
    # 鑑定書底部 (官方質感)
    st.markdown(f"""
        <hr style="border-top: 2px dashed #00ffcc;">
        <h2 style="color: #00ffcc; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center; color: white;"><b>總評級：S 級 (戰略領航者) | ID: ZPIM-2026-{int(time.time())}</b></p>
        <p style="text-align: right; color: #00ffcc;"><b>首席顧問 已授權核可</b></p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # 啟動前的燈塔星空說明
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-box" style="text-align: center;"><h2>🌌 已連結 2026 實相星空</h2><p>101 戰略燈塔已定位完成，請啟動診斷以顯化 4Q 柱圖。</p></div>', unsafe_allow_html=True)

if st.sidebar.button("🔒 安全退出"):
    st.session_state.clear(); st.rerun()
