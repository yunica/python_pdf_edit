from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal
from reportlab.lib.colors import black, red, blue

resultado_entrevista_choise = ['COMPLETA', 'RECHAZADA', 'AUSENTE']
tipo_usuario_choise = ['ACTIVA', 'FACTIBLE', 'POTENCIAL', 'CLANDESTINA', ]

tipo_interior_choise = ['DEPARTAMENTO', 'OFICINA', 'TIENDA', 'LOCAL', 'OTRO', 'OTRO']
tipo_documento_identidad_choise = ["L.E / DNI", "RUC", "CARNET EXTRANJERIA.", "PASAPORTE", "P. NAC."]
tipo_persona_entrevistada_choise = ['PROPIETARIO', 'INQUILINO', 'ENTIDAD PUBLICA/PRIVADA', 'FAMILIAR DIRECTO', 'OTRO']


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
can.setFillColor(black)
can.setFont("Helvetica", 12)
can.setFontSize()
can.drawString(124, 109, "X")
# 1
can = ficha_num(canv=can)
# 2
olist = Lista(choise=resultado_entrevista_choise, ubix=134, ubiy=714, separacion=62, text='AUSENTE')
olist.crear_bloque_horizontal()
can.setFillColor(red)
can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
olist = None
opoint = None
# 3
olist = Lista(choise=tipo_usuario_choise, ubix=350, ubiy=714, lubix=[350, 400, 441, 492], text='CLANDESTINA')
olist.crear_bloque_horizontal()
can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
# 4
can = texto_separado(ubix=130, ubiy=685, isseparado=False, canv=can)
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
can = texto_separado(txt='JUNIOR GROVER', ubix=45, ubiy=386, canv=can)

olist = Lista(choise=tipo_documento_identidad_choise, ubiy=359, lubix=[51, 83, 113, 166, 166], text='P. NAC.')
olist.crear_bloque_horizontal()
can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')
if 'PASAPORTE' in ["PASAPORTE", "P. NAC."]:
    can = texto_separado(txt='PASAPORTE', ubix=189, ubiy=360, txtsize=9, isseparado=False, canv=can)

can = texto_separado(txt='70804143', ubix=248, ubiy=358, isseparado=False, canv=can)
can = texto_separado(txt='327855', ubix=362, ubiy=358, isseparado=False, canv=can)
can = texto_separado(txt='966 288 465', ubix=455, ubiy=358, isseparado=False, canv=can)
can = texto_separado(txt='www .gooogle. com', ubix=140, ubiy=336, isseparado=False, canv=can)
can = texto_separado(txt='FLORES', ubix=45, ubiy=309, canv=can)
can = texto_separado(txt='MARTINEZ', ubix=220, ubiy=309, canv=can)
can = texto_separado(txt='JUNIOR GROVER', ubix=370, ubiy=309, canv=can)
can = texto_separado(txt='70804143', ubix=45, ubiy=288, txtsize=10, isseparado=False, canv=can)

olist = Lista(choise=tipo_persona_entrevistada_choise, ubiy=287, lubix=[134, 187, 226, 310, 380], text='OTRO',
              otro=True, ubixotro=400, ubiyotro=289, otrotext='asdasdasd')
olist.crear_bloque_horizontal()
can.drawString(olist.get_punto().ubix, olist.get_punto().ubiy, 'X')

if olist.get_otro():
    can = texto_separado(txt=olist.get_otro().txt, ubix=olist.get_otro().ubix, ubiy=olist.get_otro().ubiy, txtsize=9,
                         isseparado=False, canv=can)

can = texto_separado(txt='freesoftandskate@gmail.com', ubix=448, ubiy=290, txtsize=9, isseparado=False, canv=can)

can.setFont("Helvetica", 5)
can.setFillColor(blue)
for i in range(0, 600, 10):
    can.drawString(i, 455, str(i))

for i in range(0, 840, 10):
    can.drawString(280, i, str(i))

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
