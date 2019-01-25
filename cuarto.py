from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, blue
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph




def texto_separado(txt=None, isred=False, isseparado=True, txtsize=18, ubix=0, ubiy=0,
                   canv=None):
    if txt:
        canv.setFontSize(txtsize)
        if isred:
            canv.setFillColor(red)
        else:
            canv.setFillColor(blue)

        if isseparado:
            salida = ''
            for i in txt:
                salida += i + ' '
            canv.drawString(ubix, ubiy, salida)
        else:
            canv.drawString(ubix, ubiy, txt)

    canv.setFontSize(12)
    canv.setFillColor(blue)
    return canv


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)

# text
can.setFillColor(blue)
can.setFont("Helvetica", 12)

#                   HOJA UNICA

can = texto_separado(txt='C12-0000162', isseparado=False, txtsize=23, ubix=830, ubiy=1325, canv=can)



"""

tema para guardar las imagenes
"""
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("NOMBRE FICHA.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


# finally, write "output" to a real file
outputStream = open("ordenpago_out.pdf", "wb")
output.write(outputStream)
outputStream.close()
