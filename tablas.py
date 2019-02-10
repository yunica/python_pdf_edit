from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import black, purple, white, gray
from reportlab.pdfgen import canvas


# ======================= CLASE reportePDF =========================

class reportePDF(object):
    def __init__(self, titulo, datos, nombre_pdf):
        super(reportePDF, self).__init__()
        self.titulo = titulo
        self.cabecera = ('N°', 'CÓDIGO', 'NOMBRE', 'APELLIDO PATERNO', 'APELLIDO PATERNO', 'FIRMA', 'HUELLA')
        self.datos = datos
        self.nombre_pdf = nombre_pdf

        self.estilos = getSampleStyleSheet()

    @staticmethod
    def _encabezado_pie_pagina(canvas, archivoPDF):
        """Guarde el estado de nuestro lienzo para que podamos aprovecharlo"""

        canvas.saveState()
        estilos = getSampleStyleSheet()

        # alineacion = ParagraphStyle(name="alineacion", alignment=TA_RIGHT,
        #                             parent=estilos["Normal"])
        #
        # # Encabezado
        # encabezadoNombre = Paragraph("Andres Niño 1.0", estilos["Normal"])
        # anchura, altura = encabezadoNombre.wrap(archivoPDF.width, archivoPDF.topMargin)
        # encabezadoNombre.drawOn(canvas, archivoPDF.leftMargin, 736)

        # fechaReporte = str(datetime.today())
        #
        # encabezadoFecha = Paragraph(fechaReporte, alineacion)
        # anchura, altura = encabezadoFecha.wrap(archivoPDF.width, archivoPDF.topMargin)
        # encabezadoFecha.drawOn(canvas, archivoPDF.leftMargin, 736)

        # Pie de página
        piePagina = Paragraph("Fecha de impresión: {}".format(datetime.today().__str__()), estilos["Normal"])
        anchura, altura = piePagina.wrap(archivoPDF.width, archivoPDF.bottomMargin)
        piePagina.drawOn(canvas, archivoPDF.leftMargin, 15 * mm + (0.2 * inch))

        # Suelta el lienzo
        canvas.restoreState()

    @staticmethod
    def _encabezado(canvas, archivoPDF):
        """Guarde el estado de nuestro lienzo para que podamos aprovecharlo"""

        canvas.saveState()
        estilos = getSampleStyleSheet()

        # encabezado imagen
        encabezado_imagen = Image("LOGOCONDORCUNCA-min.png", 150, 169.63)
        anchura, altura = encabezado_imagen.wrap(archivoPDF.width, archivoPDF.topMargin)
        encabezado_imagen.drawOn(canvas, 200, 600)

        # Suelta el lienzo
        canvas.restoreState()

    def convertirDatos(self):

        estiloEncabezado = ParagraphStyle(name="estiloEncabezado", alignment=TA_CENTER, fontSize=10, textColor=black,
                                          fontName="Helvetica-Bold", parent=self.estilos["Normal"])

        estiloCuerpo = ParagraphStyle(name="estiloCuerpo", alignment=TA_LEFT, fontSize=9, textColor=black,
                                      fontName="Helvetica", parent=self.estilos["Normal"])

        encabezado = [Paragraph(i, estiloEncabezado) for i in self.cabecera]
        cuerpo = [(Paragraph(j, estiloCuerpo) for j in i) for i in self.datos]

        return [encabezado] + cuerpo

    def Exportar(self):
        """Exportar los datos a un archivo PDF."""

        alineacionTitulo = ParagraphStyle(name="centrar", alignment=TA_CENTER, fontSize=12,
                                          leading=15, textColor=black, parent=self.estilos["Heading1"])
        alineacionSubTitulo = ParagraphStyle(name="centrar", alignment=TA_CENTER, fontSize=10,
                                             leading=15, textColor=black, parent=self.estilos["Normal"])
        alineacionSubTitulo2 = ParagraphStyle(name="centrar", alignment=TA_CENTER, fontSize=10,
                                              leading=15, textColor=black, spaceAfter=0,
                                              parent=self.estilos["Heading1"])
        self.ancho, self.alto = letter

        convertirDatos = self.convertirDatos()
        tabla = Table(convertirDatos, [40, 90, 80, 76, 76, 75, 75], hAlign="CENTER")
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), gray),
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Texto centrado y alineado a la izquierda
            ("INNERGRID", (0, 0), (-1, -1), 0.4, black),  # Lineas internas
            ("BOX", (0, 0), (-1, -1), 0.25, black),  # Linea (Marco) externa
        ]))

        historia = []
        historia.append(Image('LOGOCONDORCUNCA-min.png', 90, 101.78))
        historia.append(
            Paragraph("ESCUELA SUPERIOR DE FORMACIÓN ARTÍSTICA PUBLICA “CONDORCUNCA” AYACUCHO", alineacionTitulo))
        historia.append(Paragraph("RANGO UNIVERSITARIO LEY 29696", alineacionSubTitulo))
        historia.append(Paragraph("CREACIÓN R.M. N.º 1598 DEL 18/02/1957 – REINSCRIPCIÓN  D.S. N.º 017-2002-ED",
                                  alineacionSubTitulo))

        historia.append(Spacer(1, 0.09 * inch))
        historia.append(Paragraph(self.titulo, alineacionSubTitulo2))
        historia.append(Spacer(1, 0.16 * inch))
        historia.append(tabla)

        archivoPDF = SimpleDocTemplate(self.nombre_pdf, leftMargin=50, rightMargin=50, pagesize=letter, topMargin=30,
                                       title="ReportePostulantes", author="Junior Flores", )

        try:
            archivoPDF.build(historia, onLaterPages=self._encabezado_pie_pagina, canvasmaker=numeracionPaginas)
            return archivoPDF

        except Exception as e:
            return None


# ================== CLASE numeracionPaginas =======================

class numeracionPaginas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        numeroPaginas = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(numeroPaginas)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, conteoPaginas):
        self.drawRightString(204 * mm, 15 * mm + (0.2 * inch),
                             "Página {} de {}".format(self._pageNumber, conteoPaginas))

    # ===================== FUNCIÓN generarReporte =====================


# ================== EJECUTAR =======================

datos = [(str(i).zfill(3), "19137080414354", "JUNIOR GROVER", 'FLORES', 'MARTINEZ',) for i in range(0, 50)]

titulo = "LISTA DE POSTULANTES PARA CEA ESPECIALIDAD GUITARRA MODALIDAD PRIMERO Y SEGUNDOS PEUSTOS HIJOS DE LAS MIRE LRE"

# cabecera = ('N°', 'CÓDIGO', 'DNI', 'NOMBRE', 'APELLIDO PATERNO', 'APELLIDO PATERNO', 'FECHA INSCRIPCION')

nombre_pdf = "ListadoAlumnos.pdf"

reporte = reportePDF(titulo, datos, nombre_pdf).Exportar()

# ======================== LLAMAR FUNCIÓN ==========================
