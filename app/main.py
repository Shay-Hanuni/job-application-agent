import os
import argparse
from app.agent import create_ats_analysis, create_text_report
from app.report_writer import save_text_report, save_json_report


def read_file(path: str) -> str:
    """
    Reads a text file and returns its content.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def parse_arguments():
    """
    Defines and reads command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Job Application Agent - Analyze a CV against a job description."
    )

    parser.add_argument(
        "--cv",
        default="data/cv.txt",
        help="Path to the CV text file. Default: data/cv.txt"
    )

    parser.add_argument(
        "--job",
        default="data/job_description.txt",
        help="Path to the job description text file. Default: data/job_description.txt"
    )

    parser.add_argument(
        "--output",
        default="outputs/report",
        help="Output path without extension. Default: outputs/report"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    cv_text = read_file(args.cv)
    job_text = read_file(args.job)

    analysis = create_ats_analysis(cv_text, job_text)
    text_report = create_text_report(analysis)

    print(text_report)

    txt_output_path = f"{args.output}.txt"
    json_output_path = f"{args.output}.json"

    save_text_report(text_report, txt_output_path)
    save_json_report(analysis, json_output_path)

    print("\nReports saved successfully:")
    print(f"- {txt_output_path}")
    print(f"- {json_output_path}")


if __name__ == "__main__":
    main()