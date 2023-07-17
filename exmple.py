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


