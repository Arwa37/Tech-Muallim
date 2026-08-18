import streamlit as st
st.set_page_config(layout="wide")

st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    [data-testid="stSidebar"] { background-color: #B71C1C !important; color: white !important; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stMarkdown { color: white !important; }
    .card { background-color: #ffffff; padding: 25px; border-radius: 15px; border: 2px solid #D32F2F; box-shadow: 0 4px 12px rgba(211, 47, 47, 0.15); margin-bottom: 25px; }
    h1, h2, h3 { color: #B71C1C !important; }
    div.stButton > button { background-color: #D32F2F !important; color: white !important; border-radius: 8px !important; width: 100%; font-weight: bold; }
</style>""", unsafe_allow_html=True)

st.markdown('<div class="card"><h1>المكتبة الرقمية وأغلفة المناهج</h1><p>اختاري مقرر الفيزياء والفصل الدراسي لتفعيل السياق التعليمي.</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><h3>اختيار المقرر</h3>', unsafe_allow_html=True)
    courses = ["فيزياء 102 (فيز 102)", "فيزياء 210 (فيز 210)", "فيزياء 217 (فيز 217)", "فيزياء 218 (فيز 218)", "فيزياء 219 (فيز 219)"]
    selected_c = st.selectbox("المقرر الدراسي:", courses)
    semester = st.selectbox("الفصل الدراسي:", ["الفصل الأول", "الفصل الثاني"])
    if st.button("تفعيل المقرر والسياق"):
        st.success(f"تم تفعيل مقرر {selected_c} - {semester} بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>رفع كتاب خارجي (PDF)</h3>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("ارفعي ملف الـ PDF هنا لتحليله:", type=["pdf"])
    if uploaded_file is not None:
        st.success(f"تم رفع الملف '{uploaded_file.name}' وتفعيل سياقه بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)