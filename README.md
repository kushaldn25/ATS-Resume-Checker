# 📝 ATS Resume Checker

An intelligent, AI-powered tool designed to help job seekers optimize
their resumes for Applicant Tracking Systems (ATS). This application
compares a Job Description (JD) against a PDF resume, calculates a match
score, and identifies missing keywords using Natural Language Processing
(NLP).

## 🚀 Overview

The ATS Resume Checker streamlines the job application process by
analyzing how well a resume matches a specific job description. It
utilizes TF-IDF to extract relevant keywords and provides instant
feedback on skill gaps.

## ✨ Key Features

-   Smart Keyword Extraction using scikit-learn's TfidfVectorizer.
-   PDF Resume Parsing with PyMuPDF.
-   Match Score Visualization using Plotly gauge chart.
-   Detailed Gap Analysis for matched and missing keywords.
-   Interactive Streamlit UI.

## 🛠️ Technologies Used

-   Streamlit
-   Scikit-Learn
-   PyMuPDF
-   Plotly

## 📂 Project Structure

```
ATS-Resume-Checker/ 
    ├── app.py 
    ├── jd_parser.py 
    ├── resume_parser.py 
    ├──matcher.py 
    ├── requirements.txt 
    └── README.md
```

## ⚙️ Installation & Setup

``` bash
git clone <https://github.com/kushaldn25/ATS-Resume-Checker>
cd ATS-Resume-Checker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 📖 Usage Guide

1.  Paste Job Description.
2.  Upload Resume (PDF).
3.  View match score, keywords, and missing skills.

## 🧠 How It Works

-   TF-IDF extracts top keywords.
-   PDF text is extracted page-by-page.
-   Keywords are matched and a score is computed.

## 📬 Contact

Feel free to reach out for improvements or suggestions!
