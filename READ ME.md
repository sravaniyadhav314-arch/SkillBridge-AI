# SkillBridge AI

A beginner-friendly Python project that compares a candidate's skills with a predefined job skill list.

## Features

- Accepts skills entered by the user
- Identifies matching skills
- Lists skills that may need improvement
- Calculates a basic skill overlap percentage

## Technologies Used

- Python
- Lists, loops, conditional statements, and user input

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run `python main.py`.
5. Enter your skills separated by commas when prompted.

## Example

Input: `Python, SQL, C`

Required skills: Python, SQL, Git, Selenium

Matching skills: Python, SQL

Skills to learn: Git, Selenium

Skill match score: 50%

## Current Limitations

- Uses a predefined list of required skills
- Uses exact skill matching after converting text to lowercase
- Does not yet read resumes from PDF files
- The match score measures skill overlap and does not predict hiring outcomes

## Future Improvements

- Add resume PDF upload and text extraction
- Allow users to enter job descriptions
- Store job comparisons using SQLite
- Build a web interface using Streamlit

## Author

KUMMARI SRAVANI