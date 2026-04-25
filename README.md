# Job Application Agent

A Python-based job application analysis tool that compares a candidate's CV against a job description and generates a structured improvement report.

## Overview

Job Application Agent is a Python project designed to help candidates improve their CV before applying to a specific job.

The system receives a CV and a job description, analyzes the content, identifies relevant and missing skills, and generates a clear report with practical recommendations for improving the CV.

The project currently focuses on rule-based and structured text analysis. It is built with a modular architecture that can support future integration with an AI API for deeper semantic analysis and personalized recommendations.

## Features

- Analyze a CV against a target job description
- Identify matching skills and keywords
- Detect missing skills from the job requirements
- Generate a structured improvement report
- Normalize technical skills for better comparison
- Work with local text files as input
- Save generated reports to an output folder
- Modular code structure for future expansion
- Designed for future AI API integration

## Tech Stack

- Python
- File Processing
- Text Processing
- Rule-Based Analysis
- Modular Software Design
- Git / GitHub

## Project Structure

```text
job-application-agent/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── main.py
│   ├── prompts.py
│   ├── report_writer.py
│   ├── skill_normalizer.py
│   └── tools.py
│
├── data/
│   ├── cv.txt
│   ├── job_description.txt
│   └── backend_job.txt
│
├── outputs/
│   └── generated reports
│
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

The project follows a simple local analysis workflow:

1. **Input CV**  
   The user adds a CV text file inside the `data` folder.

2. **Input Job Description**  
   The user adds a job description text file inside the `data` folder.

3. **Read Input Files**  
   The program reads both files and prepares the text for analysis.

4. **Normalize Skills**  
   Technical skills and keywords are normalized so similar terms can be compared more effectively.

5. **Compare CV Against Job Requirements**  
   The program compares the CV content with the job description and checks which skills and keywords appear in both.

6. **Detect Gaps**  
   The system identifies missing skills, missing keywords, and areas where the CV can be improved.

7. **Generate Report**  
   A structured report is created and saved in the `outputs` folder.

The generated report includes:

- Matching skills
- Missing skills
- Keyword gaps
- Improvement suggestions
- General application readiness feedback

## Clone the Repository

To use this project locally, clone the repository from GitHub:

```bash
git clone https://github.com/YOUR_USERNAME/job-application-agent.git
```

Enter the project folder:

```bash
cd job-application-agent
```

> Replace `YOUR_USERNAME` with your GitHub username.

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the project:

```bash
python -m app.main
```

The program reads the input files from the `data` folder and generates an output report in the `outputs` folder.

## Example Use Case

A candidate wants to apply for a Backend Developer position.

The user provides:

- A CV file
- A backend job description

The system analyzes both files and produces a report showing:

- Which job requirements are already reflected in the CV
- Which technical skills are missing
- Which keywords should be added
- How the CV can be improved for better job matching

## Why I Built This Project

I built this project to demonstrate how automation and structured text analysis can support the job application process.

The project shows practical experience with Python, file processing, text analysis, modular code organization, and report generation. It also provides a strong foundation for adding AI-based analysis in the future.

## Future Improvements

- Integrate an AI API for semantic CV-job matching
- Add support for PDF and DOCX CV files
- Generate an improved CV automatically
- Add a simple web interface
- Export reports to PDF
- Compare one CV against multiple job descriptions
- Save previous analyses in a database
- Add ATS-style keyword scoring
- Add LinkedIn profile analysis

## Author

Shay Hanuni
