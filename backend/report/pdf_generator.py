from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(
    language,
    code,
    explanation,
    review,
    bugs,
    optimization,
    complexity
):

    os.makedirs("reports", exist_ok=True)

    filename = "reports/code_analysis_report.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("AI Code Explainer & Reviewer", styles["Title"]))

    story.append(Paragraph(f"<b>Language:</b> {language}", styles["Heading2"]))

    story.append(Paragraph("<b>Source Code</b>", styles["Heading2"]))
    story.append(Paragraph(code.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<b>Explanation</b>", styles["Heading2"]))
    story.append(Paragraph(explanation, styles["BodyText"]))

    story.append(Paragraph("<b>Code Review</b>", styles["Heading2"]))
    story.append(Paragraph(review, styles["BodyText"]))

    story.append(Paragraph("<b>Bugs</b>", styles["Heading2"]))
    story.append(Paragraph(bugs, styles["BodyText"]))

    story.append(Paragraph("<b>Optimization</b>", styles["Heading2"]))
    story.append(Paragraph(optimization, styles["BodyText"]))

    story.append(Paragraph("<b>Complexity</b>", styles["Heading2"]))
    story.append(Paragraph(complexity, styles["BodyText"]))

    doc.build(story)

    return filename