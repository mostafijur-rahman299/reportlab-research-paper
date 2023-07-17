# ReportLab Research Paper

## Installation
```sh
pip install reportlab
```

## Example

### Paragraph Tag
```python
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

# Paragraph
para_style = ParagraphStyle(
            name='para',
            parent=self.styles['Normal'], # Type of text has more parent like "title", "Heading5" etc..
            fontSize=28,
            textColor=colors.HexColor("#5e5b5b"),
            alignment=1,  # It's vairation like 0,1 and 2. 0=Left, 1=Center, 2=Right
            leftIndent=10,
            rightIndent=15,
            spaceAfter=10,
            leading=10, # space between two line of text
        )

paragraph = Paragraph("Hello World", para_style)
content.append(paragraph)

# Underline text
underline_text = Paragraph(f'<u>Hey Therer, </u>')
content.append(underline_text)

# Images Inside Paragraph tag
para_image = Paragraph(f"<img src='phone-192.png' width='15' height='15' /> +8894847497  <img src='whatsapp-192.png' width='15' height='15' />  +19373973  <img src='email-50.png' width='15' height='15' />example@gmail.com")
content.append(para_image)

doc.build(content)
```
For more on paragraph checkout [docs](https://docs.reportlab.com/reportlab/userguide/ch6_paragraphs)

### Adding Custom Fonts
```python
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

# Download your desired font and replace font_path1 and font_path2 variable with your actual downloaded paths
font_path1 = 'static/fonts/microsoft-yahei/msyhbd.ttc'
font_path2 = 'static/fonts/microsoft-yahei/chinese.msyh.ttf'

pdfmetrics.registerFont(TTFont('MSYTC-Bold', font_path1))
pdfmetrics.registerFont(TTFont('MSYTC-Regular', font_path2))

content = []

# Paragraph
para_style = ParagraphStyle(
            name='para',
            parent=self.styles['Normal']
            fontSize=28,
            fontName='MSYTC-Regular',
        )
paragraph = Paragraph("Hello World", para_style)
content.append(paragraph)

doc.build(content)
```

### Image Tag
```python
from reportlab.platypus import SimpleDocTemplate, Image, Spacer
from reportlab.lib.units import inch

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

# simple image tag
image = Image(path_of_image, width=450, height=250)
content.append(image)

# giving some left margin
image2 = Image(path_of_image, width=450, height=250)
left_margin = [Spacer(6.7*inch, 0)]
content.append(left_margin)
content.append(image2)

# image with following perfect the original image ratio
desired_width = 280
desired_height = 250

img = ImageReader(attachment_path)

width, height = img.getSize()
aspect_ratio = width / height

# Adjust width and height to maintain aspect ratio
if aspect_ratio > 1:
    width = desired_width
    height = int(desired_width / aspect_ratio)
else:
    width = int(desired_height * aspect_ratio)
    height = desired_height

# Create an Image object with adjusted width and height
image = Image(attachment_path, width=width, height=height)
content.append(image)

doc.build(content)
```