import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 تحليل نتائج الطلبة والفجوات التعليمية")
st.markdown("---")

st.info("أدخل درجات التقييمات لتحليل مستويات الإتقان واكتشاف الفجوات بشكل فوري.")

chart_data = pd.DataFrame({
    'مستوى الإتقان': ['ممتاز (90-100%)', 'جيد جداً (80-89%)', 'جيد (70-79%)', 'يحتاج دعم (<70%)'],
    'عدد الطلاب': [12, 15, 6, 3]
})

fig = px.bar(
    chart_data,
    x='مستوى الإتقان',
    y='عدد الطلاب',
    title="توزيع درجات الطلاب في التقييم الأخير",
    color_discrete_sequence=['#D32F2F']
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 🔍 تقرير الفجوات الآلي:")
st.warning("⚠️ لوحظ وجود انخفاض طفيف في إجابات أسئلة (تطبيق قوانين الاحتكاك). يُقترح تقديم حصة دعم إضافية أو نشاط علاجي لهذا المعيار.")