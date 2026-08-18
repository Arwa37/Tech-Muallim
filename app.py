import streamlit as st

st.set_page_config(
    page_title="Tech-Muallim | منصة المعلم الذكية",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تعريف الصفحات وتخصيص العنوان الظاهر في القائمة الجانبية للمستخدم
pages = {
    "المنصة الرئيسية": [
        st.Page("app.py", title="الرئيسية 🏠", default=True),
    ],
    "أقسام المعلم": [
        st.Page("pages/1_الرئيسية.py", title="المكتبة الرقمية"),
        st.Page("pages/2_الخطة_والتحضير.py", title="الخطة والتحضير"),
        st.Page("pages/3_العروض_التقديمية.py", title="العروض التقديمية"),
        st.Page("pages/4_المختبر_والتجارب.py", title="المختبر والتجارب"),
        st.Page("pages/5_التقييمات_والشهادات.py", title="التقييمات والشهادات"),
        st.Page("pages/6_مؤشر_التقدم.py", title="مؤشر التقدم"),
        st.Page("pages/7_كشوف_الحضور.py", title="كشوف الحضور"),
        st.Page("pages/8_تحليل_النتائج.py", title="تحليل النتائج"),
    ]
}

pg = st.navigation(pages)
pg.run()