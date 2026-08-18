import streamlit as st

st.set_page_config(page_title="المكتبة الرقمية", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700&display=swap');
    body { font-family: 'Cairo', sans-serif; background-color: #f8f9fa; }
    .card { background-color: white; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    h1, h2 { color: #b71c1c; }
    .stButton>button { border: 1px solid #d32f2f; color: #d32f2f; background: white; border-radius: 8px; width: 100%; font-weight: bold; }
    .stButton>button:hover { background: #d32f2f; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card"><h1>المكتبة الرقمية</h1><p>اختر المقرر الدراسي لتفعيل السياق التعليمي.</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><h3>اختيار المقرر</h3>', unsafe_allow_html=True)
    course = st.selectbox("المقرر", ["فيز 102", "فيز 210", "فيز 217"])
    st.button("تفعيل المقرر")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h3>رفع ملف خارجي</h3>', unsafe_allow_html=True)
    st.file_uploader("اختر ملف PDF")
    st.markdown('</div>', unsafe_allow_html=True)