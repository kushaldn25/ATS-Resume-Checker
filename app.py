import streamlit as st
import plotly.graph_objects as go
import time
from jd_parser import extract_keywords
from resume_parser import extract_text_from_pdf
from matcher import keyword_match_score

st.set_page_config(page_title="Resume vs JD Matcher", layout="centered")

st.title("📝 ATS Resume Checker")

# 1. JD Input
jd_input = st.text_area("📄 Paste Job Description Here")

jd_keywords = []
if jd_input:
    jd_keywords = extract_keywords(jd_input)
    st.write("🔑 **Extracted Keywords:**", ", ".join(jd_keywords))

# 2. Upload Resume
resume_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

if resume_file and jd_keywords:
    resume_text = extract_text_from_pdf(resume_file)
    score, matched, missing = keyword_match_score(jd_keywords, resume_text)

    # 3. Gauge for Match Score
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Match Score (%)"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "green"},
               'steps': [
                   {'range': [0, 50], 'color': "red"},
                   {'range': [50, 75], 'color': "yellow"},
                   {'range': [75, 100], 'color': "lightgreen"}]}
    ))
    st.plotly_chart(fig, use_container_width=True)

    # 4. Animated Matched Keywords
    st.subheader("✅ Matched Keywords")
    placeholder_matched = st.empty()
    matched_display = ""
    for kw in matched:
        matched_display += f"✅ {kw}\n"
        placeholder_matched.markdown(f"```\n{matched_display}\n```")
        time.sleep(0.1)  # animation delay

    # 5. Animated Missing Keywords
    st.subheader("❌ Missing Keywords")
    placeholder_missing = st.empty()
    missing_display = ""
    for kw in missing:
        missing_display += f"❌ {kw}\n"
        placeholder_missing.markdown(f"```\n{missing_display}\n```")
        time.sleep(0.1)  # animation delay
