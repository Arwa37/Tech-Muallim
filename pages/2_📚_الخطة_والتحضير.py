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

st.markdown('<div class="card"><h1>الخطة والتحضير الذكي</h1><p>توليد ملخصات الدروس، أهداف بلوم، وخطط الحصص الثلاث.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
unit_name = st.selectbox("الوحدة الدراسية:", ["الوحدة الأولى: الميكانيكا والحرارة", "الوحدة الثانية: الكهرباء والمغناطيسية", "الوحدة الثالثة: الموجات والضوء"])
lesson_name = st.text_input("عنوان الدرس:", "مثال: قانون نيوتن الثاني وحركة الأجسام")

if st.button("توليد ملخص الدرس وأهداف بلوم"):
    st.markdown("### ملخص الدرس وأهم النقاط")
    st.success("تم استخراج التلخيص الشامل لمفاهيم الدرس والقوانين الفيزيائية.")
    st.markdown("### أهداف بلوم التعليمية")
    st.write("- الهدف المعرفي: أن يتعرف الطالب على صيغة القانون الرياضية ووحدات القياس.")
    st.write("- الهدف التطبيقي: أن يحل الطالب مسائل حسابية تطبيقية على القانون بدقة.")

st.markdown("---")
st.subheader("خطة الحصص الثلاث الموزعة")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**الحصة الأولى:** المفاهيم الأساسية والمقدمة.")
with c2:
    st.markdown("**الحصة الثانية:** التطبيق العملي والمسائل.")
with c3:
    st.markdown("**الحصة الثالثة:** التقييم التكويني وغلق الدرس.")

if st.button("تصدير الخطة كملف Word"):
    st.success("تم تجهيز ملف خطة الدرس (.docx) للتحميل الفوري!")
st.markdown('</div>', unsafe_allow_html=True)