import streamlit as st
import pandas as pd
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

st.markdown('<div class="card"><h1>كشوف الحضور والغياب والاستمارات</h1><p>السجل اليومي للطلبة وتحديث الحالات مباشرة.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("السجل اليومي للطلبة")
student_data = {
    "اسم الطالب": ["أحمد محمد", "فاطمة علي", "يوسف خالد", "مريم حسن", "عبدالله إبراهيم"],
    "الحالة اليومية": ["حاضر", "حاضر", "غائب", "متأخر", "حاضر"],
    "ملاحظات": ["", "", "عذر مبرر", "تأخر 10 دقائق", ""]
}
df_students = pd.DataFrame(student_data)
edited_df = st.data_editor(df_students)

if st.button("حفظ كشوف الحضور اليومية"):
    st.success("تم حفظ السجل وتحديث كشوف الحضور بنجاح!")

st.markdown("---")
if st.button("تصدير الكشوف كملف Excel معتمد"):
    st.success("تم تجهيز ملف Excel للتحميل الفوري!")
st.markdown('</div>', unsafe_allow_html=True)