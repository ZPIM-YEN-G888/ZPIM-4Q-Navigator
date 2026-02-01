import streamlit as st
import pandas as pd

# --- 1. 視覺與背景主權設定 (星際噴發 & 101燈塔 CSS) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #001524 0%, #000000 100%);
        color: #e0e0e0;
    }
    /* 101 戰略燈塔繪圖 */
    .tower {
        position: fixed; bottom: 0; right: 5%; width: 150px; height: 400px;
        background: linear-gradient(to top, #00ffcc66, transparent);
        clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%);
        z-index: 0; filter: drop-shadow(0 0 15px #00ffcc);
    }
    /* 側邊欄拉桿美化 */
    .stSlider label { color: #00ffcc !important; font-weight: bold; }
    </style>
    <div class="tower"></div>
    """, unsafe_allow_html=True)

# --- 2. 門禁安全系統 (密碼與網址隱身) ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🛡️ ZPIM 2026 核心安全驗證")
    # 電路板 SVG 裝飾 (簡化表示)
    st.markdown("🔒 系統已進入主權防護狀態，請輸入首席顧問密鑰：")
    pwd = st.text_input("PASSWORD", type="password")
    if st.button("啟動電路導通"):
        if pwd == "zpim888-2560" or pwd == "1-1":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("密鑰錯誤，存取拒絕。")
    st.stop()

# --- 3. 戰略操控區 (拉桿補齊標籤與%數) ---
st.sidebar.title("🎮 戰略導航控制中心")
st.sidebar.info("首席顧問：已接通計次門禁系統")

q1 = st.sidebar.slider("Q1 實體資產權重 (%)", 0, 100, 80, format="%d%%")
q2 = st.sidebar.slider("Q2 邏輯導向參數 (%)", 0, 100, 75, format="%d%%")
q3 = st.sidebar.slider("Q3 財務動能指標 (%)", 0, 100, 60, format="%d%%")
q4 = st.sidebar.slider("Q4 營運藥方配比 (%)", 0, 100, 90, format="%d%%")

# --- 4. 二次扣點與運算邏輯 ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    # 此處觸發扣點邏輯 (對應您的 Google Sheets API)
    st.toast("二次調整確認，正在核銷點數...", icon="💳")
    
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 四維度深度診斷報告")
        # 恢復 ✅ 符號與深度說明
        st.write(f"✅ **Q1 實體維度 ({q1}%)**：實相資產穩固，具備噴發基礎。")
        st.write(f"✅ **Q2 靈性邏輯 ({q2}%)**：思維導航清晰，建議強化主權意識。")
        st.write(f"✅ **Q3 財務權限 ({q3}%)**：流動性安全，應注意計次扣點頻率。")
        st.write(f"✅ **Q4 營運藥方 ({q4}%)**：藥品與電路狀態優良，建議執行 101 加值。")
        
        st.success("🎯 改善對策：根據 101 模式，建議提升 Q3 權重以觸發最高等級鑑定。")

    with col2:
        # 101 燈塔數據視覺化 (示意)
        chart_data = pd.DataFrame([q1, q2, q3, q4], index=['Q1', 'Q2', 'Q3', 'Q4'], columns=['強度'])
        st.bar_chart(chart_data)
        st.caption("101 戰略燈塔數據投影")

st.markdown("---")
st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v2.0")
