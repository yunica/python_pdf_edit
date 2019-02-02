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

    canv.setFontSize(6)
    canv.setFillColor(blue)
    return canv


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)

# text
can.setFillColor(blue)
can.setFont("Helvetica", 20)

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=legal)

# text
can.setFillColor(blue)
can.setFont("Helvetica", 10)

# HOJA UNICA

can = texto_separado(txt='MELENDEZ', txtsize=8, ubix=234, ubiy=554, canv=can)
can = texto_separado(txt='TORRES', txtsize=8, ubix=234, ubiy=539, canv=can)
can = texto_separado(txt='LAURA', txtsize=8, ubix=234, ubiy=524, canv=can)
can = texto_separado(txt='M', txtsize=8, ubix=234, ubiy=509, canv=can)
can = texto_separado(txt='DNI', txtsize=8, ubix=234, ubiy=496, canv=can)
can = texto_separado(txt='41569658', txtsize=8, ubix=234, ubiy=480, canv=can)
can = texto_separado(txt='JR. LONDRES 568', txtsize=8, ubix=234, ubiy=465, canv=can)
can = texto_separado(txt='SI', txtsize=8, ubix=234, ubiy=451, canv=can)
can = texto_separado(txt='GUITARRA', txtsize=8, ubix=234, ubiy=436, canv=can)
can = texto_separado(txt='GUITARRA', txtsize=8, ubix=234, ubiy=421, canv=can)
can = texto_separado(txt='ORDINARIO', txtsize=8, ubix=234, ubiy=406, canv=can)
can = texto_separado(txt='20193654897',isred=True ,txtsize=10, ubix=234, ubiy=393, canv=can)
can = texto_separado(txt='GUADALUPE', txtsize=8, ubix=234, ubiy=361, canv=can)
can = texto_separado(txt='PRIMARIA', txtsize=8, ubix=234, ubiy=346, canv=can)
can = texto_separado(txt='2', txtsize=8, ubix=234, ubiy=332, canv=can)
#
can = texto_separado(txt='Flores martinez junior frover', txtsize=8, ubix=350, ubiy=280, canv=can)
can = texto_separado(txt='70804143', txtsize=8, ubix=385, ubiy=270, canv=can)

can = texto_separado(txt='FECHA INSCRIPCIÓN :', isseparado=False, txtsize=9, ubix=47, ubiy=75, canv=can)
can = texto_separado(txt='CODIGO INSCRIPCIÓN :', isseparado=False, txtsize=9, ubix=40, ubiy=60, canv=can)
can = texto_separado(txt='25d de de d ede :', isseparado=False, txtsize=12, ubix=160, ubiy=75, canv=can)
can = texto_separado(txt='INSCRIPCION :', isseparado=False, txtsize=12, ubix=160, ubiy=60, canv=can)


"""

tema para guardar las imagenes
"""
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("PDF_FOBAS.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

# finally, write "output" to a real file
outputStream = open("ficha_matricula_cea_ouT_fobas.pdf", "wb")
output.write(outputStream)
outputStream.close()
