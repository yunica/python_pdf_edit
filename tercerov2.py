from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, blue
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from PIL import Image

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


def resize_image(tamanio, muestra):
    if tamanio:
        x, y = tamanio
        try:

            num = muestra / y
            peque = round(num, 4)
            return peque
        except Exception:
            pass
    return 1


def ficha_num(txt='123456', canv=None):
    canv.setFontSize(20)
    canv.setFillColor(red)
    canv.drawString(485, 748, txt)
    canv.setFontSize(12)
    canv.setFillColor(blue)
    return canv


def texto_separado(txt=None, isred=False, isseparado=False, txtsize=12, ubix=0, ubiy=0,
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

#                   PRIMERA hoja

# numero ficha
can = texto_separado(txt='C12-0000162', ubix=470, ubiy=775, canv=can)
can = texto_separado(txt='tt-0000162', ubix=470, ubiy=735, canv=can)
can = texto_separado(txt='rr-4869', ubix=470, ubiy=690, canv=can)
can = texto_separado(txt='aa-785', ubix=470, ubiy=663, canv=can)
# Localizacion
can = texto_separado(txt='05', ubix=40, ubiy=707, canv=can)
can = texto_separado(txt='001', ubix=75, ubiy=707, canv=can)
can = texto_separado(txt='001', ubix=109, ubiy=707, canv=can)
can = texto_separado(txt='001', ubix=145, ubiy=707, canv=can)
can = texto_separado(txt='sdf', ubix=200, ubiy=707, canv=can)
can = texto_separado(txt='Av.Los incas con numero # 170', ubix=245, txtsize=7,
                     ubiy=705, canv=can)
# cotas del esquinero
can = texto_separado(txt='012 ', ubix=40, ubiy=663, canv=can)
can = texto_separado(txt='013', ubix=113, ubiy=663, canv=can)
can = texto_separado(txt='014', ubix=180, ubiy=663, canv=can)
can = texto_separado(txt='016', ubix=250, ubiy=663, canv=can)
can = texto_separado(txt='0176', ubix=330, ubiy=663, canv=can)
can = texto_separado(txt='018', ubix=410, ubiy=663, canv=can)

# grilla ubicacion
grilla = 18
grilla_x = None
list_grilla_y = [0, 172, 161, 150, 140, 129, 118, 107, 94,
                 94, 107, 118, 129, 140, 150, 161, 172,
                 172, 161, 150, 140, 129, 118, 107, 94,
                 94, 107, 118, 129, 140, 150, 161, 172,
                 172, 161, 150, 140, 129, 118, 107, 94, ]
if grilla <= 8 and grilla >= 1:
    grilla_x = 73
if grilla <= 16 and grilla >= 9:
    grilla_x = 88
if grilla <= 24 and grilla >= 17:
    grilla_x = 100
if grilla <= 32 and grilla >= 25:
    grilla_x = 115
if grilla <= 40 and grilla >= 33:
    grilla_x = 130
can = texto_separado(txt='x', txtsize=16, ubix=grilla_x, ubiy=list_grilla_y[grilla], canv=can)

#
# vista_panoramica1
im = Image.open('iamgen.jpg')
peque = resize_image(im.size, 280)
x, y = im.size
can.drawImage('iamgen.jpg', 53, 225, x * peque, y * peque)
peque = resize_image(im.size, 110)

can.drawImage('iamgen.jpg', 200, 70, x * peque, y * peque)

#
can = texto_separado(txt='17/01/2019', ubix=32, ubiy=32, canv=can)
can = texto_separado(txt='wjfhrutb', ubix=150, ubiy=32, canv=can)
can = texto_separado(txt='sftgre', ubix=250, ubiy=32, canv=can)
can = texto_separado(txt='Jose Flores', ubix=350, ubiy=32, canv=can)
can = texto_separado(txt='Pepe Flores', ubix=460, ubiy=32, canv=can)

#                   SEGUNDA hoja


can.showPage()

can = texto_separado(txt='C12-0000162', ubix=470, ubiy=788, canv=can)
can = texto_separado(txt='tt-0000162', ubix=470, ubiy=758, canv=can)
# Localizacion
can = texto_separado(txt='05', ubix=40, ubiy=700, canv=can)
can = texto_separado(txt='001', ubix=78, ubiy=700, canv=can)
can = texto_separado(txt='001', ubix=112, ubiy=700, canv=can)
can = texto_separado(txt='001', ubix=150, ubiy=700, canv=can)
can = texto_separado(txt='sdf', ubix=200, ubiy=700, canv=can)
can = texto_separado(txt='sdf', ubix=250, ubiy=700, canv=can)

can = texto_separado(txt='Av.Los incas con numero # 170', ubix=330, txtsize=7,
                     ubiy=700, canv=can)

if False:
    can = texto_separado(txt='XXX', ubix=470, ubiy=728, canv=can)
else:
    can = texto_separado(txt='XXX', ubix=515, ubiy=728, canv=can)

# ubicado en
olist = Lista(choise=ubicado_choices, ubix=46, lubiy=[646, 633, 619, 606], text='OTRO', otro=True,
              ubixotro=80, ubiyotro=608, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isred=True, canv=can)
# accesibilidad al buzon
variable_accesibilidad = True
if variable_accesibilidad:
    can = texto_separado(txt='X', ubix=159, ubiy=646, canv=can)
else:
    can = texto_separado(txt='X', ubix=159, ubiy=632, canv=can)
    # falta especifique
olist = Lista(choise=accesibilidad_tipo_choice, ubix=195, lubiy=[622, 608, 594, 582, 568], text='OTRO', otro=True,
              ubixotro=229, ubiyotro=570, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isred=True, canv=can)

# corrdenadas
can = texto_separado(txt='CORRDENADA X.', ubix=290, ubiy=626, canv=can)
can = texto_separado(txt='CORRDENADA y .', ubix=290, ubiy=590, canv=can)
can = texto_separado(txt='cota tapa .', ubix=455, ubiy=626, canv=can)
can = texto_separado(txt='cota fondo .', ubix=455, ubiy=590, canv=can)

# datos fisicos   -------  tipo buzon
olist = Lista(choise=tipo_buzon_choice, lubix=[46, 46, 46, 143, 143, 143, 243],
              lubiy=[507, 494, 481, 507, 494, 481, 507], text='OTRO', otro=True,
              ubixotro=276, ubiyotro=246, otrotext='asdasdasd')
olist.crear_bloque_especial()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isred=True, canv=can)
# montaje buzon
olist = Lista(choise=montaje_buzon_choice, ubix=351, lubiy=[507, 493, 480], text='EMISOR', otro=True,
              ubixotro=390, ubiyotro=484, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.text == 'EMISOR':
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isred=True, canv=can)
montaje_sabuzon_choice = ['PRIMARIO', 'SECUNDARIO', 'EMISOR', ]

