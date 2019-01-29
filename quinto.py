from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, black
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph



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
can.setFont("Helvetica", 8)

# HOJA UNICA

can.drawImage('iamgen.jpg', 460,640,50,135)

can = texto_separado(txt='MELENDEZ', ubix=234, ubiy=554, canv=can)
can = texto_separado(txt='TORRES', ubix=234, ubiy=539, canv=can)
can = texto_separado(txt='LAURA', ubix=234, ubiy=524, canv=can)
can = texto_separado(txt='M', ubix=234, ubiy=509, canv=can)
can = texto_separado(txt='DNI', ubix=234, ubiy=494, canv=can)
can = texto_separado(txt='JR. LONDRES 568', ubix=234, ubiy=480, canv=can)
can = texto_separado(txt='JR. LONDRES 568', ubix=234, ubiy=465, canv=can)
can = texto_separado(txt='SI', ubix=234, ubiy=451, canv=can)
can = texto_separado(txt='963568945', ubix=234, ubiy=436, canv=can)
can = texto_separado(txt='327855', ubix=300, ubiy=436, canv=can)

can = texto_separado(txt='A@GMAIL.COM', ubix=234, ubiy=421, canv=can)
can = texto_separado(txt='CARRERA DE FORMACION ARTISTICA ESPECIALIDAD MUSICA (CEA) 123', ubix=234, ubiy=406, canv=can)
can = texto_separado(txt='GUITARRA', ubix=234, ubiy=393, canv=can)
can = texto_separado(txt='ORDINARIO', ubix=234, ubiy=377, canv=can)
can = texto_separado(txt='2019365489',txtsize=10,isred=True, ubix=234, ubiy=363, canv=can)
#
can = texto_separado(txt='FATIMA', ubix=234, ubiy=319, canv=can)
can = texto_separado(txt='SECUNDARIO', ubix=234, ubiy=304, canv=can)
can = texto_separado(txt='2', ubix=234, ubiy=289, canv=can)
#
can = texto_separado(txt='flores martinez junior', txtsize=10, ubix=370, ubiy=236, canv=can)
can = texto_separado(txt='12345678', txtsize=10, ubix=415, ubiy=221, canv=can)

#
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
existing_pdf = PdfFileReader(open("PDF12.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


# finally, write "output" to a real file
outputStream = open("ficha_matricula_cea_ou_cea.pdf", "wb")
output.write(outputStream)
outputStream.close()
