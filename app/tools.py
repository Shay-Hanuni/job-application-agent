import re
from collections import Counter
from app.skill_normalizer import normalize_keywords


def extract_keywords(text: str, limit: int = 30) -> list[str]:
    """
    Extracts common important keywords from text.
    This is a simple local version without AI API usage.
    """
    words = re.findall(r"\b[a-zA-Z][a-zA-Z0-9+#.-]{2,}\b", text.lower())

    stop_words = {
        "and", "the", "for", "with", "you", "are", "this", "that",
        "from", "will", "have", "has", "our", "your", "but", "not",
        "all", "can", "job", "role", "work", "team", "about", "into",
        "looking", "includes", "strong", "skills", "working", "issues",
        "knowledge", "engineer", "junior", "candidate", "experience",
        "using", "maintaining", "writing", "built", "academic", "software",
        "development", "developer"
    }

    filtered_words = [
        word for word in words
        if word not in stop_words and len(word) > 2
    ]

    most_common = Counter(filtered_words).most_common(limit)

    return [word for word, count in most_common]


def extract_phrase_skills(text: str) -> list[str]:
    """
    Finds known multi-word skill phrases inside the text.
    """
    text = text.lower()

    known_phrases = [
        "version control",
        "source control",
        "rest api",
        "api testing",
        "http requests",
        "quality assurance",
        "test cases",
        "test plans",
        "manual testing",
        "software testing",
        "automated tests",
        "test automation",
        "automation testing",
        "browser automation",
        "web automation",
        "ui automation",
        "automated browser tests",
        "python scripting",
        "python automation",
        "bug fixing",
        "issue investigation",
        "object oriented programming",
        "object-oriented programming"
    ]

    found_phrases = []

    for phrase in known_phrases:
        if phrase in text:
            found_phrases.append(phrase)

    return found_phrases


def extract_all_skills(text: str) -> list[str]:
    """
    Extracts both single keywords and known phrase-based skills,
    then normalizes them into canonical skill names.
    """
    single_keywords = extract_keywords(text)
    phrase_skills = extract_phrase_skills(text)

    combined = single_keywords + phrase_skills
    normalized = normalize_keywords(combined)

    return normalized


def compare_keywords(cv_keywords: list[str], job_keywords: list[str]) -> dict:
    """
    Compares normalized CV keywords with normalized job description keywords.
    """
    cv_set = set(cv_keywords)
    job_set = set(job_keywords)

    matched_keywords = sorted(cv_set.intersection(job_set))
    missing_keywords = sorted(job_set.difference(cv_set))

    if len(job_set) == 0:
        match_score = 0
    else:
        match_score = round((len(matched_keywords) / len(job_set)) * 100, 2)

    return {
        "match_score": match_score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords
    }