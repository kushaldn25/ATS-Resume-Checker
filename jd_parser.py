from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, top_n=15):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    _ = vectorizer.fit_transform([text])
    return list(vectorizer.get_feature_names_out())
