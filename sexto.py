from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, black
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfbase.pdfmetrics import stringWidth




def resize_image(tamanio):
    if tamanio:
        x, y = tamanio
        try:
            if x <= 800:
                return 1, 1
            else:
                num = 800 / x
                peque = round(num, 3)
                media = round((peque + ((1 - peque) / 2)), 3)
                return peque, media
        except Exception:
            pass
    return None, None

def texto_separado(txt=None, isred=False, isseparado=True, txtsize=8, ubix=0, ubiy=0,
                   canv=None):
    if txt:
        canv.setFontSize(txtsize)
        canv.setFillColor(black)
        if isred:
            canv.setFillColor(red)
            
        if isseparado:
            salida = ''
            for i in txt:
                salida += i + ' '
            canv.drawString(ubix, ubiy, salida)
        else:
            canv.drawString(ubix, ubiy, txt)
    else :
        canv.setFillColor(red)
        canv.drawString(ubix, ubiy, ' -- -- --')

    canv.setFontSize(8)
    canv.setFillColor(black)
    return canv


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)

# text
can.setFillColor(black)
can.setFont("Helvetica", 12)

#                   HOJA UNICA

can.drawImage('iamgen.jpg', 460,615,120,135)

can.setFont("Helvetica-Bold", 14)
can = texto_separado(txt='FORMACIÓN TEMPRANA', isseparado=False, txtsize=13, ubix=285, ubiy=635, canv=can)
can = texto_separado(txt='( FOBAS )', isseparado=False, txtsize=14, ubix=270, ubiy=615, canv=can)
can.setFont("Helvetica", 8)
can = texto_separado(txt='GOMEZ',  ubix=234, ubiy=570, canv=can)
can = texto_separado(txt='SOSA',  ubix=234, ubiy=556, canv=can)
can = texto_separado(txt='PEDRO',  ubix=234, ubiy=540, canv=can)
can = texto_separado(txt='M',  ubix=234, ubiy=526, canv=can)
can = texto_separado(txt='DNI',  ubix=234, ubiy=511, canv=can)
can = texto_separado(txt='895632145',  ubix=234, ubiy=498, canv=can)
can = texto_separado(txt='JR CALLAO 594',  ubix=234, ubiy=482, canv=can)
can = texto_separado(txt='NO',  ubix=234, ubiy=467, canv=can)
can = texto_separado(txt='FOBAS',  ubix=234, ubiy=452, canv=can)
can = texto_separado(txt='FLAUTA',  ubix=234, ubiy=438, canv=can)
can = texto_separado(txt='ORDINARIO',  ubix=234, ubiy=424, canv=can)
can = texto_separado(txt='201945847854',isred=True, txtsize=10, ubix=234, ubiy=410, canv=can)
#
can = texto_separado(txt='GOMEZ',  ubix=234, ubiy=380, canv=can)
can = texto_separado(txt='FLORES',  ubix=234, ubiy=365, canv=can)
can = texto_separado(txt='JUANA',  ubix=234, ubiy=350, canv=can)
can = texto_separado(txt='DNI',  ubix=234, ubiy=337, canv=can)
can = texto_separado(txt='785412584',  ubix=234, ubiy=322, canv=can)
can = texto_separado(txt='MADRE',  ubix=234, ubiy=307, canv=can)
can = texto_separado(txt='JR CUZCO',  ubix=234, ubiy=292, canv=can)
can = texto_separado(txt='879654896',  ubix=234, ubiy=277, canv=can)
#
can = texto_separado(txt='A@GMAIL.COM',  ubix=234, ubiy=262, canv=can)
can = texto_separado(txt='SAN JUAN',  ubix=234, ubiy=232, canv=can)
can = texto_separado(txt='SECUNDARIA',  ubix=234, ubiy=218, canv=can)
can = texto_separado(txt='0',  ubix=234, ubiy=204, canv=can)
#
can = texto_separado(txt='flores martinez junior', txtsize=10, ubix=370, ubiy=150, canv=can)
can = texto_separado(txt='12345678', txtsize=10, ubix=415, ubiy=137, canv=can)
#
can = texto_separado(txt='FECHA INSCRIPCIÓN :',isseparado=False,  ubix=35, ubiy=15, canv=can)
can = texto_separado(txt='25d de diciembre del 2019 ass as', isseparado=False,txtsize=10, ubix=130, ubiy=15, canv=can)

can = texto_separado(txt='CODIGO INSCRIPCIÓN :',isseparado=False,  ubix=290, ubiy=15, canv=can)
can = texto_separado(txt='261cd210-0d55-11e9-88ff-309c23c19f92',isseparado=False, txtsize=10, ubix=400, ubiy=15, canv=can)



"""

tema para guardar   las imagenes
"""
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("PDF12.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(1)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


# finally, write "output" to a real file
outputStream = open("ficha_matricula_cea_out_generico.pdf", "wb")
output.write(outputStream)
outputStream.close()
