                    #  Creating payment receipts using Python


from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Image, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# --- PDF Setup ---
pdf = SimpleDocTemplate("Day9_invoice.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# --- Load Logo ---
logo = Image("logo.png", width=115, height=110)

# --- Title & Metadata ---
title_style = styles["Title"]
title_style.alignment = 1
title = Paragraph("  Purchase Tech Course  Invoice", title_style)

invoice_info = Paragraph(f"""
<b>Invoice No:</b> INV-2025-078<br/>
<b>Date:</b> {datetime.now().strftime('%d/%m/%Y')}<br/>
<b>Payment Method:</b> Cash <br/>
""", styles["Normal"])

customer_info = Paragraph(f"""
<b>Billed To:</b><br/>
Ayush Gupta<br/>
Ayush@example.com<br/>
+91-7398239800
""", styles["Normal"])

# Create header (logo + customer + invoice details)
header_table = Table(
    [[logo, customer_info, invoice_info]],
    colWidths=[120, 200, 200]
)
header_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP")
]))
elements.extend([header_table, Spacer(1, 20), title, Spacer(1, 20)])

# --- Table Data ---
data = [
    ["Date", "Product Name", "Subscription", "Price (Rs.)"],
    ["12/07/2025", "Python Mastery Bootcamp", "1 Year Access", "5,499.00/-"],
    ["12/07/2025", "DSA - Advanced", "Lifetime Access", "8,999.00/-"],
    ["12/07/2025", "AI for Beginners", "6 Months", "4,199.00/-"],
    ["", "", "", ""],
    ["Sub Total", "", "", "18,697.00/-"],
    ["Discount (SAVE10)", "", "", "-1,869.70/-"],
    ["GST (18%)", "", "", "3,029.57/-"],
    ["Total", "", "", "19,856.87/-"]
]

# --- Table Style ---
table = Table(data, style=TableStyle([
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#003366")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -4), colors.beige),
    ("BACKGROUND", (-1, -1), (-1, -1), colors.lightgreen),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
]))
elements.append(table)

# --- Footer Note or Signature ---
footer = Paragraph("<br/><br/>This is a computer-generated invoice. No signature required.", styles["Normal"])
elements.extend([Spacer(1, 30), footer])

# --- Build the PDF ---
pdf.build(elements)
