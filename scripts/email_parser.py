import json
from pathlib import Path

def load_emails(email_dir: str):
    emails = []
    for file in Path("../input").glob("*.json"):
        with open(file, "r") as f:
            emails.append(json.load(f))
    return emails

