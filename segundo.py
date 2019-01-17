from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal, letter, A4
from reportlab.lib.colors import red, blue
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

resultado_entrevista_choise = ['COMPLETA', 'RECHAZADA', 'AUSENTE']
tipo_usuario_choise = ['ACTIVA', 'FACTIBLE', 'POTENCIAL', 'CLANDESTINA', ]

tipo_interior_choise = ['DEPARTAMENTO', 'OFICINA', 'TIENDA', 'LOCAL', 'OTRO', 'OTRO']
tipo_documento_identidad_choise = ["L.E / DNI", "RUC", "CARNET EXTRANJERIA.", "PASAPORTE", "P. NAC."]
tipo_persona_entrevistada_choise = ['PROPIETARIO', 'INQUILINO', 'ENTIDAD PUBLICA/PRIVADA', 'FAMILIAR DIRECTO', 'OTRO']
# 7
tipo_situacion_predio_choise = ['EDIFICADO', 'EN CONSTRUCCION', 'LOTE CERDADO', 'LOTE VACIO', 'DESOCUPADO', 'OTRO']
tipo_predio_choise = ['VIVIENDA UNIFAMILIAR', 'EDIFICIO MULTIFAMILIAR', 'QUINTA SOLAR', 'COMERCIAL', 'INDUSTRIAL',
                      'INTITUCION PUBLICA', 'INTITUCION PRIVADA', 'PARQUE O BERMA', 'OTRO']
tipo_material_predio_choise = ['NOBLE', 'ADOBE', 'QUINCHA', 'MADERA', 'OTRO']
tipo_servicio_choise = ['AGUA DESAGUE', 'SOLO AGUA', 'SOLO DESAGUE', 'NINGUNO']
tipo_medio_abastecimiento_choise = ['INTRADOMICILIARIA', 'CAMION CISTERNA', 'PILETA PUBLICA', 'FUENTE PROPIA', 'OTRO']
tipo_almacenamiento_choise = ['TANQUE ELEVADO', 'CISTERNA', 'POZA', 'PISCINA', 'NO ALMACENA', 'OTRO']

# 8
tipo_unidad_uso_choise = ['SOCIAL', 'DOMESTICO', 'COMERCIAL', 'INDUSTRIAL', 'ESTATAL']
# 9
ubicacion_caja_conex_choise = ['VEREDA', 'PISTA', 'JARDIN EXTERIOR', 'INTERIOR PREDIO', 'OTRO', 'NO UBICADA']
estado_conex_choise = ['CON MEDIDOR', 'NIPLE', 'DIRECTO', 'OTRO']
condicion_conex_choise = ['ACTIVA', 'CORTADA', 'MECHA', 'INACTIVA']
tipo_conex_choise = ['NORMAL', 'CUENTA DE CONTROL', 'PILETA PUBLICA', 'CONEXION ESPECIAL', ]
material_conex_choise = ['PVC', 'FIERRO GALVANIZADO', 'POLIETILENO', 'OTRO']
diametro_conex_choise = ['1/2-15mm', '3/4-20mm', '1-25mm', '2-50mm', '4-100mm', '6-150mm', 'OTRO']
llave_paso_conex_choise = ['ANTES Y DESPUES', 'ANTES - PRIMERA', 'DESPUES - SEGUNDA', 'SIN LLAVE']
material_caja_conex_choise = ['CONCRETO', 'TERMOPLASTICO', 'LADRILLO', 'OTRO']
estado_caja_conex_choise = ['BUENO', 'MAL ESTADO']
# fuga_conex_choise
material_tapa_marco_conex_choise = ['FIERRO GALVANIZADO', 'FIERRO FUNDIDO', 'TERMOPLASTICO', 'CONCRETO', 'NO TIENE',
                                    'OTRO']
# 10
# estado_tapa_marco_conex_choise
diametro_medidor_choise = ['1/2-15mm', '3/4-20mm', '1-25mm', '1 1/2-40mm', '2-50mm', '3-80mm', '4-100mm', '6-150mm',
                           'OTRO']
marca_medidor_choise = ['ELSTER', 'ACTARIS', 'IBERCONTA', 'SCHLUMBERGER', 'ZENNER', 'INCA', 'KENT', 'ABB', 'DH',
                        'NINGUNO', 'OTRO']
estado_medidor_choise = ['OPERATIVO', 'LUNA EMPANIADA', 'CAPSULA ROTA/QUEMADA', 'REGISTRO SUELTO', 'MANECILLAS SUELTAS',
                         'OTRO']
