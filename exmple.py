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
