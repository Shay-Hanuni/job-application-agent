SKILL_ALIASES = {
    "git": [
        "github",
        "version control",
        "source control"
    ],
    "sql": [
        "database",
        "databases",
        "queries",
        "mysql",
        "postgresql",
        "sqlite"
    ],
    "api": [
        "rest api",
        "api testing",
        "http requests",
        "postman",
        "endpoints"
    ],
    "testing": [
        "qa",
        "quality assurance",
        "test cases",
        "test plans",
        "manual testing",
        "software testing"
    ],
    "automation": [
        "automated tests",
        "test automation",
        "automation testing",
        "scripts",
        "scripting"
    ],
    "selenium": [
        "browser automation",
        "web automation",
        "ui automation",
        "automated browser tests"
    ],
    "python": [
        "python scripting",
        "python automation",
        "pytest"
    ],
    "debugging": [
        "debug",
        "bug fixing",
        "troubleshooting",
        "issue investigation"
    ],
    "oop": [
        "object oriented programming",
        "object-oriented programming",
        "classes",
        "inheritance"
    ]
}


def normalize_keyword(keyword: str) -> str:
    """
    Converts a keyword or alias into a canonical skill name.
    Example:
    github -> git
    postman -> api
    browser automation -> selenium
    """
    keyword = keyword.lower().strip()

    for canonical_skill, aliases in SKILL_ALIASES.items():
        if keyword == canonical_skill:
            return canonical_skill

        if keyword in aliases:
            return canonical_skill

    return keyword


def normalize_keywords(keywords: list[str]) -> list[str]:
    """
    Normalizes a list of keywords and removes duplicates.
    """
    normalized = []

    for keyword in keywords:
        normalized_keyword = normalize_keyword(keyword)

        if normalized_keyword not in normalized:
            normalized.append(normalized_keyword)

    return normalized