accesorio_seguridad_medidor_choise = ['SIN DISPOSITIVO', 'PRECINTO PVC (1 PZA)', 'PRECINTO COBRE (1 PZA)', 'ANCLAJE',
                                      'OTRO']

# ubicacion_caja_conex_desague_choise =
diametro_conex_desague_choise = ['4-100mm', '6-150mm', '8-150mm', 'OTRO']
condicion_conex_desague_choise = ['ACTIVA', 'CORTADA', 'SIN CONEXION', 'OTRO']
# material_conex_desague_choise
estado_tapa_caja_registro_choise = ['BUENO', 'MAL ESTADO', 'OTRO']
material_tapa_desague_choise = ['FIERRO GALVANIZADO', 'FIERRO FUNDIDO', 'CONCRETO', 'NO TIENE', 'OTRO']


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
# 1
can = ficha_num(canv=can)
# 2
olist = Lista(choise=resultado_entrevista_choise, ubix=134, ubiy=714, separacion=62, text='AUSENTE')
olist.crear_bloque_horizontal()
can.setFillColor(red)
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
olist = None
opoint = None
# 3
olist = Lista(choise=tipo_usuario_choise, ubix=350, ubiy=714, lubix=[350, 400, 441, 492], text='CLANDESTINA')
olist.crear_bloque_horizontal()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# 4
can = texto_separado(txt='asdas asdasd asdas asdasd', ubix=130, ubiy=685, isseparado=False, canv=can)
can = texto_separado(txt='3216544', ubix=500, ubiy=685, isseparado=False, canv=can)
can = texto_separado(txt='HUAMANGA', ubix=490, ubiy=666, isseparado=False, canv=can)
can = texto_separado(txt='flores martinez junior grover', ubix=80, ubiy=666, isseparado=False, canv=can)
can = texto_separado(txt='Psje. mao tse tung 1081 MZA=A', ubix=80, ubiy=647, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=45, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=100, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=150, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=200, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=250, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=310, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=355, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=415, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=470, ubiy=620, isseparado=False, canv=can)
can = texto_separado(txt='005', ubix=530, ubiy=620, isseparado=False, canv=can)
# 5
can = texto_separado(txt='1234', ubix=42, ubiy=571, isseparado=True, canv=can)
can = texto_separado(txt='PSJE. MAO TSE TUNG 10801 MZA A', ubix=93, ubiy=571, txtsize=11, canv=can)
can = texto_separado(txt='5678', ubix=42, ubiy=544, isseparado=True, canv=can)
can = texto_separado(txt='PSJE. MAO TSE TUNG 10801 MZA AKJSH DKA JS HD', ubix=93, ubiy=544, txtsize=11, canv=can)

can = texto_separado(txt='1234', ubix=45, ubiy=522, txtsize=10, isseparado=False, canv=can)
can = texto_separado(txt='56789', ubix=95, ubiy=522, txtsize=10, isseparado=False, canv=can)
can = texto_separado(txt='56789', ubix=142, ubiy=522, txtsize=10, isseparado=False, canv=can)
can = texto_separado(txt='56789', ubix=175, ubiy=522, txtsize=10, isseparado=False, canv=can)
can = texto_separado(txt='56789', ubix=205, ubiy=522, txtsize=10, isseparado=False, canv=can)
can = texto_separado(txt='56789', ubix=235, ubiy=522, txtsize=10, isseparado=False, canv=can)

olist = Lista(choise=tipo_interior_choise, ubiy=523, lubix=[309, 340, 381, 422, 462],
              otro=True, ubixotro=490, ubiyotro=524, otrotext='asdasdad', text='OTRO')
olist.crear_bloque_horizontal()
can.setFillColor(red)
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can.drawString(olist.get_otro().ubix, olist.get_otro().ubiy, olist.get_otro().txt)

can = texto_separado(txt='asjdhas kasjhdkjashd kajshdkjash ', ubix=42, ubiy=502, txtsize=11, isseparado=False, canv=can)
can = texto_separado(txt='tipo edi', ubix=423, ubiy=502, txtsize=11, isseparado=False, canv=can)
can = texto_separado(txt='codigo edif ', ubix=485, ubiy=502, txtsize=11, isseparado=False, canv=can)
can = texto_separado(txt='complemento complemente complemento complemente ', ubix=42, ubiy=484, txtsize=10,
                     isseparado=False, canv=can)
