```python
import streamlit as st
import re

st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🚀"
)

st.title("🚀 SkillBridge AI")
st.write("Compare your skills with a real job description.")

user_skills = st.text_input(
    "👩‍💻 Enter Your Skills",
    placeholder="Python, SQL, C, Selenium"
)

job_description = st.text_area(
    "📋 Paste the Job Description",
    placeholder="Paste the complete job description here...",
    height=250
)

if st.button("Analyze My Match"):
    if not user_skills.strip() or not job_description.strip():
        st.warning("Please enter your skills and the job description.")
    else:
        skills = [
            skill.strip().lower()
            for skill in user_skills.split(",")
            if skill.strip()
        ]

        job_text = job_description.lower()

        matched = [
            skill for skill in skills
            if re.search(
                r"(?<!\w)" + re.escape(skill) + r"(?!\w)",
                job_text
            )
        ]

        missing = [
            skill for skill in skills
            if skill not in matched
        ]

        score = len(matched) / len(skills) * 100

        st.subheader("📊 Your Results")
        st.metric("Skill Match", f"{score:.0f}%")

        st.write("✅ Skills found in the job description:")
        st.write(", ".join(matched) if matched else "No matches found.")

        st.write("📚 Skills not mentioned in the job description:")
        st.write(", ".join(missing) if missing else "None")

        st.caption(
            "This is a basic keyword comparison, not an AI-powered "
            "assessment. A skill may be relevant even if its exact "
            "keyword is absent."
        )
```
