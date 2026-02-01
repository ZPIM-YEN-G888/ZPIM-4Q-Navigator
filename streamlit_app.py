import streamlit as st
import pandas as pd
import time

# --- 1. 頂級視覺 CSS (強化左側亮度、右側圖騰、繁體美化) ---
st.set_page_config(page_title="ZPIM 2026 巔峰導航儀", layout="wide")
st.markdown("""
    <style>
    /* 全局字體與背景 */
    html, body, [class*="st-"] {
        font-family: "Microsoft JhengHei", "Noto Sans TC", sans-serif !important;
        color: #FFFFFF !important;
    }
    .stApp {
        background-color: #000c14;
        background-image: radial-gradient(circle at 2px 2px, #00ffcc 1px, transparent 0);
        background-size: 50px 50px;
    }
    
    /* 左側邊欄強化：解決字體模糊問題 */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 30, 40, 0.95) !important;
        border-right: 2px solid #00ffcc;
    }
    section[data-testid="stSidebar"] .stMarkdown p, section[data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 0 5px #00ffcc;
    }

    /* 右側旗艦 101 圖騰意象 */
    .stApp::after {
        content: "🏢 101 戰略頂點";
        position: fixed; bottom: 20px; right: 20px;
        font-size: 5rem; opacity: 0.05; color: #00ffcc;
        writing-mode: vertical-rl; pointer-events: none;
    }

    .main-box {
        border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;
        background: rgba(0, 15, 25, 0.9); box-shadow: 0 0 25px rgba(0, 255, 204, 0.4);
    }
    .watermark {
        position: fixed; top: 40%; left: 50%; transform: translate(-50%, -50%) rotate(-25deg);
        color: #00ffcc; opacity: 0.05; font-size: 80px; font-weight: bold; pointer-events: none;
    }
    </style>
    <div class="watermark">ZPIM 2026 繁體主權核定</div>
    """, unsafe_allow_html=True)

# --- 2. 授權與門禁 ---
if "auth" not in st.session_state: st.session_state["auth"] = False
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {"1-1":3, "a-1":5, "zpim2026":999}

if not st.session_state["auth"]:
    st.markdown('<div class="main-box" style="max-width:500px; margin: 100px auto;">', unsafe_allow_html=True)
    st.header("🔒 ZPIM 2026 系統鎖定")
    pwd = st.text_input("輸入授權代碼", type="password")
    if st.button("🚀 驗證身份"):
        if pwd.isdigit() and int(pwd) >= 999:
            st.session_state["auth"] = True; st.session_state["lvl"] = "首席顧問"; st.rerun()
        elif pwd in st.session_state["auth_db"] and st.session_state["auth_db"][pwd] > 0:
            st.session_state["auth_db"][pwd] -= 1
            st.session_state["auth"] = True; st.session_state["lvl"] = "合作夥伴"; st.rerun()
        else: st.error("❌ 代碼無效")
    st.markdown('</div>', unsafe_allow_html=True); st.stop()

# --- 3. 核心內容 ---
st.sidebar.title("📊 戰略參數對位")
st.sidebar.markdown(f"🚩 **權限等級**：{st.session_state['lvl']}")

q1 = st.sidebar.slider("Q1 實體實相 %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯實相 %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務實相 %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運實相 %", 0, 100, 100)

st.title("🚀 ZPIM 2026 旗艦戰略導航儀")

if st.sidebar.button("🚀 啟動完整診斷"):
    # 顯化紅色柱圖
    data = pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '值':[q1,q2,q3,q4]})
    st.bar_chart(data.set_index('維度'), color="#FF0000")
    
    # 強化版鑑定結論
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("📜 首席顧問 鑑定結論 (繁體巔峰版)")
    c1, c2 = st.columns(2)
    with c1:
        st.success(f"✅ **Q1 實體實相** ({q1}%): 資產底蘊定格穩定。")
        st.success(f"✅ **Q2 邏輯實相** ({q2}%): 運算邏輯純度極高。")
    with c2:
        st.success(f"✅ **Q3 財務實相** ({q3}%): 獲利實相已達成閉環。")
        st.success(f"✅ **Q4 營運實相** ({q4}%): 主權清晰，執行精準。")
    
    st.info("💡 **戰略建議**：結構極度穩固。請維持 4Q 維度之同步噴發，確保 2026 實相主權。")
    
    st.markdown(f"""
        <hr style="border-top: 2px dashed #00ffcc;">
        <h2 style="color: #00ffcc; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center;">總評級：<b>S 級 (戰略領航者)</b> | ID: ZPIM-{int(time.time())}</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.sidebar.button("🔒 安全退出"):
    st.session_state.clear(); st.rerun()
