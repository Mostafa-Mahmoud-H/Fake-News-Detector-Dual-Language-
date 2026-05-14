# 🛡️ TruthGuard AI: Cross-Language Fake News Detection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)

## 📌 Project Overview
TruthGuard AI is a scalable, real-time machine learning system designed to combat misinformation by verifying news authenticity across linguistic boundaries. Featuring a dual-engine architecture, it accurately classifies news as **Real** or **Fake** in both **Arabic** and **English**.

This project was developed to address the rapid spread of fabricated news, providing a user-friendly web interface for instant text analysis and credibility scoring.

## ✨ Key Features
* **Dual-Language Support:** Dedicated models for Arabic (handling regional dialects and diacritics) and English text.
* **High Accuracy:** * **Arabic Engine:** 93% Overall Accuracy (utilizing ISRIStemmer and advanced preprocessing).
  * **English Engine:** 82% Overall Accuracy.
* **Real-Time Dashboard:** Interactive and responsive UI built with Streamlit for instant text verification.
* **Lightweight Deployment:** Utilizing highly optimized Logistic Regression models with TF-IDF vectorization for fast inference.

## 📂 Project Structure
For better organization and maintainability, the project is structured as follows:

```text
TruthGuard-AI/
│
├── data/                       # Contains datasets (e.g., clean_egypt_fake_news.csv)
├── notebooks/                  # Jupyter notebooks for EDA and model training (Notebook.ipynb, en_v.ipynb)
├── utils/                      # Helper scripts and modularized text cleaning functions
├── models/                     # Serialized models and vectorizers
│   ├── model.pkl               # Arabic Logistic Regression Model
│   ├── vectorizer.pkl          # Arabic TF-IDF Vectorizer
│   ├── model_en.pkl            # English Logistic Regression Model
│   └── vectorizer_en.pkl       # English TF-IDF Vectorizer
│
├── app.py                      # Main Streamlit application script
├── NewsForTest.txt             # Sample text data for testing purposes
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation 

```

## ⚙️ Installation & Setup
1. Clone the repository:
    git clone [https://github.com/YourUsername/TruthGuard-AI.git](https://github.com/YourUsername/TruthGuard-AI.git)
    cd TruthGuard-AI 
2. Create a virtual environment (Optional but recommended): 
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install the required dependencies: 
    pip install -r requirements.txt 
4. Run the Streamlit application: 
    streamlit run app.py        
***
## 💻 Usage
1. Open the provided Local URL (usually http://localhost:8501) in your web browser.

2. Select the language of the news snippet (Arabic or English) from the sidebar.

3. Paste the news text into the input area.

4. Click "Verify News 🔍" to get the credibility prediction and confidence score.     

***
## 🛠️ Technologies Used
* Programming Language: Python

* Machine Learning: Scikit-Learn (Logistic Regression, TF-IDF Vectorizer)

* Natural Language Processing (NLP): NLTK (ISRIStemmer, Stopwords), Regular Expressions

* Web Framework: Streamlit

* Data Manipulation: Pandas, NumPy

***
## 👨‍💻 Author
**Mostafa Mahmoud**

*Developer & AI Researcher*

Linked-In|https://www.linkedin.com/in/mostafa-hamad-4914292a8/ 