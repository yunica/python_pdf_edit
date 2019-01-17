from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, blue
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

# VARIABLES ESTATICAS

resultado_entrevista_choise = ['COMPLETA', 'RECHAZADA', 'AUSENTE', ]
# 1
provincia_choices = ['001', '002', ]
distrito_choices = ['(01) AYACUCHO', '(10) SAN JUAN BAUTISTA', '(16) - ANDRES AVELINO CACERES', 'HUANTA']

localidad_choices = ['(001) HUAMANGA', '002) HUANTA']

# FtbLocalizacionUbicacion
estado_ficha_choices = ['COMPLETA', 'INCOMPLETA']
ubicado_choices = ['PISTA', 'BERMA', 'VEREDA', 'OTRO']
accesibilidad_tipo_choice = ['ASFALTO', 'CONCRETO', 'ADOQUINADO', 'CESPED', 'OTRO']
# FtbDatosFisicos - buzon
tipo_buzon_choice = ['ESTANDAR', 'DESARENADOR', 'REJILLA', 'REPARTIDOR', 'VMA', 'ALIVIO', 'OTRO']
montaje_buzon_choice = ['PRIMARIO', 'SECUNDARIO', 'EMISOR', ]
tapa_centrico_choice = ['CENTRICO', 'EXCENTRICO']
# FtbDatosFisicos - tapa
estado_generico = ['BUENO', 'REGULAR', 'MALO', 'NINGUNO']
tapa_geometria_choice = ['CIRCULAR', 'CUADRADA', 'OTRO']
material_tapa_choice = ['HIERRO FUNDIDO', 'CONCRETO ARMADO', 'HIERRO DUCTIL', 'OTRO']
# FtbDatosFisicos - Anillo
material_anillo_choice = ['HIERRO FUNDIDO', 'ACERO - PLATINA', 'OTRO']
estado_anillo_choices = ['BUENO', 'MALO', 'OTRO']
# FtbDatosFisicos - techo - respiradero
geometria_techo_choice = ['CIRCULAR', 'CUADRADA']

# FtbDatosFisicos anillo - techo
techo_anillo_material_choice = ['METALICO', 'OTRO']
# FtbDatosFisicos - fuste
fuste_geometria_choice = ['CIRCULAR', 'CUADRADA', 'CONICO']
fuste_material_choice = ['MAMPOSTERIA', 'CONCRETO ARMADO', 'OTRO']
# FtbDatosFisicos -  fuste mesa
fuste_mesa_estado_choice = ['BUENO', 'REGULAR', 'MALO', 'COLAPSADA', 'OTRO']
# estado buzon
estado_buzon_choice = ['FUNCIONANDO', 'COLMATADO (ATORADO)', 'SEDIMENTADO', 'CON ESCOMBROS/BASURA', 'OTRO']
escala_olores_choices = ['ALTO', 'MEDIO', 'BAJO']
llegada_choice = ['GRAVEDAD', 'BOMBEO']
cantidad_sedimento_choice = ['ALTA CANTIDAD DE SEDIMENTO', 'MEDIA CANTIDAD DE SEDIMENTO',
                             'POCA O NULA CANTIDAD DE SEDIMENTO']


def ficha_num(txt='123456', canv=None):
    canv.setFontSize(20)
    canv.setFillColor(red)
    canv.drawString(485, 748, txt)
    canv.setFontSize(12)
    canv.setFillColor(blue)
    return canv


def texto_separado(txt=None, isred=False, isseparado=True, txtsize=12, ubix=0, ubiy=0,
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
can.setFont("Helvetica", 12)
#                   PRIMERA hoja
for i in range(0, 600, 30):
    can.drawString(i, 770, str(i))
    can.drawString(i, 220, str(i))

for i in range(0, 840, 20):
    can.drawString(280, i, str(i))

#                   SEGUNDA hoja
can.showPage()

for i in range(0, 600, 30):
    can.drawString(i, 770, str(i))
    can.drawString(i, 220, str(i))

for i in range(0, 840, 20):
    can.drawString(280, i, str(i))

#                   TERCERA hoja
can.showPage()

for i in range(0, 600, 30):
    can.drawString(i, 770, str(i))
    can.drawString(i, 220, str(i))

for i in range(0, 840, 20):
    can.drawString(280, i, str(i))
#                   CUARTAa hoja
can.showPage()

for i in range(0, 600, 30):
    can.drawString(i, 770, str(i))
    can.drawString(i, 220, str(i))

for i in range(0, 840, 20):
    can.drawString(280, i, str(i))

"""

tema para guardar las imagenes
"""
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("ficha.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

# segunda pagina
page = existing_pdf.getPage(1)
page.mergePage(new_pdf.getPage(1))
output.addPage(page)

# segunda pagina
page = existing_pdf.getPage(2)
page.mergePage(new_pdf.getPage(2))
output.addPage(page)

# segunda pagina
page = existing_pdf.getPage(3)
page.mergePage(new_pdf.getPage(3))
output.addPage(page)

# finally, write "output" to a real file
outputStream = open("destinoa4.pdf", "wb")
output.write(outputStream)
outputStream.close()
