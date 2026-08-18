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

st.markdown('<div class="card"><h1>التقييمات والشهادات الآلية</h1></div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["مولد الامتحانات", "صانع الشهادات"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("مولد الامتحانات والأسئلة")
    q_type = st.selectbox("نوع الأسئلة المطلوبة:", ["اختيار من متعدد", "أسئلة مقالية", "كتابة قصيرة"])
    num_q = st.slider("عدد الأسئلة:", 1, 10, 5)
    if st.button("توليد اختبار مطابق للنماذج السابقة"):
        st.success(f"تم توليد اختبار مكون من {num_q} أسئلة بنجاح ({q_type})!")
        st.write("1. سؤال تجريبي أول...")
        st.write("2. سؤال تجريبي ثاني...")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("صانع الشهادات التلقائي للطلبة")
    uploaded_excel = st.file_uploader("ارفعي ملف أسماء الطلاب (Excel / CSV):", type=["xlsx", "csv"])
    selected_cert_template = st.selectbox("اختر قالب الشهادة:", ["قالب التفوق الأكاديمي", "قالب التميز العلمي", "شهادة شكر وتقدير"])
    if uploaded_excel is not None:
        if st.button("توليد الشهادات آلياً"):
            st.success("تم دمج أسماء الطلبة وتوليد جميع الشهادات بنجاح جاهزة للتحميل!")
    st.markdown('</div>', unsafe_allow_html=True)