import streamlit as st
import pandas as pd
try:
    import plotly.graph_objects as go
    has_plotly = True
except:
    has_plotly = False

# --- 1. 全域視覺主權 (解決模糊與隱形問題) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

# 動態電路圖 SVG
circuit_svg = """
<div style="text-align:center; margin-bottom: 20px;">
    <svg width="200" height="60" viewBox="0 0 250 60">
        <path d="M0 30 L60 30 L80 10 L110 50 L130 30 L250 30" stroke="#00AA00" fill="transparent" stroke-width="4">
            <animate attributeName="stroke-dasharray" from="0,500" to="500,0" dur="2s" repeatCount="indefinite" />
        </path>
        <circle cx="130" cy="30" r="6" fill="#00FF00" />
    </svg>
    <p style="color:#007700; font-weight:900; font-size:1rem;">⚡ 核心數據通訊中</p>
</div>
"""

st.markdown("""
    <style>
    /* 全域背景保持星空感 */
    .stApp {
        background: radial-gradient(circle at center, #001a1a 0%, #000000 100%) !important;
    }
    
    /* 修正側邊欄字體：在淺色背景下使用深色字 */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {
        color: #111111 !important;  /* 強制深黑字體，確保清晰度 */
        font-weight: 900 !important;
        font-size: 1.1rem !important;
    }
    
    /* 修正按鈕文字看不到的問題 */
    div.stButton > button {
        background-color: #00FF00 !important;
        color: #000000 !important; /* 按鈕字體改為黑色 */
        font-weight: 900 !important;
        border: 2px solid #004400 !important;
    }
    
    /* 101 戰略燈塔 */
    .tower {
        position: fixed; bottom: 0; right: 5%; width: 150px; height: 400px;
        background: linear-gradient(to top, #00FF0011, transparent);
        clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%);
        z-index: 0;
    }
    </style>
    <div class="tower"></div>
    """, unsafe_allow_html=True)

# --- 2. 門禁系統 ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🛡️ ZPIM 2026 核心安全驗證")
    st.markdown(circuit_svg, unsafe_allow_html=True)
    
    pwd = st.text_input("輸入首席顧問密鑰：", type="password")
    if st.button("啟動電路導通"):
        if pwd == "zpim888-2560" or pwd == "1-1":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("密鑰錯誤")
    st.stop()

# --- 3. 戰略操控區 (左側) ---
st.sidebar.markdown(circuit_svg, unsafe_allow_html=True) # 將跳動電路圖移至左側上方
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

# --- 4. 鑑定書產出 ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
        <div style="background: rgba(0,255,0,0.05); padding: 20px; border-radius: 10px; border: 1px solid #00FF00;">
            <h3 style="color:#00FF00 !important;">📊 四維度深度診斷報告</h3>
            <p style="color:white !important;">✅ <b>Q1 實體維度 ({q1}%)</b></p>
            <p style="color:white !important;">✅ <b>Q2 靈性邏輯 ({q2}%)</b></p>
            <p style="color:white !important;">✅ <b>Q3 財務權限 ({q3}%)</b></p>
            <p style="color:white !important;">✅ <b>Q4 營運藥方 ({q4}%)</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.success("🎯 改善對策：根據 101 模式建議持續監控。")

    with col2:
        if has_plotly:
            fig = go.Figure(data=go.Scatterpolar(
                r=[q1, q2, q3, q4, q1], theta=['Q1','Q2','Q3','Q4','Q1'],
                fill='toself', line_color='#00FF00', fillcolor='rgba(0, 255, 0, 0.2)'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100], color="white")),
                showlegend=False, paper_bgcolor='rgba(0,0,0,0)', font_color="#00FF00"
            )
            st.plotly_chart(fig, use_container_width=True)

st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v2.4")
