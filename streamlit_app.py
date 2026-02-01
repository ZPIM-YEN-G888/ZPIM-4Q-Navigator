import streamlit as st
import pandas as pd
import time

# --- 1. 頂級旗艦視覺 CSS (星空噴發、101 圖騰、清晰字體) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")
st.markdown("""
    <style>
    /* 全局星空背景與 101 宏偉意象 */
    .stApp {
        background: radial-gradient(circle at center, #001a1a 0%, #00050a 100%);
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png");
        background-attachment: fixed;
    }
    
    /* 101 戰略塔影 (代碼繪製，右側定格) */
    .stApp::after {
        content: "";
        position: fixed; bottom: 0; right: 5%; width: 220px; height: 600px;
        background: linear-gradient(to top, rgba(0, 255, 204, 0.1) 0%, transparent 100%);
        clip-path: polygon(45% 0, 55% 0, 60% 8%, 40% 8%, 40% 10%, 65% 10%, 75% 20%, 25% 20%, 25% 22%, 80% 22%, 90% 40%, 10% 40%, 10% 42%, 95% 42%, 100% 100%, 0 100%);
        z-index: -1;
    }

    /* 左側邊欄字體與發光強化 */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 20, 30, 0.95) !important;
        border-right: 2px solid #00ffcc;
    }
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 0 10px #00ffcc;
    }

    .main-box {
        border: 2px solid #00ffcc; padding: 30px; border-radius: 15px;
        background: rgba(0, 10, 20, 0.9); box-shadow: 0 0 40px rgba(0, 255, 204, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 授權與門禁 ---
if "auth" not in st.session_state: st.session_state["auth"] = False
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {"1-1":3, "a-1":5, "zpim2026":999}

# --- 3. 登入畫面 (貫穿宏偉背景) ---
if not st.session_state["auth"]:
    st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.header("🔒 ZPIM 2026 系統鎖定")
        st.write("Access Restricted: Authorized Personnel Only (Secure Node)")
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

# --- 4. 進入後的首頁 (延續 101 星空背景) ---
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.sidebar.markdown(f"🚩 **當前權限**：{st.session_state['lvl']}")

# 4Q 拉桿 (顯示 % 數)
q1 = st.sidebar.slider("Q1 實體實相 %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯實相 %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務實相 %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運實相 %", 0, 100, 100)

if st.sidebar.button("🚀 啟動完整診斷"):
    st.bar_chart(pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '值':[q1,q2,q3,q4]}).set_index('維度'), color="#FF0000")
    
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("📜 首席顧問 鑑定結論")
    st.success(f"✅ Q1 實體 ({q1}%): 資產底蘊定格穩定。")
    st.success(f"✅ Q2 邏輯 ({q2}%): 運算邏輯純度極高。")
    st.success(f"✅ Q3 財務 ({q3}%): 獲利實相已達成閉環。")
    st.success(f"✅ Q4 營運 ({q4}%): 主權清晰，執行精準。")
    
    st.markdown(f"""
        <hr style="border-top: 2px dashed #00ffcc;">
        <h2 style="color: #00ffcc; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center;">總評級：<b>S 級 (戰略領航者)</b> | ID: ZPIM-{int(time.time())}</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.sidebar.button("🔒 安全退出"):
    st.session_state.clear(); st.rerun()
