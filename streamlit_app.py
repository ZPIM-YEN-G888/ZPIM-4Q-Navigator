import streamlit as st
import pandas as pd
import time

# --- 1. 旗艦設定與星空背景注入 ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

# 這裡注入星空背景圖與 CSS 樣式
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/ZPIM-YEN-G888/ZPIM-4Q-Navigator/main/background.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .st-emotion-cache-16idsys p { color: white; } /* 確保文字清晰 */
    </style>
    """, unsafe_allow_html=True)

# --- 2. 戰略授權庫 (分級計次) ---
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {
        "1-1": 3, "1-2": 3, "1-3": 3, "1-5": 3, "1-6": 3,
        "a-1": 5, "a-2": 5, "a-3": 5, "a-5": 5, "a-6": 5
    }

# --- 3. 數位門禁介面 (電路板風格) ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🛡️ ZPIM 2026 戰略授權節點")
    st.info("Access Restricted: Authorized Personnel Only")
    pwd = st.text_input("輸入授權代碼", type="password")
    if st.button("🚀 啟動驗證"):
        if pwd.isdigit() and int(pwd) >= 999:
            st.session_state["authenticated"] = True
            st.session_state["level"] = "MASTER"
            st.rerun()
        elif pwd in st.session_state["auth_db"]:
            if st.session_state["auth_db"][pwd] > 0:
                st.session_state["auth_db"][pwd] -= 1
                st.session_state["authenticated"] = True
                st.session_state["level"] = "GUEST"
                st.session_state["remains"] = st.session_state["auth_db"][pwd]
                st.rerun()
            else:
                st.error("🚫 授權已枯竭")
    st.stop()

# --- 4. 巔峰顯化：第一張畫面即是星空導航 ---
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.sidebar.markdown(f"**授權身份：** {st.session_state['level']}")

# 4Q 調整拉桿
q1 = st.sidebar.slider("Q1 實體 (Physical) %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯 (Logic) %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務 (Financial) %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運 (Operation) %", 0, 100, 100)

if st.sidebar.button("🚀 啟動完整診斷"):
    # 紅色柱圖顯化
    data = pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '值':[q1,q2,q3,q4]})
    st.bar_chart(data.set_index('維度'), color="#FF0000")
    
    # 首席鑑定結論與帶浮水印證書
    st.markdown(f"""
    <div style="border: 4px solid #D4AF37; padding: 25px; border-radius: 15px; background: rgba(0,0,0,0.6); position: relative;">
        <div style="position: absolute; opacity: 0.1; transform: rotate(-30deg); font-size: 50px; width:100%; text-align:center; color:white;">CONFIDENTIAL</div>
        <h2 style="color: #D4AF37; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center; color: white;"><b>總評級：S 級 (結構穩固，主權定格)</b></p>
        <p style="text-align: right; color: white;">鑑定編號：ZPIM-{int(time.time())}</p>
    </div>
    """, unsafe_allow_html=True)
