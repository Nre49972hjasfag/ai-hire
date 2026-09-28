import re
import io
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text

def extract_text_from_pdf(uploaded_file):
    """Extracts text safely from an uploaded file object in-memory."""
    try:
        if hasattr(uploaded_file, 'getvalue'):
            # Convert Streamlit UploadedFile bytes stream directly for pdfminer
            pdf_stream = io.BytesIO(uploaded_file.getvalue())
            return extract_text(pdf_stream)
        return extract_text(uploaded_file)
    except Exception as e:
        st.error(f"Error parsing PDF file: {e}")
        return ""

def clean_text(text):
    """Normalizes text by lowercase conversion, space reduction, and punctuation removal."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Normalizes newlines and multiple spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def calculate_similarity(resume_text, jd_text):
    """Calculates TF-IDF cosine similarity percentage between text segments, ignoring stop words."""
    if not resume_text or not jd_text:
        return 0.0
    try:
        # Use  stop words to filter out common structural terms
        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        score = cosine_similarity(vectors[0:1], vectors[1:2])
        return round(float(score[0][0]) * 100, 2)
    except ValueError:
        # Failsafe if text contains only stop words or is completely empty
        return 0.0

def find_missing_keywords(resume_clean, jd_clean):
    """Identifies distinct words >5 characters present in the job description but omitted from the resume."""
    jd_words = set(word for word in jd_clean.split() if len(word) > 5)
    resume_words = set(resume_clean.split())
    missing = list(jd_words - resume_words)
    return ", ".join(sorted(missing)[:5])
