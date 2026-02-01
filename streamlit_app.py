import streamlit as st
import pandas as pd
try:
    import plotly.graph_objects as go
    has_plotly = True
except:
    has_plotly = False

# --- 1. 全域視覺主權 (字體銳化與電路圖) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

# 電路跳動動畫代碼 (用於重複調用)
circuit_svg = """
<div style="text-align:center;">
    <svg width="250" height="60" viewBox="0 0 250 60">
        <path d="M0 30 L60 30 L80 10 L110 50 L130 30 L250 30" stroke="#00FF00" fill="transparent" stroke-width="3">
            <animate attributeName="stroke-dasharray" from="0,500" to="500,0" dur="2s" repeatCount="indefinite" />
        </path>
        <circle cx="130" cy="30" r="6" fill="#00FF00">
            <animate attributeName="opacity" values="1;0.3;1" dur="1s" repeatCount="indefinite" />
        </circle>
    </svg>
    <p style="color:#00FF00; font-weight:900; letter-spacing:2px; font-size:1.1rem;">ZPIM 核心數據通訊中</p>
</div>
"""

st.markdown(f"""
    <style>
    .stApp {{
        background: radial-gradient(circle at center, #001a1a 0%, #000000 100%) !important;
        -webkit-font-smoothing: antialiased;
    }}
    /* 強制所有字體銳化與加粗 */
    .stSlider label, .stMarkdown, p, h1, h2, h3, span, li {{
        color: #FFFFFF !important;  /* 改為純白以解決模糊問題 */
        font-weight: 900 !important;
        font-family: "Microsoft JhengHei", sans-serif !important;
        text-shadow: none !important; /* 移除陰影以防暈光 */
    }}
    /* 特殊標籤顏色：維持亮綠但增加對比 */
    .stSlider label {{ color: #00FF00 !important; font-size: 1.2rem !important; }}
    
    .tower {{
        position: fixed; bottom: 0; right: 5%; width: 180px; height: 500px;
        background: linear-gradient(to top, #00FF0022, transparent);
        clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%);
        z-index: 0;
    }}
    </style>
    <div class="tower"></div>
    """, unsafe_allow_html=True)

# --- 2. 門禁系統 (含電路跳動) ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🛡️ ZPIM 2026 核心安全驗證")
    st.markdown(circuit_svg, unsafe_allow_html=True) # 登入頁電路圖
    
    pwd = st.text_input("輸入首席顧問密鑰：", type="password")
    if st.button("啟動電路導通"):
        if pwd == "zpim888-2560" or pwd == "1-1":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("密鑰錯誤")
    st.stop()

# --- 3. 戰略操控區 (字體加粗加大) ---
st.sidebar.title("🎮 戰略導航中心")
st.sidebar.markdown(circuit_svg, unsafe_allow_html=True) # 主頁側邊欄電路圖
st.sidebar.markdown("---")

q1 = st.sidebar.slider("Q1 實體資產權重 (%)", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯導向參數 (%)", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務動能指標 (%)", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運藥方配比 (%)", 0, 100, 100)

st.sidebar.markdown("---")
if st.sidebar.button("🔒 安全退出系統"):
    st.session_state.authenticated = False
    st.rerun()

# --- 4. 鑑定書產出 (高對比銳化) ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        ### 📊 四維度深度診斷報告
        * ✅ **Q1 實體維度 ({q1}%)**：實相資產穩固。
        * ✅ **Q2 靈性邏輯 ({q2}%)**：思維導航清晰。
        * ✅ **Q3 財務權限 ({q3}%)**：流動性安全。
        * ✅ **Q4 營運藥方 ({q4}%)**：藥品電路優良。
        """)
        st.success("🎯 改善對策：根據 101 模式，建議維持核心權限。")

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
        else:
            st.json({"Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4})

st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v2.3")
