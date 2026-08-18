import streamlit as st

st.set_page_config(
    page_title="Tech-Muallim | منصة المعلم الذكية",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص CSS شامل لتلوين التطبيق بالكامل بالفايب الأحمر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* تلوين الشريط الجانبي بالكامل بدرجة حمراء خفيفة وراقية */
    [data-testid="stSidebar"] {
        background-color: #FFF5F5;
        border-left: 1px solid #FFCDD2;
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

    /* صندوق الترحيب الديناميكي */
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

    /* تنسيق الأزرار باللون الأحمر */
    .stButton>button {
        background-color: #D32F2F;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: 700;
        font-family: 'Cairo', sans-serif;
        transition: 0.3s ease;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #B71C1C;
        color: white;
        box-shadow: 0 4px 12px rgba(183, 28, 28, 0.4);
    }

    /* تخصيص بطاقات المقاييس */
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

# نظام إدخال اسم المعلم ديناميكياً
if 'teacher_name' not in st.session_state:
    st.session_state['teacher_name'] = ""

# شريط جانبي لإعداد ملف المعلم ديناميكياً
with st.sidebar:
    st.markdown("### ⚙️ إعدادات المعلم")
    input_name = st.text_input("أدخل اسم المعلم/ـة:", value=st.session_state['teacher_name'])
    if input_name:
        st.session_state['teacher_name'] = input_name
    st.markdown("---")
    st.info("💡 النظام ديناميكي بالكامل ويتكيف مع بيانات المستخدم المسجلة حالياً.")

# واجهة الترحيب الرئيسية
st.markdown("""
    <div class="main-header">
        <h1>🎓 منصة Tech-Muallim الذكية</h1>
        <p>مساعدك الرقمي المتقدم لأتمتة المناهج، تحضير الدروس، وإدارة الصفوف بذكاء</p>
    </div>
""", unsafe_allow_html=True)

# التحقق من الاسم الديناميكي وعرض الترحيب
current_teacher = st.session_state.get('teacher_name', '')
if current_teacher:
    welcome_text = f"✨ أهلاً بك يا أستاذ(ة) {current_teacher} في منصتك التعليمية المتكاملة."
else:
    welcome_text = "✨ أهلاً بك في منصتك التعليمية المتكاملة (يرجى إدخال اسمك من القائمة الجانبية)."

st.markdown(f"""
    <div class="welcome-box">
        {welcome_text}
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# إحصائيات سريعة متناسقة
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📚 الكتب المرفوعة", value="4 كتب", delta="نشط")

with col2:
    st.metric(label="📝 الحصص المنجزة", value="18 حصة", delta="+3 هذا الأسبوع")

with col3:
    st.metric(label="🎯 نسبة التقدم العام", value="75%", delta="على المسار الصحيح ✅")

st.markdown("---")
st.markdown("### 🧭 دليل التنقل السريع")
st.info("استخدم القائمة الجانبية (Sidebar) للانتقال بسلاسة بين الأقسام المختلفة للمنصة.")