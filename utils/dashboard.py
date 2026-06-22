import streamlit as st

def show_dashboard(score, jd_score):
    st.subheader("📊 Resume Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATS Score", f"{score}%")

    with col2:
        st.metric("JD Match", f"{jd_score}%")

    st.divider()

    if score >= 80:
        st.success("Excellent ATS Score")
    elif score >= 60:
        st.warning("Good ATS Score")
    else:
        st.error("Needs Improvement")