from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from pathlib import Path

def text_to_pdf(text: str, output_path: Path):
    c = canvas.Canvas(str(output_path), pagesize=LETTER)
    width, height = LETTER

    y = height - 40
    for line in text.split("\n"):
        c.drawString(40, y, line)
        y -= 15

    c.save()

