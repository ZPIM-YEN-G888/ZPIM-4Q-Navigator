import streamlit as st
import pandas as pd
try:
    import plotly.graph_objects as go
    has_plotly = True
except:
    has_plotly = False

# --- 1. 全域視覺 (極致對比、背景點亮、防偽浮水印) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

st.markdown("""
    <style>
    /* 點亮星際背景：改用較亮的藍綠底色 */
    .stApp {
        background: radial-gradient(circle at 40% 40%, #004d4d 0%, #000000 100%) !important;
        background-attachment: fixed !important;
    }
    
    /* 全域防偽浮水印：改為科技綠暗紋 */
    .stApp::before {
        content: "ZPIM 2026 OFFICIAL 首席顧問專屬 ";
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        font-size: 26px; color: rgba(0, 255, 204, 0.12);
        pointer-events: none; z-index: 1000;
        display: flex; flex-wrap: wrap; transform: rotate(-30deg);
        justify-content: space-around; line-height: 220px;
    }

    /* 登入標題：加粗白字 */
    h1 { color: #FFFFFF !important; font-weight: 900 !important; letter-spacing: 3px; }

    /* 左側側邊欄：徹底解決白底白字，改用深綠色 */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {
        color: #004400 !important; /* 極致深綠，確保在白底看得見 */
        font-weight: 900 !important;
        font-size: 1.2rem !important;
    }

    /* 鑑定書區塊：強制亮化 */
    .id-card {
        background: rgba(0, 20, 20, 0.95);
        border: 3px solid #00FFCC;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 0 50px rgba(0, 255, 204, 0.5);
    }
    .id-card p, .id-card h3 {
        color: #FFFFFF !important; /* 診斷文字維持白色 */
        font-weight: 900 !important;
    }

    /* 按鈕亮化 */
    div.stButton > button {
        background-color: #00FF00 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        border: 2px solid #FFFFFF;
    }

    /* 101 戰略燈塔：全功率增亮 */
    .tower {
        position: fixed; bottom: 0; right: 5%; width: 220px; height: 550px;
        background: linear-gradient(to top, rgba(0, 255, 204, 0.6), transparent);
        clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%);
        z-index: -1;
        filter: brightness(1.5) drop-shadow(0 0 40px #00FFCC);
    }
    </style>
    <div class="tower"></div>
    """, unsafe_allow_html=True)

# 電路跳動動畫
circuit_svg = """
<div style="text-align:center; margin-bottom: 20px;">
    <svg width="280" height="70" viewBox="0 0 280 70">
        <path d="M0 35 L80 35 L100 10 L130 60 L160 35 L280 35" stroke="#00AA00" fill="transparent" stroke-width="5">
            <animate attributeName="stroke-dasharray" from="0,500" to="500,0" dur="1.3s" repeatCount="indefinite" />
        </path>
    </svg>
    <p style="color:#004400; font-weight:900; letter-spacing:2px;">⚡ ZPIM 數據通訊中</p>
</div>
"""

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
st.sidebar.markdown(circuit_svg, unsafe_allow_html=True)
st.sidebar.title("🎮 戰略導航中心")
st.sidebar.markdown("---")
q1 = st.sidebar.slider("Q1 實體資產權重 (%)", 0, 100, 100)
q2 = st.sidebar.slider("Q2 靈性邏輯參數 (%)", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務動能指標 (%)", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運藥方配比 (%)", 0, 100, 100)

if st.sidebar.button("🔒 安全退出系統"):
    st.session_state.authenticated = False
    st.rerun()

# --- 4. 鑑定書產出 ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
        <div class="id-card">
            <h3 style="color:#00FFCC !important;">📊 四維度深度診斷報告</h3>
            <br>
            <p>✅ <b>Q1 實體維度：{q1}%</b> - 核心資產已定格</p>
            <p>✅ <b>Q2 靈性邏輯：{q2}%</b> - 指引路徑極致</p>
            <p>✅ <b>Q3 財務權限：{q3}%</b> - 點數核銷正常</p>
            <p>✅ <b>Q4 營運藥方：{q4}%</b> - 電路通訊優良</p>
            <hr style="border: 1px solid #00FFCC;">
            <p style="color:#00FFCC !important; font-size:1.1rem;">🎯 <b>改善對策：</b>101 燈塔全功率運作中，防偽主權已鎖定。</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if has_plotly:
            fig = go.Figure(data=go.Scatterpolar(
                r=[q1, q2, q3, q4, q1], theta=['Q1','Q2','Q3','Q4','Q1'],
                fill='toself', line_color='#00FFCC', fillcolor='rgba(0, 255, 204, 0.5)'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100], color="#00FFCC", gridcolor="#444")),
                showlegend=False, paper_bgcolor='rgba(0,0,0,0)', font_color="#00FFCC"
            )
            st.plotly_chart(fig, use_container_width=True)

st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v3.0")
