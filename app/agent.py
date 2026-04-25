from app.tools import extract_all_skills, compare_keywords

def create_ats_analysis(cv_text: str, job_text: str) -> dict:
    """
    Creates a structured ATS analysis based on CV and job description.
    Returns a dictionary that can be saved as JSON.
    """
    cv_keywords = extract_all_skills(cv_text)
    job_keywords = extract_all_skills(job_text)
    comparison = compare_keywords(cv_keywords, job_keywords)

    recommendations = []

    if comparison["missing_keywords"]:
        for keyword in comparison["missing_keywords"][:10]:
            recommendations.append(
                f"Add or emphasize '{keyword}' in your CV if it reflects your real knowledge, coursework, or projects."
            )
    else:
        recommendations.append(
            "Your CV already contains the main keywords from the job description."
        )

    return {
        "match_score": comparison["match_score"],
        "cv_keywords": cv_keywords,
        "job_keywords": job_keywords,
        "matched_keywords": comparison["matched_keywords"],
        "missing_keywords": comparison["missing_keywords"],
        "recommendations": recommendations
    }


def create_text_report(analysis: dict) -> str:
    """
    Converts the structured ATS analysis into a readable text report.
    """
    report = f"""
JOB APPLICATION AGENT - LOCAL ATS REPORT
========================================

MATCH SCORE:
{analysis["match_score"]}%

CV KEYWORDS:
{", ".join(analysis["cv_keywords"])}

JOB DESCRIPTION KEYWORDS:
{", ".join(analysis["job_keywords"])}

MATCHED KEYWORDS:
{", ".join(analysis["matched_keywords"]) if analysis["matched_keywords"] else "No matched keywords found."}

MISSING KEYWORDS:
{", ".join(analysis["missing_keywords"]) if analysis["missing_keywords"] else "No missing keywords found."}

RECOMMENDATIONS:
"""

    for recommendation in analysis["recommendations"]:
        report += f"- {recommendation}\n"

    report += """
IMPORTANT NOTE:
Do not add skills or experience that are not true.
Only include missing keywords if they reflect your real knowledge, coursework, or projects.
"""

    return report