can = texto_separado(txt='sector muni ', ubix=95, ubiy=466, txtsize=11, isseparado=False, canv=can)
can = texto_separado(txt='etapa  ', ubix=320, ubiy=466, txtsize=11, isseparado=False, canv=can)
can = texto_separado(txt='zona zona ', ubix=475, ubiy=466, txtsize=11, isseparado=False, canv=can)
# 6
if False:
    can = texto_separado(txt='X', ubix=145, ubiy=442, canv=can)
else:
    can = texto_separado(txt='X', ubix=52, ubiy=335, canv=can)

can = texto_separado(txt='FLORES', ubix=45, ubiy=412, canv=can)
can = texto_separado(txt='MARTINEZ', ubix=290, ubiy=412, canv=can)
can = texto_separado(txt='JUNIOR GROVER', ubix=45, ubiy=387, canv=can)

olist = Lista(choise=tipo_documento_identidad_choise, ubiy=359, lubix=[51, 83, 113, 166, 166], text='P. NAC.')
olist.crear_bloque_horizontal()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if 'PASAPORTE' in ["PASAPORTE", "P. NAC."]:
    can = texto_separado(txt='pasaporte', ubix=189, ubiy=360, isred=True, txtsize=9, isseparado=False, canv=can)

can = texto_separado(txt='70804143', ubix=248, ubiy=358, isseparado=False, canv=can)
can = texto_separado(txt='327855', ubix=362, ubiy=358, isseparado=False, canv=can)
can = texto_separado(txt='966 288 465', ubix=455, ubiy=358, isseparado=False, canv=can)
can = texto_separado(txt='www .gooogle. com', ubix=140, ubiy=335, isseparado=False, canv=can)
can = texto_separado(txt='FLORES', ubix=45, ubiy=309, canv=can)
can = texto_separado(txt='MARTINEZ', ubix=220, ubiy=309, canv=can)
can = texto_separado(txt='JUNIOR GROVER', ubix=370, ubiy=309, canv=can)
can = texto_separado(txt='70804143', ubix=45, ubiy=288, txtsize=10, isseparado=False, canv=can)

olist = Lista(choise=tipo_persona_entrevistada_choise, ubiy=287, lubix=[134, 187, 226, 310, 380], text='OTRO',
              otro=True, ubixotro=400, ubiyotro=289, otrotext='asdasdasd')
olist.crear_bloque_horizontal()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=9,
                         isseparado=False, isred=True, canv=can)

can = texto_separado(txt='freesoftandskate@gmail.com', ubix=448, ubiy=290, txtsize=9, isseparado=False, canv=can)

# 7
olist = Lista(choise=tipo_situacion_predio_choise, ubix=52, lubiy=[248, 237, 226, 216, 206, 193], text='OTRO',
              otro=True, ubixotro=77, ubiyotro=196, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=tipo_predio_choise, lubix=[124, 124, 124, 124, 124, 186, 186, 186, 186],
              lubiy=[248, 237, 226, 216, 206, 248, 237, 226, 216], text='OTRO',
              otro=True, ubixotro=211, ubiyotro=219, otrotext='asdasdasd')
olist.crear_bloque_especial()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=tipo_material_predio_choise, ubix=267, lubiy=[248, 237, 226, 216, 206], text='OTRO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=tipo_servicio_choise, ubix=340, lubiy=[248, 237, 226, 216], text='AGUA DESAGUE')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=tipo_medio_abastecimiento_choise, ubix=411, lubiy=[248, 237, 226, 216, 206], text='OTRO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=tipo_almacenamiento_choise, ubix=503, lubiy=[248, 237, 226, 216, 206, 193], text='CISTERNA',
              otro=True, ubixotro=526, ubiyotro=196, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

can = texto_separado(txt='12', ubix=200, ubiy=194, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='12', ubix=280, ubiy=194, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=360, ubiy=194, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=380, ubiy=194, txtsize=9, isseparado=False, canv=can)
# 8
can = texto_separado(txt='12', ubix=96, ubiy=162, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=125, ubiy=162, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=125, ubiy=151, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=125, ubiy=139, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=125, ubiy=128, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=125, ubiy=117, txtsize=9, isseparado=False, canv=can)

