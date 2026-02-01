import streamlit as st
import plotly.graph_objects as go

# --- 1. 全域視覺主權注入 (星空背景) ---
st.set_page_config(page_title="ZPIM 2026 旗艦導航儀", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 50%, #001a1a 0%, #000000 100%);
        background-attachment: fixed;
    }
    /* 左側字體加深加亮 */
    .stSlider label, .stMarkdown p {
        color: #00ffcc !important;
        font-weight: 900 !important;
        text-shadow: 0 0 5px #000;
    }
    /* 101 戰略燈塔 */
    .tower {
        position: fixed; bottom: 0; right: 5%; width: 150px; height: 450px;
        background: linear-gradient(to top, #00ffcc33, transparent);
        clip-path: polygon(45% 0, 55% 0, 100% 100%, 0 100%);
        z-index: 0; filter: drop-shadow(0 0 20px #00ffcc);
    }
    </style>
    <div class="tower"></div>
    """, unsafe_allow_html=True)

# --- 2. 門禁系統 (含電路板門禁視覺) ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🛡️ ZPIM 2026 核心安全驗證")
    # 電路板圖示模擬 (SVG)
    st.markdown("""
        <svg width="200" height="100" viewBox="0 0 200 100">
            <path d="M10 50 L50 50 L60 20 L80 80 L90 50 L150 50" stroke="#00ffcc" fill="transparent" stroke-width="2">
                <animate attributeName="stroke-dasharray" from="0,200" to="200,0" dur="2s" repeatCount="indefinite" />
            </path>
            <circle cx="150" cy="50" r="5" fill="#00ffcc" />
        </svg>
    """, unsafe_allow_html=True)
    
    pwd = st.text_input("輸入首席顧問密鑰：", type="password")
    if st.button("啟動電路導通"):
        if pwd == "zpim888-2560" or pwd == "1-1":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("密鑰錯誤")
    st.stop()

# --- 3. 戰略操控區 (含退出鍵) ---
st.sidebar.title("🎮 戰略導航中心")
q1 = st.sidebar.slider("Q1 實體資產權重", 0, 100, 100)
q2 = st.sidebar.slider("Q2 邏輯導向參數", 0, 100, 100)
q3 = st.sidebar.slider("Q3 財務動能指標", 0, 100, 100)
q4 = st.sidebar.slider("Q4 營運藥方配比", 0, 100, 100)

st.sidebar.markdown("---")
if st.sidebar.button("🔒 安全登出系統"):
    st.session_state.authenticated = False
    st.rerun()

# --- 4. 鑑定書產出 (戰略雷達圖替代藍色柱子) ---
if st.sidebar.button("🚀 啟動 101 戰略診斷"):
    st.title("🏆 ZPIM 2026 官方旗艦鑑定書")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        ### 📊 四維度深度診斷報告
        - ✅ **Q1 實體維度 ({q1}%)**：實相資產穩固。
        - ✅ **Q2 靈性邏輯 ({q2}%)**：思維導航清晰。
        - ✅ **Q3 財務權限 ({q3}%)**：流動性安全。
        - ✅ **Q4 營運藥方 ({q4}%)**：藥品電路優良。
        """)
        st.info("🎯 改善對策：建議維持 101 模式輸出。")

    with col2:
        # 使用 Plotly 製作專業雷達圖
        fig = go.Figure(data=go.Scatterpolar(
          r=[q1, q2, q3, q4, q1],
          theta=['Q1','Q2','Q3','Q4','Q1'],
          fill='toself',
          line_color='#00ffcc'
        ))
        fig.update_layout(
          polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
          showlegend=False,
          paper_bgcolor='rgba(0,0,0,0)',
          plot_bgcolor='rgba(0,0,0,0)',
          font_color="white"
        )
        st.plotly_chart(fig, use_container_width=True)

st.caption("© 2026 ZPIM 零點實相 - 首席顧問專屬導航儀 v2.1")
