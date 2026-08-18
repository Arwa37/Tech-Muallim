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

st.markdown('<div class="card"><h1>المختبر والتجارب العملية</h1><p>استخراج وتنظيم التجارب العلمية والمختبرية الموجودة في الكتاب المدرسي.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
if st.button("البحث عن التجارب في المنهج الحالي"):
    data = {
        "اسم التجربة": ["تحقيق قانون نيوتن الثاني", "دراسة أثر الاحتكاك"],
        "الأدوات المطلوبة": ["عربية ديناميكية، أثقال، مسطرة زمنية", "سطح مائل، عربية، ميزان حساسة"],
        "خطوات التنفيذ": ["1. ضبط الأجهزة\n2. قياس التسارع بتغيير القوة", "1. رفع السطح تدريجياً\n2. حساب زاوية الانزلاق"],
        "الوقت المستغرق": ["45 دقيقة", "45 دقيقة"],
        "إجراءات السلامة": ["تثبيت الأثقال جيداً لمنع سقوطها", "الحذر عند التعامل مع الأسطح الحادة"]
    }
    df = pd.DataFrame(data)
    st.table(df)
    st.success("تم استخراج كافة تفاصيل المختبر بنجاح!")
st.markdown('</div>', unsafe_allow_html=True)