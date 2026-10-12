import streamlit as st
import re

st.set_page_config(
page_title="SkillBridge AI",
page_icon="🚀",
layout="centered"
)

st.title("🚀 SkillBridge AI")
st.subheader("Resume and Job Description Matcher")

st.write(
"Compare your skills with a job description "
"and find matching and missing skills."
)

user_skills = st.text_input(
"👩‍💻 Enter Your Skills",
placeholder="Python, SQL, C, Selenium"
)

job_description = st.text_area(
"📋 Paste the Job Description",
placeholder="Paste the complete job description here...",
height=250
)

if st.button("Analyze My Match", type="primary"):
if not user_skills.strip() or not job_description.strip():
st.warning("Please enter your skills and the job description.")
else:
skills = list(dict.fromkeys(
skill.strip().lower()
for skill in user_skills.split(",")
if skill.strip()
))

```
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

    st.divider()
    st.subheader("📊 Your Results")
    st.metric("Keyword Match", f"{score:.0f}%")

    st.write("✅ **Skills found in the job description**")
    if matched:
        st.success(", ".join(matched))
    else:
        st.info("No matching keywords found.")

    st.write("📚 **Skills not mentioned in the job description**")
    if missing:
        st.warning(", ".join(missing))
    else:
        st.success("All your entered skills were found!")

    st.caption(
        "This is a basic keyword comparison, not a complete "
        "AI assessment. Related skills may not be detected "
        "if their exact keywords are absent."
    )
```
