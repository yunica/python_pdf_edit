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
can.setFont("Helvetica", 20)

#                   PRIMERA hoja

# desde aqui inicio
# numero ficha
can = texto_separado(txt='C12-0000162', isseparado=False, txtsize=23, ubix=830, ubiy=1325, canv=can)
can = texto_separado(txt='tt-0000162', isseparado=False, txtsize=23, ubix=830, ubiy=1259, canv=can)
can = texto_separado(txt='rr-4869', isseparado=False, txtsize=23, ubix=830, ubiy=1190, canv=can)
can = texto_separado(txt='aa-785', isseparado=False, txtsize=23, ubix=830, ubiy=1149, canv=can)
can = texto_separado(txt='bb-123', isseparado=False, txtsize=23, ubix=830, ubiy=1109, canv=can)
can = texto_separado(txt='cc-123', isseparado=False, txtsize=23, ubix=830, ubiy=1067, canv=can)
# Localizacion
can = texto_separado(txt='05', isseparado=False, txtsize=23, ubix=103, ubiy=1219, canv=can)
can = texto_separado(txt='001', isseparado=False, txtsize=23, ubix=173, ubiy=1219, canv=can)
can = texto_separado(txt='001', isseparado=False, txtsize=23, ubix=233, ubiy=1219, canv=can)
can = texto_separado(txt='001', isseparado=False, txtsize=23, ubix=293, ubiy=1219, canv=can)
can = texto_separado(txt='sdf', isseparado=False, txtsize=23, ubix=390, ubiy=1219, canv=can)
can = texto_separado(txt='Av.Los incas con numero # 170', isseparado=False, txtsize=19, ubix=465,
                     ubiy=1219, canv=can)
# cotas del esquinero
can = texto_separado(txt='012 ', isseparado=False, ubix=113, ubiy=1149, canv=can)
can = texto_separado(txt='013', isseparado=False, ubix=113, ubiy=1132, canv=can)
can = texto_separado(txt='014', isseparado=False, ubix=113, ubiy=1115, canv=can)
can = texto_separado(txt='015', isseparado=False, ubix=113, ubiy=1098, canv=can)
can = texto_separado(txt='016', isseparado=False, ubix=113, ubiy=1080, canv=can)
can = texto_separado(txt='012 ', isseparado=False, ubix=220, ubiy=1149, canv=can)
can = texto_separado(txt='013', isseparado=False, ubix=210, ubiy=1132, canv=can)
can = texto_separado(txt='014', isseparado=False, ubix=210, ubiy=1115, canv=can)
can = texto_separado(txt='015', isseparado=False, ubix=210, ubiy=1098, canv=can)
can = texto_separado(txt='016', isseparado=False, ubix=210, ubiy=1080, canv=can)
can = texto_separado(txt='012 ', isseparado=False, ubix=340, ubiy=1149, canv=can)
can = texto_separado(txt='013', isseparado=False, ubix=330, ubiy=1132, canv=can)
can = texto_separado(txt='014', isseparado=False, ubix=330, ubiy=1115, canv=can)
can = texto_separado(txt='015', isseparado=False, ubix=330, ubiy=1098, canv=can)
can = texto_separado(txt='016', isseparado=False, ubix=330, ubiy=1080, canv=can)
can = texto_separado(txt='112 ', isseparado=False, ubix=470, ubiy=1150, canv=can)
can = texto_separado(txt='013', isseparado=False, ubix=470, ubiy=1132, canv=can)
can = texto_separado(txt='014', isseparado=False, ubix=470, ubiy=1115, canv=can)
can = texto_separado(txt='015', isseparado=False, ubix=470, ubiy=1098, canv=can)
can = texto_separado(txt='016', isseparado=False, ubix=470, ubiy=1080, canv=can)
can = texto_separado(txt='212 ', isseparado=False, ubix=600, ubiy=1149, canv=can)
can = texto_separado(txt='013', isseparado=False, ubix=600, ubiy=1132, canv=can)
can = texto_separado(txt='014', isseparado=False, ubix=600, ubiy=1115, canv=can)
can = texto_separado(txt='015', isseparado=False, ubix=600, ubiy=1098, canv=can)
can = texto_separado(txt='016', isseparado=False, ubix=600, ubiy=1080, canv=can)
can = texto_separado(txt='312 ', isseparado=False, ubix=740, ubiy=1149, canv=can)
can = texto_separado(txt='13', isseparado=False, ubix=740, ubiy=1132, canv=can)
can = texto_separado(txt='014', isseparado=False, ubix=740, ubiy=1115, canv=can)
can = texto_separado(txt='015', isseparado=False, ubix=740, ubiy=1098, canv=can)
can = texto_separado(txt='016', isseparado=False, ubix=740, ubiy=1080, canv=can)

# grilla ubicacion
grilla = 20
grilla_x = None
list_grilla_y = [0, 385, 370, 350, 335, 315, 300, 282, 265,
                 265, 282, 300, 315, 335, 350, 370, 385,
                 385, 370, 350, 335, 315, 300, 282, 265,
                 265, 282, 300, 315, 335, 350, 370, 385,
                 385, 370, 350, 335, 315, 300, 282, 265, ]
if grilla <= 8 and grilla >= 1:
    grilla_x = 162
if grilla <= 16 and grilla >= 9:
    grilla_x = 183
if grilla <= 24 and grilla >= 17:
    grilla_x = 212
if grilla <= 32 and grilla >= 25:
    grilla_x = 235
