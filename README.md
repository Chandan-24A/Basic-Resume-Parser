# Resume Parser and Job Matcher

A Python mini-project that uses an LLM to extract structured information from a resume PDF and evaluate how well the candidate matches a Full Stack Web Developer Intern role.

## What it does

- Lets you select a PDF resume from a file picker.
- Extracts text from the PDF with `pypdf`.
- Uses the Groq API to identify the candidate's contact details, skills, education, experience, projects, certifications, and achievements.
- Compares the extracted profile with the job requirements and prints a match score, explanation, and eligibility result.

## Output

The application prints:

- A score from 0 to 100
- A short explanation of the score
- An eligibility message based on the current 70-point threshold

## Notes

- The job description is currently hard-coded in `resume_parse.py`.
- Scanned/image-only PDFs may not work because they require OCR.
- The LLM score is a helpful recommendation, not a final hiring decision.