# buzon de arranque
buzonarranque = False
if buzonarranque:
    can = texto_separado(txt='X', ubix=510, ubiy=498, canv=can)
else:
    can = texto_separado(txt='X', ubix=510, ubiy=485, canv=can)

# tapa
tapa_var = True
if tapa_var:
    can = texto_separado(txt='X', ubix=76, ubiy=452, canv=can)
else:
    can = texto_separado(txt='X', ubix=101, ubiy=452, canv=can)
seguridad_var = True
if tapa_var:
    can = texto_separado(txt='X', ubix=178, ubiy=452, canv=can)
else:
    can = texto_separado(txt='X', ubix=205, ubiy=452, canv=can)

# centrico excentrico
olist = Lista(choise=tapa_centrico_choice, ubiy=432, lubix=[68, 127], text='EXCENTRICO')
olist.crear_bloque_horizontal()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# sellado hermetico
sellado_hermetico = False
if sellado_hermetico:
    can = texto_separado(txt='X', ubix=170, ubiy=424, canv=can)
else:
    can = texto_separado(txt='X', ubix=195, ubiy=421, canv=can)

# estado
olist = Lista(choise=estado_generico, lubix=[249, 249, 307, 307],
              lubiy=[424, 409, 424, 424], text='REGULAR')
olist.crear_bloque_especial()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

# geometria
olist = Lista(choise=tapa_geometria_choice, ubix=58, lubiy=[376, 362, 349], text='OTRO', otro=True,
              ubixotro=93, ubiyotro=348, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isred=True, canv=can)
# medida
can = texto_separado(txt='diametro', txtsize=9, ubix=190, ubiy=375, canv=can)
can = texto_separado(txt='espesor', txtsize=9, ubix=190, ubiy=362, canv=can)
# material
olist = Lista(choise=material_tapa_choice, ubix=249, lubiy=[381, 371, 360, 348], text='OTRO', otro=True,
              ubixotro=280, ubiyotro=348, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isred=True, canv=can)

