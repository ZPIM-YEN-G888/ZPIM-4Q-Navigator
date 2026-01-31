import streamlit as st
import pandas as pd
import time

# --- 1. 旗艦設定 ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

# --- 2. 戰略授權庫 (分級計次熔斷) ---
# 避開 4，1-x 系列限 3 次，a-x 系列限 5 次
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {
        "1-1": 3, "1-2": 3, "1-3": 3, "1-5": 3, "1-6": 3,
        "a-1": 5, "a-2": 5, "a-3": 5, "a-5": 5, "a-6": 5
    }

# --- 3. 門禁入口 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("### 🛡️ ZPIM 2026 戰略授權節點")
    pwd = st.text_input("輸入授權代碼", type="password")
    if st.button("🚀 驗證身份"):
        if pwd.isdigit() and int(pwd) >= 999: # 首席無限版
            st.session_state["authenticated"] = True
            st.session_state["level"] = "MASTER"
            st.rerun()
        elif pwd in st.session_state["auth_db"]: # 客用計次版
            if st.session_state["auth_db"][pwd] > 0:
                st.session_state["auth_db"][pwd] -= 1
                st.session_state["authenticated"] = True
                st.session_state["level"] = "GUEST"
                st.session_state["remains"] = st.session_state["auth_db"][pwd]
                st.rerun()
            else:
                st.error("🚫 授權已枯竭")
        else:
            st.error("❌ 無效代碼")
    st.stop()

# --- 4. 核心系統 (100張素材邏輯) ---
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.sidebar.markdown(f"**授權：** {st.session_state.get('level')}")
if st.session_state.get("level") == "GUEST":
    st.sidebar.warning(f"⏳ 剩餘次數：{st.session_state.get('remains')}")

# 4Q 拉桿調整
q1 = st.sidebar.slider("Q1 實體 %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯 %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務 %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運 %", 0, 100, 100)

if st.sidebar.button("🚀 啟動完整診斷"):
    # 紅色柱圖顯化
    data = pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '值':[q1,q2,q3,q4]})
    st.bar_chart(data.set_index('維度'), color="#FF0000")
    
    # 浮水印證書
    st.markdown(f"""
    <div style="border: 2px solid #D4AF37; padding: 20px; position: relative;">
        <div style="position: absolute; opacity: 0.1; transform: rotate(-30deg); font-size: 50px;">CONFIDENTIAL</div>
        <h2 style="text-align: center;">📜 ZPIM 2026 戰略診斷書</h2>
        <p>總評級：S 級</p>
        <p style="text-align: right;">首席顧問 鑑定核可</p>
    </div>
    """, unsafe_allow_html=True)
