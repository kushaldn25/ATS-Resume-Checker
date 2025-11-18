# ATS Resume Checker

**ATS Resume Checker** is an AI-powered web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). By comparing a job description (JD) against a PDF resume, it provides a compatibility score and actionable feedback on missing keywords.

## 🚀 Overview

In today's hiring process, resumes are often filtered by algorithms before they reach human eyes. This tool helps users bridge the gap by:
1.  Extracting high-value keywords from a specific Job Description using NLP.
2.  Scanning a PDF resume to see if those keywords are present.
3.  Providing a visual "Match Score" and a list of missing skills to improve acceptance chances.

## ✨ Key Features

-   **Smart Keyword Extraction**: Utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** via `scikit-learn` to identify the top 15 most important keywords from any text, filtering out common stop words.
-   **PDF Parsing Engine**: Integrates `PyMuPDF` to accurately extract text from uploaded PDF resumes.
-   **Instant Match Scoring**: Calculates a percentage match based on the presence of required keywords in the resume.
-   **Interactive Visualizations**:
    -   **Gauge Chart**: A dynamic color-coded gauge (Red/Yellow/Green) allows users to instantly see their compatibility score.
    -   **Animated Feedback**: "Matched" and "Missing" keywords are displayed with a typing animation for a polished user experience.

## 🛠️ Tech Stack

-   **Frontend**: [Streamlit](https://streamlit.io/) - For the interactive web interface.
-   **Data Processing**: [Scikit-Learn](https://scikit-learn.org/) - For TF-IDF vectorization and keyword extraction.
-   **PDF Handling**: [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) - For reading PDF files.
-   **Visualization**: [Plotly](https://plotly.com/) - For the interactive gauge chart.

## 📂 Project Structure

```text
ATS-Resume-Checker/
├── app.py              # Main Streamlit application entry point
├── jd_parser.py        # NLP logic for extracting keywords using TF-IDF
├── resume_parser.py    # Utility to extract text from PDF files
├── matcher.py          # Logic for calculating match scores
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
