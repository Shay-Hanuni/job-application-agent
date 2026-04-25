# Job Application Agent

A Python-based job application analysis tool that compares a candidate's CV against a job description and generates a structured improvement report.

## Overview

Job Application Agent is a Python project designed to help candidates improve their CV before applying to a specific job.

The system receives a CV and a job description, analyzes the content, identifies relevant and missing skills, and generates a clear report with practical recommendations for improving the CV.

The project currently focuses on rule-based and structured text analysis, and is built with a modular architecture that can support future integration with an AI API for deeper semantic analysis and personalized recommendations.

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
