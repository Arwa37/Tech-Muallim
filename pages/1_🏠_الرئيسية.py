import streamlit as st

st.set_page_config(page_title="الرئيسية - Tech-Muallim", layout="wide")

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

        semester = st.selectbox(
            "اختر الفصل:",
            ["الفصل الأول", "الفصل الثاني"],
            key=f"sem_{course['code']}"
        )

        if st.button(f"تفعيل {course['code']}", key=f"btn_{course['code']}"):
            selected_context = f"{course['name']} ({course['code']}) - {semester}"
            st.session_state['selected_book'] = selected_context
            st.success("تم التفعيل بنجاح!")

if 'selected_book' in st.session_state:
    st.warning(f"📌 المقرر المفعل حالياً: **{st.session_state['selected_book']}**")

st.markdown("---")
st.subheader("📤 رفع كتاب خارجي جديد (PDF Upload)")
uploaded_file = st.file_uploader("إذا كان المقرر غير موجود، ارفع ملف الـ PDF هنا:", type=["pdf"])
if uploaded_file is not None:
    st.success(f"تم رفع الملف '{uploaded_file.name}' بنجاح وتفعيل سياقه!")
    st.session_state['selected_book'] = f"كتاب خارجي: {uploaded_file.name}"