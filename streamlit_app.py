import streamlit as st
import pandas as pd
import time

# --- 1. 旗艦視覺總控 (星空、101、電路板、禁止遮蔽文字) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #003333 0%, #000c14 100%);
        background-image: url("https://www.transparenttextures.com/patterns/stardust.png");
        background-attachment: fixed;
    }
    
    /* 注入 101 宏偉塔影 (代碼繪製版，無侵權風險) */
    .stApp::after {
        content: "";
        position: fixed; bottom: 0; right: 8%; width: 180px; height: 500px;
        background: linear-gradient(to top, rgba(0, 255, 204, 0.15) 0%, transparent 100%);
        clip-path: polygon(45% 0, 55% 0, 60% 10%, 40% 10%, 40% 12%, 65% 12%, 75% 25%, 25% 25%, 25% 27%, 80% 27%, 90% 45%, 10% 45%, 10% 47%, 95% 47%, 100% 100%, 0 100%);
        z-index: -1;
    }

    /* 強化側邊欄字體與背景 */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 20, 30, 0.9) !important;
        border-right: 1px solid #00ffcc;
    }
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {
        color: #FFFFFF !important;
        font-weight: bold !important;
        text-shadow: 0 0 5px #00ffcc;
    }

    .main-box {
        border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;
        background: rgba(0, 10, 20, 0.85); box-shadow: 0 0 30px rgba(0, 255, 204, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 授權資料庫 ---
if "auth" not in st.session_state: st.session_state["auth"] = False
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {"1-1":3, "a-1":5, "zpim2026":999}

# --- 3. 登入畫面 (貫穿背景) ---
if not st.session_state["auth"]:
    st.markdown('<div style="height: 150px;"></div>', unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.header("🔒 ZPIM 2026 系統鎖定")
        st.write("Access Restricted: Authorized Personnel Only")
        pwd = st.text_input("請輸入授權代碼", type="password")
        if st.button("🚀 啟動驗證"):
            if pwd.isdigit() and int(pwd) >= 999:
                st.session_state["auth"] = True; st.session_state["lvl"] = "首席顧問"; st.rerun()
            elif pwd in st.session_state["auth_db"] and st.session_state["auth_db"][pwd] > 0:
                st.session_state["auth_db"][pwd] -= 1
                st.session_state["auth"] = True; st.session_state["lvl"] = "合作夥伴"; st.rerun()
            else: st.error("❌ 代碼無效")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 4. 進入後的首頁 (延續背景與 101) ---
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.sidebar.markdown(f"🚩 **當前權限**：{st.session_state['lvl']}")

# 4Q 調整
q1 = st.sidebar.slider("Q1 實體實相 %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯實相 %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務實相 %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運實相 %", 0, 100, 100)

if st.sidebar.button("🚀 啟動完整診斷"):
    st.bar_chart(pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '值':[q1,q2,q3,q4]}).set_index('維度'), color="#FF0000")
    
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("📜 首席顧問 鑑定結論")
    st.success(f"✅ Q1 實體 ({q1}%) | ✅ Q2 邏輯 ({q2}%) | ✅ Q3 財務 ({q3}%) | ✅ Q4 營運 ({q4}%)")
    st.markdown(f"""
        <hr style="border-top: 2px dashed #00ffcc;">
        <h2 style="color: #00ffcc; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center;">總評級：<b>S 級 (戰略領航者)</b> | ID: ZPIM-{int(time.time())}</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.sidebar.button("🔒 安全退出"):
    st.session_state.clear(); st.rerun()
