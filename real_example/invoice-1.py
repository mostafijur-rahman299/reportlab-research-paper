from data import invoice_table_data
from generator import GenerateInvoicePDF

data = {
    "shop_logo": "",
    "shop_name": "AK National",
    "registration_no": "8494JFU8474",
    "address1": "Weinmeisterstraße 12-14, 10178 Berlin, Germany",
    "address2": " Showroom, Weinmeisterstr. 12-14.",
    "phone_number": "+904840947",
    "whatsapp_number": "+84947495",
    "member_email": "ex@gmail.com",
    "email": "ex2@gmail.com",
    "invoice_to": "Sk Khalid",
    "invoice_no": "849487493434",
    "DO_No": "048404745",
    "PO_No": "89484",
    "invoice_date": "12/14/2024",
    "issued_time": "12:10 PM",
    "handled_by": "Mostafijur Rahman",
    "payment_term": 'C.O.D',
    "telephone_no": "84893749",
    "account_number": '04849484934',
    "invoice_table_data": invoice_table_data[0],
    "attachments": ["https://tickme-release.s3.amazonaws.com/order_attachment/4/351/IMG_20230212_110433.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAX2XAKZGPKVWBVMOS%2F20230717%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20230717T114642Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d04128b1de511995bb10110c154c371aa772f0a197a3de1944814be9fda6cbb0"],
    "attachment_remark": '',
    "subtotal": "12909.00",
    "discount": "10.00",
    "total": "10909.00",
    "payment": "0.00",
    "balance": "143.00",
    "rounding": "0.00",
    "credit": "10.00",
    "payment_list": [
        {
            "id": 91,
            "name": "BOOST",
            "amount": "12.00"
        },
        {
            "id": 92,
            "name": "VISA",
            "amount": "10.00"
        }
    ]
}


instance = GenerateInvoicePDF("invoice-1.pdf", )
instance.build_shop_invoice_pdf(data)
