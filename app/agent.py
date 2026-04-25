from app.skill_normalizer import compare_skill_sets, calculate_match_score


def analyze_application(cv_text: str, job_description_text: str) -> dict:
    """
    Analyze the match between a CV and a job description.

    The analysis focuses on relevant skills instead of generic keywords.
    This prevents unrelated words from lowering the final score.
    """
    comparison = compare_skill_sets(cv_text, job_description_text)
    scores = calculate_match_score(comparison)

    recommendations = generate_recommendations(comparison, scores)

    return {
        "scores": scores,
        "comparison": comparison,
        "recommendations": recommendations,
    }


def generate_recommendations(comparison: dict, scores: dict) -> list:
    """
    Generate practical recommendations based on missing skills.
    """
    recommendations = []

    missing_technical = comparison.get("missing_technical_skills", [])
    missing_soft = comparison.get("missing_soft_skills", [])
    final_score = scores.get("final_score", 0)

    if missing_technical:
        recommendations.append(
            "Consider adding relevant technical skills from the job description if you have real experience with them: "
            + ", ".join(missing_technical)
        )

    if missing_soft:
        recommendations.append(
            "Consider reflecting the following soft skills in your CV using real examples: "
            + ", ".join(missing_soft)
        )

    if final_score >= 80:
        recommendations.append(
            "The CV has a strong match with the job description. Focus on polishing wording and adding measurable achievements."
        )
    elif final_score >= 60:
        recommendations.append(
            "The CV has a reasonable match, but several important skills are missing or not clearly shown."
        )
    else:
        recommendations.append(
            "The CV has a low match for this role. Add only skills that truly reflect your experience and consider tailoring the CV more specifically to the job."
        )

    return recommendations