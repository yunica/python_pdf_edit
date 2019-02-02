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
# #vista_panoramica1
# can.drawImage('iamgen.jpg', 140, 465,640,480)
# #vista_panoramica1
# can.drawImage('iamgen.jpg', 480, 227,227,170)
#
#
#


#
can = texto_separado(txt='17/01/2019', isseparado=False, txtsize=23, ubix=100, ubiy=166, canv=can)
can = texto_separado(txt='wjfhrutb', isseparado=False, txtsize=23, ubix=300, ubiy=166, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, txtsize=23, ubix=475, ubiy=166, canv=can)
can = texto_separado(txt='Jose Flores', isseparado=False, txtsize=23, ubix=645, ubiy=166, canv=can)
can = texto_separado(txt='Pepe Flores', isseparado=False, txtsize=23, ubix=820, ubiy=166, canv=can)

#                   SEGUNDA hoja


can.showPage()

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
seguridad_var = True
if tapa_var:
    can = texto_separado(txt='X', isseparado=False, ubix=344, ubiy=816, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=390, ubiy=816, canv=can)

# centrico excentrico
olist = Lista(choise=tapa_centrico_choice, ubiy=787, lubix=[154, 253], text='EXCENTRICO')
olist.crear_bloque_horizontal()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# sellado hermetico
sellado_hermetico = False
if sellado_hermetico:
    can = texto_separado(txt='X', isseparado=False, ubix=325, ubiy=770, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=370, ubiy=770, canv=can)

can = texto_separado(txt='CENTRICO', isseparado=False, ubix=158, ubiy=760, canv=can)

# estado
olist = Lista(choise=estado_generico, lubix=[460, 460, 562, 560],
              lubiy=[772, 752, 772, 772], text='REGULAR')
olist.crear_bloque_especial()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

# geometria
olist = Lista(choise=tapa_geometria_choice, ubix=140, lubiy=[698, 675, 657], text='OTRO', otro=True,
              ubixotro=190, ubiyotro=658, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isseparado=False, isred=True, canv=can)
# medida
can = texto_separado(txt='diametro', isseparado=False, txtsize=15, ubix=360, ubiy=698, canv=can)
can = texto_separado(txt='espesor', isseparado=False, txtsize=15, ubix=360, ubiy=676, canv=can)
# material
olist = Lista(choise=material_tapa_choice, ubix=462, lubiy=[707, 689, 671, 653], text='OTRO', otro=True,
              ubixotro=514, ubiyotro=658, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=10,
                         isseparado=False, isred=True, canv=can)

anillo = True
if anillo:
    can = texto_separado(txt='X', isseparado=False, ubix=225, ubiy=610, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=285, ubiy=610, canv=can)

# anillo material
olist = Lista(choise=material_anillo_choice, ubix=140, lubiy=[570, 550, 530], text='OTRO', otro=True,
              ubixotro=193, ubiyotro=532, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=10,
                         isseparado=False, isred=True, canv=can)