can = texto_separado(txt='12', ubix=300, ubiy=162, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=330, ubiy=162, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X ASDASD ASDASD ASD', ubix=395, ubiy=162, txtsize=9, isseparado=False, canv=can)

can = texto_separado(txt='X', ubix=330, ubiy=151, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X ASDASD ASDASD ASD', ubix=395, ubiy=151, txtsize=9, isseparado=False, canv=can)

can = texto_separado(txt='X', ubix=330, ubiy=139, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X ASDASD ASDASD ASD', ubix=395, ubiy=139, txtsize=9, isseparado=False, canv=can)

can = texto_separado(txt='X', ubix=330, ubiy=128, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X ASDASD ASDASD ASD', ubix=395, ubiy=128, txtsize=9, isseparado=False, canv=can)

can = texto_separado(txt='X', ubix=330, ubiy=117, txtsize=9, isseparado=False, canv=can)
can = texto_separado(txt='X ASDASD ASDASD ASD', ubix=395, ubiy=117, txtsize=9, isseparado=False, canv=can)

# segunda hoja
# 9
can.showPage()
can.setFillColor(blue)

olist = Lista(choise=ubicacion_caja_conex_choise, ubix=52, lubiy=[747, 736, 725, 714, 704, 693], text='OTRO',
              otro=True, ubixotro=75, ubiyotro=706, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=estado_conex_choise, ubix=135, lubiy=[747, 736, 725, 714], text='OTRO',
              otro=True, ubixotro=157, ubiyotro=717, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=condicion_conex_choise, ubix=217, lubiy=[747, 737, 726, 714], text='INACTIVA')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=tipo_conex_choise, ubix=299, lubiy=[747, 736, 726, 715], text='CONEXION ESPECIAL')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=material_conex_choise, ubix=369, lubiy=[747, 736, 726, 715], text='OTRO',
              otro=True, ubixotro=392, ubiyotro=717, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=diametro_conex_choise, lubix=[451, 451, 451, 502, 502, 502, 502],
              lubiy=[747, 737, 726, 747, 736, 725, 715], text='OTRO', otro=True, ubixotro=527, ubiyotro=717,
              otrotext='asdasdasd')
olist.crear_bloque_especial()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=llave_paso_conex_choise, ubix=52, lubiy=[658, 646, 635, 624], text='SIN LLAVE')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=material_caja_conex_choise, ubix=135, lubiy=[682, 670, 658, 646], text='OTRO',
              otro=True, ubixotro=157, ubiyotro=648, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=estado_caja_conex_choise, ubix=217, lubiy=[682, 670], text='MAL ESTADO')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

olist = Lista(choise=material_tapa_marco_conex_choise, ubix=299, lubiy=[682, 669, 658, 646, 635, 624], text='OTRO',
              otro=True, ubixotro=322, ubiyotro=626, otrotext='asdasdasd')
olist.crear_bloque_vertical()

if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)
# 10
can = texto_separado(txt='ASDAS ASDASD', ubix=45, ubiy=574, txtsize=11, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=41, ubiy=560, txtsize=11, isseparado=False, canv=can)

can = texto_separado(txt='ASDAS ASDASD', ubix=45, ubiy=538, txtsize=11, isseparado=False, canv=can)
can = texto_separado(txt='X', ubix=41, ubiy=524, txtsize=11, isseparado=False, canv=can)

can = texto_separado(txt='12313.464', ubix=51, ubiy=491, txtsize=11, isseparado=False, canv=can)

olist = Lista(choise=diametro_medidor_choise, ubix=175, lubiy=[586, 572, 559, 548, 537, 524, 513, 502, 502],
              text='OTRO', otro=True, ubixotro=200, ubiyotro=505, otrotext='asdasdasd')
olist.crear_bloque_vertical()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if '502' == '6-150mm':
    can = texto_separado(txt='6-150mm', ubix=200, ubiy=505, txtsize=7, isseparado=False, isred=True, canv=can)
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=marca_medidor_choise, lubix=[268, 268, 268, 268, 268, 320, 320, 320, 320, 320, 268],
              lubiy=[586, 573, 560, 548, 537, 586, 573, 560, 548, 537, 524], text='NINGUNO', otro=True, ubixotro=288,
              ubiyotro=528, otrotext='asdasda')
olist.crear_bloque_especial()
if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=estado_medidor_choise, ubix=390, lubiy=[586, 573, 560, 548, 537, 525], text='OTRO',
              otro=True, ubixotro=415, ubiyotro=526, otrotext='asdasdasd')
olist.crear_bloque_vertical()

if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=ubicacion_caja_conex_choise, ubix=53, lubiy=[440, 427, 413, 400, 388, 388], text='OTRO', otro=True,
              ubixotro=91, ubiyotro=389, otrotext='/ OTRO')
olist.crear_bloque_vertical()

