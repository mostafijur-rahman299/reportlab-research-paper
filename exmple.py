from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15, title="Example PDF")

styles = getSampleStyleSheet()

content = []

# Paragraph with Left Alignment
para_style = ParagraphStyle(
            name='para',
            parent=styles['Normal'], 
            fontSize=20,
            textColor=colors.HexColor("#5e5b5b"),
            alignment=0, # Align Left
        )

paragraph = Paragraph("Hello World", para_style)
content.append(paragraph)

# Paragraph With Center Alignment
para_style = ParagraphStyle(
            name='para',
            parent=styles['title'], 
            fontSize=20,
            textColor=colors.HexColor("#5e5b5b"),
            alignment=1, # Align Center
        )

paragraph = Paragraph("Hello World", para_style)
content.append(paragraph)

# Paragraph With Right Alignment
para_style = ParagraphStyle(
            name='para',
            parent=styles['Heading2'], 
            fontSize=20,
            textColor=colors.HexColor("#5e5b5b"),
            alignment=2, # Align Center
        )

paragraph = Paragraph("Hello World", para_style)
content.append(paragraph)

# Paragraph With Right Alignment
para_style = ParagraphStyle(
            name='para',
            parent=styles['Heading2'], 
            fontSize=10,
            textColor=colors.HexColor("#5e5b5b"),
            alignment=0, # Align Center
            leading=8, # spacing between lines
            leftIndent=30,
            rightIndent=30,
            spaceAfter=10,
        )

paragraph = Paragraph("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used", para_style)
content.append(paragraph)


# Underline text
para_style = ParagraphStyle(
            name='para',
            parent=styles['Heading2'], 
            fontSize=20,
            textColor=colors.HexColor("#5e5b5b"),
            alignment=0, # Align Center
        )
underline_text = Paragraph(f'<u>Hey There</u>', para_style)
content.append(underline_text)

content.append(Spacer(1, 20)) # Give some space

# Images Inside Paragraph tag
para_image = Paragraph(f"<img src='images/phone-192.png' width='15' height='15' /> +8894847497  <img src='images/whatsapp-192.png' width='15' height='15' />  +19373973  <img src='images/email-50.png' width='15' height='15' />example@gmail.com")
content.append(para_image)

doc.build(content)
