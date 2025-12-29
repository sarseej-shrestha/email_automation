from pathlib import Path
from email_parser import load_emails
from pdf_converter import text_to_pdf
from file_router import route_file

EMAIL_DIR = "input_emails"

def run():
    emails = load_emails(EMAIL_DIR)

    for email in emails:
        for attachment in email["attachments"]:
            output_dir = route_file(email["subject"])
            pdf_name = attachment["filename"].replace(".txt", ".pdf")
            output_path = output_dir / pdf_name

            text_to_pdf(attachment["content"], output_path)
            print(f"Processed: {output_path}")

if __name__ == "__main__":
    run()

