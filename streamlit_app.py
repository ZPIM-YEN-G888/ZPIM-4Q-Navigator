import streamlit as st
import pandas as pd
try:
    import plotly.graph_objects as go
    has_plotly = True
except:
    has_plotly = False

# --- 1. 全域視覺與防偽浮水印設定 ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

st.markdown("""
    <style>
    /* 星際背景 */
    .stApp {
        background: radial-gradient(circle at center, #001f1f 0%, #000000 100%) !important;
    }
    
    /* 全域浮水印設定 */
    .stApp::before {
        content: "ZPIM 2026 OFFICIAL 首席顧問專屬  ";
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        font-size: 20px; color: rgba(255, 255, 255, 0.05); /* 淡淡的白色 */
        pointer-events: none; z-index: 1000;
        display: flex; flex-wrap: wrap; transform: rotate(-30deg);
        justify-content: space-around; line-height: 150px;
    }

    /* 登入標題：純白銳化 */
    h1 { color: #FFFFFF !important; font-weight: 900 !important; }

    /* 側邊欄：解決文字看不見問題 */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] label {
        color: #111111 !important; font-weight: 900 !important; font-size: 1.1rem !important;
    }

    /* 診斷結果文字容器：確保文字呈現 */
    .result-card {
        background: rgba(0, 50, 50, 0.8);
        padding: 20px; border-radius: 15px; border: 2px solid #00FF00;
        margin-top: 20px;
    }
    .result-text {
        color: #FFFFFF !important; font-size: 1.2rem !important; font-weight: 900 !important;
        margin-bottom: 10px; display: block;
    }

    /* 按鈕樣式 */
    div.stButton > button {
        background-color: #00FF00 !important; color: #000000 !important;
        font-weight: 900 !important; border: 2px solid #004400;
    }

    /* 101 戰略燈塔 */
    .tower {
        position: fixed; bottom: 0; right: 5%; width: 180px; height: 450px;
        background: linear-gradient(to top, rgba(0, 255, 0, 0.2), transparent);
        clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%); z-index: -1;
    }
    </style>
    <div class="tower"></div>
    """, unsafe_allow_html=True)

circuit_svg = """
<div style="text-align:center; margin: 20px 0;">
    <svg width="250" height="70" viewBox="0 0 250 70">
        <path d="M0 35 L70 35 L90 10 L120 60 L150 35 L250 35" stroke="#00FF00" fill="transparent" stroke-width="4">
            <animate attributeName="stroke-dasharray" from="0,500" to="500,0" dur="1.5s" repeatCount="indefinite" />
        </path>
    </svg>
    <p style="color:#00FF00; font-weight:900;">⚡ ZPIM 數據通訊中 (ANTI-COPY ON)</p>
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

if st.sidebar.button("🔒 安全退出"):
    st.session_state.authenticated = False
    st.rerun()

# --- 4. 鑑定書產出 (強制顯示文字與防偽) ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # 使用自定義容器強制顯示文字
        st.markdown(f"""
        <div class="result-card">
            <span class="result-text">✅ Q1 實體維度：{q1}% (已達噴發位)</span>
            <span class="result-text">✅ Q2 靈性邏輯：{q2}% (路徑已鎖定)</span>
            <span class="result-text">✅ Q3 財務權限：{q3}% (動能充足)</span>
            <span class="result-text">✅ Q4 營運藥方：{q4}% (藥電同步)</span>
            <hr style="border: 0.5px solid #00FF00;">
            <p style="color:#00FF00; font-weight:900;">🎯 改善對策：101 戰略燈塔指引中，請維持高主權權重。</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if has_plotly:
            fig = go.Figure(data=go.Scatterpolar(
                r=[q1, q2, q3, q4, q1], theta=['Q1','Q2','Q3','Q4','Q1'],
                fill='toself', line_color='#00FF00', fillcolor='rgba(0, 255, 0, 0.4)'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100], color="#00FF00")),
                showlegend=False, paper_bgcolor='rgba(0,0,0,0)', font_color="#00FF00"
            )
            st.plotly_chart(fig, use_container_width=True)

st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v2.6")
