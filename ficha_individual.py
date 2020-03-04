from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, blue
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

# VARIABLES ESTATICAS


def texto_separado(txt=None, isred=False, isseparado=True, txtsize=7, ubix=0, ubiy=0,
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

    canv.setFontSize(7)
    canv.setFillColor(blue)
    return canv


class Punto():
    def __init__(self, ubix=0, ubiy=0, txt=None):
        self.ubix = ubix
        self.ubiy = ubiy
        self.txt = txt


class Lista():
    def __init__(self, choise=[], ubix=0, ubiy=0, separacion=0, lubix=[], lubiy=[], text=None, otro=False,
                 ubixotro=0, ubiyotro=0, otrotext=None):
        self.choise = choise
        self.ubix = ubix
        self.ubiy = ubiy
        self.separacion = separacion
        self.lubix = lubix
        self.lubiy = lubiy
        self.otro = otro
        self.ubixotro = ubixotro
        self.ubiyotro = ubiyotro
        self.otrotext = otrotext
        self.listaobj = []
        self.text = text

    def crear_bloque_horizontal(self):
        ubixsum = self.ubix
        self.listaobj = []
        try:
            if not self.lubix:
                for i in self.choise:
                    opunto = Punto(ubixsum, self.ubiy, str(i))
                    ubixsum += self.separacion
                    self.listaobj.append(opunto)
            else:
                for i, x in enumerate(self.lubix):
                    opunto = Punto(x, self.ubiy, self.choise[i])
                    self.listaobj.append(opunto)
        except Exception:
            print(Exception.__str__())

    def crear_bloque_vertical(self):
        ubiysum = self.ubiy
        self.listaobj = []
        try:
            if not self.lubiy:
                for i in self.choise:
                    opunto = Punto(self.ubix, ubiysum, str(i))
                    ubiysum -= self.separacion
                    self.listaobj.append(opunto)
            else:
                for i, y in enumerate(self.lubiy):
                    opunto = Punto(self.ubix, y, self.choise[i])
                    self.listaobj.append(opunto)
        except Exception:
            print(Exception.__str__())

    def crear_bloque_especial(self):
        self.listaobj = []
        try:
            if len(self.lubix) > 0 and len(self.lubiy) > 0:
                for i, txt in enumerate(self.choise):
                    opunto = Punto(self.lubix[i], self.lubiy[i], str(txt))
                    self.listaobj.append(opunto)
        except Exception:
            print(Exception.__str__())

    def get_punto(self):
        if self.text and self.listaobj:
            if self.text in self.choise:
                for i in self.listaobj:
                    if i.txt == self.text:
                        return i
            else:
                return None
        else:
            return None

    def get_otro(self):
        if self.otro and self.otrotext:
            if 'OTRO' in self.choise and self.text == 'OTRO':
                return Punto(self.ubixotro, self.ubiyotro, self.otrotext)
            else:
                return None
        else:
            return None


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=legal)

# text
can.setFillColor(blue)

#                   PRIMERA hoja

# desde aqui inicio
# ======  enmallador

can.setFont("Helvetica", 2)
#y
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
can.setFont("Helvetica", 30)

can = texto_separado(txt='COD VIA 1', isseparado=False, ubix=55, ubiy=656, canv=can)
can = texto_separado(txt='COD VIA 2', isseparado=False, ubix=55, ubiy=648, canv=can)
can = texto_separado(txt='COD VIA 3', isseparado=False, ubix=55, ubiy=640, canv=can)
can = texto_separado(txt='COD VIA 4', isseparado=False, ubix=55, ubiy=635, canv=can)


#                   SEGUNDA hoja

can.showPage()
# ======  enmallador

can.setFont("Helvetica", 2)
#y
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
can.setFont("Helvetica", 20)
# Numero de ficha
can = texto_separado(txt='C12-0000162', isseparado=False, ubix=840, ubiy=1342, canv=can)

"""
tema para guardar las imagenes
"""
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("ficha_individual.pdf", "rb"))
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
outputStream = open("ficha_individual_ouput.pdf", "wb")
output.write(outputStream)
outputStream.close()
