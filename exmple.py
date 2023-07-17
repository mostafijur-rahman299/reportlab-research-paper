from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.pagesizes import A4

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

paragraph = Paragraph(" ")
content.append(paragraph)

content.append(PageBreak())
content.append(PageBreak())


def add_page_numbers(canvas, doc):
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(200, 20, text)

doc.build(content, onFirstPage=add_page_numbers, onLaterPages=add_page_numbers)
