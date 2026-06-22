import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image

from utils.pdf_generator import create_pdf
from utils.analyzer import analyze_resume
from utils.keyword_matcher import calculate_match
from utils.dashboard import show_dashboard
from utils.helpers import generate_ai_suggestions
from utils.skill_visualizer import show_skill_visualization
# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Smart ATS Resume Analyzer",
    page_icon="🤖",
    layout="wide"
   
)
logo = Image.open("assets/logo/logo.png")
st.image(logo, width=100)
# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.image("assets/logo/logo.png", width=120)

    st.title("Smart ATS")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "📄 Resume Analyzer",
            "💼 JD Matcher",
            "📊 Dashboard",
            "ℹ️ About"
        ]
    )

    st.markdown("---")

    st.write("### 👩‍💻 Developer")
    st.success("Shreya Jain")

    st.markdown("---")

    st.caption("Version 2.0")
st.markdown("""
# 🤖 Smart ATS Resume Analyzer

### AI-powered Resume Screening & ATS Optimization

Analyze your resume, identify missing keywords, calculate ATS compatibility, and generate improvement suggestions with downloadable reports.

---
""")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📄 Resume Analysis")

with col2:
    st.success("📊 ATS Score")

with col3:
    st.warning("💡 AI Suggestions")
st.write("Upload or paste resume to get ATS Score, Missing Keywords & Suggestions (Downloadable PDF)")
st.divider()

# ----------------------------
# PDF Upload
# ----------------------------
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
resume = ""
job_description = st.text_area(
    "💼 Paste Job Description (Optional)",
    height=200,
    placeholder="Paste the job description here..."
)
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

if uploaded_file is not None:
    resume = extract_text_from_pdf(uploaded_file)
    st.success("✅ PDF uploaded successfully!")
else:
    resume = st.text_area("📌 Paste Your Resume", height=200)

# ----------------------------
# Role Selection
# ----------------------------
role = st.selectbox(
    "🎯 Target Role",
    sorted([
        "AI Engineer",
        "Cloud Engineer",
        "Cybersecurity",
        "Data Analyst",
        "Data Scientist",
        "Full Stack Developer",
        "Game Developer",
        "IoT / Robotics",
        "Python Developer",
        "Software Engineer"
    ])
)

# ----------------------------
# Role-based keywords
# ----------------------------
def get_role_keywords(role):
    keywords = {
        "Data Analyst": ["python","sql","pandas","numpy","data visualization","power bi","tableau","excel","statistics","data cleaning"],
        "Software Engineer": ["java","dsa","oop","system design","api","backend","frontend","react","database","algorithms"],
        "AI Engineer": ["machine learning","deep learning","nlp","tensorflow","pytorch","model deployment","llm","transformers","python","data"],
        "Data Scientist": ["python","machine learning","statistics","data analysis","pandas","numpy","scikit-learn","visualization","modeling"],
        "Cybersecurity": ["network security","osint","penetration testing","ethical hacking","firewalls","encryption","threat analysis","linux","security tools"],
        "Full Stack Developer": ["react","node.js","express","mongodb","frontend","backend","api","javascript","html","css"],
        "Cloud Engineer": ["aws","azure","gcp","docker","kubernetes","cloud computing","devops","ci/cd","infrastructure"],
        "Game Developer": ["unity","unreal engine","c#","c++","game physics","3d modeling","animation","game design"],
        "IoT / Robotics": ["arduino","raspberry pi","embedded systems","sensors","robotics","iot","microcontrollers","python","c++"],
        "Python Developer": ["python","django","flask","api","backend","automation","scripting","sql","debugging"]
    }
    return keywords.get(role, [])

# ----------------------------
# ATS Analysis
# ----------------------------


