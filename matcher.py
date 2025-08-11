def keyword_match_score(jd_keywords, resume_text):
    jd_keywords = [kw.lower() for kw in jd_keywords]
    matched = [kw for kw in jd_keywords if kw in resume_text.lower()]
    missing = [kw for kw in jd_keywords if kw not in resume_text.lower()]
    score = round(len(matched) / len(jd_keywords) * 100, 2) if len(jd_keywords) > 0 else 0
    return score, matched, missing
