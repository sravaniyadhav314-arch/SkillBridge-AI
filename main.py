print("=" * 45)
print("       SKILLBRIDGE AI")
print("  Resume and Job Description Matcher")
print("=" * 45)

candidate_input = input("\nEnter your skills separated by commas: ")

candidate_skills = [
    skill.strip().lower()
    for skill in candidate_input.split(",")
    if skill.strip()
]

required_skills = ["python", "sql", "git", "selenium"]

matched_skills = []
missing_skills = []

for skill in required_skills:
    if skill in candidate_skills:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

match_score = (len(matched_skills) / len(required_skills)) * 100

print("\n--- YOUR RESULTS ---")
print("Matched skills:", matched_skills)
print("Skills to learn:", missing_skills)
print("Skill match score:", round(match_score, 2), "%")
print("\nNote: This score measures skill overlap only.")