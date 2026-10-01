import streamlit as st

st.set_page_config(page_title="تطبيق الأذكار", page_icon="📿", layout="centered")

st.markdown("""
    <style>
    .main { text-align: center; }
    div.stButton > button {
        width: 100%;
        height: 3.5em;
        font-size: 20px !important;
        border-radius: 12px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📿 تطبيق الأذكار")
st.write("### 🤍 إهداء من: عبد الإله عيد")
st.info("💻 تم تطوير وتصميم هذا التطبيق بواسطة المبرمج: **عبد الإله عيد** كصدقة جارية نسأل الله أن ينفع بها الجميع.")

if 'count' not in st.session_state:
    st.session_state.count = 0

st.metric(label="عدد مرات الاستغفار", value=st.session_state.count)

col1, col2 = st.columns(2)

with col1:
    if st.button("أستغفر الله (+1)"):
        st.session_state.count += 1
        st.rerun()

with col2:
    if st.button("إعادة ضبط (0)"):
        st.session_state.count = 0
        st.rerun()

st.write("---")
st.caption("أستغفر الله العظيم وأتوب إليه")
