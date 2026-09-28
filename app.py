import streamlit as st
import utils

st.set_page_config(page_title="AI Resume Screener", page_icon="🎯", layout="wide")

st.title("🎯 AI Resume Screener")
st.markdown("Compare multiple resumes (PDF and DOCX) against a job description instantly using TF-IDF text similarity.")

# Job Description Input Section
st.subheader("📝 Job Description")
jd_input = st.text_area("Paste the Job Description here:", height=200, placeholder="Requirements, responsibilities, skills...")
jd_clean = utils.clean_text(jd_input)

# Resume Upload Section
st.subheader("📤 Upload Resumes")
uploaded_files = st.file_uploader("Upload multiple resumes (PDF or DOCX format)", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files:
    if not jd_clean:
        st.error("⚠️ Please paste a Job Description first to calculate matches.")
    else:
        st.subheader("📊 Resume Match Results")
        results = []

        # Process uploaded files
        for uploaded_file in uploaded_files:
            # Route logic based on file extension
            if uploaded_file.name.lower().endswith('.pdf'):
                resume_text = utils.extract_text_from_pdf(uploaded_file)
            elif uploaded_file.name.lower().endswith('.docx'):
                resume_text = utils.extract_text_from_docx(uploaded_file)
            else:
                resume_text = ""
                
            resume_clean = utils.clean_text(resume_text)
            
            if not resume_clean.strip():
                st.warning(f"Could not extract meaningful text from **{uploaded_file.name}**. It might be scanned, empty, or corrupted.")
                continue
                
            match_score = utils.calculate_similarity(resume_clean, jd_clean)
            keyword_hint = utils.find_missing_keywords(resume_clean, jd_clean) if match_score < 70 else ""

            results.append({
                "Resume": uploaded_file.name,
                "Score": match_score,
                "Recommendation": "✅ Strong Match" if match_score >= 70 else "⚠️ Needs Improvement",
                "Hint": keyword_hint
            })

        # Display Results in UI
        if results:
            for res in results:
                col1, col2 = st.columns()
                with col1:
                    st.write(f"📁 **{res['Resume']}**")
                    st.progress(int(res['Score']))
                with col2:
                    st.write(f"Match Score: **{res['Score']}%**")
                    st.caption(res['Recommendation'])
                    
                if res['Hint']:
                    st.markdown(f"🔍 *Might be missing important terms:* `{res['Hint']}`")
                st.markdown("---")
else:
    st.info("Please upload at least one resume to begin screening.")
