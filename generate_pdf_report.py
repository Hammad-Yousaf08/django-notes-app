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

# Starting y-position
y_position = height - 100

# Define a function to handle page breaks
def add_text_with_page_break(text, y_position):
    global c, width, height
    lines = text.split("\n")
    for line in lines:
        if y_position < 50:  # If we're too close to the bottom, start a new page
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = height - 50  # Reset y-position to top
        c.drawString(100, y_position, line)
        y_position -= 12  # Move down the page

# Adjust this part depending on how your JSON looks
for key, value in data.items():
    text = f"{key}: {value}"
    add_text_with_page_break(text, y_position)

# Save the PDF
c.save()

print(f"PDF report generated: {pdf_filename}")
