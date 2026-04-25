import re


TECHNICAL_SKILLS = {
    "python",
    "java",
    "c#",
    "c++",
    "javascript",
    "typescript",
    "html",
    "css",
    "sql",
    "react",
    "node.js",
    "express",
    "django",
    "flask",
    ".net",
    "spring",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "redis",
    "git",
    "github",
    "linux",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "jira",
    "oop",
    "object oriented programming",
    "data structures",
    "algorithms",
    "rest api",
    "api",
    "microservices",
    "debugging",
    "unit testing",
    "integration testing",
    "qa",
    "manual testing",
    "automation",
    "test automation",
    "selenium",
    "pytest",
    "playwright",
    "postman",
    "test cases",
    "bug reports",
    "network security",
    "firewalls",
    "ids",
    "cryptography",
    "authentication",
    "authorization",
}


SOFT_SKILLS = {
    "communication",
    "teamwork",
    "team player",
    "problem solving",
    "fast learner",
    "independent",
    "self learning",
    "attention to detail",
    "detail oriented",
    "responsibility",
    "motivation",
    "adaptability",
}


ALIASES = {
    "js": "javascript",
    "ts": "typescript",
    "nodejs": "node.js",
    "node": "node.js",
    "reactjs": "react",
    "postgres": "postgresql",
    "mongo": "mongodb",
    "rest": "rest api",
    "apis": "api",
    "object-oriented": "object oriented programming",
    "object oriented": "object oriented programming",
    "c sharp": "c#",
    "dotnet": ".net",
}


def normalize_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_skill(skill: str) -> str:
    skill = normalize_text(skill)
    skill = skill.strip(".,:;()[]{}")
    return ALIASES.get(skill, skill)


def contains_phrase(text: str, phrase: str) -> bool:
    phrase = normalize_skill(phrase)
    escaped = re.escape(phrase)
    pattern = rf"(?<!\w){escaped}(?!\w)"
    return re.search(pattern, text) is not None


def extract_skills_by_category(text: str) -> dict:
    normalized_text = normalize_text(text)

    technical_matches = set()
    soft_matches = set()

    for skill in TECHNICAL_SKILLS:
        normalized_skill = normalize_skill(skill)
        if contains_phrase(normalized_text, normalized_skill):
            technical_matches.add(normalized_skill)

    for skill in SOFT_SKILLS:
        normalized_skill = normalize_skill(skill)
        if contains_phrase(normalized_text, normalized_skill):
            soft_matches.add(normalized_skill)

    return {
        "technical": sorted(technical_matches),
        "soft": sorted(soft_matches),
    }


def extract_relevant_keywords(text: str) -> list:
    categories = extract_skills_by_category(text)
    keywords = set(categories["technical"]) | set(categories["soft"])
    return sorted(keywords)


def compare_skill_sets(cv_text: str, job_text: str) -> dict:
    cv_skills = extract_skills_by_category(cv_text)
    job_skills = extract_skills_by_category(job_text)

    cv_technical = set(cv_skills["technical"])
    job_technical = set(job_skills["technical"])

    cv_soft = set(cv_skills["soft"])
    job_soft = set(job_skills["soft"])

    matched_technical = cv_technical & job_technical
    missing_technical = job_technical - cv_technical

    matched_soft = cv_soft & job_soft
    missing_soft = job_soft - cv_soft

    return {
        "cv_technical_skills": sorted(cv_technical),
        "job_technical_skills": sorted(job_technical),
        "matched_technical_skills": sorted(matched_technical),
        "missing_technical_skills": sorted(missing_technical),
        "cv_soft_skills": sorted(cv_soft),
        "job_soft_skills": sorted(job_soft),
        "matched_soft_skills": sorted(matched_soft),
        "missing_soft_skills": sorted(missing_soft),
    }


def calculate_match_score(comparison: dict) -> dict:
    job_technical = comparison["job_technical_skills"]
    matched_technical = comparison["matched_technical_skills"]

    job_soft = comparison["job_soft_skills"]
    matched_soft = comparison["matched_soft_skills"]

    if job_technical:
        technical_score = len(matched_technical) / len(job_technical) * 100
    else:
        technical_score = 100

    if job_soft:
        soft_score = len(matched_soft) / len(job_soft) * 100
    else:
        soft_score = 100

    final_score = technical_score * 0.85 + soft_score * 0.15

    return {
        "technical_score": round(technical_score, 2),
        "soft_score": round(soft_score, 2),
        "final_score": round(final_score, 2),
    }