if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=diametro_conex_desague_choise, ubix=145, lubiy=[440, 426, 413, 400], text='OTRO',
              otro=True, ubixotro=170, ubiyotro=403, otrotext='asdasdasd')
olist.crear_bloque_vertical()

if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=condicion_conex_desague_choise, ubix=236, lubiy=[440, 426, 413, 400], text='OTRO',
              otro=True, ubixotro=260, ubiyotro=403, otrotext='asdasdasd')
olist.crear_bloque_vertical()

if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=estado_tapa_caja_registro_choise, ubix=420, lubiy=[426, 413, 400], text='BUENO',
              otro=True, ubixotro=443, ubiyotro=403, otrotext='asdasdasd')
olist.crear_bloque_vertical()

if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)

olist = Lista(choise=material_tapa_desague_choise, ubix=503, lubiy=[440, 426, 413, 389, 400], text='OTRO',
              otro=True, ubixotro=528, ubiyotro=403, otrotext='asdasdasd')
olist.crear_bloque_vertical()

if olist.get_punto():
    can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=7,
                         isseparado=False, isred=True, canv=can)
# 13
can = texto_separado(txt='123 ASDASD', ubix=423, ubiy=349, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='456 ASDASD', ubix=473, ubiy=349, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='789 ASDASD', ubix=514, ubiy=349, txtsize=7, isseparado=False, canv=can)

# 14
can = texto_separado(txt='123 ASDASD', ubix=423, ubiy=312, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='456 ASDASD', ubix=473, ubiy=312, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='789 ASDASD', ubix=514, ubiy=312, txtsize=7, isseparado=False, canv=can)

# 15
can = texto_separado(txt='123 ASDASD', ubix=423, ubiy=277, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='456 ASDASD', ubix=495, ubiy=277, txtsize=7, isseparado=False, canv=can)
# 16
can = texto_separado(txt='123 ASDASD', ubix=423, ubiy=245, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='456 ASDASD', ubix=495, ubiy=245, txtsize=7, isseparado=False, canv=can)
# 17
can = texto_separado(txt='123 ASDASD 123 123', ubix=430, ubiy=217, txtsize=7, isseparado=False, canv=can)
# 19
ptext = """Lorem ipsum dolor sit amet, consectetur adipisicing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
        culpa qui officia deserunt mollit anim id est laborum."""
p = Paragraph(ptext, style=getSampleStyleSheet()["Normal"])
p.wrapOn(can, 440, 30)
p.drawOn(can, 110, 140)

# 19
can = texto_separado(txt='123 ASDASD 123 123', ubix=430, ubiy=217, txtsize=7, isseparado=False, canv=can)
# encuestador
can = texto_separado(txt='123 ASSD', ubix=75, ubiy=100, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='21/08/2018', ubix=130, ubiy=100, txtsize=7, isseparado=False, canv=can)
# digitador
can = texto_separado(txt='123 ASSD', ubix=220, ubiy=100, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='21/08/2018', ubix=280, ubiy=100, txtsize=7, isseparado=False, canv=can)
# supervisor
can = texto_separado(txt='123 ASSD', ubix=360, ubiy=100, txtsize=7, isseparado=False, canv=can)
can = texto_separado(txt='21/08/2018', ubix=420, ubiy=100, txtsize=7, isseparado=False, canv=can)

# 20
can = texto_separado(txt='x', ubix=506, ubiy=89, txtsize=14, isseparado=False, canv=can)
can = texto_separado(txt='x', ubix=548, ubiy=89, txtsize=14, isseparado=False, canv=can)

# can.setFillColor(red)
# can.setFont("Helvetica", 15)
# can.drawString(167, 214, "X")

can.save()

# Tercera hoja
packet2 = io.BytesIO()
can2 = canvas.Canvas(packet2, pagesize=legal)
# text
can2.setFillColor(blue)
can2.setFont("Helvetica", 4)
for i in range(0, 600, 10):
    can2.drawString(i, 770, str(i))

for i in range(0, 840, 10):
    can2.drawString(280, i, str(i))

can2.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')


can2.showPage()
can2.save()

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

# tercera hoja
packet2.seek(0)
new_pdf2 = PdfFileReader(packet2)
existing_pdf2 = PdfFileReader(open("pdfblanco.pdf", "rb"))

page2 = existing_pdf2.getPage(0)
page2.mergePage(new_pdf2.getPage(0))

output.addPage(page2)

# finally, write "output" to a real file
outputStream = open("destinoa4.pdf", "wb")
output.write(outputStream)
outputStream.close()
