import streamlit as st

st.set_page_config(
    page_title="Tech-Muallim | منصة المعلم الذكية",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص CSS متقدم لضبط الفايب الأحمر، الخطوط، وتنسيق الواجهة بالكامل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    /* فرض خط كايرو وتطبيق الاتجاه العربي على كافة العناصر */
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* الهيدر الأحمر الفاخر */
    .main-header {
        background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%);
        padding: 40px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(211, 47, 47, 0.35);
    }

    .main-header h1 {
        font-weight: 900;
        font-size: 2.5rem;
        margin-bottom: 10px;
    }

    .main-header p {
        font-weight: 600;
        font-size: 1.1rem;
        opacity: 0.95;
    }

    /* صندوق الترحيب المخصص بلون متناسق */
    .welcome-box {
        background-color: #FFEBEE;
        border-right: 5px solid #D32F2F;
        padding: 15px 20px;
        border-radius: 8px;
        color: #B71C1C;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* تخصيص أزرار الاستريملت لتأخذ الطابع الأحمر الفاخر */
    .stButton>button {
        background-color: #D32F2F;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: 700;
        font-family: 'Cairo', sans-serif;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #B71C1C;
        color: white;
        box-shadow: 0 4px 12px rgba(183, 28, 28, 0.4);
    }

    /* تحسين مظهر بطاقات المقاييس (Metrics) */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #FFCDD2;
    }

    div[data-testid="stMetric"] label {
        font-family: 'Cairo', sans-serif;
        color: #555555;
        font-weight: 600;
    }

    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #D32F2F;
        font-weight: 900;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة الترحيب الرئيسية
st.markdown("""
    <div class="main-header">
        <h1>🎓 منصة Tech-Muallim الذكية</h1>
        <p>مساعدك الرقمي المتقدم لأتمتة المناهج، تحضير الدروس، وإدارة الصفوف بذكاء</p>
    </div>
""", unsafe_allow_html=True)

# رسالة الترحيب الشخصية بصندوق أنيق
st.markdown("""
    <div class="welcome-box">
        ✨ أهلاً بك يا أستاذة أروى في منصتك التعليمية المتكاملة.
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# إحصائيات سريعة بتصميم منسق
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📚 الكتب المرفوعة", value="4 كتب", delta="نشط")

with col2:
    st.metric(label="📝 الحصص المنجزة", value="18 حصة", delta="+3 هذا الأسبوع")

with col3:
    st.metric(label="🎯 نسبة التقدم العام", value="75%", delta="على المسار الصحيح ✅")

st.markdown("---")
st.markdown("### 🧭 دليل التنقل السريع")
st.info(
    "استخدم القائمة الجانبية (Sidebar) للانتقال بسلاسة بين الأقسام المختلفة للمنصة (الرئيسية، الخطة والتحضير، المختبر، التقييمات، تحليلات النتائج، وغيرها).")