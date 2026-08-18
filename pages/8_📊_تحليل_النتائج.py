import streamlit as st
import pandas as pd
import plotly.express as px
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

st.markdown('<div class="card"><h1>تحليل نتائج الطلبة والفجوات التعليمية</h1><p>تحليل مستويات الإتقان واكتشاف الفجوات عبر الرسوم البيانية التفاعلية.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
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

st.markdown("### تقرير الفجوات الآلي:")
st.warning("لوحظ وجود انخفاض طفيف في إجابات أسئلة (تطبيق قوانين الاحتكاك). يُقترح تقديم حصة دعم إضافية أو نشاط علاجي لهذا المعيار.")
st.markdown('</div>', unsafe_allow_html=True)