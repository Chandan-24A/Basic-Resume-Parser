import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel,Field
from pypdf import PdfReader
from tkinter import Tk, filedialog
from typing import List, Optional


load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api key not found")

client = Groq(api_key=my_api_key)
role="user"
model ="openai/gpt-oss-120b"

Tk().withdraw()

file_path = filedialog.askopenfilename(
    title="Select Resume",
    filetypes=[("PDF Files", "*.pdf")]
)

if not file_path:
    raise ValueError("No file selected")

reader = PdfReader(file_path)

resume_text = ""

for page in reader.pages:
    resume_text += (page.extract_text() or "") + "\n"

class Resume(BaseModel):
    name:str
    email:Optional[str]=None
    phone:Optional[str]=None
    skills:List[str] = Field(default_factory=list)
    education:List[str]=Field(default_factory=list)
    experience:List[str]=Field(default_factory=list)
    projects:List[str]=Field(default_factory=list)
    certifications:List[str]=Field(default_factory=list)
    achievements: List[str] = Field(default_factory=list)

schema = Resume.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt = f"""
You are a resume parsing assistant.

Extract information from the resume and return it as JSON according to the following schema:

{schema}

Rules:
1. Extract only information explicitly present in the resume.
2. Do not invent or assume information.
3. If optional information is missing, use null.
4. If a list-based field has no information, return an empty list.
5. Keep the extracted information concise and relevant.
6. Return only valid JSON.
"""

message_system ={
    "role":"system",
    "content":system_prompt
}

prompt = f"""
Parse the following resume according to the schema provided in the system prompt.

Resume:
{resume_text}
"""

message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]

response = client.chat.completions.create(model=model,messages=messages,response_format=response_format)

answer = response.choices[0].message.content


import json

raw_data = answer

data = json.loads(raw_data)

resume_content = Resume(**data)

class ResumeMatch(BaseModel):
    score:int
    matched_skills: List[str] = Field(default_factory=list)
    missing_skills: List[str] = Field(default_factory=list)
    strengths: List[str] = Field(default_factory=list)
    weaknesses: List[str] = Field(default_factory=list)
    explanation: str

match_schema = ResumeMatch.model_json_schema()

match_system_prompt = f"""
You are an expert technical recruiter.

Your task is to compare a candidate's resume against a job requirement
and determine how relevant the candidate is for the position.

Return your response according to this schema:

{match_schema}

Scoring guidelines:
- 50%: Required technical skills
- 20%: Relevant experience
- 15%: Projects
- 10%: Education
- 5%: Certifications and other relevant qualifications

Rules:
1. Score the candidate from 0 to 100.
2. Only use information explicitly present in the resume.
3. Do not assume missing skills or experience.
4. Match skills semantically when appropriate.
5. Required skills are more important than preferred skills.
6. AI/LLM experience should be treated as an advantage, not a mandatory requirement.
7. Clearly identify matched and missing skills.
8. Explain the main reasons behind the score.
9. Return only valid JSON.
"""

match_message_system={
    "role":"system",
    "content":match_system_prompt
}

job_requirement="""
FULL STACK WEB DEVELOPER INTERN

Job Description:
We are looking for a motivated Full Stack Web Developer Intern to help build and maintain modern web applications.

REQUIRED SKILLS:
- JavaScript
- Node.js
- Express.js
- React.js
- HTML
- CSS
- REST APIs
- MongoDB or PostgreSQL
- Git and GitHub
- Basic authentication concepts
- Basic understanding of backend development

PREFERRED SKILLS:
- TypeScript
- Docker
- Cloud deployment
- JWT authentication
- Session-based authentication
- Experience deploying full-stack applications

AI INTEGRATION - ADVANTAGE:
Experience with AI/LLM integration will be considered an advantage.

Examples:
- OpenAI, Gemini, Groq, or similar APIs
- Integrating LLM APIs into web applications
- Prompt engineering
- Building AI-powered features
- Using AI APIs with Node.js and Express.js

EDUCATION:
- Pursuing B.Tech/B.E. in Computer Science, Information Technology, or a related field
- 2nd, 3rd, or 4th year students are welcome

EXPERIENCE:
- 0-1 years
- Freshers are welcome

OTHER REQUIREMENTS:
- Good problem-solving skills
- Good understanding of web development fundamentals
- Ability to learn new technologies
- Good debugging skills
- Ability to work in a team
- Personal or academic projects are preferred
"""

match_prompt = f"""
Compare the candidate's resume with the following job requirements.

JOB REQUIREMENTS:
{job_requirement}

CANDIDATE RESUME:
{resume_content.model_dump_json()}

Evaluate how well the candidate matches the job requirements.

Give a score from 0 to 100.

Consider:
- Required technical skills
- Relevant experience
- Projects
- Education
- Certifications
- Overall relevance to the job

Do not give credit for information that is not present in the resume.

Return the result according to the provided schema.
"""
match_message={
    "role":role,
    "content":match_prompt
}

match_messages = [match_message_system,match_message]
match_response = client.chat.completions.create(model=model,messages=match_messages,response_format=response_format)

match_answer = match_response.choices[0].message.content

raw_data2 = match_answer

data_files = json.loads(raw_data2)

match_res = ResumeMatch(**data_files)

print("your score:",match_res.score)

print()

print("summery:",match_res.explanation)

print()


if match_res.score >=70:
    print("You are eligible")
else:
    print("You are not eligible")