anillo = True
if anillo:
    can = texto_separado(txt='X', ubix=108, ubiy=317, canv=can)
else:
    can = texto_separado(txt='X', ubix=144, ubiy=317, canv=can)

# anillo material
olist = Lista(choise=material_anillo_choice, ubix=58, lubiy=[294, 280, 267], text='OTRO', otro=True,
              ubixotro=95, ubiyotro=269, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isred=True, canv=can)

# material estado
olist = Lista(choise=estado_generico, ubix=153, lubiy=[294, 280, 267], text='MALO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# respiradero
respiradero = False
if respiradero:
    can = texto_separado(txt='X', ubix=303, ubiy=318, canv=can)
else:
    can = texto_separado(txt='X', ubix=335, ubiy=318, canv=can)
# respiradero pestaña
respiradero_pestania = False
if respiradero_pestania:
    can = texto_separado(txt='X', ubix=265, ubiy=292, canv=can)
else:
    can = texto_separado(txt='X', ubix=265, ubiy=278, canv=can)
# respiradero pasador
respiradero_pasador = False
if respiradero_pasador:
    can = texto_separado(txt='X', ubix=311, ubiy=292, canv=can)
else:
    can = texto_separado(txt='X', ubix=311, ubiy=278, canv=can)

# techo ----
olist = Lista(choise=geometria_techo_choice, ubix=393, lubiy=[424, 412], text='CUADRADA')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# estado
olist = Lista(choise=estado_generico, ubix=485, lubiy=[424, 410, 396], text='MALO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# techi_anillo
techo_anillo = True
if techo_anillo:
    can = texto_separado(txt='X', ubix=461, ubiy=359, canv=can)
else:
    can = texto_separado(txt='X', ubix=502, ubiy=359, canv=can)

# techo anillo material
olist = Lista(choise=techo_anillo_material_choice, ubix=397, lubiy=[334, 316], text='OTRO', otro=True,
              ubixotro=430, ubiyotro=314, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isred=True, canv=can)
# estado
olist = Lista(choise=estado_generico, ubix=488, lubiy=[329, 316, 303], text='REGULAR')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

# fuste geometria
olist = Lista(choise=fuste_geometria_choice, ubix=55, lubiy=[210, 196, 183], text='CONICO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=estado_generico, ubix=138, lubiy=[210, 196, 183], text='MALO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

# material
olist = Lista(choise=fuste_material_choice, ubix=218, lubiy=[210, 196, 183], text='OTRO', otro=True,
              ubixotro=250, ubiyotro=182, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isred=True, canv=can)

escalera = False
if escalera:
    can = texto_separado(txt='X', ubix=318, ubiy=208, canv=can)
else:
    can = texto_separado(txt='X', ubix=355, ubiy=208, canv=can)

can = texto_separado(txt='123456', ubix=305, ubiy=172, canv=can)

# estado
olist = Lista(choise=estado_generico, ubix=385, lubiy=[198, 186, 172], text='BUENO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# mesa-estado-mesa
olist = Lista(choise=fuste_mesa_estado_choice, ubix=482, lubiy=[213, 200, 191, 179, 169], text='OTRO', otro=True,
              ubixotro=485, ubiyotro=155, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro), txtsize=7,
                         isred=True, canv=can)
can = texto_separado(txt='123456789123', ubix=460, ubiy=107, canv=can)
can = texto_separado(txt='123456789123', ubix=460, ubiy=78, canv=can)
desface_techo = True
if desface_techo:
    can = texto_separado(txt='X', ubix=158, ubiy=116, canv=can)
else:
    can = texto_separado(txt='X', ubix=158, ubiy=100, canv=can)
#
desface_tapa = False
if desface_tapa:
    can = texto_separado(txt='X', ubix=252, ubiy=116, canv=can)
else:
    can = texto_separado(txt='X', ubix=252, ubiy=100, canv=can)
#
desface_tapa = True
if desface_tapa:
    can = texto_separado(txt='X', ubix=345, ubiy=116, canv=can)
else:
    can = texto_separado(txt='X', ubix=345, ubiy=100, canv=can)

can = texto_separado(txt='17/01/2019', ubix=32, ubiy=34, canv=can)
can = texto_separado(txt='wjfhrutb', ubix=150, ubiy=34, canv=can)
can = texto_separado(txt='sftgre', ubix=250, ubiy=34, canv=can)
can = texto_separado(txt='Jose Flores', ubix=350, ubiy=34, canv=can)
can = texto_separado(txt='Pepe Flores', ubix=460, ubiy=33, canv=can)
# tercera pagina


can = texto_separado(txt='C12-0000162', ubix=470, ubiy=787, canv=can)
can = texto_separado(txt='tt-0000162', ubix=470, ubiy=757, canv=can)


list_estado = 'FUNCIONANDO,COLMATADO (ATORADO),SEDIMENTADO,CON ESCOMBROS/BASURA'.split(',')
if list_estado:
    for i in list_estado:
        olist = Lista(choise=estado_buzon_choice, lubix=[57, 57, 145, 145, 238],
                      lubiy=[680, 664, 680, 664, 680, ], text=i, otro=True, ubixotro=268, ubiyotro=682,
                      otrotext='asdasdasd')
        olist.crear_bloque_especial()
        if olist.get_punto():
            can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
        if olist.get_otro():
            can = texto_separado(txt=olist.otrotext, ubix=int(olist.ubixotro), ubiy=int(olist.ubiyotro),
                                 txtsize=7, isred=True, canv=can)

olist = Lista(choise=escala_olores_choices, ubix=333, lubiy=[690, 672, 654], text='BAJO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

texto_separado(txt='X', ubix=499, ubiy=704, txtsize=15, canv=can)
texto_separado(txt='X', ubix=530, ubiy=704, txtsize=15, canv=can)
texto_separado(txt='21', ubix=498, ubiy=687, txtsize=9, canv=can)
# diametro
texto_separado(txt='diametro1', ubix=455, ubiy=661,  canv=can)
texto_separado(txt='material1', ubix=455, ubiy=646,  canv=can)


#
olist = Lista(choise=llegada_choice, ubix=56, lubiy=[612, 596], text='GRAVEDAD')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=cantidad_sedimento_choice, ubix=165, lubiy=[618, 604, 591],
              text='POCA O NULA CANTIDAD DE SEDIMENTO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

can = texto_separado(txt='sftgre', txtsize=15, ubix=300, ubiy=518, canv=can)

can = texto_separado(txt='sftgre', ubix=105, txtsize=15, ubiy=483, canv=can)
can = texto_separado(txt='sftgre', ubix=197, txtsize=15, ubiy=483, canv=can)
can = texto_separado(txt='sftgre', ubix=288, txtsize=15, ubiy=483, canv=can)
can = texto_separado(txt='sftgre', ubix=380, txtsize=15, ubiy=483, canv=can)
can = texto_separado(txt='sftgre', ubix=473, txtsize=15, ubiy=483, canv=can)

can = texto_separado(txt='sftgre', ubix=105, txtsize=15, ubiy=454, canv=can)
can = texto_separado(txt='sftgre', ubix=197, txtsize=15, ubiy=454, canv=can)
can = texto_separado(txt='sftgre', ubix=288, txtsize=15, ubiy=454, canv=can)
can = texto_separado(txt='sftgre', ubix=380, txtsize=15, ubiy=454, canv=can)
can = texto_separado(txt='sftgre', ubix=473, txtsize=15, ubiy=454, canv=can)

can = texto_separado(txt='sftgre', ubix=105, txtsize=15, ubiy=425, canv=can)
can = texto_separado(txt='sftgre', ubix=197, txtsize=15, ubiy=425, canv=can)
can = texto_separado(txt='sftgre', ubix=288, txtsize=15, ubiy=425, canv=can)
can = texto_separado(txt='sftgre', ubix=380, txtsize=15, ubiy=425, canv=can)
can = texto_separado(txt='sftgre', ubix=473, txtsize=15, ubiy=425, canv=can)

can = texto_separado(txt='sftgre', ubix=105, txtsize=15, ubiy=397, canv=can)
can = texto_separado(txt='sftgre', ubix=197, txtsize=15, ubiy=397, canv=can)
can = texto_separado(txt='sftgre', ubix=288, txtsize=15, ubiy=397, canv=can)
can = texto_separado(txt='sftgre', ubix=380, txtsize=15, ubiy=397, canv=can)
can = texto_separado(txt='sftgre', ubix=473, txtsize=15, ubiy=397, canv=can)

can = texto_separado(txt='sftgre', txtsize=15, ubix=300, ubiy=360, canv=can)

can = texto_separado(txt='sftgre', ubix=105, txtsize=15, ubiy=322, canv=can)
can = texto_separado(txt='sftgre', ubix=197, txtsize=15, ubiy=322, canv=can)
can = texto_separado(txt='sftgre', ubix=288, txtsize=15, ubiy=322, canv=can)
can = texto_separado(txt='sftgre', ubix=380, txtsize=15, ubiy=322, canv=can)
can = texto_separado(txt='sftgre', ubix=473, txtsize=15, ubiy=322, canv=can)

can = texto_separado(txt='sftgre', ubix=105, txtsize=15, ubiy=293, canv=can)
can = texto_separado(txt='sftgre', ubix=197, txtsize=15, ubiy=293, canv=can)
can = texto_separado(txt='sftgre', ubix=288, txtsize=15, ubiy=293, canv=can)
can = texto_separado(txt='sftgre', ubix=380, txtsize=15, ubiy=293, canv=can)
can = texto_separado(txt='sftgre', ubix=473, txtsize=15, ubiy=293, canv=can)

can = texto_separado(txt='sftgre', ubix=105, txtsize=15, ubiy=265, canv=can)
can = texto_separado(txt='sftgre', ubix=197, txtsize=15, ubiy=265, canv=can)
can = texto_separado(txt='sftgre', ubix=288, txtsize=15, ubiy=265, canv=can)
can = texto_separado(txt='sftgre', ubix=380, txtsize=15, ubiy=265, canv=can)
can = texto_separado(txt='sftgre', ubix=473, txtsize=15, ubiy=265, canv=can)

# Loc
can.setFont("Helvetica", 10)
ptext = """Lorem ipsum dolor sit amet, consectetur adipisicing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco """
p = Paragraph(ptext, style=getSampleStyleSheet()["Normal"],)
p.wrapOn(can, 530, 20)
p.drawOn(can, 40, 70)

can = texto_separado(txt='17/01/2019', ubix=32, ubiy=33, canv=can)
can = texto_separado(txt='wjfhrutb', ubix=150, ubiy=33, canv=can)
can = texto_separado(txt='sftgre', ubix=250, ubiy=33, canv=can)
can = texto_separado(txt='Jose Flores', ubix=350, ubiy=33, canv=can)
can = texto_separado(txt='Pepe Flores', ubix=460, ubiy=33, canv=can)

#                   CUARTAa hoja
can.showPage()

can.showPage()
can.setFont("Helvetica", 2)
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
    can.drawString(820, i, str(i))
# Numero de ficha
# Numero de ficha
can = texto_separado(txt='C12-0000162', ubix=470, ubiy=778, canv=can)
can = texto_separado(txt='tt-0000162', ubix=470, ubiy=746, canv=can)
# Localizacion
can = texto_separado(txt='05', ubix=40, ubiy=697, canv=can)
can = texto_separado(txt='001', ubix=78, ubiy=697, canv=can)
can = texto_separado(txt='001', ubix=112, ubiy=697, canv=can)
can = texto_separado(txt='001', ubix=150, ubiy=697, canv=can)
can = texto_separado(txt='sdf', ubix=200, ubiy=697, canv=can)

can = texto_separado(txt='Av.Los incas con numero # 170 asdas asdas as as ', ubix=250, txtsize=9,
                     ubiy=697, canv=can)



can = texto_separado(txt='17/01/2019', ubix=32, ubiy=30, canv=can)
can = texto_separado(txt='wjfhrutb', ubix=150, ubiy=30, canv=can)
can = texto_separado(txt='sftgre', ubix=250, ubiy=30, canv=can)
can = texto_separado(txt='Jose Flores', ubix=350, ubiy=30, canv=can)
can = texto_separado(txt='Pepe Flores', ubix=460, ubiy=30, canv=can)

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
peque = resize_image(im.size, 165)
x, y = im.size
can.drawImage('iamgen.jpg', 35, 438, x * peque, y * peque)
can.drawImage('iamgen.jpg', 297, 438, x * peque, y * peque)
can.drawImage('iamgen.jpg', 35, 154, x * peque, y * peque)
can.drawImage('iamgen.jpg', 297, 154, x * peque, y * peque)


"""

tema para guardar las imagenes
"""
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(open("fichacatastrov1sther.pdf", "rb"))
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
outputStream = open("destinoa4v2sther.pdf", "wb")
output.write(outputStream)
outputStream.close()
