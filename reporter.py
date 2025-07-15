import os
import sqlite3
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# определяем путь к установленному шрифту
FONT_PATH = os.path.join("app", "static", "fonts", "DejaVuSans.ttf")
pdfmetrics.registerFont(TTFont('DejaVuSans', FONT_PATH))

DB_PATH = "history.db"
REPORT_DIR = os.path.join("app", "static", "reports")
os.makedirs(REPORT_DIR, exist_ok=True)

def generate_pdf_report():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT timestamp, filename, count FROM requests ORDER BY timestamp"
    ).fetchall()
    conn.close()

    pdf_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(REPORT_DIR, pdf_name)

    c = canvas.Canvas(pdf_path, pagesize=A4)
    w, h = A4
    c.setFont('DejaVuSans', 16)
    c.drawString(100, h - 50, "Отчёт по учёту жирафов")

    c.setFont('DejaVuSans', 12)
    y = h - 90
    c.drawString(60, y, "Дата")
    c.drawString(200, y, "Файл")
    c.drawString(400, y, "Кол-во")
    y -= 20
    for ts, name, cnt in rows:
        c.drawString(60, y, ts[:19])
        c.drawString(200, y, str(name))
        c.drawString(400, y, str(cnt))
        y -= 15
        if y < 100:
            c.showPage()
            y = h - 90
    c.save()
    return pdf_path