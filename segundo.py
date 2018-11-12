from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal
from reportlab.lib.colors import black, red

resultado_entrevista_choise = ['COMPLETA', 'RECHAZADA', 'AUSENTE']
tipo_usuario_choise = ['ACTIVA', 'FACTIBLE', 'POTENCIAL', 'CLANDESTINA', ]

tipo_interior_choise = ['DEPARTAMENTO', 'OFICINA', 'TIENDA', 'LOCAL', 'OTRO', 'OTRO']


def ficha_num(txt='123456', canv=None):
    canv.setFontSize(20)
    canv.setFillColor(red)
    canv.drawString(485, 748, txt)
    canv.setFontSize(12)
    canv.setFillColor(black)
    return canv


def texto_separado(txt='20180-0321321-31321-54654', isred=True, isseparado=True, txtsize=12, ubix=0, ubiy=0, canv=None):
    canv.setFontSize(txtsize)
    if isred:
        canv.setFillColor(red)
    salida = ''
    if isseparado:
        for i in txt:
            salida += i + ' '
        canv.drawString(ubix, ubiy, salida)
    else:
        canv.drawString(ubix, ubiy, txt)
    canv.setFontSize(12)
    canv.setFillColor(black)
    return canv


class Punto():
    def __init__(self, ubix=0, ubiy=0, txt=None):
        self.ubix = ubix
        self.ubiy = ubiy
        self.txt = txt


class Lista():
    def __init__(self, choise=[], ubix=0, ubiy=0, separacion=0, lubix=[], lubiy=[], otro=False, separacionotro=0,
                 otrotext=None):
        self.choise = choise
        self.ubix = ubix
        self.ubiy = ubiy
        self.separacion = separacion
        self.lubix = lubix
        self.lubiy = lubiy
        self.otro = otro
        self.separacionotro = separacionotro
        self.otrotext = otrotext
        self.listaobj = []

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

    def get_punto(self, txt=None):
        if txt and self.listaobj:
            for i in self.listaobj:
                if i.txt == txt:
                    return i
        else:
            return None

    def get_otro(self):
        if self.otro and self.otrotext:
            opunto_otro = self.get_punto('OTRO')
            if opunto_otro:
                opunto = Punto(int(opunto_otro.ubix + self.separacionotro), opunto_otro.ubiy, self.otrotext)
                return opunto


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=legal)

# text
can.setFillColor(black)
can.setFont("Helvetica", 12)
can.setFontSize()
can.drawString(124, 109, "X")
# 1
can = ficha_num(canv=can)
# 2
resultados_entrevista = Lista(resultado_entrevista_choise, 133, 713, 62)
resultados_entrevista.crear_bloque_horizontal()
oresultados_entrevista = resultados_entrevista.get_punto('AUSENTE')
can.setFillColor(red)
can.drawString(oresultados_entrevista.ubix, oresultados_entrevista.ubiy, 'X')
# 3
resultados_entrevista = Lista(tipo_usuario_choise, 350, 713, 0, [352, 404, 444, 496])
resultados_entrevista.crear_bloque_horizontal()
oresultados_entrevista = resultados_entrevista.get_punto('CLANDESTINA')
can.setFillColor(red)
can.drawString(oresultados_entrevista.ubix, oresultados_entrevista.ubiy, 'X')
# 4
can = texto_separado(ubix=130, ubiy=685,isseparado=False, canv=can)
can = texto_separado(txt='3216544',ubix=500, ubiy=685,isseparado=False, canv=can)
can = texto_separado(txt='HUAMANGA',ubix=490, ubiy=666,isseparado=False, canv=can)
can = texto_separado(txt='flores martinez junior grover',ubix=80, ubiy=665,isseparado=False, canv=can)
can = texto_separado(txt='Psje. mao tse tung 1081 MZA=A',ubix=80, ubiy=646,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=45, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=100, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=150, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=200, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=250, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=310, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=355, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=415, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=470, ubiy=618,isseparado=False, canv=can)
can = texto_separado(txt='005',ubix=530, ubiy=618,isseparado=False, canv=can)
# 5



can.setFont("Helvetica", 5)
can.setFillColor(red)
for i in range(0, 600, 10):
    can.drawString(i, 500, str(i))

for i in range(0, 840, 10):
    can.drawString(500, i, str(i))

# segunda hoja
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