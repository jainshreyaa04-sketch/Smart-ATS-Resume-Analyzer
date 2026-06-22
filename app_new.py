import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image
from utils.charts import show_ats_gauge, show_skill_pie
# ============================
# Import Utility Modules
# ============================

from utils.analyzer import analyze_resume
from utils.keyword_matcher import calculate_match
from utils.dashboard import show_dashboard
from utils.helpers import generate_ai_suggestions
from utils.skill_visualizer import show_skill_visualization
from utils.pdf_generator import create_pdf

# ============================
# Page Configuration
# ============================

st.set_page_config(
    page_title="Smart ATS Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ============================
# Logo
# ============================

logo = Image.open("assets/logo/logo.png")

# ============================
# Sidebar
# ============================

with st.sidebar:

    st.image(logo, width=120)

    st.title("Smart ATS")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "📄 Resume Analyzer",
            "💼 Job Description Matcher",
            "📊 Dashboard",
            "ℹ️ About"
        ]
    )

    st.markdown("---")

    st.write("### 👩‍💻 Developer")

    st.success("Shreya Jain")

    st.markdown("---")

    st.caption("Version 2.0")

# ============================
# Home Page
# ============================

if page == "🏠 Home":

    st.title("🤖 Smart ATS Resume Analyzer")

    st.markdown("""
### AI-Powered Resume Analysis Platform

Analyze your resume, compare it with job descriptions,
identify missing skills, improve ATS compatibility,
and generate professional resume reports.
""")

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Supported Roles", "10+")

    with c2:
        st.metric("ATS Engine", "Version 2.0")

    with c3:
        st.metric("Report Format", "PDF")

    st.divider()

    st.subheader("✨ Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✔ ATS Resume Analysis")
        st.success("✔ Job Description Matching")
        st.success("✔ AI Resume Suggestions")

    with col2:
        st.success("✔ Skill Visualization")
        st.success("✔ Analytics Dashboard")
        st.success("✔ PDF Report Generation")
# ============================
# Resume Analyzer Page
# ============================

elif page == "📄 Resume Analyzer":

    st.title("📄 Resume Analyzer")

    st.write(
        "Upload your Resume or paste Resume Text to analyze ATS score."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    resume = ""

    if uploaded_file is not None:

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            if page.extract_text():

                text += page.extract_text() + "\n"

        resume = text

        st.success("Resume Uploaded Successfully ✅")

    else:

        resume = st.text_area(

            "Paste Resume",

            height=250,

            key="resume_text"

        )

    st.divider()

    job_description = st.text_area(

        "Paste Job Description",

        height=250,

        key="job_description"

    )

    role = st.selectbox(

        "Target Role",

        [

            "Software Engineer",

            "Python Developer",

            "AI Engineer",

            "Data Analyst",

            "Data Scientist",

            "Cybersecurity",

            "Cloud Engineer",

            "Full Stack Developer"

        ]

    )
        # =====================================
    # Analyze Resume
    # =====================================

    if st.button("🚀 Analyze Resume", key="analyze_btn"):

        if resume.strip() == "":
            st.warning("⚠️ Please upload or paste your resume.")
        else:

            # ATS Analysis
            score, missing = analyze_resume(resume, role)

            try:
                score = int(score)
            except:
                score = 0

            # Job Description Matching
            jd_score, jd_missing = calculate_match(
                resume,
                job_description
            )

            try:
                jd_score = int(jd_score)
            except:
                jd_score = 0

            st.divider()

            # Dashboard
            show_dashboard(score, jd_score)

            st.divider()

            # Skill Visualization

            matched = []

            if len(missing) > 0:

                role_keywords = [
                    skill.lower()
                    for skill in resume.lower().split()
                ]

                for word in resume.lower().split():

                    if word not in missing:

                        matched.append(word)

            show_skill_visualization(
                matched,
                missing
            )
            show_skill_pie(
    len(matched),
    len(missing)
)

            st.divider()

            # JD Match

            st.subheader("💼 Job Description Match")

            st.metric(
                "Resume Match",
                f"{jd_score}%"
            )

            show_ats_gauge(score)

            if jd_missing:

                st.write("### Missing Keywords")

                for word in jd_missing[:15]:

                    st.write(f"• {word}")

            else:

                st.success(
                    "Excellent! Resume matches the Job Description."
                )

            st.divider()

            # AI Suggestions

            st.subheader("🤖 AI Suggestions")

            ai_suggestions = generate_ai_suggestions(
                score,
                missing
            )

            for suggestion in ai_suggestions:

                st.write(f"✅ {suggestion}")

            st.divider()

            # PDF Download

            pdf_file = create_pdf(resume)

            st.download_button(

                label="📥 Download Resume Report",

                data=pdf_file,

                file_name="Resume_Report.pdf",

                mime="application/pdf",

                key="download_resume"

            )
            # =====================================
# Dashboard Page
# =====================================

elif page == "📊 Dashboard":

    st.title("📊 Dashboard")

    st.info(
        "Analyze a resume from the Resume Analyzer page to view detailed analytics."
    )

    st.markdown("""
### Dashboard Features
- ATS Score
- Resume Match Score
- Skill Visualization
- AI Suggestions
- Resume Report
""")

# =====================================
# Job Description Matcher Page
# =====================================

elif page == "💼 Job Description Matcher":

    st.title("💼 Job Description Matcher")

    st.write(
        """
Paste a Job Description and analyze your resume from the
Resume Analyzer page.

The application will calculate:

- Resume Match Percentage
- Missing Skills
- ATS Compatibility
- Improvement Suggestions
"""
    )

# =====================================
# About Page
# =====================================

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.markdown("""
## Smart ATS Resume Analyzer

### Version
2.0

### Developed By
**Shreya Jain**

### Technologies Used

- Python
- Streamlit
- PyPDF2
- FPDF
- NLP (Keyword Matching)
- Modular Python Architecture

### Features

- ATS Resume Analysis
- Job Description Matching
- AI Resume Suggestions
- Skill Visualization
- PDF Report Generation
- Interactive Dashboard

### Future Enhancements

- OpenAI-powered resume rewriting
- Resume history
- Authentication
- Database integration
- Cloud deployment
""")

# =====================================
# Footer
# =====================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center; color:gray;">

Smart ATS Resume Analyzer • Version 2.0

Developed by <b>Shreya Jain</b>

Built with ❤️ using Python & Streamlit

</div>
""",
    unsafe_allow_html=True,
)