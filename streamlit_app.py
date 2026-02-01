import streamlit as st
import pandas as pd
import time

# --- 1. 旗艦設定與 CSS 視覺注入 (發光電路板、發光星空、發光浮水印) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

st.markdown("""
    <style>
    /* 全局背景：發光電路板風格 */
    .stApp {
        background-color: #000c14; /* 深藍黑色底 */
        background-image: radial-gradient(circle at 2px 2px, #00ffcc 1px, transparent 0); /* 發光點 */
        background-size: 40px 40px; /* 點陣密度 */
        animation: glow_bg 10s infinite alternate; /* 背景發光動畫 */
    }
    @keyframes glow_bg {
        from { box-shadow: inset 0 0 50px rgba(0, 255, 204, 0.2); }
        to { box-shadow: inset 0 0 80px rgba(0, 255, 204, 0.6); }
    }

    /* 確保所有文字在深色背景下可見 */
    h1, h2, h3, h4, h5, h6, p, .stMarkdown, .stLabel, .streamlit-expanderHeader {
        color: #E0FFFF !important; /* 淺青色發光文字 */
    }
    
    /* 左側邊欄背景 */
    .st-emotion-cache-vk3377 { /* Sidebar的CSS class會隨版本變動，這是一個常見的 */
        background-color: rgba(0, 15, 30, 0.8) !important; /* 半透明深藍 */
    }

    /* 門禁與證書的區塊樣式 */
    .main-box {
        border: 2px solid #00ffcc; /* 發光邊框 */
        padding: 25px;
        border-radius: 10px;
        background-color: rgba(0, 20, 20, 0.9); /* 更深背景 */
        box-shadow: 0 0 20px #00ffcc; /* 發光效果 */
        animation: pulse_box 3s infinite alternate; /* 區塊脈動動畫 */
    }
    @keyframes pulse_box {
        from { box-shadow: 0 0 10px #00ffcc; }
        to { box-shadow: 0 0 30px #00ffcc; }
    }

    /* 證書浮水印：發光效果 */
    .certificate-watermark {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(-30deg);
        opacity: 0.15; /* 更明顯一些 */
        font-size: 60px;
        color: #00ffcc; /* 發光顏色 */
        text-shadow: 0 0 15px #00ffcc; /* 文字發光 */
        z-index: 1000;
        pointer-events: none;
        white-space: nowrap;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 戰略授權庫 (避 4 計次熔斷) ---
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {
        "1-1": 3, "1-2": 3, "1-3": 3, "1-5": 3, "1-6": 3,
        "a-1": 5, "a-2": 5, "a-3": 5, "a-5": 5, "a-6": 5
    }

# --- 3. 電路板門禁介面 (Gateway) ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.title("🔒 ZPIM 2026 系統鎖定")
    st.write("Access Restricted: Authorized Personnel Only (ZPIM Secure Node)")
    pwd = st.text_input("輸入授權代碼", type="password")
    if st.button("🚀 啟動驗證"):
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
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- 4. 巔峰顯化：發光星空、紅柱、發光證書 ---
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.sidebar.markdown(f"**授權身份：** {st.session_state['level']}")
if st.session_state.get('level') == "GUEST":
    st.sidebar.warning(f"⏳ 剩餘可用次數：{st.session_state.get('remains')}")


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
    <div class="main-box" style="margin-top: 30px;">
        <div class="certificate-watermark">ZPIM 2026 EXCLUSIVE</div>
        <h2 style="color: #00ffcc; text-align: center; text-shadow: 0 0 10px #00ffcc;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center; color: #E0FFFF;"><b>總評級：S 級 (結構穩固，主權定格)</b></p>
        <p style="color: #E0FFFF;"><b>鑑定編號：ZPIM-{int(time.time())}</b></p>
        <hr style="border-top: 2px dashed #00ffcc;">
        <p style="color: #E0FFFF;">✅ **Q1 實體**：優異，資產定格狀態穩定。</p>
        <p style="color: #E0FFFF;">✅ **Q2 邏輯**：強悍，算法主權是關鍵。</p>
        <p style="color: #E0FFFF;">✅ **Q3 財務**：閉環，注意資金流實相。</p>
        <p style="color: #E0FFFF;">✅ **Q4 營運**：主權清晰，強化決策純度。</p>
        <p style="text-align: right; color: #E0FFFF; margin-top: 20px;"><b>首席顧問 已授權數位簽章</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. 安全退出 ---
if st.sidebar.button("🔒 安全退出"):
    st.session_state.clear()
    st.rerun()
