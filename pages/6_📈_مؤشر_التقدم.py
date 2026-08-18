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

st.markdown('<div class="card"><h1>مؤشر التقدم والتقويم الأكاديمي</h1><p>لوحة القيادة الزمنية ومتابعة إنجاز المنهج.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("إجمالي حصص المقرر", "48 حصة")
with col2:
    st.metric("الحصص المنجزة", "18 حصة")
with col3:
    st.metric("الحصص المتبقية", "30 حصة")

st.markdown("### شريط حالة التقدم")
st.progress(0.37, text="نسبة إنجاز المنهج: 37%")
st.success("الحالة: أنت تسير على المسار الصحيح ومطابق للتقويم الأكاديمي الثابت.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("إعدادات التنبيهات البريدية")
email_input = st.text_input("أدخل بريدك الإلكتروني لتلقي التنبيهات أسبوعياً:", "teacher@school.bh")
if st.button("حفظ وتفعيل التنبيهات"):
    st.success("تم تفعيل التنبيهات البريدية بنجاح!")
st.markdown('</div>', unsafe_allow_html=True)