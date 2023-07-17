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

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15, title="Example PDF")

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
### Draw a Line
```python
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.graphics.shapes import Line

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

line = Table(
     [[""]],
     colWidths="100%",
     style=[("LINEABOVE", (0, 0), (-1, -1), 1, colors.red)],
)
content.append(line)

doc.build(content)
```
### Draw a Dotted line
```python
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.graphics.shapes import Line

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

line = Table(
     [[""]],
     colWidths="100%",
     style=[("LINEABOVE", (0, 0), (-1, -1), 1, colors.red)],
)
content.append(line)

doc.build(content)
```

### Table
```python
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

data = [
    ['Dedicated Hosting', 'VPS Hosting', 'Sharing Hosting', 'Memory Management'],
    ['$200/Month', '$100/Month', '20/Month'],
    ['Free Domain', 'Free Domain', 'Free Domain'],
    ['2GB DDR2', '20 GB Disc Space', 'Unlimited Disc Space'],
]

table = Table(data)

style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.green),
    ('TEXTCOLOR', (0,0), (3,0), colors.whitesmoke),
    
    ('ALIGN', (0,1), (-1,-1), 'CENTER'),
    
    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    
    ('FONTSIZE', (0,0), (-1,0), 14),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
])
table.setStyle(style)

# Alternate colors
for i in range(1, len(data)):
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige
        
    ts = TableStyle([
        ('BACKGROUND', (0, i), (-1, i), bc)
    ])
    
    table.setStyle(ts)
    
# Add borders
ts = TableStyle([
    ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ('LINEBEFORE', (2, 1), (2, -1), 1, colors.black),
    ('LINEAFTER', (2, 1), (2, -1), 1, colors.black),
    ('LINEABOVE', (2, 1), (2, -1), 1, colors.red),
    ('GRID', (0, 1), (-1, -1), 1, colors.green),
])


table.setStyle(ts)

content.append(table)

doc.build(content)
```
### Adding Current Page Number in footer or header
```python
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

paragraph = Paragraph("Page Number In Footer")
content.append(paragraph)

def add_page_numbers(canvas, doc):
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(200, 20, text)

doc.build(content, onFirstPage=page_number_update, onLaterPages=page_number_update)
```
### Adding Current/Total Page Number in Footer or Header
```python
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from functools import partial

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

paragraph = Paragraph("Page Number In Footer")
content.append(paragraph)

doc.build(
  content,
  canvasmaker=partial(NumberedPage, adjusted_height=-21, adjusted_width=-78, 
  adjusted_caption='', xx_position=209, yy_position=627.5)
)

class NumberedPage(canvas.Canvas):
    _adjusted_height = 0
    _adjusted_width = 0
    _adjusted_caption = ''

    def __init__(self,  *args, **kwargs):
        self._adjusted_height = kwargs.pop('adjusted_height', 0)
        self._adjusted_width = kwargs.pop('adjusted_width', 0)
        self._adjusted_caption = kwargs.pop('adjusted_caption', '')
        self.xx_position = kwargs.pop('xx_position',0)
        self.yy_position = kwargs.pop('yy_position', 0)
        self.x_position = kwargs.pop('x_position', self.xx_position * mm - 35 + self._adjusted_width)
        self.y_position = kwargs.pop('y_position', 15 * mm + (0.2 * inch) + self.yy_position + self._adjusted_height)
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.setFillColor(colors.black)
        self.drawRightString(self.x_position, self.y_position, self._adjusted_caption + "%d/%d" % (self._pageNumber, page_count))
  
```