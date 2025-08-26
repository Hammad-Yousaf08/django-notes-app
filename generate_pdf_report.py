import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Read the JSON file
with open('report.json', 'r') as file:
    data = json.load(file)

# Set up the PDF
pdf_filename = "report_output.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)
width, height = letter

# Example: Add title
c.setFont("Helvetica-Bold", 14)
c.drawString(100, height - 50, "SonarQube Report")

# Add the report data
c.setFont("Helvetica", 10)

# Adjust this part depending on how your JSON looks
y_position = height - 100
for key, value in data.items():
    text = f"{key}: {value}"
    c.drawString(100, y_position, text)
    y_position -= 20

# Save the PDF
c.save()

print(f"PDF report generated: {pdf_filename}")
