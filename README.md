# ReportLab Research Paper

## Installation
```sh
pip install reportlab
```

## Example

### Paragraph Tag

A paragraph in ReportLab consists of one or more lines of text with consistent formatting. It can include various attributes such as font size, font family, alignment, indentation, and more. Paragraphs allow you to organize and format text content in your PDF documents, making it easier to generate professional-looking reports, documents, or other materials.

Here's a simple some of example of how you can create a paragraph using ReportLab:

```python
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
```
#### Output:
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/Screenshot%20from%202023-07-17%2013-55-31.png?raw=true)

### Image Tag

`Image` class to include images in PDF documents. The `Image` class allows to add various image formats, such as JPEG, PNG, GIF, and more, to PDFs.

Here's a simple example of how to use the `Image` class in ReportLab:

```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Table
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

# simple image tag
image = Image("images/ex-img.png", width=200, height=200)
content.append(image)

# giving some left margin
flowables = []
image2 = [Image("images/ex-img.png", width=200, height=200)]
left_margin = [Spacer(6.7*inch, 0)]
flowables.append(left_margin)
flowables.append(image2)
content.append(Table(flowables))

content.append(Spacer(1, 40))

# image with following perfect the original image ratio
desired_width = 200
desired_height = 200

img = ImageReader("images/ex-img.png")

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
image = Image("images/ex-img.png", width=width, height=height)
content.append(image)

doc.build(content)
```
#### Output:
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/ex-image-output.png?raw=true)

### Draw a Line

Here's an example of how to draw a line in ReportLab using Table:

```python
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

line = Table(
     [[""]],
     colWidths="100%",
     style=[("LINEABOVE", (0, 0), (-1, -1), 1, colors.red)],
)
content.append(line)

line = Table(
     [[""]],
     colWidths="50%",
     style=[("LINEABOVE", (0, 0), (-1, -1), 1, colors.red)],
)
content.append(line)

line = Table(
     [[""]],
     colWidths="80%",
     style=[("LINEABOVE", (0, 0), (-1, -1), 1, colors.red)],
)
content.append(line)

doc.build(content)
```
#### Output:
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/line.png?raw=true)

### Draw a Dotted line

Here's an example of how to draw a dotted line in ReportLab using Table:

```python
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

line = Table(
     [[""]],
     colWidths="100%",
     style=[("LINEABOVE", (0, 0), (-1, -1), 1, colors.red, 0.2, (0, 2, 1, 0))],
)
content.append(line)

line = Table(
     [[""]],
     colWidths="50%",
     style=[("LINEABOVE", (0, 0), (-1, -1), 1, colors.red, 0.2, (0, 2, 1, 0))],
)
content.append(line)

doc.build(content)
```
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/dotted-line.png?raw=true)

### Table

In ReportLab, we can create tables in PDF documents using the Table class. Tables are a powerful way to organize and display tabular data in a structured format. We can customize the appearance of the table, including cell borders, cell colors, text styles, and more.

Here's a basic example of how to create a table in ReportLab using the Table class:

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
    
    # (Style Name, (Start Row, Start Column), (End Row, End Column), Properties)
    
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
#### Output:
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/table-ex.png?raw=true)

### Adding Current Page Number in footer or header
```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.pagesizes import A4

doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

paragraph = Paragraph(" ")
content.append(paragraph)

content.append(PageBreak()) # Blank page for test purposes
content.append(PageBreak()) # Blank page for test purposes


def add_page_numbers(canvas, doc):
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Helvetica", 9)
    x_position = 500
    y_position = 800
    canvas.drawRightString(x_position, y_position, text)

doc.build(content, onFirstPage=add_page_numbers, onLaterPages=add_page_numbers)
```
#### Output:
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/footer-page-number.png?raw=true)


### Adding Current/Total Page Number in Footer or Header
```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from functools import partial
from reportlab.lib.units import inch
from reportlab.lib.units import mm


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
        
        
doc = SimpleDocTemplate("example.pdf", pagesize=A4, topMargin=0.5, leftMargin=15, rightMargin=15)

content = []

paragraph = Paragraph(" ")
content.append(paragraph)
content.append(PageBreak())
content.append(PageBreak())

doc.build(
  content,
  canvasmaker=partial(NumberedPage, adjusted_height=-21, adjusted_width=-78, 
  adjusted_caption='', xx_position=209, yy_position=627.5)
)
```
#### Output: 
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/footer-current-total-page-number.png?raw=true)

### Adding Same Header on each Page Of the PDF

```python
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
```
#### Output:
![Paragraph Example](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/loop-header.png?raw=true)

## Another More Examples

### Example 1:
![Example1](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/invoice-ex-1.png?raw=true)

Find out code [Here](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/real_example/invoice-1.py)

### Example 2:
![Example1](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/images/invoice-ex-2.png?raw=true)

Find out code [Here](https://github.com/mostafijur-rahman299/reportlab-research-paper/blob/master/real_example/invoice2.py)