# ----------------------------
# Keyword Suggestions
# ----------------------------
def keyword_suggestions(missing_keywords):
    suggestions = []
    for word in missing_keywords:
        if word in ["python","sql","pandas","numpy"]:
            suggestions.append(f"Add projects using {word}")
        elif word in ["power bi","tableau","data visualization"]:
            suggestions.append(f"Include dashboards using {word}")
        elif word in ["machine learning","deep learning"]:
            suggestions.append(f"Add ML projects using {word}")
        elif word in ["api","backend"]:
            suggestions.append("Include backend/API development experience")
        elif word in ["aws","azure","gcp"]:
            suggestions.append(f"Add cloud experience ({word})")
        elif word in ["docker","kubernetes"]:
            suggestions.append(f"Mention DevOps tools like {word}")
        elif word in ["react","frontend"]:
            suggestions.append("Include frontend projects")
        elif word in ["statistics"]:
            suggestions.append("Highlight statistics or analysis work")
        else:
            suggestions.append(f"Try to include {word} in your resume")
    return suggestions

# ----------------------------
# Remove Suggestions
# ----------------------------

# ----------------------------
# Remove Suggestions
# ----------------------------
def removal_suggestions(resume, role):
    suggestions = []
    res = resume.lower()

    if role == "Data Analyst":
        if "java" in res:
            suggestions.append("Reduce focus on Java")
        if "c++" in res:
            suggestions.append("Avoid highlighting C/C++ too much")

    elif role == "Software Engineer":
        if "tableau" in res:
            suggestions.append("Tableau is less relevant")
        if "power bi" in res:
            suggestions.append("Reduce BI tools focus")

    elif role == "AI Engineer":
        if "excel" in res:
            suggestions.append("Excel is not important for AI roles")

    return suggestions

# ----------------------------
# PDF Creation (Unicode-safe)
# ----------------------------

# ----------------------------
# Analyze Button
# ----------------------------
# ----------------------------
# Analyze Button
# ----------------------------
if st.button("🚀 Analyze Resume"):

    if resume.strip() == "":
        st.warning("⚠️ Please upload or paste your resume.")
    else:

        st.divider()

        # ATS Score
        score, missing = analyze_resume(resume, role)

        try:
            score = int(score)
        except:
            score = 0

        # Job Description Match
        jd_score, jd_missing = calculate_match(resume, job_description)

        try:
            jd_score = int(jd_score)
        except:
            jd_score = 0

        # ---------------- ATS ----------------
        show_dashboard(score, jd_score)

        # ---------------- JD Match ----------------
        st.divider()

        st.subheader("💼 Job Description Match")

        st.progress(jd_score / 100)

        st.metric("Resume Match", f"{jd_score}%")

        if jd_missing:
            st.write("### Missing Keywords from Job Description")
            for word in jd_missing:
                st.write(f"• {word}")
        else:
            st.success("Excellent! Your resume matches the job description.")

        # ---------------- Missing Keywords ----------------
        st.divider()

        matched = get_role_keywords(role)

matched = [skill for skill in matched if skill not in missing]

show_skill_visualization(matched, missing)

        # ---------------- Suggestions ----------------#
        #       st.subheader("🤖 AI Resume Suggestions")

ai_suggestions = generate_ai_suggestions(score, missing)

for suggestion in ai_suggestions:
    st.write(f"• {suggestion}")

        # ---------------- Remove Suggestions ----------------
    st.subheader("⚠️ Remove / Reduce")

    remove = removal_suggestions(resume, role)

    if remove:
            for r in remove:
                st.write(f"• {r}")
    else:
            st.success("No major issues found.")

        # ---------------- PDF ----------------
    st.divider()

    pdf_file = create_pdf(resume)
st.download_button(
    label="📥 Download Resume Report",
    data=pdf_file,
    file_name="resume_report.pdf",
    mime="application/pdf",
    key="download_resume_report"
)

st.markdown(
    """
    <div style='text-align:center; color:gray;'>
        <h4>🤖 Smart ATS Resume Analyzer</h4>
        <p>Developed by <b>Shreya Jain</b></p>
        <p>Python • Streamlit • NLP • PDF Processing</p>
    </div>
    """,
    unsafe_allow_html=True
)
