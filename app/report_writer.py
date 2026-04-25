import os


def write_report(analysis_result: dict, output_path: str) -> None:
    """
    Write the analysis result into a readable text report.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    scores = analysis_result.get("scores", {})
    comparison = analysis_result.get("comparison", {})
    recommendations = analysis_result.get("recommendations", [])

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("JOB APPLICATION ANALYSIS REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write("MATCH SCORES\n")
        file.write("-" * 40 + "\n")
        file.write(f"Final Score: {scores.get('final_score', 0)}%\n")
        file.write(f"Technical Skills Score: {scores.get('technical_score', 0)}%\n")
        file.write(f"Soft Skills Score: {scores.get('soft_score', 0)}%\n\n")

        file.write("MATCHED TECHNICAL SKILLS\n")
        file.write("-" * 40 + "\n")
        write_list(file, comparison.get("matched_technical_skills", []))

        file.write("\nMISSING TECHNICAL SKILLS\n")
        file.write("-" * 40 + "\n")
        write_list(file, comparison.get("missing_technical_skills", []))

        file.write("\nMATCHED SOFT SKILLS\n")
        file.write("-" * 40 + "\n")
        write_list(file, comparison.get("matched_soft_skills", []))

        file.write("\nMISSING SOFT SKILLS\n")
        file.write("-" * 40 + "\n")
        write_list(file, comparison.get("missing_soft_skills", []))

        file.write("\nRECOMMENDATIONS\n")
        file.write("-" * 40 + "\n")
        write_list(file, recommendations)


def write_list(file, items: list) -> None:
    """
    Write a list of items into the report.
    """
    if not items:
        file.write("- None\n")
        return

    for item in items:
        file.write(f"- {item}\n")