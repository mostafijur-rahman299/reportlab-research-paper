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