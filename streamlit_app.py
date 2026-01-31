import streamlit as st
import pandas as pd
import numpy as np

# 1. 頁面設定與深邃背景
st.set_page_config(page_title="ZPIM 2026 戰略導航", layout="wide")

# 2. 真鑰匙門禁
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🛡️ ZPIM 2026 旗艦實相已鎖定")
    pwd = st.text_input("輸入戰略密碼", type="password")
    if pwd == "zpim2026master":
        st.session_state["authenticated"] = True
        st.rerun()
    else:
        st.stop()

# --- 進入授權區域 ---

# 3. 浮水印與證書標誌 (CSS)
st.markdown("""
    <style>
    .watermark {
        position: fixed; bottom: 10px; right: 10px; opacity: 0.1;
        font-size: 50px; color: white; transform: rotate(-30deg);
    }
    .certificate {
        border: 2px solid #D4AF37; padding: 20px; border-radius: 10px;
        background-color: rgba(212, 175, 55, 0.05);
    }
    </style>
    <div class="watermark">ZPIM 2026 AUTHORIZED</div>
    """, unsafe_allow_html=True)

# 4. 主標題
st.title("🚀 ZPIM 2026 旗艦戰略導航儀")
st.markdown('<div class="certificate"><b>📜 2026 戰略授權證書：</b> 此實相已由首席顧問正式核准並啟動</div>', unsafe_allow_html=True)

# 5. 側邊欄控制（拉桿百分比）
st.sidebar.header("📊 戰略維度調整")
val1 = st.sidebar.slider("核心實力 (Core Power) %", 0, 100, 88)
val2 = st.sidebar.slider("市場擴張 (Market Expansion) %", 0, 100, 75)
val3 = st.sidebar.slider("戰略佈局 (Strategic Layout) %", 0, 100, 92)
val4 = st.sidebar.slider("實相顯化 (Reality Manifestation) %", 0, 100, 80)

# 6. 四個紅色柱子數據
data = pd.DataFrame({
    '指標名稱': ['核心實力', '市場擴張', '戰略佈局', '實相顯化'],
    '百分比': [val1, val2, val3, val4]
})

# 顯示圖表
st.subheader("🔷 2026 戰略實相矩陣 (動態監測)")
st.bar_chart(data.set_index('指標名稱'), color="#FF0000") # 指定紅色柱子

# 7. 說明區域
col1, col2 = st.columns(2)
with col1:
    st.info(f"🚩 目前核心總量：{(val1+val2+val3+val4)/4}%")
with col2:
    st.success("✅ 系統已處於私人最高防禦模式")

st.markdown("---")
st.write("✨ *星空背景已注入，數據即時校準中...*")
