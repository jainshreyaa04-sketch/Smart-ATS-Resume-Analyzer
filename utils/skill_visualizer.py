import streamlit as st

def show_skill_visualization(matched, missing):
    st.subheader("📊 Skill Visualization")

    total = len(matched) + len(missing)

    if total == 0:
        st.info("No skills available to visualize.")
        return

    for skill in matched:
        st.write(f"✅ {skill}")
        st.progress(1.0)

    for skill in missing:
        st.write(f"❌ {skill}")
        st.progress(0.2)