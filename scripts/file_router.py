from pathlib import Path
from datetime import datetime

def route_file(subject: str):
    year = datetime.now().year

    if "invoice" in subject.lower():
        category = "Invoices"
    else:
        category = "General"

    base_path = Path("processed_pdfs") / str(year) / category
    base_path.mkdir(parents=True, exist_ok=True)

    return base_path

