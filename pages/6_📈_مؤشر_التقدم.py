import streamlit as st

st.title("📈 مؤشر التقدم والتقويم الأكاديمي")
st.markdown("---")

st.markdown("### ⏱️ لوحة القيادة الزمنية للمنهج")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("إجمالي حصص المقرر", "48 حصة")
with col2:
    st.metric("الحصص المنجزة", "18 حصة")
with col3:
    st.metric("الحصص المتبقية", "30 حصة")

st.markdown("### 📊 شريط حالة التقدم")
st.progress(0.37, text="نسبة إنجاز المنهج: 37%")
st.success("✅ الحالة: أنت تسير على المسار الصحيح ومطابق للتقويم الأكاديمي الثابت.")

st.markdown("---")
st.subheader("📧 إعدادات التنبيهات البريدية")
email_input = st.text_input("أدخل بريدك الإلكتروني لتلقي التنبيهات الأسبوعية:", "teacher@school.bh")
if st.button("حفظ وتفعيل التنبيهات"):
    st.success("تم تفعيل التنبيهات الأسبوعية بنجاح!")