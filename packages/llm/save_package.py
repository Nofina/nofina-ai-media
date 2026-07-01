import json
from pathlib import Path


OUTPUT_DIR = Path("outputs/content_packages")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_content_package(package):

    filename = (
        package["title"]
        .replace("/", "-")
        .replace("\\", "-")
        .replace(":", "")
        .replace("?", "")
        .replace("*", "")
        .replace('"', "")
    )

    filepath = OUTPUT_DIR / f"{filename}.json"

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(
            package,
            f,
            ensure_ascii=False,
            indent=4
        )

    return filepath