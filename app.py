import streamlit as st
import pickle
import re
import nltk
import PyPDF2
import requests
import io
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load vectorizer locally
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# --- Load classifier model from Hugging Face ---
@st.cache_resource
def load_model_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    model_file = io.BytesIO(response.content)
    return pickle.load(model_file)

clf_url = "https://huggingface.co/bhushanp9/Movie-recommender-system/resolve/main/clf.pkl"
clf = load_model_from_url(clf_url)

# --- Resume and JD Cleaning Function ---
def cleanResume(txt):
    txt = re.sub(r'http\S+|www.\S+', ' ', txt)
    txt = re.sub(r'\bRT\b|\bcc\b', ' ', txt)
    txt = re.sub(r'@\S+|#\S+', ' ', txt)
    punctuation = re.escape("""!"$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
    txt = re.sub(rf'[{punctuation}]', ' ', txt)
    txt = re.sub(r'[^\x00-\x7F]+', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

# --- Resume Text Extraction from Uploaded File ---
def extract_text(upload_file):
    if upload_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(upload_file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    else:  # TXT file
        try:
            return upload_file.read().decode('utf-8')
        except UnicodeDecodeError:
            return upload_file.read().decode('latin-1')

# --- Streamlit App Logic ---
def main():
    st.title("📄 Resume Screening App")
    st.write("Upload a resume (PDF or TXT) to predict its category and calculate an ATS score.")

    upload_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'])

    if upload_file is not None:
        txt = extract_text(upload_file)

        if txt:
            cleaned_resume = cleanResume(txt)
            input_features = tfidf.transform([cleaned_resume])
            prediction_id = clf.predict(input_features)[0]

            category_mapping = {
                1: "Arts",
                2: "Automation testing",
                4: "Business Analyst",
                5: "Civil Engineer",
                6: "Data Science",
                7: "Database",
                8: "Blockchain",
                9: "DotNet Developer",
                10: "ETL Developer",
                11: "Electrical Engineering",
                12: "HR",
                13: "Hadoop",
                14: "Health and fitness",
                15: "Java Developer",
                16: "Mechanical Engineer",
                17: "Network Security Engineer",
                18: "Operations Manager",
                19: "PMO",
                20: "Python Developer",
                21: "SAP Developer",
                22: "Sales",
                23: "Testing",
                24: "Web Designing"
            }

            category_name = category_mapping.get(prediction_id, "Unknown")
            st.success(f"✅ Predicted Category: **{category_name}**")

            st.markdown("### 📄 Job Description for ATS Score")
            with st.form("ats_form"):
                job_description = st.text_area("Paste Job Description Here")
                submitted = st.form_submit_button("Check ATS Score")

            if submitted and job_description:
                cleaned_jd = cleanResume(job_description)
                jd_vector = tfidf.transform([cleaned_jd])
                resume_vector = tfidf.transform([cleaned_resume])

                score = cosine_similarity(jd_vector, resume_vector)[0][0]
                percentage = round(score * 100, 2)

                st.info(f"📊 ATS Score (Resume vs Job Description): **{percentage}%**")
                st.progress(int(percentage))

                if percentage > 80:
                    st.success("✅ Strong match!")
                elif percentage > 60:
                    st.warning("🟡 Moderate match — could be improved.")
                else:
                    st.error("❌ Low match — consider editing your resume.")
        else:
            st.error("❌ Could not extract text from the uploaded file.")

if __name__ == "__main__":
    main()
