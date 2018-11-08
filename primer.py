from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal
from reportlab.lib.colors import black, red

packet = io.BytesIO()

# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=legal)
# text
can.setFillColor(black)
can.setFont("Helvetica", 12)
can.drawString(124, 109, "X")
can.showPage()

can.setFillColor(red)
can.setFont("Helvetica", 32)
can.drawString(150, 150, "X")
can.showPage()


# can.setFillColor(red)
# can.setFont("Helvetica", 15)
# can.drawString(167, 214, "X")

can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("fichacatastro.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# segunda pagina

page = existing_pdf.getPage(1)
page.mergePage(new_pdf.getPage(1))
output.addPage(page)

# finally, write "output" to a real file
outputStream = open("destinoa4.pdf", "wb")
output.write(outputStream)
outputStream.close()
