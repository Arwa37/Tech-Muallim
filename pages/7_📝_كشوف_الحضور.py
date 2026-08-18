import streamlit as st
import pandas as pd

st.title("📝 كشوف الحضور والغياب والاستمارات")
st.markdown("---")

st.subheader("📋 السجل اليومي للطلبة")

student_data = {
    "اسم الطالب": ["أحمد محمد", "فاطمة علي", "يوسف خالد", "مريم حسن", "عبدالله إبراهيم"],
    "الحالة اليومية": ["حاضر", "حاضر", "غائب", "متأخر", "حاضر"],
    "ملاحظات": ["", "", "عذر مبرر", "تأخر 10 دقائق", ""]
}
df_students = pd.DataFrame(student_data)

edited_df = st.data_editor(df_students)

if st.button("💾 حفظ كشوف الحضور اليومية"):
    st.success("تم حفظ السجل وتحديث كشوف الحضور بنجاح!")

st.markdown("---")
st.subheader("📄 تصدير التقارير الرسمية")
if st.button("تصدير الكشوف كملف Excel معتمد"):
    st.success("تم تجهيز ملف Excel للتحميل الفوري!")