# material
olist = Lista(choise=estado_generico, ubix=300, lubiy=[571, 550, 530], text='MALO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# respiradero
respiradero = False
if respiradero:
    can = texto_separado(txt='X', isseparado=False, ubix=555, ubiy=610, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=609, ubiy=610, canv=can)
# respiradero pestaña
respiradero_pestania = False
if respiradero_pestania:
    can = texto_separado(txt='X', isseparado=False, ubix=489, ubiy=568, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=489, ubiy=546, canv=can)
# respiradero pasador
respiradero_pasador = False
if respiradero_pasador:
    can = texto_separado(txt='X', isseparado=False, ubix=570, ubiy=568, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=570, ubiy=546, canv=can)

# techo
olist = Lista(choise=geometria_techo_choice, ubix=706, lubiy=[774, 753], text='CUADRADA')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# estado
olist = Lista(choise=estado_generico, ubix=864, lubiy=[772, 753, 732], text='MALO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# techi_anillo
techo_anillo = True
if techo_anillo:
    can = texto_separado(txt='X', isseparado=False, ubix=835, ubiy=675, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=890, ubiy=675, canv=can)

# techo anillo material
olist = Lista(choise=techo_anillo_material_choice, ubix=715, lubiy=[630, 605], text='OTRO', otro=True,
              ubixotro=770, ubiyotro=604, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=10,
                         isseparado=False, isred=True, canv=can)
# estado
olist = Lista(choise=estado_generico, ubix=870, lubiy=[625, 605, 585], text='BUENO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

# fuste geometria
olist = Lista(choise=fuste_geometria_choice, ubix=135, lubiy=[440, 420, 399], text='CONICO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=estado_generico, ubix=275, lubiy=[440, 420, 399], text='MALO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

# material
olist = Lista(choise=fuste_material_choice, ubix=410, lubiy=[440, 420, 399], text='OTRO', otro=True,
              ubixotro=460, ubiyotro=400, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=10,
                         isseparado=False, isred=True, canv=can)

escalera = False
if escalera:
    can = texto_separado(txt='X', isseparado=False, ubix=580, ubiy=438, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=640, ubiy=438, canv=can)

can = texto_separado(txt='123456', isseparado=False, ubix=580, ubiy=385, canv=can)

# estado
olist = Lista(choise=estado_generico, ubix=695, lubiy=[423, 402, 382], text='BUENO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# mesa-estado-mesa
olist = Lista(choise=fuste_mesa_estado_choice, ubix=855, lubiy=[443, 425, 408, 392, 372], text='OTRO', otro=True,
              ubixotro=860, ubiyotro=355, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=10,
                         isseparado=False, isred=True, canv=can)
can = texto_separado(txt='123456789123', txtsize=19, isseparado=False, ubix=825, ubiy=280, canv=can)
can = texto_separado(txt='123456789123', txtsize=19, isseparado=False, ubix=825, ubiy=233, canv=can)
desface_techo = True
if desface_techo:
    can = texto_separado(txt='X', isseparado=False, ubix=306, ubiy=295, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=306, ubiy=270, canv=can)
#
desface_tapa = False
if desface_tapa:
    can = texto_separado(txt='X', isseparado=False, ubix=465, ubiy=294, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=465, ubiy=269, canv=can)
#
desface_tapa = True
if desface_tapa:
    can = texto_separado(txt='X', isseparado=False, ubix=625, ubiy=294, canv=can)
else:
    can = texto_separado(txt='X', isseparado=False, ubix=625, ubiy=269, canv=can)

can = texto_separado(txt='17/01/2019', isseparado=False, txtsize=23, ubix=100, ubiy=168, canv=can)
can = texto_separado(txt='wjfhrutb', isseparado=False, txtsize=23, ubix=300, ubiy=168, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, txtsize=23, ubix=475, ubiy=168, canv=can)
can = texto_separado(txt='Jose Flores', isseparado=False, txtsize=23, ubix=645, ubiy=168, canv=can)
can = texto_separado(txt='Pepe Flores', isseparado=False, txtsize=23, ubix=820, ubiy=168, canv=can)
# tercera pagina

can.showPage()
can.setFont("Helvetica", 5)
for i in range(0, 1200, 10):
    can.drawString(i, 1230, str(i))
    can.drawString(i, 860, str(i))
    can.drawString(i, 660, str(i))
    can.drawString(i, 460, str(i))
    can.drawString(i, 360, str(i))
    can.drawString(i, 360, str(i))
    can.drawString(i, 180, str(i))
    can.drawString(i, 100, str(i))

for i in range(0, 1600, 10):
    can.drawString(150, i, str(i))
    can.drawString(700, i, str(i))
    can.drawString(350, i, str(i))
    can.drawString(450, i, str(i))
    can.drawString(860, i, str(i))

for i in range(0, 600, 30):
    can.drawString(i, 770, str(i))
    can.drawString(i, 220, str(i))
can.setFont("Helvetica", 20)
# Numero de ficha
can = texto_separado(txt='C12-0000162', isseparado=False, ubix=840, ubiy=1342, canv=can)
can = texto_separado(txt='tt-0000162', isseparado=False, ubix=840, ubiy=1294, canv=can)
list_estado = 'FUNCIONANDO,COLMATADO (ATORADO),SEDIMENTADO,CON ESCOMBROS/BASURA'.split(',')
if list_estado:
    for i in list_estado:
        olist = Lista(choise=estado_buzon_choice, lubix=[135, 135, 288, 288, 440],
                      lubiy=[1175, 1148, 1175, 1148, 1175, ], text=i, otro=True, ubixotro=490, ubiyotro=1178,
                      otrotext='asdasdasd')
        olist.crear_bloque_especial()
        if olist.get_punto():
            can.setFont("Helvetica", 20)
            can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
        if olist.get_otro():
            can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro),
                                 txtsize=10, isseparado=False, isred=True, canv=can)

olist = Lista(choise=escala_olores_choices, ubix=606, lubiy=[1189, 1160, 1132], text='BAJO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

texto_separado(txt='X', ubix=885, ubiy=1212, txtsize=20, isseparado=False, canv=can)
texto_separado(txt='X', ubix=938, ubiy=1211, txtsize=20, isseparado=False, canv=can)
texto_separado(txt='21', ubix=885, ubiy=1185, txtsize=14, isseparado=False, canv=can)
# diametro
texto_separado(txt='diametro1', ubix=810, ubiy=1143, txtsize=14, isseparado=False, canv=can)
texto_separado(txt='material1', ubix=810, ubiy=1119, txtsize=14, isseparado=False, canv=can)

texto_separado(txt='1', ubix=810, ubiy=1094, txtsize=20, isseparado=False, canv=can)
texto_separado(txt='2', ubix=870, ubiy=1094, txtsize=20, isseparado=False, canv=can)

texto_separado(txt='diametro12', ubix=810, ubiy=1057, txtsize=14, isseparado=False, canv=can)
texto_separado(txt='material12', ubix=810, ubiy=1033, txtsize=14, isseparado=False, canv=can)

texto_separado(txt='3', ubix=810, ubiy=1010, txtsize=20, isseparado=False, canv=can)
texto_separado(txt='4', ubix=870, ubiy=1010, txtsize=20, isseparado=False, canv=can)
#
olist = Lista(choise=llegada_choice, ubix=135, lubiy=[1068, 1040], text='GRAVEDAD')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=cantidad_sedimento_choice, ubix=322, lubiy=[1075, 1054, 1034], text='POCA O NULA CANTIDAD DE SEDIMENTO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.setFont("Helvetica", 20)
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

can = texto_separado(txt='sftgre', isseparado=False, txtsize=25, ubix=530, ubiy=920, canv=can)

can = texto_separado(txt='sftgre', isseparado=False, ubix=220, txtsize=25, ubiy=865, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=380, txtsize=25, ubiy=865, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=530, txtsize=25, ubiy=865, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=690, txtsize=25, ubiy=865, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=840, txtsize=25, ubiy=865, canv=can)

can = texto_separado(txt='sftgre', isseparado=False, ubix=220, txtsize=25, ubiy=822, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=380, txtsize=25, ubiy=822, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=530, txtsize=25, ubiy=822, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=690, txtsize=25, ubiy=822, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=840, txtsize=25, ubiy=822, canv=can)

can = texto_separado(txt='sftgre', isseparado=False, ubix=220, txtsize=25, ubiy=777, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=380, txtsize=25, ubiy=777, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=530, txtsize=25, ubiy=777, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=690, txtsize=25, ubiy=777, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=840, txtsize=25, ubiy=777, canv=can)

can = texto_separado(txt='sftgre', isseparado=False, ubix=220, txtsize=25, ubiy=732, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=380, txtsize=25, ubiy=732, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=530, txtsize=25, ubiy=732, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=690, txtsize=25, ubiy=732, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=840, txtsize=25, ubiy=732, canv=can)


can = texto_separado(txt='sftgre', isseparado=False, txtsize=25, ubix=530, ubiy=673, canv=can)

can = texto_separado(txt='sftgre', isseparado=False, ubix=220, txtsize=25, ubiy=615, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=380, txtsize=25, ubiy=615, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=530, txtsize=25, ubiy=615, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=690, txtsize=25, ubiy=615, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=840, txtsize=25, ubiy=615, canv=can)

can = texto_separado(txt='sftgre', isseparado=False, ubix=220, txtsize=25, ubiy=570, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=380, txtsize=25, ubiy=570, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=530, txtsize=25, ubiy=570, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=690, txtsize=25, ubiy=570, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=840, txtsize=25, ubiy=570, canv=can)

can = texto_separado(txt='sftgre', isseparado=False, ubix=220, txtsize=25, ubiy=523, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=380, txtsize=25, ubiy=523, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=530, txtsize=25, ubiy=523, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=690, txtsize=25, ubiy=523, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, ubix=840, txtsize=25, ubiy=523, canv=can)


# Loc

ptext = """Lorem ipsum dolor sit amet, consectetur adipisicing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
        culpa qui officia deserunt mollit anim id est laborum."""
p = Paragraph(ptext, style=getSampleStyleSheet()["Normal"])
p.wrapOn(can, 800, 20)
p.drawOn(can, 110, 225)

can = texto_separado(txt='17/01/2019', isseparado=False, txtsize=23, ubix=100, ubiy=168, canv=can)
can = texto_separado(txt='wjfhrutb', isseparado=False, txtsize=23, ubix=300, ubiy=168, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, txtsize=23, ubix=475, ubiy=168, canv=can)
can = texto_separado(txt='Jose Flores', isseparado=False, txtsize=23, ubix=645, ubiy=168, canv=can)
can = texto_separado(txt='Pepe Flores', isseparado=False, txtsize=23, ubix=820, ubiy=168, canv=can)

#                   CUARTAa hoja
can.showPage()

can.setFont("Helvetica", 20)
# Numero de ficha
can = texto_separado(txt='C12-0000162', isseparado=False, ubix=840, ubiy=1342, canv=can)
can = texto_separado(txt='tt-0000162', isseparado=False, ubix=840, ubiy=1294, canv=can)

# Localizacion
can = texto_separado(txt='Ayac', isseparado=False, ubix=107, ubiy=1212, canv=can)
can = texto_separado(txt='001', isseparado=False, ubix=173, ubiy=1212, canv=can)
can = texto_separado(txt='001', isseparado=False, ubix=233, ubiy=1212, canv=can)
can = texto_separado(txt='001', isseparado=False, ubix=293, ubiy=1212, canv=can)
can = texto_separado(txt='sdf', isseparado=False, ubix=390, ubiy=1212, canv=can)
can = texto_separado(txt='Av.Los incas ...', isseparado=False, ubix=465, ubiy=1212, canv=can)

can = texto_separado(txt='17/01/2019', isseparado=False, txtsize=23, ubix=100, ubiy=168, canv=can)
can = texto_separado(txt='wjfhrutb', isseparado=False, txtsize=23, ubix=300, ubiy=168, canv=can)
can = texto_separado(txt='sftgre', isseparado=False, txtsize=23, ubix=475, ubiy=168, canv=can)
can = texto_separado(txt='Jose Flores', isseparado=False, txtsize=23, ubix=645, ubiy=168, canv=can)
can = texto_separado(txt='Pepe Flores', isseparado=False, txtsize=23, ubix=820, ubiy=168, canv=can)

# # imagenes
# #vista_panoramica1
# can.drawImage('iamgen.jpg', 110, 810,400,300)
# #vista_panoramica1
# can.drawImage('iamgen.jpg', 548, 810,400,300)
# #fotografia_interna1
# can.drawImage('iamgen.jpg', 110, 365,400,300)
# #fotografia_interna2
# can.drawImage('iamgen.jpg', 548, 365,400,300)
#


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
outputStream = open("destinoa4v2old.pdf", "wb")
output.write(outputStream)
outputStream.close()
