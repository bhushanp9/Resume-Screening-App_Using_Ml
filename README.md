# 📄 Resume Screening App with ATS Score

A Streamlit web application that automatically classifies resumes into categories and calculates an ATS (Applicant Tracking System) match score against a provided job description.

---

# [![Check your resume with ATS score](https://img.shields.io/badge/🚀%20Check%20your%20resume%20with%20ATS%20score-Click%20Here-brightgreen?style=for-the-badge)](https://resume-screening-appusingml-ayf7aznmszhvd9pbqxcuih.streamlit.app/)

---

## 🚀 Features

- ✅ Upload resumes in PDF or TXT format
- 🧠 Predicts the professional category (e.g., Data Science, Java Developer)
- 📊 Calculates ATS (Applicant Tracking System) match score against a job description
- 🔍 Instant results with an interactive web interface
- 🌐 Hosted with Streamlit Cloud

---

## 🧠 Model Info

- `clf.pkl`: Resume classification model hosted on Hugging Face  
  🔗 [View on Hugging Face](https://huggingface.co/bhushanp9/Movie-recommender-system/resolve/main/clf.pkl)

- `tfidf.pkl`: TF-IDF vectorizer used to vectorize resume/job description (must be available locally)

---

## 📁 Project Structure

resume-screening-app/
├── app.py # Main Streamlit app
├── tfidf.pkl # TF-IDF vectorizer (required locally)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---
# Screenshot of Resume Screening App UI

![Image](https://github.com/user-attachments/assets/98efc075-7d6d-4ab7-b478-bc22df4ef7af)

![Image](https://github.com/user-attachments/assets/4cd49764-58f4-427d-b058-f8bdbff70d13)

![Image](https://github.com/user-attachments/assets/f69eabe5-d80c-4be5-b02a-e942c15c16f9)

---
 
 **Clone the repository**:

```bash
git clone https://github.com/bhushanp9/Resume-Screening-App_Using_Ml.git
cd resume-screening-app

