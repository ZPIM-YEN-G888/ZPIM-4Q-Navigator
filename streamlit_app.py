import streamlit as st
import pandas as pd
# 嘗試導入高級圖表，如果還沒安裝好就用備用圖表
try:
    import plotly.graph_objects as go
    has_plotly = True
except:
    has_plotly = False

# --- 1. 視覺主權暴力加強 (星空、電路板、字體) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

st.markdown("""
    <style>
    /* 星際噴發全域背景 */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #001a1a 0%, #000000 100%) !important;
        background-attachment: fixed !important;
    }
    /* 左側字體：極致螢光綠，加粗加黑底 */
    .stSlider label, .stMarkdown p, .stSideBar label {
        color: #00ffcc !important;
        font-size: 1.2rem !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 4px #000000 !important;
    }
    /* 101 戰略燈塔實體化 */
    .tower {
        position: fixed; bottom: 0; right: 5%; width: 180px; height: 500px;
        background: linear-gradient(to top, #00ffcc44, transparent);
        clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%);
        z-index: 0; filter: drop-shadow(0 0 20px #00ffcc);
    }
    </style>
    <div class="tower"></div>
    """, unsafe_allow_html=True)

# --- 2. 門禁系統 (含動態電路板) ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🛡️ ZPIM 2026 核心安全驗證")
    # 封面動態電路板
    st.markdown("""
        <div style="text-align:center; padding: 20px;">
            <svg width="300" height="100" viewBox="0 0 300 100">
                <path d="M0 50 L50 50 L70 20 L100 80 L130 50 L300 50" stroke="#00ffcc" fill="transparent" stroke-width="3">
                    <animate attributeName="stroke-dasharray" from="0,500" to="500,0" dur="3s" repeatCount="indefinite" />
                </path>
                <circle cx="130" cy="50" r="8" fill="#00ffcc">
                    <animate attributeName="r" values="5;10;5" dur="1s" repeatCount="indefinite" />
                </circle>
            </svg>
            <p style="color:#00ffcc; font-weight:bold;">電路掃描中... 準備解鎖</p>
        </div>
    """, unsafe_allow_html=True)
    
    pwd = st.text_input("輸入首席顧問密鑰：", type="password")
    if st.button("啟動電路導通"):
        if pwd == "zpim888-2560" or pwd == "1-1":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("密鑰錯誤")
    st.stop()

# --- 3. 戰略操控區 (含安全退出) ---
st.sidebar.title("🎮 戰略導航中心")
st.sidebar.markdown("---")
q1 = st.sidebar.slider("Q1 實體資產權重 (%)", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯導向參數 (%)", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務動能指標 (%)", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運藥方配比 (%)", 0, 100, 100)

st.sidebar.markdown("---")
if st.sidebar.button("🔒 安全退出系統"):
    st.session_state.authenticated = False
    st.rerun()

# --- 4. 鑑定書產出 (告別藍柱子) ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        ### 📊 四維度深度診斷報告
        - ✅ **Q1 實體維度 ({q1}%)**：實相資產穩固，具備噴發基礎。
        - ✅ **Q2 靈性邏輯 ({q2}%)**：思維導航清晰，建議強化主權意識。
        - ✅ **Q3 財務權限 ({q3}%)**：流動性安全，應注意計次扣點。
        - ✅ **Q4 營運藥方 ({q4}%)**：藥品與電路狀態優良，執行 101 加值。
        """)
        st.success("🎯 改善對策：根據 101 模式，建議維持核心權限以確保戰略主權。")

    with col2:
        if has_plotly:
            # 高級戰略雷達圖
            fig = go.Figure(data=go.Scatterpolar(
              r=[q1, q2, q3, q4, q1],
              theta=['Q1實體','Q2邏輯','Q3財務','Q4營運','Q1實體'],
              fill='toself',
              line_color='#00ffcc',
              fillcolor='rgba(0, 255, 204, 0.3)'
            ))
            fig.update_layout(
              polar=dict(radialaxis=dict(visible=True, range=[0, 100], color="white", gridcolor="#444")),
              showlegend=False,
              paper_bgcolor='rgba(0,0,0,0)',
              font_color="#00ffcc"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            # 備用圖表（如果 plotly 還在安裝中）
            st.warning("雷達圖工具安裝中，暫以導航數據呈現：")
            st.json({"Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4})

st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v2.2")
