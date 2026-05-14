import streamlit as st
import pickle
import re
import emoji
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.isri import ISRIStemmer

# Page configuration for a professional look
st.set_page_config(page_title="TruthGuard AI", page_icon="🛡️", layout="wide")

# --- Load Models and Vectorizers ---
@st.cache_resource
def load_assets(lang_choice):
    if lang_choice == "Arabic":
        # Paths based on your local directory
        model = pickle.load(open("models/model.pkl", "rb"))
        vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
        return model, vectorizer
    else:
        # English model assets
        model = pickle.load(open("models/model_en.pkl", "rb"))
        vectorizer = pickle.load(open("models/vectorizer_en.pkl", "rb"))
        return model, vectorizer
    
# --- Arabic Preprocessing ---
def clean_ar(text):
    st_stemmer = ISRIStemmer()
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ة', 'ه', text)
    text = re.sub(r'[\u064B-\u065F\u0670]', '', text) # Remove diacritics
    text = re.sub(r'http\S+|www\S+', '', text)      # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)             # Remove punctuation
    text = emoji.replace_emoji(text, replace='')    # Remove emojis
    stop_words = set(stopwords.words('arabic'))
    words = [st_stemmer.stem(w) for w in text.split() if w not in stop_words]
    return ' '.join(words)

# --- English Preprocessing ---
def clean_en(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)      # Remove URLs
    text = re.sub(r'[^a-z\s]', '', text)             # Remove non-alpha
    return text.strip() 

# Sidebar settings
st.sidebar.title("🛠️ Configuration")
lang = st.sidebar.radio("Select Language / اختر اللغة", ("Arabic", "English"))

# Dynamic UI Content
if lang == "Arabic":
    header = "🛡️ TruthGuard: كاشف الأخبار المفبركة"
    desc = "نظام ذكاء اصطناعي متقدم للتحقق من صحة الأخبار العربية."
    input_label = "أدخل نص الخبر هنا:"
    btn_label = "تحليل المصداقية 🔍"
    warning_msg = "برجاء إدخال نص للتحليل"
else:
    header = "🛡️ TruthGuard: Global News Verifier"
    desc = "Advanced AI system to verify the authenticity of English news."
    input_label = "Enter the news text here:"
    btn_label = "Verify News 🔍"
    warning_msg = "Please enter text to analyze"

st.title(header)
st.info(desc)

# Input area
user_input = st.text_area(input_label, height=200)

if st.button(btn_label):
    if not user_input.strip():
        st.warning(warning_msg)
    else:
        with st.spinner('Analyzing...'):
            # Load assets and clean text
            model, vectorizer = load_assets(lang)
            cleaned = clean_ar(user_input) if lang == "Arabic" else clean_en(user_input)
            
            # Predict
            vec_input = vectorizer.transform([cleaned])
            pred = model.predict(vec_input)[0]
            prob = model.predict_proba(vec_input)[0]
            confidence = prob[1] if pred == 1 else prob[0]

            st.markdown("---")
            res_col, meter_col = st.columns([1, 1])

            with res_col:
                if pred == 1:
                    st.success("✅ **Real News / خبر حقيقي**" if lang=="English" else "✅ **النتيجة: خبر حقيقي**")
                else:
                    st.error("🚨 **Fake News / خبر مفبرك**" if lang=="English" else "🚨 **النتيجة: خبر مفبرك**")
                st.metric(label="Confidence Score", value=f"{confidence*100:.2f}%")

            with meter_col:
                st.write("**Authenticity Meter:**")
                st.progress(float(prob[1]))
                st.caption("0% (Fake) <---------------------> 100% (Real)")