if grilla <= 40 and grilla >= 33:
    grilla_x = 260
can = texto_separado(txt='x', txtsize=20, ubix=grilla_x, ubiy=list_grilla_y[grilla], canv=can)

#
can = texto_separado(txt='17/01/2019', isseparado=False, txtsize=23, ubix=100, ubiy=166, canv=can)
can = texto_separado(txt='wjfhrutb', isseparado=False, txtsize=23, ubix=300, ubiy=166, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, txtsize=23, ubix=475, ubiy=166, canv=can)
can = texto_separado(txt='Jose Flores', isseparado=False, txtsize=23, ubix=645, ubiy=166, canv=can)
can = texto_separado(txt='Pepe Flores', isseparado=False, txtsize=23, ubix=820, ubiy=166, canv=can)

#                   SEGUNDA hoja


can.showPage()
can.setFont("Helvetica", 5)
for i in range(0, 1200, 10):
    can.drawString(i, 850, str(i))

for i in range(0, 1600, 10):
    can.drawString(350, i, str(i))

can.setFont("Helvetica", 20)
# Numero de ficha
can = texto_separado(txt='C12-0000162', isseparado=False, ubix=840, ubiy=1342, canv=can)
can = texto_separado(txt='tt-0000162', isseparado=False, ubix=840, ubiy=1294, canv=can)

completa = False
if completa:
    can = texto_separado(txt='XXX', isseparado=False, ubix=840, ubiy=1242, canv=can)
else:
    can = texto_separado(txt='XXX', isseparado=False, ubix=910, ubiy=1242, canv=can)

# Localizacion
can = texto_separado(txt='Ayac', isseparado=False, ubix=107, ubiy=1201, canv=can)
can = texto_separado(txt='001', isseparado=False, ubix=173, ubiy=1201, canv=can)
can = texto_separado(txt='001', isseparado=False, ubix=233, ubiy=1201, canv=can)
can = texto_separado(txt='001', isseparado=False, ubix=293, ubiy=1201, canv=can)
can = texto_separado(txt='sdf', isseparado=False, ubix=390, ubiy=1201, canv=can)
can = texto_separado(txt='y-997', isseparado=False, ubix=465, ubiy=1201, canv=can)
can = texto_separado(txt='Av.Los incas ...', isseparado=False, ubix=603, ubiy=1201, canv=can)

# ubicado en
olist = Lista(choise=ubicado_choices, ubix=120, lubiy=[1118, 1099, 1078, 1060], text='OTRO', otro=True,
              ubixotro=170, ubiyotro=1060, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)
# accesibilidad al buzon
variable_accesibilidad = True
if variable_accesibilidad:
    can = texto_separado(txt='X', isseparado=False, ubix=311, ubiy=1119, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=311, ubiy=1099, canv=can)
    # falta especifique
olist = Lista(choise=accesibilidad_tipo_choice, ubix=372, lubiy=[1080, 1060, 1040, 1020, 1000], text='OTRO', otro=True,
              ubixotro=426, ubiyotro=1003, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

# corrdenadas
can = texto_separado(txt='CORRDENADA X.', isseparado=False, ubix=530, ubiy=1090, canv=can)
can = texto_separado(txt='CORRDENADA y .', isseparado=False, ubix=530, ubiy=1036, canv=can)
can = texto_separado(txt='cota tapa .', isseparado=False, ubix=805, ubiy=1090, canv=can)
can = texto_separado(txt='cota fondo .', isseparado=False, ubix=805, ubiy=1036, canv=can)

# datos fisicos
# tipo buzon
olist = Lista(choise=tipo_buzon_choice, lubix=[120, 120, 120, 288, 288, 288, 453],
              lubiy=[903, 882, 860, 903, 882, 860, 903], text='OTRO', otro=True,
              ubixotro=505, ubiyotro=907, otrotext='asdasdasd')
olist.crear_bloque_especial()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)
# montaje buzon
olist = Lista(choise=montaje_buzon_choice, ubix=635, lubiy=[903, 882, 861], text='EMISOR', otro=True,
              ubixotro=700, ubiyotro=866, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.text == 'EMISOR':
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isseparado=False, isred=True, canv=can)
montaje_sabuzon_choice = ['PRIMARIO', 'SECUNDARIO', 'EMISOR', ]

# buzon de arranque
buzonarranque = False
if buzonarranque:
    can = texto_separado(txt='X', isseparado=False, ubix=905, ubiy=890, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=905, ubiy=870, canv=can)

# tapa
tapa_var = True
if tapa_var:
    can = texto_separado(txt='X', isseparado=False, ubix=168, ubiy=816, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=213, ubiy=816, canv=can)


olist = Lista(choise=fuste_mesa_estado_choice, ubix=850, lubiy=[400, 440, 430, 420, 410], text='BUENO', otro=True,
              ubixotro=362, ubiyotro=960, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)
# accesibilidad al buzon


# estado mesa
variable_escalera = False
if variable_escalera:
    can = texto_separado(txt='X.', isseparado=False, ubix=570, ubiy=400, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=630, ubiy=400, canv=can)

# choise=[], ubix=0, ubiy=0, separacion=0, lubix=[], lubiy=[], text=None, otro=False,
# ubixotro=0, ubiyotro=0, otrotext=None
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
existing_pdf = PdfFileReader(open("fichav2.pdf", "rb"))
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
outputStream = open("destinoa4v2.pdf", "wb")
output.write(outputStream)
outputStream.close()
