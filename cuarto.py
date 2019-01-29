from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, black
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph




def texto_separado(txt=None, isred=False, isseparado=True, txtsize=10, ubix=0, ubiy=0,
                   canv=None):
    if txt:
        canv.setFontSize(txtsize)
        if isred:
            canv.setFillColor(red)
        else:
            canv.setFillColor(black)

        if isseparado:
            salida = ''
            for i in txt:
                salida += i + ' '
            canv.drawString(ubix, ubiy, salida)
        else:
            canv.drawString(ubix, ubiy, txt)
    else:
        canv.setFillColor(red)
        canv.drawString(ubix, ubiy, ' --- --')

    canv.setFontSize(12)
    canv.setFillColor(black)
    return canv


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)

# text
can.setFillColor(black)
can.setFont("Helvetica", 12)

#                   HOJA UNICA
can.setFont("Helvetica-Bold", 12)
can = texto_separado(txt='19/04/2019',  txtsize=13, ubix=342, ubiy=577, canv=can)
can.setFont("Helvetica", 12)
can = texto_separado(txt='MELENDEZ TORRES LAURA',   ubix=234, ubiy=553, canv=can)
can = texto_separado(txt='FOBAS',   ubix=234, ubiy=535, canv=can)
can = texto_separado(txt='ORDINARIO',   ubix=234, ubiy=518, canv=can)
can = texto_separado(txt='GUITARRA',   ubix=234, ubiy=501, canv=can)
can = texto_separado(txt='45236541',   ubix=234, ubiy=484, canv=can)
can = texto_separado(txt='201936594',   ubix=234, ubiy=467, canv=can)
can = texto_separado(txt='200.00',  isred=True,txtsize=16, ubix=234, ubiy=450, canv=can)
can = texto_separado(txt='15/04/2019',   ubix=234, ubiy=416, canv=can)



"""

tema para guardar las imagenes
"""
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("orden de pago.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


# finally, write "output" to a real file
outputStream = open("ordenpago_out.pdf", "wb")
output.write(outputStream)
outputStream.close()
