import streamlit as st
import pandas as pd
import time

# --- 1. 頂級旗艦視覺 CSS (強制繁體、字體加粗、101 意象) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@700&display=swap');
    
    .stApp {
        background-color: #000c14;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(0, 255, 204, 0.1) 0%, transparent 80%),
            url("https://www.transparenttextures.com/patterns/stardust.png"); /* 星空紋理 */
        background-attachment: fixed;
    }
    
    /* 強制繁體字體與清晰度 */
    html, body, [class*="st-"] {
        font-family: "Microsoft JhengHei", "Noto Sans TC", sans-serif !important;
        color: #FFFFFF !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }

    /* 旗艦 101 宏偉背景意象 */
    .stApp::before {
        content: "";
        position: fixed; bottom: 0; right: 10%; width: 150px; height: 400px;
        background: linear-gradient(to top, rgba(0, 255, 204, 0.2) 0%, transparent 100%);
        clip-path: polygon(40% 0%, 60% 0%, 100% 100%, 0% 100%); /* 簡約塔型意象 */
        z-index: -1;
    }

    .main-box {
        border: 2px solid #00ffcc; padding: 30px; border-radius: 15px;
        background: rgba(0, 20, 30, 0.85); box-shadow: 0 0 30px rgba(0, 255, 204, 0.3);
        margin-bottom: 20px;
    }

    .watermark {
        position: fixed; top: 45%; left: 50%; transform: translate(-50%, -50%) rotate(-25deg);
        color: #00ffcc; opacity: 0.07; font-size: 90px; font-weight: bold; pointer-events: none; z-index: 999;
        white-space: nowrap;
    }
    </style>
    <div class="watermark">ZPIM 2026 繁體主權專屬</div>
    """, unsafe_allow_html=True)

# --- 2. 授權資料庫 ---
if "auth_db" not in st.session_state:
    st.session_state["auth_db"] = {"1-1":3, "1-2":3, "a-1":5, "a-2":5}
if "auth" not in st.session_state: st.session_state["auth"] = False

# --- 3. 門禁介面 ---
if not st.session_state["auth"]:
    st.markdown('<div class="main-box" style="max-width:500px; margin: 100px auto;">', unsafe_allow_html=True)
    st.header("🔒 ZPIM 2026 戰略授權節點")
    pwd = st.text_input("輸入授權代碼", type="password")
    if st.button("🚀 啟動驗證"):
        if pwd.isdigit() and int(pwd) >= 999:
            st.session_state["auth"] = True; st.session_state["lvl"] = "首席顧問"; st.rerun()
        elif pwd in st.session_state["auth_db"] and st.session_state["auth_db"][pwd] > 0:
            st.session_state["auth_db"][pwd] -= 1
            st.session_state["auth"] = True; st.session_state["lvl"] = "高級夥伴"; st.rerun()
        else: st.error("🚫 授權無效或已過期")
    st.markdown('</div>', unsafe_allow_html=True); st.stop()

# --- 4. 旗艦系統內容 ---
st.sidebar.title("📊 戰略參數對位")
st.sidebar.info(f"當前權限：{st.session_state['lvl']}")

q1 = st.sidebar.slider("Q1 實體實相 (資產/基礎) %", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯實相 (專利/算法) %", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務實相 (利潤/閉環) %", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運實相 (主權/團隊) %", 0, 100, 100)

st.title("🚀 ZPIM 2026 巔峰戰略導航儀")

if st.sidebar.button("🚀 啟動完整診斷"):
    # 紅色柱圖
    data = pd.DataFrame({'維度':['Q1','Q2','Q3','Q4'], '百分比':[q1,q2,q3,q4]})
    st.bar_chart(data.set_index('維度'), color="#FF0000")
    
    # 首席鑑定區
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("📜 首席顧問 鑑定結論 (繁體正式版)")
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"✅ **Q1 實體實相** ({q1}%): 資產底蘊定格穩定。")
        st.write(f"✅ **Q2 邏輯實相** ({q2}%): 運算邏輯純度極高。")
    with c2:
        st.write(f"✅ **Q3 財務實相** ({q3}%): 獲利實相已達成閉環。")
        st.write(f"✅ **Q4 營運實相** ({q4}%): 主權清晰，團隊執行精準。")
    
    st.info("💡 **戰略核心建議**：結構穩固，主權定格。請維持 4Q 維度之高頻共振。")
    
    st.markdown(f"""
        <hr style="border-top: 2px dashed #00ffcc;">
        <h2 style="color: #00ffcc; text-align: center;">📜 零點實相 2026 官方鑑定書</h2>
        <p style="text-align: center;"><b>總評級：S 級 (戰略領航者)</b></p>
        <p style="text-align: right;">鑑定編號：ZPIM-{int(time.time())}</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.sidebar.button("🔒 安全登出"):
    st.session_state.clear(); st.rerun()
