import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;600;700&display=swap');
    .card { background-color: #ffffff; padding: 25px; border-radius: 15px; border: 2px solid #D32F2F; box-shadow: 0 4px 12px rgba(211, 47, 47, 0.15); margin-bottom: 25px; }
    h1, h2, h3 { color: #B71C1C !important; font-family: 'Cairo', sans-serif; }
    div.stButton > button { background-color: #D32F2F !important; color: white !important; border-radius: 8px !important; width: 100%; font-family: 'Cairo', sans-serif; }
</style>""", unsafe_allow_html=True)

st.markdown('<div class="card"><h1>🏠 الرئيسية</h1><p>أهلاً بكِ في منصتك التعليمية. اختاري المقرر للبدء.</p></div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><h3>اختيار المقرر</h3>', unsafe_allow_html=True)
    st.selectbox("المقرر الدراسي", ["فيز 102", "فيز 210"])
    st.button("تفعيل")
    st.markdown('</div>', unsafe_allow_html=True)