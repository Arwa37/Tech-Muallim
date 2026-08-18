import streamlit as st

st.set_page_config(page_title="الرئيسية - Tech-Muallim", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; }
    [data-testid="stSidebar"] { background-color: #FFF5F5; border-left: 1px solid #FFCDD2; }
    .main-header { background: linear-gradient(135deg, #D32F2F 0%, #B71C1C 100%); padding: 30px; border-radius: 16px; color: white; text-align: center; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3); }
    .stButton>button { background-color: #D32F2F; color: white; border-radius: 8px; border: none; padding: 8px 20px; font-weight: 700; font-family: 'Cairo', sans-serif; }
    .stButton>button:hover { background-color: #B71C1C; color: white; }
    div[data-testid="stMetric"] { background-color: #FFFFFF; padding: 15px; border-radius: 12px; border: 1px solid #FFCDD2; }
    </style>
""", unsafe_allow_html=True)

st.title("🏠 المكتبة الرقمية وأغلفة المناهج الثانوية")
st.markdown("---")

teacher = st.session_state.get('teacher_name', 'الاستاذ/ة')
st.info(f"مرحباً بك يا {teacher}. يمكنك اختيار المقرر الدراسي أو رفع كتاب خارجي لتفعيل السياق.")

st.markdown("### 📂 اختر مقرر الفيزياء والفصل الدراسي لتفعيل السياق:")
physics_courses = [
    {"code": "فيز 102", "name": "فيزياء 102"},
    {"code": "فيز 210", "name": "فيزياء 210"},
    {"code": "فيز 217", "name": "فيزياء 217"},
    {"code": "فيز 218", "name": "فيزياء 218"},
    {"code": "فيز 219", "name": "فيزياء 219"}
]

cols = st.columns(len(physics_courses))
for i, course in enumerate(physics_courses):
    with cols[i]:
        st.markdown(f"### ⚛️ {course['code']}")
        st.write(course['name'])
        semester = st.selectbox("اختر الفصل:", ["الفصل الأول", "الفصل الثاني"], key=f"sem_{course['code']}")
        if st.button(f"تفعيل {course['code']}", key=f"btn_{course['code']}"):
            st.session_state['selected_book'] = f"{course['name']} ({course['code']}) - {semester}"
            st.success("تم التفعيل!")

if 'selected_book' in st.session_state:
    st.warning(f"📌 المقرر المفعل حالياً: **{st.session_state['selected_book']}**")

st.markdown("---")
st.subheader("📤 رفع كتاب خارجي جديد (PDF Upload)")
uploaded_file = st.file_uploader("ارفع ملف الـ PDF هنا:", type=["pdf"])
if uploaded_file is not None:
    st.success(f"تم رفع الملف '{uploaded_file.name}' بنجاح وتفعيل سياقه!")
    st.session_state['selected_book'] = f"كتاب خارجي: {uploaded_file.name}"