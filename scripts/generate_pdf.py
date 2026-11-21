#!/usr/bin/env python3
"""Build a printable A4 PDF from the reviewed CSV vocabulary files."""
import csv
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "english_ukrainian_dictionary.pdf"
LEVELS = [
    ("a0", "A0 — Початковий фундамент"),
    ("a1", "A1 — Початковий рівень"),
    ("a2", "A2 — Елементарний рівень"),
    ("b1", "B1 — Середній рівень"),
    ("b2", "B2 — Вище середнього"),
]


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(18 * mm, 12 * mm, "English–Ukrainian Dictionary · British English")
    canvas.drawRightString(A4[0] - 18 * mm, 12 * mm, str(doc.page))
    canvas.restoreState()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Word", parent=styles["BodyText"], leading=14, spaceAfter=4))
    styles.add(ParagraphStyle(name="LevelTitle", parent=styles["Heading1"], textColor=colors.HexColor("#243B53")))
    story = [
        Paragraph("English–Ukrainian Dictionary", styles["Title"]),
        Paragraph("British English · A0–B2", styles["Heading2"]),
        Paragraph("Навчальний словник британської англійської мови", styles["BodyText"]),
        Spacer(1, 8 * mm),
        Paragraph("Зміст", styles["Heading1"]),
    ]
    for _, title in LEVELS:
        story.append(Paragraph(escape(title), styles["BodyText"]))
    story.append(PageBreak())
    total = 0
    for folder, title in LEVELS:
        path = ROOT / "data" / folder / "words.csv"
        with path.open(encoding="utf-8-sig", newline="") as stream:
            entries = list(csv.DictReader(stream))
        story.append(Paragraph(escape(title), styles["LevelTitle"]))
        if not entries:
            story.append(Paragraph("Розділ ще не заповнений.", styles["BodyText"]))
        for row in entries:
            total += 1
            block = [
                Paragraph(f"<b>{escape(row['id'])}. {escape(row['headword'])}</b>  {escape(row['ipa_uk'])}", styles["Word"]),
                Paragraph(f"<b>Переклад:</b> {escape(row['ukrainian_translation'])} · <b>Частина мови:</b> {escape(row['part_of_speech'])}", styles["BodyText"]),
                Paragraph(f"<b>Приклад:</b> {escape(row['example_en'])}", styles["BodyText"]),
                Paragraph(f"<b>Переклад:</b> {escape(row['example_uk'])}", styles["BodyText"]),
                Paragraph(f"<font color='#666666'>Категорія: {escape(row['category'])} · Статус: {escape(row['verification_status'])}</font>", styles["BodyText"]),
                Spacer(1, 4 * mm),
            ]
            story.append(KeepTogether(block))
        story.append(PageBreak())
    if total == 0:
        story.append(Paragraph("Словник поки не містить лексичних записів. Додайте перевірені записи до папок data/.", styles["BodyText"]))
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
                            topMargin=18*mm, bottomMargin=20*mm, title="English–Ukrainian Dictionary")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Created {OUTPUT} with {total} vocabulary entries.")


if __name__ == "__main__":
    main()
