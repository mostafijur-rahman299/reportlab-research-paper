from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing, Line
from functools import partial
from reportlab.lib.units import *
doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

paragraph = Paragraph(" ")
content.append(paragraph)

content.append(PageBreak())
content.append(PageBreak())

def top_header(shop_name, primary_color, reg_number, address1="", address2="", phone_number="", whatsapp_number="", email=""):
        
        header_template = []
        styles = getSampleStyleSheet()
        
        header_style = ParagraphStyle(
            name='Header',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.black,
            leading=8,
            
        )

        subheader_style = ParagraphStyle(
            name='Subheader',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leading=6,
        )
        
        header = [
                Paragraph(shop_name, header_style),
                Spacer(1, 5),
                Paragraph(f"Reg.No: ({reg_number})", subheader_style),
                Spacer(1, 6),
                Paragraph(address1, subheader_style),
                Spacer(1, 6),
                Paragraph(address2, subheader_style),
            ]

        data = [[header]]
        table = Table(data, colWidths=[535])

        # Set table styles
        table.setStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), colors.white),
                ("TEXTCOLOR", (0, 0), (0, 0), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("LEFTPADDING", (0, 0), (-1, -1), 1.2*inch),
            ]
        )

        header_text = [
            [table],
        ]

        header_table = Table(header_text)

        center_table = Table([[header_table]], style=[('ALIGN', (0, 0), (-1, -1), 'CENTER')])
        header_template.append(center_table)
        return header_template   
        

def header(canvas, doc):
    # Save the state of our canvas so we can draw on it
    canvas.saveState()
    
    _header = top_header("AK Group & Industries", colors.red, "89484904849JH9479", "Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678", "Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678", "+9849484049", "+049484943", "example@gmail.com")
    
    for tph in _header:
        w, h = tph.wrap(doc.width, doc.topMargin)
        tph.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h + 25)
    
    def draw_line(margin, width="", color=colors.black):
        # Calculate the margin bottom for the header
        margin_bottom = doc.topMargin - h + margin
        
        width = doc.width
        if width:
            width = width
        
        # Create a drawing and add a line at the bottom of the header
        drawing = Drawing(width, 0.1)
        line = Line(0, 0, width, 0)
        line.strokeColor = color
        line.strokeWidth = 0.1
        drawing.add(line)
        
        # Draw the line at the bottom of the header
        drawing.drawOn(canvas, doc.leftMargin, margin_bottom)
        
    draw_line(margin=790)

doc.build(
  content,
  onFirstPage=partial(header),
  onLaterPages=partial(header)
)
