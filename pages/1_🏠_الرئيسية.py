import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""<style>
    .card { background-color: #ffffff; padding: 25px; border-radius: 15px; border: 2px solid #D32F2F; box-shadow: 0 4px 12px rgba(211, 47, 47, 0.15); margin-bottom: 25px; }
    h1, h2, h3 { color: #B71C1C !important; }
    div.stButton > button { background-color: #D32F2F !important; color: white !important; border-radius: 8px !important; width: 100%; font-weight: bold; }
</style>""", unsafe_allow_html=True)

st.markdown('<div class="card"><h1>🏠 المكتبة الرقمية</h1><p>مرحباً بكِ. اختاري المقرر لتفعيل السياق أو ارفعي كتاباً خارجياً.</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><h3>اختيار المقرر</h3>', unsafe_allow_html=True)
    courses = ["فيز 102", "فيز 210", "فيز 217"]
    selection = st.selectbox("المقرر الدراسي", courses)
    st.button("تفعيل المقرر")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h3>📤 رفع كتاب خارجي</h3>', unsafe_allow_html=True)
    st.file_uploader("ارفعي ملف الـ PDF هنا", type=["pdf"])
    st.markdown('</div>', unsafe_allow_html=True)