import streamlit as st
import pandas as pd
import time

# --- 1. 頂級旗艦視覺 CSS (101 燈塔、星際噴發、繁體加粗) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")
st.markdown("""
    <style>
    /* 全局星際噴發背景 */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #002222 0%, #000c14 100%);
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png");
        background-attachment: fixed;
    }
    
    /* 101 旗艦燈塔 (定格於右側，象徵領航) */
    .stApp::after {
        content: "";
        position: fixed; bottom: 0; right: 8%; width: 220px; height: 600px;
        background: linear-gradient(to top, rgba(0, 255, 204, 0.3) 0%, transparent 100%);
        clip-path: polygon(45% 0, 55% 0, 60% 8%, 40% 8%, 40% 10%, 65% 10%, 75% 20%, 25% 20%, 25% 22%, 80% 22%, 90% 40%, 10% 40%, 10% 42%, 95% 42%, 100% 100%, 0 100%);
        z-index: -1;
        filter: drop-shadow(0 0 20px #00ffcc);
    }

    /* 左側側邊欄：強化亮度與主權感 */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 25, 35, 0.95) !important;
        border-right: 2px solid #00ffcc;
    }
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 0 10px #00ffcc;
    }

    .main-box {
        border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;
        background: rgba(0, 15, 25, 0.9); box-shadow: 0 0 40px rgba(0, 255, 204, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 授權與門禁 ---
if "auth" not in st.session_state: st.session_state["auth"] = False
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {"1-1":3, "a-1":5, "zpim2026":999}

if not st.session_state["auth"]:
    st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.header("🔒 ZPIM 2026 系統鎖定")
        st.write("Authorized Personnel Only (Secure Node)")
        pwd = st.text_input("請輸入授權代碼", type="password")
        if st.button("🚀 啟動驗證"):
            if pwd.isdigit() and int(pwd) >= 999:
                st.session_state["auth"] = True; st.session_state["lvl"] = "首席顧問"; st.rerun()
            elif pwd in st.session_state["auth_db"] and st.session_state["auth_db"][pwd] > 0:
                st.session_state["auth_db"][pwd] -= 1
                st.session_state["auth"] = True; st.session_state["lvl"] = "合作夥伴"; st.rerun()
            else: st.error("🚫 代碼無效")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 3. 進入後的首頁：101 燈塔與星空 ---
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.sidebar.markdown(f"🚩 **權限等級**：{st.session_state['lvl']}")

# 4Q 拉桿
q1 = st.sidebar.slider("Q1 實體實相 %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯實相 %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務實相 %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運實相 %", 0, 100, 100)

# 初始化啟動狀態
if "started" not in st.session_state: st.session_state["started"] = False

if st.sidebar.button("🚀 啟動完整診斷"):
    st.session_state["started"] = True

if st.session_state["started"]:
    # 紅色柱圖顯化 (當啟動時，從燈塔引導出紅柱)
    data = pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '值':[q1,q2,q3,q4]})
    st.bar_chart(data.set_index('維度'), color="#FF0000")
    
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("📜 首席顧問 鑑定結論")
    st.success(f"✅ Q1 實體 ({q1}%) | ✅ Q2 邏輯 ({q2}%) | ✅ Q3 財務 ({q3}%) | ✅ Q4 營運 ({q4}%)")
    st.markdown(f"""
        <hr style="border-top: 2px dashed #00ffcc;">
        <h2 style="color: #00ffcc; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center;">總評級：<b>S 級 (戰略領航者)</b></p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # 剛進頁面，尚未啟動時的宏偉說明
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="main-box" style="text-align: center;">
            <h2 style="color: #00ffcc;">🌌 已連結 2026 實相星空</h2>
            <p style="font-size: 1.2rem;">101 戰略燈塔已定位完成，請透過左側拉桿設定 4Q 參數後啟動診斷。</p>
        </div>
    """, unsafe_allow_html=True)

if st.sidebar.button("🔒 安全退出"):
    st.session_state.clear(); st.rerun()
