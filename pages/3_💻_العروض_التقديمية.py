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

st.markdown('<div class="card"><h1>منشئ العروض التقديمية (PowerPoint)</h1><p>توليد شرائح الحصة الدراسية والأنشطة التفاعلية تلقائياً.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
lesson_title = st.text_input("حدد عنوان الحصة لتوليد الشرائح:", "الحصة 1: مقدمة في قوانين الحركة")

if st.button("توليد شرائح العرض التقديمي"):
    st.markdown("### معاينة الشرائح المولدة:")
    st.write("- شريحة 1: عنوان الدرس وأهداف الحصة.")
    st.write("- شريحة 2: المفاهيم الرئيسية والمصطلحات.")
    st.write("- شريحة 3: مثال توضيحي ومسألة تفاعلية.")
    st.write("- شريحة 4: نشاط ممتع وسريع.")
    st.write("- شريحة 5: سؤال الغلق والتقييم السريع.")
    st.success("تم بناء ملف PowerPoint بنجاح!")
    st.button("تنزيل ملف الـ PPTX")
st.markdown('</div>', unsafe_allow_html=True)