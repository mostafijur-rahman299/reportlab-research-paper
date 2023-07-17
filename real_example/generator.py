import requests
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph, TableStyle, Image, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Line
from functools import partial
from reportlab.lib.units import *
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def is_image_readable(file_path):
    try:
        Image.open(requests.get(file_path, stream=True).raw)
        return True
    except Exception as e:
        return False

class GenerateInvoicePDF:
    def __init__(self, filename, pdf_type="Company_invoice", title="Labeau Invoice"):
        self.filepath = "invoice-pdfs"
        
        if pdf_type == "company_invoice":
            self.doc = SimpleDocTemplate(
                        f"{self.filepath}/{filename}", 
                        rightMargin=15,
                        leftMargin=15,
                        topMargin=235,
                        bottomMargin=35,
                        pageSize=A4,
                        title=title
                    )
        elif pdf_type == "shop_invoice":
            self.doc = SimpleDocTemplate(
                        f"{self.filepath}/{filename}", 
                        rightMargin=15,
                        leftMargin=15,
                        topMargin=180,
                        bottomMargin=35,
                        pageSize=A4,
                        title=title
                    )
        else:
            self.doc = SimpleDocTemplate(
                        f"{self.filepath}/{filename}", 
                        rightMargin=15,
                        leftMargin=15,
                        topMargin=240,
                        bottomMargin=35,
                        pageSize=A4,
                        title=title
                    )
            
        self.story = []
        self.styles = getSampleStyleSheet()
        self.primary_color = colors.black
        
        pdfmetrics.registerFont(TTFont('MSYTC-Bold', 'fonts/microsoft-yahei/msyhbd.ttc'))
        pdfmetrics.registerFont(TTFont('MSYTC-Regular', 'fonts/microsoft-yahei/chinese.msyh.ttf'))    

    @staticmethod
    def top_header(shop_name, shop_logo_url, primary_color, reg_number, address1="", address2="", phone_number="", whatsapp_number="", email=""):
        
        header_template = []
        styles = getSampleStyleSheet()
        
        header_style = ParagraphStyle(
            name='Header',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.black,
            fontName='MSYTC-Bold',
            leading=8,
            
        )

        subheader_style = ParagraphStyle(
            name='Subheader',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            fontName='MSYTC-Regular',
            leading=6,
        )
        
        custom_style = ParagraphStyle(
            name='CustomStyle',
            fontSize=8,
            fontName='MSYTC-Regular',
            textColor=primary_color,
        )
                        
        if is_image_readable(shop_logo_url):
            image = Image(shop_logo_url, width=170, height=45)
        else:
            image = []
        
        header = [
                Paragraph(shop_name, header_style),
                Spacer(1, 5),
                Paragraph(f"Reg.No: ({reg_number})", subheader_style),
                Spacer(1, 6),
                Paragraph(address1, subheader_style),
                Spacer(1, 6),
                Paragraph(address2, subheader_style),
                Spacer(1, 6),
                Paragraph(
                    f"<img src='images/phone-192.png' width='8' height='8' /> {phone_number}  <img src='images/whatsapp-192.png' width='8' height='8' />  {whatsapp_number}  <img src='images/email-50.png' width='8' height='8' /> {email}", custom_style
                )
            ]

        data = [[image, header]]
        table = Table(data, colWidths=[135, None])

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
        
    @staticmethod
    def company_invoice_header(primary_color, company_name="", company_address="", invoice_no="", DO_No="", PO_No="", invoice_date="", handled_by="", payment_term="", telephone_no="", email=""):
        
        template_data = []
        styles = getSampleStyleSheet()
        
        # Center align Header
        centered_style = ParagraphStyle(
            name='Centered',
            parent=styles['title'],
            fontSize=18,
            textColor=colors.black,
            alignment=1,  # Center align the content
            fontName='MSYTC-Bold',
            leading=10,
        )
        
        centered_invoice_header = Paragraph("Invoice", centered_style)
        header_table = Table([[centered_invoice_header]], colWidths=[705], rowHeights=-15)
        template_data.append(header_table)
        template_data.append(Spacer(1, 4*inch))
        
        styles = getSampleStyleSheet()

        # Custom styles
        left_col_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=10,
            textColor=primary_color,
            leftIndent=0.9 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=7
        )
        tell_col_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=10,
            textColor=primary_color,
            leftIndent=0.9 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=7,
            spaceBefore=30*inch
        )

        left_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=9,
            textColor=primary_color,
            leftIndent=-0.95 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=7
        )

        left_col_username = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.black,
            rightIndent=3*inch,
            leftIndent=-3.45*inch,
            fontName='MSYTC-Bold',
            leading=7
        )
        left_col_value = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=9,
            textColor=primary_color,
            rightIndent=3*inch,
            leftIndent=-3.45*inch,
            fontName='MSYTC-Regular',
            leading=7
        )
        left_col_value_company_address = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=9,
            textColor=primary_color,
            rightIndent=3*inch,
            leftIndent=-3.45*inch,
            fontName='MSYTC-Regular',
            leading=11
        )

        right_col_style = ParagraphStyle(
            name='RightColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leftIndent=6.2*inch,
            fontName='MSYTC-Regular',
            leading=6,
        )

        right_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leftIndent=-0.9 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=6
        )

        right_col_val_style = ParagraphStyle(
            name='RightColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leftIndent=-1 * inch,
            fontName='MSYTC-Regular',
            leading=6
        )

        data = [
            [
                Paragraph('Invoice No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(invoice_no, right_col_val_style),
            ],
            [
                Paragraph('D/O No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(DO_No, right_col_val_style),
            ],
            [
                Paragraph('P/O No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(PO_No, right_col_val_style),
            ],
            [
                Paragraph('Invoice Date', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(invoice_date, right_col_val_style),
            ],
            [
                Paragraph('Handled By', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(handled_by, right_col_val_style),
            ],
            [
                Paragraph('Payment Term', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(payment_term, right_col_val_style),
            ],
            [
                Paragraph('Page No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph('', right_col_val_style),
            ],
        ]

        col_widths = [8 * inch, 0.2 * inch, 2.5 * inch]

        table = Table(data, colWidths=col_widths, hAlign='RIGHT')

        # Enable word wrapping for the content
        table.setStyle(TableStyle([
            ('WORDWRAP', (0, 0), (-1, -1), True),
        ]))

        template_data.append(table)
                
        company_address = company_address[:250] + "..." if company_address and len(company_address) >= 250 else company_address
                
        data = [
            [
                Paragraph('Invoice To', left_col_style),
                Paragraph(':', left_colon_style),
                Paragraph(company_name, left_col_username)
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph(company_address, left_col_value_company_address),
            ],
            [
                Paragraph('Tel', tell_col_style),
                Paragraph(':', left_colon_style),
                Paragraph(telephone_no, left_col_value),
            ],
            [
                Paragraph('Email', left_col_style),
                Paragraph(':', left_colon_style),
                Paragraph(email, left_col_value),
            ],
        ]
                
        if not company_address:
            data.insert(2, [])
            data.insert(2, [])
            data.insert(2, [])
            data.insert(2, [])
        elif len(company_address) <= 100:
            data.insert(2, [])
            data.insert(2, [])
            data.insert(2, [])
        elif len(company_address) <= 200:
            data.insert(2, [])
            
        table = Table(data, hAlign='LEFT')

        # Enable word wrapping for the content
        table.setStyle(TableStyle([
            ('WORDWRAP', (0, 0), (-1, -1), True),
        ]))

        template_data.append(table)
        
        return template_data
        
    @staticmethod
    def shop_invoice_header(primary_color, invoice_to="", invoice_no="", invoice_date="", handled_by="", telephone_no="", email="", issued_time=""):
        
        header_template = []
        styles = getSampleStyleSheet()
        
        # Center align Header
        centered_style = ParagraphStyle(
            name='Centered',
            parent=styles['title'],
            fontSize=18,
            textColor=colors.black,
            alignment=1,  # Center align the content
            fontName='MSYTC-Bold',
            leading=10
        )
        
        centered_invoice_header = Paragraph("Invoice", centered_style)
        header_table = Table([[centered_invoice_header]], colWidths=[705], rowHeights=-10)
        header_template.append(header_table)
        
        styles = getSampleStyleSheet()

        # Custom styles
        left_col_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leftIndent=0.9 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=7
        )
        left_col_value = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leftIndent=-1.6 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=7
        )
        left_col_username = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leftIndent=-1.6 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=7
        )

        right_col_style = ParagraphStyle(
            name='RightColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            rightIndent=0,  # Align lines to the end
            alignment=0,  # Right align the content
            leftIndent=1*inch,
            fontName='MSYTC-Regular',
            leading=6
        )

        right_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            leftIndent=-0.3 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=6
        )

        right_col_val_style = ParagraphStyle(
            name='RightColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=primary_color,
            rightIndent=0,  # Align lines to the end
            alignment=0,  # Right align the content
            leftIndent=-0.4 * inch,
            fontName='MSYTC-Regular',
            leading=6
        )


        data = [
            [
                Paragraph("<img src='images/top-account.png' width='10' height='10' />", left_col_style),
                Paragraph(''),
                Paragraph(f'{invoice_to}', left_col_username),
                Paragraph('Invoice No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(invoice_no, right_col_val_style),
            ],
            [
                Paragraph("<img src='images/whatsapp-192.png' width='10' height='10' />", left_col_style),
                Paragraph(''),
                Paragraph(f'{telephone_no}', left_col_value),
                Paragraph('Invoice Date', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(invoice_date, right_col_val_style),
            ],
            [
                Paragraph("<img src='images/email-50.png' width='10' height='10' />", left_col_style),
                Paragraph(''),
                Paragraph(f'{email}', left_col_value),
                Paragraph('Issued Time', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(issued_time, right_col_val_style),
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph('',),
                Paragraph('Handled By', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph(handled_by, right_col_val_style),
            ],
            [
                Paragraph(''),
                Paragraph('',),
                Paragraph('',),
                Paragraph('Page No.', right_col_style),
                Paragraph(':', right_colon_style),
                Paragraph('', right_col_val_style),
            ],
        ]

        col_widths = [2.5 * inch, 0.2 * inch, 2.5 * inch, 2.2 * inch, 0.2 * inch, 2.1 * inch]

        table = Table(data, colWidths=col_widths)

        # Enable word wrapping for the content
        table.setStyle(TableStyle([
            ('WORDWRAP', (0, 0), (-1, -1), True),
        ]))

        header_template.append(table)
        return header_template
              
    @staticmethod
    def company_header(canvas, doc, data, primary_color):
        
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        
        top_header = GenerateInvoicePDF.top_header(data.get("shop_name", ""), data.get("shop_logo", ""), primary_color, data.get("registration_no", ""), data.get("address1", ""), data.get("address2", ""), data.get("phone_number", ""), data.get("whatsapp_number", ""), data.get("email", ""))
        
        for tph in top_header:
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
            
        draw_line(margin=600)        
        
        company_header = GenerateInvoicePDF.company_invoice_header(primary_color, data.get("company_name", ""), data.get("company_address", ""), data.get("invoice_no", ""), data.get("DO_No", ""), data.get("PO_No", ""), data.get("invoice_date", ""), data.get("handled_by", ""), data.get("payment_term", ""), data.get("telephone_no", ""), data.get("member_email", ""))
        
        for cph in company_header:
            w, h = cph.wrap(doc.width, doc.topMargin)
            cph.drawOn(canvas, doc.leftMargin - 70, doc.height + doc.topMargin - h - 80)
                            
        draw_line(margin=480)
        
        # Release the canvas
        canvas.restoreState()
        
    @staticmethod
    def shop_header(canvas, doc, data, primary_color):
        
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        
        top_header = GenerateInvoicePDF.top_header(data.get("shop_name", ""), data.get("shop_logo", ""), primary_color, data.get("registration_no", ""), data.get("address1", ""), data.get("address2", ""), data.get("phone_number", ""), data.get("whatsapp_number", ""), data.get("email", ""))
        
        for tph in top_header:
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
            
        draw_line(margin=600)
        
        shop_header = GenerateInvoicePDF.shop_invoice_header(primary_color, data.get("invoice_to", ""), data.get("invoice_no", ""), data.get("invoice_date", ""), data.get("handled_by", ""), data.get("telephone_no", ""), data.get("member_email", ""), data.get("issued_time", "-"))
        
        for cph in shop_header:
            w, h = cph.wrap(doc.width, doc.topMargin)
            cph.drawOn(canvas, doc.leftMargin - 70, doc.height + doc.topMargin - h - 80)
            
        draw_line(margin=415)
        
        # Release the canvas
        canvas.restoreState()
                 
    def line_separator(self, width, thickness):
        # Line separator
        line = Table(
            [[""]],
            colWidths=width,
            style=[("LINEABOVE", (0, 0), (-1, -1), thickness, self.primary_color)],
        )
        self.story.append(line)

    def company_invoice_table(self, invoice_data, subtotal, discount, total, payment, balance, rounding, payment_list):
        
        wrap_style_val = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=0,
            fontName='MSYTC-Regular',
            leading=7
        )
        wrap_style_val_rtl = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=2,
            fontName='MSYTC-Regular',
            leading=7,
            rightIndent=5
        )
        wrap_style_price = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=2,
            fontName='MSYTC-Regular',
            leading=7,
            rightIndent=0.5 * inch
        )
        wrap_style_title = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            fontName='MSYTC-Bold',
            leading=7
        )
        wrap_style_title_rtl = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            fontName='MSYTC-Bold',
            leading=7,
            alignment=2,
            rightIndent=5
        )
        wrap_style_title_price = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            fontName='MSYTC-Bold',
            leading=7,
            alignment=2,
            rightIndent=0.5 * inch
        )
        
        styles = getSampleStyleSheet()

        wrap_style_val_bold = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=0,
            fontName='MSYTC-Bold',
            leading=2
        )
        package_title_col_style = ParagraphStyle(
            name='LeftColumn',
            parent=styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            fontName='MSYTC-Regular',
            leading=4
        )

        wrapped_data = []
        counter = 1
        for row in invoice_data:
            
            wrapped_row = []
            wrapped_row.append(Paragraph(str(counter), wrap_style_val))
            
            if row.get("subname", ""):
                name_with_help_text = f'<font name="MSYTC-Regular" size="8"> ({row.get("subname", "")}) </font> <font name="MSYTC-Regular"> {row.get("name", "")} </font>'
            elif row.get("key", "") == "outstanding_inv":
                name_with_help_text = f'<font name="MSYTC-Regular"><u>{row.get("name", "")}</u></font>'
            else:
                name_with_help_text = f'<font name="MSYTC-Regular"> {row.get("name", "")} </font>'
                
            wrapped_row.append(Paragraph(name_with_help_text, wrap_style_val))
            
            wrapped_row.append(Paragraph(str(row.get("unit_price", 0.00)), wrap_style_val_rtl))
            wrapped_row.append(Paragraph(str(row.get("quantity", 1)), wrap_style_val_rtl))
            wrapped_row.append(Paragraph(str(row.get("price", 1)), wrap_style_price))
            
            # Package detail for package type item
            package_detail_title = []
            package_details_title = []
            if row.get("key", "") == "package" and len(row.get("package_detail", [])) > 0:
                package_detail_title.append(Paragraph(""))
                package_detail_title.append(Paragraph("Package Detail:", wrap_style_val_bold))
                package_detail_title.append(Paragraph(""))
                package_detail_title.append(Paragraph(""))
                package_detail_title.append(Paragraph(""))
                
                for package in row.get("package_detail", []):
                    package_title = []
                    package_title.append(Paragraph(""))
                    
                    package_title.append(Paragraph(f'<para leftIndent="10"><font name="MSYTC-Regular"> - {package.get("name")} </font> <font name="MSYTC-Bold">x {package.get("quantity", "")}</font></para>', package_title_col_style))
                    
                    package_title.append(Spacer(1, -20*inch))
                    package_title.append(Paragraph(""))
                    package_title.append(Paragraph(""))
                    
                    package_details_title.append(package_title)
                                                
            # append remark, discount and credit
            additional_remark_row = []
            if row.get("remark", ""):
                additional_remark_row.append(Paragraph(""))
                additional_remark_row.append([Paragraph(row.get("remark", ""), wrap_style_val)])
                additional_remark_row.append(Paragraph(""))
                additional_remark_row.append(Paragraph(""))
                additional_remark_row.append(Paragraph(""))
            
            additional_discount_row = []
            if row.get("discount", 0.00):
                additional_discount_row.append(Paragraph(""))
                additional_discount_row.append(Paragraph(""))
                additional_discount_row.append(Paragraph(""))
                additional_discount_row.append(Paragraph("Discount", wrap_style_val_rtl))
                additional_discount_row.append(Paragraph(f"-{row.get('discount', 0.00)}", wrap_style_price))
                
            additional_credit_row = []
            if row.get('credit_applied', '0.00'):
                additional_credit_row.append(Paragraph(""))
                additional_credit_row.append(Paragraph(""))
                additional_credit_row.append(Paragraph(""))
                additional_credit_row.append(Paragraph("Credit", wrap_style_val_rtl))
                additional_credit_row.append(Paragraph(f"-{row.get('credit_applied', '0.00')}", wrap_style_price))
            
            wrapped_data.append(wrapped_row)
            
            if additional_discount_row:
                wrapped_data.append(additional_discount_row)
            if additional_credit_row:
                wrapped_data.append(additional_credit_row)
                
            if package_detail_title:
                wrapped_data.append(package_detail_title)
            if package_details_title:
                for package_detail in package_details_title:
                    wrapped_data.append(package_detail)
                    
            if additional_remark_row:
                wrapped_data.append(additional_remark_row)
            
            counter += 1
        
        
        wrapped_header = []
        for index, cell in enumerate(['No.', 'Description', 'Unit Price', 'Quantity', 'Price']):
            if index in [0, 1]:
                wrapped_header.append(Paragraph(cell, wrap_style_title))
            elif index == 4:
                wrapped_header.append(Paragraph(cell, wrap_style_title_price))
            else:
                wrapped_header.append(Paragraph(cell, wrap_style_title_rtl))
        wrapped_data.insert(0, wrapped_header)
        
        self.story.append(Spacer(1, 0.01*inch))

        # Create the table using wrapped data and column widths
        col_widths = [0.7 * inch, 3.7 * inch, 1.2 * inch, 0.8 * inch, 1.5 * inch]
        invoice_table = Table(wrapped_data, colWidths=col_widths)
            
        ts = TableStyle([
            ('TOPPADDING', (1, 1), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 15),
            ('WIDTH', (0, 0), (-1, -1), '100%'),
            
            # Values style
            ('ALIGN', (1, 1), (-1, -1), "RIGHT"),
            ('TEXTCOLOR', (0, 1), (-1, -1), self.primary_color),
            
            # Top Line
            ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
            ('ALIGN', (1, 1), (1, len(invoice_data)), "LEFT"),
        ])
        
        dotted_line = (0, 2, 1, 0)  # Dot line patter
        ts.add('LINEABOVE', (0, 1), (-1, 1), 0.1, colors.black, 0.2, dotted_line)
        ts.add('BOTTOMPADDING', (0, 0), (-1, 0), 9)
            
        invoice_table.setStyle(ts)
        self.story.append(invoice_table)
                
        self.story.append(Spacer(1, 0.1*inch))
        
        self.line_separator(7.85*inch, 1)
        
        self.story.append(Spacer(1, -0.2 * inch))
        

        table_calculation_right_col_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            rightIndent=-278,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=7
        )
        
        table_calculation_payment_detail_style = ParagraphStyle(    
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            rightIndent=-283,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=7,
        )
        table_calculation_payment_detail_child_style = ParagraphStyle(    
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            rightIndent=-287,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=7,
        )

        table_calculation_right_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            alignment=2,
            rightIndent=-210,
            fontName='MSYTC-Bold',
            leading=7
        )
        
        table_calculation_right_payment_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            alignment=2,
            rightIndent=-220,
            fontName='MSYTC-Bold',
            leading=7
        )

        table_calculation_right_col_val_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            leftIndent=2*inch,
            rightIndent=0.6*inch,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=7
        )

        # Table calculations
        table_calculation_data = [
            [
                Paragraph('Subtotal', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(subtotal, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Discount', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(f"- {discount}", table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Rounding', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(rounding, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Total', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(total, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Payment', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(payment, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Balance', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(balance, table_calculation_right_col_val_style),
            ]
        ]
        
        # Payment methods
        table_calculation_data_payment_method = []
        for payment_item in payment_list:
            table_calculation_data_payment_method.append(
                [
                    Paragraph(payment_item.get("name"), table_calculation_payment_detail_child_style),
                    Paragraph(':', table_calculation_right_payment_colon_style),
                    Paragraph(payment_item.get("amount"), table_calculation_right_col_val_style)
                ]
            )
           
        # Payment details inserted bottom of table calculation 
        if table_calculation_data_payment_method:
            table_calculation_data_payment_method.insert(0,
                [
                    Paragraph('Payment Detail', table_calculation_payment_detail_style),
                    Paragraph(''),
                    Paragraph(''),
                ]
            )
            table_calculation_data_payment_method.insert(0, 
                [   Paragraph(''),
                    Paragraph(''),
                    Paragraph(''),
                ]
            )
            
            table_calculation_data.extend(table_calculation_data_payment_method)

        col_widths = [2.2 * inch, 1 * inch, 4.6 * inch]
        table_calculation_data = Table(table_calculation_data, colWidths=col_widths, style=TableStyle([
            ('RIGHTPADDING', (0, 0), (-1, -1), -5),
        ]))
        self.story.append(table_calculation_data)
        
        # thank you text
        text_style = ParagraphStyle(
            name='thanks',
            parent=self.styles['title'],
            fontSize=10,
            textColor=colors.black,
            alignment=1,  # Center align the content
            fontName='MSYTC-Bold',
            leading=10
        )
        
        self.story.append(Spacer(1, 0.2*inch))
        self.story.append(Paragraph("Thank you", text_style))
        self.story.append(Spacer(1, 0.3*inch))
    
    def shop_invoice_table(self, invoice_data, subtotal, discount, total, payment, balance, rounding, credit, payment_list):
        
        wrap_style_val = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=0,
            fontName='MSYTC-Regular',
            leading=9
        )
        wrap_style_val_rtl = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=2,
            fontName='MSYTC-Regular',
            leading=6,
            rightIndent=5
        )
        wrap_style_price = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=2,
            fontName='MSYTC-Regular',
            leading=6,
            rightIndent=0.5 * inch
        )
        wrap_style_title = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            fontName='MSYTC-Bold',
            leading=6
        )
        
        wrap_style_title_rtl = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            fontName='MSYTC-Bold',
            leading=6,
            alignment=2,
            rightIndent=5
        )
        wrap_style_title_price = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            fontName='MSYTC-Bold',
            leading=6,
            alignment=2,
            rightIndent=0.5 * inch
        )
        wrap_style_val_bold = ParagraphStyle(
            name='WrapStyle',
            parent=getSampleStyleSheet()['Normal'],
            wordWrap='RTL',  # Set word wrap to Left To Right
            textColor=self.primary_color,
            fontSize=8,
            alignment=0,
            fontName='MSYTC-Bold',
            leading=2
        )
        package_title_col_style = ParagraphStyle(
            name='LeftColumn',
            parent=getSampleStyleSheet()['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            fontName='MSYTC-Regular',
            leading=4
        )
        
        wrapped_data = []
        index = 1
        for row in invoice_data:
            
            wrapped_row = []
            wrapped_row.append(Paragraph(str(index), wrap_style_val))
            
            if row.get("subname", ""):
                name_with_help_text = f'<font name="MSYTC-Regular" size="7">({row.get("subname", "")})</font> {row.get("name", "")}'
            elif row.get("key", "") == "outstanding_inv":
                name_with_help_text = f'<font name="MSYTC-Regular"><u>{row.get("name", "")}</u></font>'
            else:
                name_with_help_text = f'<font name="MSYTC-Regular">{row.get("name", "")}</font>'
                
            wrapped_row.append(Paragraph(name_with_help_text, wrap_style_val))
            wrapped_row.append(Paragraph(str(row.get("unit_price", 0.00)), wrap_style_val_rtl))
            wrapped_row.append(Paragraph(str(row.get("quantity", 1)), wrap_style_val_rtl))
            wrapped_row.append(Paragraph(str(row.get("price", 0.00)), wrap_style_price))
            
            # Package detail for package type item
            package_detail_title = []
            package_details_title = []
            if row.get("key", "") == "package" and len(row.get("package_detail", [])) > 0:
                package_detail_title.append(Paragraph(""))
                package_detail_title.append(Paragraph("Package Detail:", wrap_style_val_bold))
                package_detail_title.append(Paragraph(""))
                package_detail_title.append(Paragraph(""))
                package_detail_title.append(Paragraph(""))
                
                for package in row.get("package_detail", []):
                    package_title = []
                    package_title.append(Paragraph(""))
                    
                    package_title.append(Paragraph(f'<para leftIndent="10"><font name="MSYTC-Regular"> - {package.get("name")} </font> <font name="MSYTC-Bold">x {row.get("quantity", "")}</font></para>', package_title_col_style))
                    
                    package_title.append(Spacer(1, -20*inch))
                    package_title.append(Paragraph(""))
                    package_title.append(Paragraph(""))
                    
                    package_details_title.append(package_title)
                            
            # append remark, discount and credit
            additional_remark_row = []
            if row.get("remark", ""):
                additional_remark_row.append(Paragraph(""))
                additional_remark_row.append(Paragraph(row.get("remark", ""), wrap_style_val))
                additional_remark_row.append(Paragraph(""))
                additional_remark_row.append(Paragraph(""))
                additional_remark_row.append(Paragraph(""))
            
            additional_discount_row = []
            if row.get("discount", 0.00):
                additional_discount_row.append(Paragraph(""))
                additional_discount_row.append(Paragraph(""))
                additional_discount_row.append(Paragraph(""))
                additional_discount_row.append(Paragraph("Discount", wrap_style_val_rtl))
                additional_discount_row.append(Paragraph(f"-{row.get('discount', 0.00)}", wrap_style_price))
                
            additional_credit_row = []
            if row.get('credit_applied', '0.00'):
                additional_credit_row.append(Paragraph(""))
                additional_credit_row.append(Paragraph(""))
                additional_credit_row.append(Paragraph(""))
                additional_credit_row.append(Paragraph("Credit", wrap_style_val_rtl))
                additional_credit_row.append(Paragraph(f"-{row.get('credit_applied', '0.00')}", wrap_style_price))
            
            wrapped_data.append(wrapped_row)
            
            if additional_discount_row:
                wrapped_data.append(additional_discount_row)
            if additional_credit_row:
                wrapped_data.append(additional_credit_row)
            
            if package_detail_title:
                wrapped_data.append(package_detail_title)
            if package_details_title:
                for package_detail in package_details_title:
                    wrapped_data.append(package_detail)
            
            if additional_remark_row:
                wrapped_data.append(additional_remark_row)
            
            index += 1
        
        
        wrapped_header = []
        for index, cell in enumerate(['No.', 'Description', 'Unit Price', 'Quantity', 'Price']):
            if index in [0, 1]:
                wrapped_header.append(Paragraph(cell, wrap_style_title))
            elif index == 4:
                wrapped_header.append(Paragraph(cell, wrap_style_title_price))
            else:
                wrapped_header.append(Paragraph(cell, wrap_style_title_rtl))
        wrapped_data.insert(0, wrapped_header)
        
        self.story.append(Spacer(1, 0.1*inch))

        # Create the table using wrapped data and column widths
        col_widths = [0.7 * inch, 3.7 * inch, 1.2 * inch, 0.8 * inch, 1.5 * inch]
        invoice_table = Table(wrapped_data, colWidths=col_widths)
            
        ts = TableStyle([
            ('TOPPADDING', (1, 1), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 15),
            ('WIDTH', (0, 0), (-1, -1), '100%'),
            
            # Values style
            ('ALIGN', (1, 1), (-1, -1), "RIGHT"),
            ('TEXTCOLOR', (0, 1), (-1, -1), self.primary_color),
            
            # Top Line
            ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
            ('ALIGN', (1, 1), (1, len(invoice_data)), "LEFT"),
        ])
        
        dotted_line = (0, 2, 1, 0)  # Dot line patter
        ts.add('LINEABOVE', (0, 1), (-1, 1), 0.1, colors.black, 0.2, dotted_line)
        ts.add('BOTTOMPADDING', (0, 0), (-1, 0), 9)
            
        invoice_table.setStyle(ts)
        self.story.append(invoice_table)
                
        self.story.append(Spacer(1, 0.1*inch))
        
        self.line_separator(7.85*inch, 1)
        
        self.story.append(Spacer(1, -0.2 * inch))
        
        table_calculation_right_col_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            rightIndent=-278,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=6
        )
        
        table_calculation_payment_detail_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            rightIndent=-283,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=6,
        )
        
        table_calculation_payment_detail_child_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            rightIndent=-287,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=6,
        )

        table_calculation_right_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            alignment=2,
            rightIndent=-210,
            fontName='MSYTC-Bold',
            leading=6
        )
        
        table_calculation_right_payment_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            alignment=2,
            rightIndent=-220,
            fontName='MSYTC-Bold',
            leading=6
        )

        table_calculation_right_col_val_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            leftIndent=2*inch,
            rightIndent=0.6*inch,
            alignment=2,
            wordWrap='RTL',
            fontName='MSYTC-Bold',
            leading=6
        )

        table_calculation_data = [
            [
                Paragraph('Subtotal', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(subtotal, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Credit', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(f"- {credit}", table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Discount', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(f"- {discount}", table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Rounding', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(rounding, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Total', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(total, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Payment', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(payment, table_calculation_right_col_val_style),
            ],
            [
                Paragraph('Balance', table_calculation_right_col_style),
                Paragraph(':', table_calculation_right_colon_style),
                Paragraph(balance, table_calculation_right_col_val_style),
            ],
        ]

        # Payment methods
        table_calculation_data_payment_method = []
        for payment_item in payment_list:
            table_calculation_data_payment_method.append(
                [
                    Paragraph(payment_item.get("name"), table_calculation_payment_detail_child_style),
                    Paragraph(':', table_calculation_right_payment_colon_style),
                    Paragraph(payment_item.get("amount"), table_calculation_right_col_val_style)
                ]
            )
           
        # Payment details inserted bottom of table calculation 
        if table_calculation_data_payment_method:
            table_calculation_data_payment_method.insert(0,
                [
                    Paragraph('Payment Detail', table_calculation_payment_detail_style),
                    Paragraph(''),
                    Paragraph(''),
                ]
            )
            table_calculation_data_payment_method.insert(0, 
                [   Paragraph(''),
                    Paragraph(''),
                    Paragraph(''),
                ]
            )
            
            table_calculation_data.extend(table_calculation_data_payment_method)

        col_widths = [2.2 * inch, 1 * inch, 4.6 * inch]
        table_calculation_data = Table(table_calculation_data, colWidths=col_widths, style=TableStyle([
            ('RIGHTPADDING', (0, 0), (-1, -1), -5),
        ]))
        self.story.append(table_calculation_data)
        
        # thank you text
        text_style = ParagraphStyle(
            name='thanks',
            parent=self.styles['title'],
            fontSize=10,
            textColor=colors.black,
            alignment=1,  # Center align the content
            fontName='MSYTC-Bold',
            leading=10
        )
        
        self.story.append(Spacer(1, 0.2*inch))
        self.story.append(Paragraph("Thank you", text_style))
        self.story.append(Spacer(1, 0.3*inch))
       
    def terms_and_remark(self, attachment_remark=""):   
        underline_style = ParagraphStyle(
            name='Underline',
            parent=self.styles['title'],
            fontSize=10,
            textColor=self.primary_color,
            underline=True,
            underlineColor=self.primary_color,
            underlineGap=1,
            underlineOffset=-2,
            alignment=0,
            fontName='MSYTC-Bold',
            leading=7,
            leftIndent=-5
        )
        underlined_text = Paragraph('<u>Terms & Payment Remark:</u>', underline_style)
        
        self.story.append(underlined_text)
        self.story.append(Spacer(1, 0.5*inch))
    
        remark_underline_style = ParagraphStyle(
            name='Underline',
            parent=self.styles['title'],
            fontSize=10,
            textColor=self.primary_color,
            underline=True,
            underlineColor=self.primary_color,
            underlineGap=1,
            underlineOffset=-2,
            alignment=0,
            fontName='MSYTC-Bold',
            leading=14,
            leftIndent=-5
        )
        remark_text_style = ParagraphStyle(
            name='Remark Text',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=self.primary_color,
            underline=True,
            underlineColor=self.primary_color,
            alignment=0,
            fontName='MSYTC-Regular',
            leading=15,
            leftIndent=-5
        )
        
        remark = []
        remark.append(Paragraph('<u>Remark:</u>', remark_underline_style))
        remark.append(Spacer(1, -0.05*inch))
        remark.append(Paragraph(attachment_remark.replace("\n", "<br/>"), remark_text_style))
        
        self.story.append(KeepTogether(remark))
        
    def acceptance_signature(self, shop_name, reg_no="", ):
        reg_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            leftIndent=0.7 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=6,
        )

        reg_colon_style = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            leftIndent=-1.28 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=6
        )

        reg_col_val = ParagraphStyle(
            name='LeftColumn',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.primary_color,
            leftIndent=-1.38 * inch,  # Align lines to the start
            fontName='MSYTC-Regular',
            leading=6
        )

        acceptance_style = ParagraphStyle(
            name='RightColumn',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=self.primary_color,
            rightIndent=0,  # Align lines to the end
            alignment=1,  # Right align the content
            fontName='MSYTC-Regular',
            leading=7
        )

        
        # shop name section
        shop_style = ParagraphStyle(
            name='ShopName',
            parent=self.styles['title'],
            fontSize=11,
            textColor=colors.black,
            underline=True,
            underlineColor=self.primary_color,
            alignment=0,
            fontName='MSYTC-Bold',
            leading=15,
            leftIndent=-5
        )
        shop_name = Paragraph(shop_name, shop_style)
        
        acceptances = []
        acceptances.append(Spacer(1, 0.3*inch))
        acceptances.append(shop_name)
        acceptances.append(Spacer(1, -0.1*inch))
        
        data = [
            [
                Paragraph('Reg No.', reg_style),
                Paragraph(':', reg_colon_style),
                Paragraph(f"({reg_no})", reg_col_val),
                Paragraph('Acceptance & Confirmation', acceptance_style),
            ],
        ]
        col_widths = [2.5 * inch, 0.2 * inch, 2.5 * inch, 4.2 * inch]

        table = Table(data, colWidths=col_widths)

        # Enable word wrapping for the content
        table.setStyle(TableStyle([
            ('WORDWRAP', (0, 0), (-1, -1), True),
        ]))
        acceptances.append(table)
        
        acceptances.append(Spacer(1, 1*inch))
        
        line_color = colors.black

        # Create the left line
        left_line = Table(
            [[""]],
            colWidths=["32%"],
            style=[
                ("LINEABOVE", (0, 0), (-1, -1), 1, line_color),
                ("LEFTPADDING", (0, 0), (-1, -1), -20),
            ],
            hAlign="LEFT",
        )
        acceptances.append(left_line)
        
        acceptances.append(Spacer(1, -0.2 * inch))

        # Create the right line
        right_line = Table(
            [[""]],
            colWidths=["32%"],
            style=[
                ("LINEABOVE", (0, 0), (-1, -1), 1, line_color),
            ],
            hAlign="RIGHT",
        )
        acceptances.append(right_line)
        acceptances.append(Spacer(1, -0.2 * inch))
        signature_rubber_stamp = ParagraphStyle(
            name='signature_rubber_stamp',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=self.primary_color,
            alignment=2,
            fontName='MSYTC-Regular',
            leading=7,
            rightIndent=10,
        )
        signature_company_rubber_stamp = Paragraph('Signature / Company Rubber Stamp', signature_rubber_stamp)
        acceptances.append(signature_company_rubber_stamp)
        self.story.append(KeepTogether(acceptances))      
            
    def attachments(self, attachments=[], attachment_remark="-", title="", isShowRemark=False):
        attachment_tile = ParagraphStyle(
            name='attachment_tile',
            parent=self.styles['title'],
            fontSize=9,
            textColor=self.primary_color,
            alignment=0,
            fontName='MSYTC-Bold',
            leading=12,
            leftIndent=-5
        )
        if attachments:
            attachment = Paragraph(f'<u>{title}:</u>', attachment_tile)
            self.story.append(attachment)
        
        if isShowRemark:
            attachment_subtile = ParagraphStyle(
                name='attachment_subtile',
                parent=self.styles['Normal'],
                fontSize=9,
                textColor=self.primary_color,
                alignment=0,
                fontName='MSYTC-Regular',
                leftIndent=-5
            )
            attachment_subtitle = Paragraph(attachment_remark.replace("\n", "<br/>"), attachment_subtile)
            self.story.append(attachment_subtitle)
            
            self.story.append(Spacer(1, 0.2 * inch))
            
        flowables = []
        for attachment_path in attachments:
            if is_image_readable(attachment_path):
                
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
                image = [Image(attachment_path, width=width, height=height)]

                # Create a spacer for left and right margins
                left_margin = [Spacer(7.8*inch, 0)]

                # Append the left margin, image, and right margin to the flowables list
                flowables.append(left_margin)
                flowables.append(image)
            

        if flowables:
            self.story.append(Table(flowables))
        
    def build_company_invoice_pdf(self, data={}):
                
        self.company_invoice_table(
            data.get("invoice_table_data", []), 
            data.get("subtotal", "0.00"), 
            data.get("discount", "0.00"), 
            data.get("total", "0.00"),
            data.get("payment", "0.00"),
            data.get("balance", "0.00"),
            data.get("rounding", "0.00"),
            data.get("payment_list", []),
        )
                
        self.terms_and_remark(data.get("attachment_remark", "-"))
        
        self.acceptance_signature(data.get("shop_name", ""), data.get("registration_no", "-"))
        
        if data.get("attachments",[]) or data.get("attachment_remark", "-"):
            self.attachments(data.get("attachments",[]), data.get("attachment_remark", "-"), "Attachment")
        
        self.doc.build(
            self.story, 
            onFirstPage=partial(self.company_header, data=data, primary_color=self.primary_color),
            onLaterPages=partial(self.company_header, data=data, primary_color=self.primary_color),
            canvasmaker=partial(NumberedPage, adjusted_height=-31, adjusted_width=-78, adjusted_caption='', xx_position=209, yy_position=617)
        )
        
    def build_shop_invoice_pdf(self, data={}):
                
        self.shop_invoice_table(
            data.get("invoice_table_data", []), 
            data.get("subtotal", "0.00"), 
            data.get("discount", "0.00"), 
            data.get("total", "0.00"),
            data.get("payment", "0.00"),
            data.get("balance", "0.00"),
            data.get("rounding", "0.00"),
            data.get("credit", "0.00"),
            data.get("payment_list", []),
        )
        
        if data.get("attachments",[]) or data.get("attachment_remark", "-"):
            self.attachments(data.get("attachments",[]), data.get("attachment_remark", "-"), "Remark & Attachment", True)
        
        self.doc.build(
            self.story,
            onFirstPage=partial(self.shop_header, data=data, primary_color=self.primary_color),
            onLaterPages=partial(self.shop_header, data=data, primary_color=self.primary_color),
            canvasmaker=partial(NumberedPage, adjusted_height=-21, adjusted_width=-78, adjusted_caption='', xx_position=209, yy_position=627.5)
        )


# Total and current page number 
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
        pdfmetrics.registerFont(TTFont('MSYTC-Regular', 'fonts/microsoft-yahei/chinese.msyh.ttf'))
        self.setFillColor(colors.black)
        self.setFont("MSYTC-Regular", 8)
        self.drawRightString(self.x_position, self.y_position, self._adjusted_caption + "%d/%d" % (self._pageNumber, page_count))
  