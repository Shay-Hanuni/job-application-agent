import os
import json


def save_text_report(report: str, path: str) -> None:
    """
    Saves the readable text report into a TXT file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write(report)


def save_json_report(data: dict, path: str) -> None:
    """
    Saves the structured analysis into a JSON file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)