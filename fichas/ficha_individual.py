from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, blue
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

# VARIABLES ESTATICAS
from fichas.constants_ficha import *

PDF_ENTRADA = 'ficha_i.pdf'
PDF_SALIDA = 'ficha_i_out.pdf'


#
def d_txt(text_obj=None, ubixy=[], txt=None, separate=0, txtsize=11,
          isred=False):
    try:
        # text_obj = canvas.Canvas(packet, pagesize=legal).beginText()
        x, y = ubixy
        text_obj.setFont("Helvetica", txtsize)
        text_obj.setFillColor(blue)
        txt_obj.setTextOrigin(x, y)
        if isred:
            text_obj.setFillColor(red)

        if separate != 0:
            txt_obj.setCharSpace(separate)
        txt_obj.textOut(txt)
        if separate != 0:
            txt_obj.setCharSpace(0)
    except Exception as e:
        print(e.__str__())


def d_alternativas(alternativas=[], ubixy=[], separate=0, text=None,
                   otro=False, ubixy_otro=[], otrotext=None, text_obj=None,
                   txtsize=11, isred=False):
    try:
        otext_num = ''
        for i in alternativas:
            if i(0) == text:
                otext = i(1)
        d_txt(text_obj, ubixy, otext_num, separate, txtsize, isred)
        if otro:
            d_txt(text_obj, ubixy_otro, otrotext, separate, txtsize, isred)
    except Exception as e:
        print(e.__str__())


# =====================
# ======= START =======
# =====================

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=legal)

# =====================
# ======= HOLA 01 =====
# =====================


# ======  enmallador
can.setFont("Helvetica", 2)
# y
for i in range(0, 590, 5):
    can.drawString(i, 700, str(i))
    can.drawString(i, 550, str(i))
    can.drawString(i, 460, str(i))
    can.drawString(i, 360, str(i))
    can.drawString(i, 180, str(i))
    can.drawString(i, 100, str(i))
# x
can.setFont("Helvetica", 3)
for i in range(0, 830, 4):
    can.drawString(35, i, str(i))
    can.drawString(180, i, str(i))
    can.drawString(350, i, str(i))
    can.drawString(390, i, str(i))
    can.drawString(480, i, str(i))
    can.drawString(450, i, str(i))
# ======
txt_obj = can.beginText()
d_txt(txt_obj, ubixy=[55, 642], txt='COD VIA 1', separate=8)
d_txt(txt_obj, ubixy=[55, 632], txt='COD VIA 2')
d_txt(txt_obj, ubixy=[55, 622], txt='COD VIA 3', txtsize=40)
d_txt(txt_obj, ubixy=[55, 612], txt='COD VIA 4')

can.drawText(txt_obj)

# =====================
# ======= HOLA 02 =====
# =====================


can.showPage()
txt_obj = can.beginText()

# ======  enmallador
can.setFont("Helvetica", 2)
# y
for i in range(0, 590, 5):
    can.drawString(i, 700, str(i))
    can.drawString(i, 550, str(i))
    can.drawString(i, 460, str(i))
    can.drawString(i, 360, str(i))
    can.drawString(i, 180, str(i))
    can.drawString(i, 100, str(i))
# x
can.setFont("Helvetica", 3)
for i in range(0, 830, 4):
    can.drawString(35, i, str(i))
    can.drawString(180, i, str(i))
    can.drawString(350, i, str(i))
    can.drawString(390, i, str(i))
    can.drawString(480, i, str(i))
    can.drawString(450, i, str(i))
# ======
# Numero de ficha
d_txt(txt_obj, txt='C12-0000162', ubixy=[55, 632], txtsize=40)

can.drawText(txt_obj)

# =====================
# ======= LOGISTICA =====
# =====================

can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(PDF_ENTRADA, "rb")
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
outputStream = open(PDF_SALIDA, "wb")
output.write(outputStream)
outputStream.close()
