import streamlit as st

# 1. 強行設定深邃星空背景
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

# 3. 進入後顯示內容
st.title("🚀 ZPIM 2026 旗艦導航")
st.subheader("🔷 實相狀態：星空已全面噴發")
st.write("首席，歡迎登艦。目前系統已處於私人最高防禦模式。")
