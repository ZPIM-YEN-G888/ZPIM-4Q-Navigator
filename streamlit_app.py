import streamlit as st
import pandas as pd
try:
    import plotly.graph_objects as go
    has_plotly = True
except:
    has_plotly = False

# --- 1. 全域視覺主權 (文字銳化、點亮 101、防偽浮水印) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #003333 0%, #000000 100%) !important; }
    
    /* 防偽浮水印 */
    .stApp::before {
        content: "ZPIM 2026 OFFICIAL 首席顧問專屬 ";
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        font-size: 24px; color: rgba(0, 255, 204, 0.08);
        pointer-events: none; z-index: 1000;
        display: flex; flex-wrap: wrap; transform: rotate(-30deg);
        justify-content: space-around; line-height: 200px;
    }

    /* 登入標題銳化 */
    h1 { color: #FFFFFF !important; font-weight: 900 !important; }

    /* 左側側邊欄標題：鎖定深戰略綠 */
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] .stMarkdown p {
        color: #006600 !important; font-weight: 900 !important;
    }

    /* 鑑定書區塊 */
    .id-card {
        background: rgba(0, 40, 40, 0.9);
        border: 2px solid #00FFCC;
        border-radius: 15px; padding: 25px;
    }
    .id-card p { color: #FFFFFF !important; font-weight: 900 !important; font-size: 1.1rem; }

    /* 按鈕亮化 */
    div.stButton > button {
        background-color: #00FF00 !important; color: #000000 !important;
        font-weight: 900 !important; border: 2px solid #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# 閃電與電路動畫 (修正字體顏色為正亮綠)
circuit_svg = """
<div style="text-align:center; margin-bottom: 20px;">
    <svg width="250" height="60" viewBox="0 0 250 60">
        <path d="M0 30 L60 30 L85 5 L110 55 L135 30 L250 30" stroke="#00FF00" fill="transparent" stroke-width="5">
            <animate attributeName="stroke-dasharray" from="0,500" to="500,0" dur="1s" repeatCount="indefinite" />
        </path>
    </svg>
    <p style="color:#00FF00 !important; font-weight:900; font-size:1.2rem; letter-spacing:2px; text-shadow: 0 0 10px #00FF00;">⚡ ZPIM 數據通訊中</p>
</div>
"""

# --- 2. 門禁與主頁邏輯 ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- 修改後的安全驗證區 (替換您截圖中的 67-75 行) ---
if not st.session_state.authenticated:
    st.title("🛡️ ZPIM 2026 核心安全驗證")
    st.markdown(circuit_svg, unsafe_allow_html=True)
    pwd = st.text_input("輸入首席顧問密鑰：", type="password")
    if st.button("啟動電路導通"):
        # 關鍵修改：刪除所有舊密碼 (如 "1-1")，改向保險箱討鑰匙
        if pwd == st.secrets["ident_code"]: 
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("密碼錯誤，請聯繫本人獲取授權。")
    st.stop()

# --- 3. 戰略操控區 (左側) ---
st.sidebar.markdown(circuit_svg, unsafe_allow_html=True)
st.sidebar.title("🎮 戰略導航中心")
q1 = st.sidebar.slider("Q1 實體資產權重 (%)", 0, 100, 100)
q2 = st.sidebar.slider("Q2 靈性邏輯參數 (%)", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務動能指標 (%)", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運藥方配比 (%)", 0, 100, 100)

if st.sidebar.button("🔒 安全退出系統"):
    st.session_state.authenticated = False
    st.rerun()

# --- 4. 鑑定書產出 (植入 101 燈塔視覺) ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="id-card">
            <h3 style="color: white !important; font-weight: bold; text-shadow: 2px 2px 4px #000000;">📊 四維度深度診斷報告</h3>
            <p>✅ Q1 實體：{q1}% - 核心資產已定格</p>
            <p>✅ Q2 邏輯：{q2}% - 指引路徑極致</p>
            <p>✅ Q3 財務：{q3}% - 點數核銷正常</p>
            <p>✅ Q4 營運：{q4}% - 電路通訊優良</p>
            <hr style="border: 0.5px solid #00FFCC;">
            <p style="color: white !important; font-weight: bold; text-shadow: 2px 2px 4px #000000;">🎯 改善對策：101888 燈塔戰略就位。</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # 在雷達圖上方植入 101 燈塔 SVG
        st.markdown("""
        <div style="text-align:right;">
            <svg width="100" height="150" viewBox="0 0 100 150">
                <path d="M45 0 L55 0 L100 150 L0 150 Z" fill="url(#grad1)" />
                <defs><linearGradient id="grad1" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#00FFCC;stop-opacity:0.8" />
                <stop offset="100%" style="stop-color:#00FFCC;stop-opacity:0" />
                </linearGradient></defs>
            </svg>
            <p style="color:#00FFCC; font-size:0.8rem; margin-right:20px;">101 戰略對位中</p>
        </div>
        """, unsafe_allow_html=True)
        
        if has_plotly:
            fig = go.Figure(data=go.Scatterpolar(
                r=[q1, q2, q3, q4, q1], theta=['Q1','Q2','Q3','Q4', 'Q1'],
                fill='toself', line_color='#00FFCC', fillcolor='rgba(0, 255, 204, 0.4)'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100], color="#00FFCC")),
                showlegend=False, paper_bgcolor='rgba(0,0,0,0)', font_color="#00FFCC"
            )
            st.plotly_chart(fig, use_container_width=True)

st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v3.2")
