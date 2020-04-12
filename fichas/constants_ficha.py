T_HABILIT_HURBA = (('AAHH', 'ASENTAMIENTO HUMANO'), ('AGRUP', 'AGRUPACION'),
                   ('AMP.PJ', 'AMPLIACIÃN PUEBLO JOVEN'),
                   ('ASOC', 'ASOCIACION'),
                   ('AS.PV', 'ASOCIACION PRO VIVIENDA'),
                   ('AS.VI', 'ASOCIACION DE VIVIENDA'), ('BARRIO', 'BARRIO'),
                   ('CASRIO', 'CASERIO'), ('C.H.', 'CONJUNTO HABITACIONAL'),
                   ('COMUN', 'COMUNIDAD'), ('COOP', 'COOPERATIVA'),
                   ('COOP.V', 'COOPERATIVA DE VIVIENDA'),
                   ('C.P.', 'CENTRO POBLADO'),
                   ('C.R.', 'CONJUNTO RESIDENCIAL'), ('CRCADO', 'CERCADO'),
                   ('FUNDO', 'FUNDO'), ('G.R.', 'GRUPO RESIDENCIAL'),
                   ('HABCOM', 'HABILITACION COMERCIAL'),
                   ('HACIND', 'HACIENDA'),
                   ('H.U.PR', 'HABILITACIÃN URBANO PROGESIVA'),
                   ('LOTIZ', 'LOTIZACION'), ('PARCLA', 'PARCELA'),
                   ('P.J.', 'PUEBLO JOVEN'), ('S/T', 'SIN TIPO'),
                   ('UPIS', 'URBANIZACIÃN POPULAR DE INTERES SOCIAL'),
                   ('URB', 'URBANIZACION'), ('URB.PP', 'URBANIZACION POPULAR'),
                   ('U.V.', 'UNIDAD VECINAL'), ('VALLE', 'VALLE'),)

T_VIA = (('AL.', 'ALAMEDA'), ('AV.', 'AVENIDA'), ('CA.', 'CALLE'),
         ('CAM', 'CAMINO'), ('CTRA', 'CARRETERA'), ('JR', 'JIRON'),
         ('ML.', 'MALECON'), ('OJ.', 'GGG'), ('PJE.', 'PASAJE'),
         ('PRLG.', 'PROLONGACION'), ('PS.', 'PASEO'),)
T_PUERTA = (('E', 'ESTACIONAMIENTO'), ('G', 'GARAGE'), ('P', 'PRINCIPAL'),
            ('S', 'SECUNDARIO'), ('F', 'FORANEA'),)
T_COND_NUM_PUERT = (('MUNICIPALIDAD', '01'),
                    ('AUTOGENERADO TITULAR CATASTRAL CATASTRAL', '02'),
                    ('GENERADO TECNICO CATASTRAL', '03'),)
T_EDIFI = (('BLOCK', '01'), ('CASA / CHALET', '02'), ('EDIFICIO', '03'),
           ('PABELLON', '04'),)

T_EST_FICHA = (('COMPLETA', '(01) - FICHA COMPLETA'),
               ('INCOMPLETA', '(02) - FICHA INCOMPLETA'),
               ('OFICINA', '(03) - COMPLETADA EN OFICINA'),
               ('CONTROL EXTERIOR', '(04) - COMPLETADA EN CONTROL EXTERIOR'),)
T_PERSONA = (('NATURAL', '01'), ('JURIDICA', '02'),)
T_DOCUMENTO_PERSONA = (('NO PRESENTO DOCUMENTO', '(01) NO PRESENTO DOCUMENTO'),
                       ('DNI', '(02) DNI'), ('C. POLICIA NACIONAL',
                                             '(03) CARNET DE IDENTIDAD DE POLICIA NACIONAL'),
                       ('C. FUERZAS ARMADAS',
                        '(04) CARNET DE IDENTIDAD DE FUERZAS ARMADAS'),
                       ('PARTIDA DE NACIMIENTO', '(05) PARTIDA DE NACIMIENTO'),
                       ('PASAPORTE', '(06) PASAPORTE'),
                       ('C. EXTRANJERIA', '(07) CARNET DE EXTRANJERIA'),
                       ('LIBRETA MILITAR', '(08) LIBRETA MILITAR'),
                       ('RUC', '(09) RUC'),)
T_PERSONA_JURIDICA = (('EMPRESA', 'EMPRESA'), ('COOPERATIVA', 'COOPERATIVA'),
                      ('ASOCIACION', 'ASOCIACION'), ('FUNDACION', 'FUNDACION'),
                      ('GOBIERNO', 'GOBIERNO'),)

T_FORMA_ADQUISICION = (('ADJUDICACION', 'ADJUDICACION'),
                       ('ANTICIPO LEGITIMA', 'ANTICIPO LEGITIMA'),
                       ('APORTE', 'APORTE'), ('CESION DE DERECHOS DE ACCIONES',
                                              'CESION DE DERECHOS DE ACCIONES'),
                       ('COMPRA VENTA', 'COMPRA VENTA'),
                       ('DACION EN PAGO', 'DACION EN PAGO'), (
                       'DECLARACION DE HEREDEROS', 'DECLARACION DE HEREDEROS'),
                       ('DESCONOCIDO', 'DESCONOCIDO'),
                       ('DONACION', 'DONACION'),
                       ('EXPROPIACION', 'EXPROPIACION'), ('FUSION', 'FUSION'),
                       ('PERMUTA', 'PERMUTA'), ('POSESION', 'POSESION'), (
                       'PRESCRIPCION ADQUISITIVA', 'PRESCRIPCION ADQUISITIVA'),
                       ('TESTAMENTO', 'TESTAMENTO'), ('TRASPASO', 'TRASPASO'),)
T_CONDICION_TITULAR = (
    ('COTITULARIDAD', 'COTITULARIDAD'), ('LITIGIO', 'LITIGIO'),
    ('POSEEDOR', 'POSEEDOR'), ('PROPIETARIO UNICO', 'PROPIETARIO UNICO'),
    ('SOCIEDAD CONYUGAL', 'SOCIEDAD CONYUGAL'),
    ('SUCESION INTESTADA', 'SUCESION INTESTADA'), ('OTROS', 'OTROS'),)
T_CONDICION_ESPECIAL_PREDIO = (('MONUMENTO HISTORICO', 'MONUMENTO HISTORICO'),
                               ('PREDIO RUSTICO', 'PREDIO RUSTICO'), (
                               'SISTEMA DE AYUDA DE AERONAVEGACION',
                               'SISTEMA DE AYUDA DE AERONAVEGACION'),)
T_ESTADO_CIVIL = (('CASADO(A)', 'CASADO(A)'), ('CONVIVIENTE', 'CONVIVIENTE'),
                  ('DIVORCIADO(A)', 'DIVORCIADO(A)'),
                  ('SOLTERO(A)', 'SOLTERO(A)'), ('VIUDO(A)', 'VIUDO(A)'),)

T_CONDICION_ESPECIAL_TITULAR = (('GOBIERNO CENTRAL', 'GOBIERNO CENTRAL'),
                                ('GOBIERNO LOCAL', 'GOBIERNO LOCAL'),
                                ('GOBIERNO REGIONAL', 'GOBIERNO REGIONAL'), (
                                'BENEFICENCIA PUBLICA',
                                'BENEFICENCIA PUBLICA'),
                                ('HOSPITALES', 'HOSPITALES'), (
                                'ENTIDADES RELIGIOSAS',
                                'ENTIDADES RELIGIOSAS'), (
                                'CUERPO GENERAL DE BOMBEROS',
                                'CUERPO GENERAL DE BOMBEROS'),
                                ('UNIVERSIDADES', 'UNIVERSIDADES'),
                                ('CENTRO EDUCATIVO', 'CENTRO EDUCATIVO'), (
                                'COMUNIDAD CAMPESINA / NATIVA',
                                'COMUNIDAD CAMPESINA / NATIVA'), (
                                'ORGANISMOS INTERNACIONALES',
                                'ORGANISMOS INTERNACIONALES'),
                                ('GOBIERNO EXTRANJERO', 'GOBIERNO EXTRANJERO'),
                                ('ORGANIZACION POLITICA',
                                 'ORGANIZACION POLITICA'), (
                                'PATRIMONIO CULTURAL DE LA NACION',
                                'PATRIMONIO CULTURAL DE LA NACION'), (
                                'ORGANIZACIONES SINDICALES',
                                'ORGANIZACIONES SINDICALES'), (
                                'ORGANIZACIONES DE DISCAPACITADOS',
                                'ORGANIZACIONES DE DISCAPACITADOS'),
                                ('PENSIONISTA', 'PENSIONISTA'),)

t_uso_predio_catastral = (
    ('10101	', 'CASA HABITACIÓN'), ('10201	', 'EDIFICIO'),
    ('10202	', 'QUINTA'), ('10203	', 'CALLEJÓN'),
    ('10204	', 'CORRALÓN'), ('10205	', 'SOLAR'),
    ('20101	', 'PRODUCTOS AGROPECUARIOS Y PESQUEROS NO INDUSTRIALIZADOS.'),
    ('20102	', 'PRODUCTOS DE SILVICULTURA'), ('20103	',
                                                 'PRODUCTOS MANUFACTURADOS PREDOMINANTEMENTE DE CONSUMO INMEDIATO.'),
    ('20104	', 'PRODUCTOS MANUFACTURADOS DE USO DURADERO.'),
    ('20105	', 'PRODUCTOS MANUFACTURADOS PREDOMINANTEMENTE DE INSUMOS'), (
    '20106	',
    'PRODUCTOS MANUFACTURADOS PREDOMINANTEMENTE DE BIENES DE CAPITAL.'),
    ('20107	', 'DE BIENES NO ESPECIFICADOS.'),
    ('20201	', 'PRODUCTOS AGROPECUARIOS Y PESQUEROS NO INDUSTRIALIZADOS.'),
    ('20202	', 'PRODUCTOS DE SILVICULTURA'), ('20203	',
                                                 'PRODUCTOS MANUFACTURADOS PREDOMINANTEMENTE DE CONSUMO INMEDIATO.'),
    ('20204	', 'PRODUCTOS MANUFACTURADOS DE USO DURADERO.'),
    ('20205	', 'PRODUCTOS MANUFACTURADOS PREDOMINANTEMENTE DE INSUMOS'), (
    '20206	',
    'PRODUCTOS MANUFACTURADOS PREDOMINANTEMENTE DE BIENES DE CAPITAL.'),
    ('20207	', 'EQUIPAMIENTO DE COMERCIO AMBULATORIO.'),
    ('20208	', 'DE BIENES NO ESPECIFICADOS'),
    ('20301	', 'DE PRODUCTOS AGRÍCOLAS COMESTIBLES'), ('20302	',
                                                          'DE PRODUCTOS AGRÍCOLAS NO UTILIZADOS EN LA ALIMENTACIÓN HUMANA'),
    ('20303	',
     'DE ANIMALES GENERALMENTE NO UTILIZADOS EN LA ALIMENTACIÓN HUMANA'), (
    '20304	',
    'DE ANIMALES GENERALMENTE UTILIZADOS EN LA ALIMENTACIÓN HUMANA'),
    ('20305	', 'DE PRODUCTOS EN ESTADO NATURAL'),
    ('20306	', 'DE PRODUCTOS DERIVADOS NO INDUSTRIALIZADOS'),
    ('20307	', 'DE PRODUCTOS ALIMENTICIOS'),
    ('20308	', 'DE ALIMENTOS PREPARADOS PARA ANIMALES'),
    ('20309	', 'DE BEBIDAS'),
    ('20310	', 'DE PRODUCTOS FARMACÉUTICOS Y ARTÍCULOS DE TOCADOR'),
    ('20311	', 'DE COMBUSTIBLES Y LUBRICANTES'), ('20312	', 'DE TELAS'),
    ('20313	', 'DE ARTÍCULOS DEL HOGAR'), ('20314	', 'DE LIBROS'),
    ('20315	', 'DE ARTÍCULOS ARTÍSTICOS Y DE LUJO'), ('20316	',
                                                         'DE AUTOMÓVILES Y OTROS MEDIOS DE TRANSPORTE Y TRACCIÓN PERSONAL'),
    ('20317	', 'DE DIVERSOS ARTÍCULOS DE USO DURADERO'),
    ('20318	', 'DE FERTILIZANTES'), ('20319	',
                                        'DE INSUMOS MANUFACTURADOS PARA LA INDUSTRIA DE TRANSFORMACIÓN'),
    ('20320	', 'DE INSUMOS MANUFACTURADOS'),
    ('20321	', 'DE REPUESTOS Y ACCESORIOS'),
    ('20322	', 'DE MAQUINARIAS'), ('20323	', 'DE APARATOS DE MEDICIÓN'),
    ('20324	', 'DE VEHÍCULOS'),
    ('20325	', 'DE PRODUCTOS DE DIVERSAS RAMAS DEL MISMO RUBRO'),
    ('20326	', 'TIENDA MÚLTIPLE DE DIFERENTE RUBRO'),
    ('20401	', 'DE ESTUDIOS Y PROYECTOS'),
    ('20402	', 'DE PROFESIÓN MÉDICA'), ('20403	', 'ESTUDIOS JURÍDICOS'),
    ('20404	', 'ASESORES Y CONSULTORES'), ('20405	', 'DE ENFERMERÍA'),
    ('20406	', 'DE CORRETAJE Y AFINES'), ('20407	', 'DE CONSTRUCCIÓN.'),
    ('20408	', 'DE BIENES Y EXPORTACIÓN / IMPORTACIÓN.'),
    ('20409	', 'ADMINISTRATIVA'),
    ('20501	', 'DE ALIMENTACIÓN Y BEBIDAS (RESTAURANTE)'),
    ('20502	', 'DE VESTIMENTA (SASTRERÍA)'),
    ('20503	', 'DE VIVIENDA Y ALOJAMIENTO (HOTEL)'),
    ('20504	', 'DE HIGIENE Y ESTÉTICA PERSONAL (PELUQUERÍA)'),
    ('20505	', 'DE MANTENIMIENTO Y LIMPIEZA DE MUEBLES.'),
    ('20506	', 'TÉCNICOS ESPECIALIZADOS.'),
    ('20507	', 'DE MECÁNICA AUTOMOTRIZ.'),
    ('20508	', 'DE MECÁNICA EN GENERAL Y ELECTRICIDAD.'),
    ('20509	', 'PARA APARATOS Y MUEBLES PREFERENTEMENTE DE USO DOMÉSTICO.'),
    ('20510	', 'DE MECÁNICA FINA.'),
    ('20511	', 'PRESTADOS A LAS EMPRESAS.'),
    ('20512	', 'ALQUILER Y ARRENDAMIENTO DE MAQUINARIA Y EQUIPO.'),
    ('20513	', 'DE SANEAMIENTO Y SIMILARES.'),
    ('20514	', 'DE VETERINARIA.'), ('20515	', 'AGENCIAS DE TURISMO'),
    ('20516	', 'DE CABALLERIZA.'),
    ('20517	', 'DE ESPARCIMIENTO NO ESPECIFICADO.'),
    ('30101	', 'AGRICULTURA'), ('30102	', 'EXPLOTACIÓN DE MINAS'),
    ('30201	', 'PRODUCTOS ALIMENTICIOS'), ('30202	', 'TEXTILES'), (
    '30203	',
    'INDUSTRIA DE LA MADERA Y PRODUCTOS DE LA MADERA INCLUIDOS MUEBLES.'),
    ('30204	', 'FABRICACIÓN DEL PAPEL Y PRODUCTOS DEL PAPEL'), ('30205	',
                                                                   'FABRICACIÓN DE SUSTANCIAS Y PRODUCTOS QUÍMICOS DERIVADOS DEL PETRÓLEO'),
    ('30206	',
     'FABRICACIÓN DE PRODUCTOS MINERALES NO METÁLICOS EXCEPTO LOS DERIVADOS DEL PETRÓLEO Y CARBÓN.'),
    ('30207	', 'INDUSTRIAS METÁLICAS BÁSICAS.'),
    ('30208	', 'FABRICACIÓN DE PRODUCTOS METÁLICOS'),
    ('30209	', 'OTRAS INDUSTRIAS MANUFACTURERAS NO ESPECIFICADAS.'),
    ('40101	', 'PARQUE METROPOLITANO.'), ('40102	', 'PARQUE ZONAL.'),
    ('40103	', 'PARQUE.'), ('40104	', 'ESTADIO.'),
    ('40105	', 'HIPÓDROMO'), ('40106	', 'COLISEO.'),
    ('40107	', 'CLUB O CÍRCULO.'), ('40108	', 'CENTRO DEPORTIVO.'),
    ('40109	', 'PISTA DE PATINAJE.'), ('40110	', 'CANCHA DE BOWLING.'),
    ('40111	', 'MESA DE BILLAR Y BILLAS.'),
    ('40112	', 'CANCHA DE BOCHAS'), ('40113	', 'GIMNASIO'),
    ('40114	', 'GALERÍA DE TIRO.'), ('40115	', 'PISCINA DE NATACIÓN.'),
    ('40116	', 'ACADEMIA DE DANZA'), ('40117	', 'ACADEMIA DE DEPORTES'),
    ('40118	', 'ACADEMIA DE ARTES MARCIALES'), ('40119	', 'PLAZOLETA'),
    ('40201	', 'MUSEO.'), ('40202	', 'CENTRO DE CONVENCIONES.'),
    ('40203	', 'SALA DE EXPOSICIÓN'), ('40204	',
                                          'MONUMENTO ARQUEOLÓGICO PREHISPÁNICO/HISTÓRICO COLONIAL- REPUBLICANO.'),
    ('40205	', 'TEATRO'), ('40206	', 'JARDÍN BOTÁNICO.'),
    ('40207	', 'ZOOLÓGICO.'), ('40208	', 'CINE.'),
    ('40209	', 'BIBLIOTECA.'), ('40210	', 'OBSERVATORIO'),
    ('40301	', 'DISCOTECA.'), ('40302	', 'BINGO'),
    ('40303	', 'PINBALL O SIMILAR.'), ('40304	', 'PEÑA.'),
    ('40305	', 'CAFÉ TEATRO'), ('40306	', 'SALÓN DE BAILE.'),
    ('40307	', 'CENTRO DE APUESTA'),
    ('40308	', 'CASA DE CITA Y PROSTÍBULO'), ('40309	', 'CIRCO'),
    ('40310	', 'KARAOKE'), ('50101	', 'EDUCACIÓN INICIAL ESTATAL'),
    ('50102	', 'EDUCACIÓN INICIAL PARTICULAR'),
    ('50103	', 'EDUCACIÓN PRIMARIA ESTATAL'),
    ('50104	', 'EDUCACIÓN PRIMARIA PARTICULAR'),
    ('50105	', 'EDUCACIÓN SECUNDARIA ESTATAL'),
    ('50106	', 'EDUCACIÓN SECUNDARIA PARTICULAR'),
    ('50107	', 'EDUCACIÓN PRIMARIA-SECUNDARIA ESTATAL'),
    ('50108	', 'EDUCACIÓN PRIMARIA-SECUNDARIA PARTICULAR'),
    ('50109	', 'EDUCACIÓN PRE-UNIVERSITARIA (ACADEMIA)'),
    ('50110	', 'EDUCACIÓN SUPERIOR UNIVERSITARIA ESTATAL'),
    ('50111	', 'EDUCACIÓN SUPERIOR UNIVERSITARIA PARTICULAR'),
    ('50112	', 'EDUCACIÓN SUPERIOR INSTITUTO ESTATAL.'),
    ('50113	', 'EDUCACIÓN SUPERIOR INSTITUTO PARTICULAR'),
    ('50114	', 'CALIFICACIÓN PROFESIONAL ESPECIALIZADA'),
    ('50115	', 'EDUCACIÓN ESPECIAL'), ('50116	', 'OTRO NO ESPECIFICADO'),
    ('50201	', 'HOSPITAL ESPECIALIZADO'), ('50202	', 'HOSPITAL GENERAL'),
    ('50203	', 'HOSPITAL GENERAL DE LAS FUERZAS ARMADAS Y POLICIALES'),
    ('50204	', 'CLÍNICA ESPECIALIZADA'), ('50205	', 'CLÍNICA'),
    ('50206	', 'CENTRO DE SALUD TIPO C'), ('50207	', 'PUESTO SANITARIO'),
    ('50208	', 'CENTRO ESPECIALIZADO DE ASISTENCIA SOCIAL'),
    ('50209	', 'CEMENTERIO'), ('50210	', 'FUNERARIA'),
    ('50301	', 'TERMINAL MARÍTIMO'), ('50302	', 'TERMINAL AÉREO'),
    ('50303	', 'TERMINAL TERRESTRE'), ('50304	', 'TERMINAL FERROVIARIO'),
    ('50305	', 'DEPÓSITO Y ALMACENAMIENTO'), ('50306	', 'PLAYA'),
    ('50307	', 'SERVICIO RELACIONADO AL TRANSPORTE FERROVIARIO'), (
    '50308	',
    'SERVICIO RELACIONADO AL TRANSPORTE TERRESTRE INTERPROVINCIAL'),
    ('50309	', 'SERVICIO RELACIONADO AL TRANSPORTE DE CARGA POR CARRETERA'),
    ('50310	',
     'OTROS SERVICIOS DE TRANSPORTE TERRESTRE DE PASAJEROS EN LA CIUDAD'),
    ('50311	', 'SERVICIO RELACIONADO AL TRANSPORTE AÉREO'),
    ('50312	', 'SERVICIO RELACIONADO AL TRANSPORTE POR AGUA'),
    ('50401	', 'CORREO'), ('50402	', 'TELÉFONO'),
    ('50403	', 'TELEVISIÓN'), ('50404	', 'TELÉGRAFO'),
    ('50405	', 'RADIO'), ('50406	', 'CABLES'),
    ('50407	', 'VÍA SATÉLITE'), ('50408	', 'TÉLEX'),
    ('50409	', 'TELETIPO'), ('50410	', 'TELEFOTO'),
    ('50411	', 'PRENSA'), ('50412	', 'AGENCIA DE PRENSA'),
    ('50413	', 'AGENCIA NOTICIOSA'), ('50414	', 'MENSAJERÍA'),
    ('50415	', 'INTERNET'), ('50416	', 'OTRO NO ESPECIFICADO'),
    ('50501	', 'LUZ Y FUERZA ELÉCTRICA'),
    ('50502	', 'PRODUCCIÓN Y DISTRIBUCIÓN DE GAS'),
    ('50503	', 'SUMINISTRO DE VAPOR'), ('50504	', 'CENTRO DE CAPTACIÓN'),
    ('50505	', 'CENTRAL DE GENERACIÓN ELÉCTRICA'),
    ('50506	', 'SUB ESTACIÓN DE TELECOMUNICACIONES'),
    ('50601	', 'MERCADOS'), ('50602	', 'MERCADO AMBULATORIO'),
    ('60101	', 'EDIFICACIÓN UTILIZADA POR EL GOBIERNO CENTRAL'),
    ('60102	', 'EDIFICACIÓN UTILIZADA POR EL GOBIERNO REGIONAL'),
    ('60103	', 'EDIFICACIÓN UTILIZADA POR EL GOBIERNO LOCAL'),
    ('60104	', 'EDIFICACIÓN UTILIZADA POR EL GOBIERNO NO ESPECIFICADO'),
    ('60201	', 'PREFECTURA'),
    ('60202	', 'ESTACIÓN DE LA POLICÍA NACIONAL'),
    ('60203	', 'CENTRO DE INSTRUCCIÓN DE LAS FUERZAS ARMADAS'),
    ('60204	', 'CENTRO DE INSTRUCCIÓN DE LAS FUERZAS POLICIALES.'),
    ('60205	', 'CUARTEL DE LA GUARDIA REPUBLICANA POLICÍA NACIONAL'),
    ('60206	', 'CUARTEL DEL EJÉRCITO'),
    ('60207	', 'CUARTEL DE LA FUERZA AÉREA'),
    ('60208	', 'CUARTEL DE LA MARINA O BASE NAVAL'), ('60209	',
                                                         'CENTRO DE REHABILITACIÓN Y ASISTENCIA SOCIAL (C.R.A.S.- CÁRCELES).'),
    ('60301	', 'FINANCIERA'), ('60302	', 'BOLSA DE VALORES'),
    ('60303	', 'AGENCIA CAMBIARÍA'),
    ('60304	', 'COMPAÑÍA DE PATENTES Y LICENCIAS'),
    ('60305	', 'OTRO ESTABLECIMIENTO FINANCIERO NO ESPECIFICADO'),
    ('60306	', 'BANCO DE LA ENTIDAD PÚBLICA'),
    ('60307	', 'BANCO COMERCIAL'), ('60308	', 'AGENCIA BANCARIA'),
    ('60309	', 'CAJA DE AHORRO'), ('60310	', 'MUTUAL'),
    ('60311	', 'COOPERATIVA DE CRÉDITO'), ('60312	', 'CASA DE PRÉSTAMO'),
    ('60313	', 'OTRA INSTITUCIÓN MONETARIA NO ESPECIFICADA'),
    ('60314	', 'SEGUROS'),
    ('60315	', 'OTRO SERVICIO DE SEGUROS NO ESPECIFICADO'),
    ('60316	', 'CAJERO AUTOMÁTICO'),
    ('60317	', 'ADMINISTRACIÓN FONDO DE PENSIONES (AFP)'),
    ('60401	', 'INSTITUTO DE INVESTIGACIÓN Y CIENTÍFICO'),
    ('60501	', 'EMBAJADA'), ('60502	', 'CONSULADO'),
    ('60503	', 'LEGACIÓN'), ('60504	', 'ORGANISMO INTERNACIONAL'),
    ('60601	', 'CATEDRAL'), ('60602	', 'PARROQUIA'),
    ('60603	', 'CAPILLA'), ('60604	', 'TEMPLO DE LA IGLESIA ADVENTISTA'),
    ('60605	', 'TEMPLO DE LA IGLESIA ALIANZA CRISTIANA Y MISIONERA'),
    ('60606	', 'TEMPLO DE LA IGLESIA ANGLICANA'),
    ('60607	', 'TEMPLO DE LA IGLESIA BAUTISTA'),
    ('60608	', 'TEMPLO DE LA IGLESIA EVANGÉLICA'), ('60609	',
                                                       'TEMPLO DE LA IGLESIA DE JESUCRISTO DE LOS SANTOS DE LOS ÚLTIMOS DÍAS'),
    ('60610	', 'CONVENTO'),
    ('60611	', 'SALA DE REUNIÓN DEPENDIENTE DE LA ENTIDAD RELIGIOSA'),
    ('60612	', 'TEMPLO TESTIGO DE JEHOVÁ'), ('60701	', 'HOSPICIO'),
    ('60702	', 'ALBERGUE.'), ('60703	', 'PUERICULTORIO'),
    ('60704	', 'ASILO'), ('60705	', 'COMPAÑÍA DE BOMBEROS'),
    ('60706	', 'COMEDOR POPULAR'), ('60707	', 'LOCAL COMUNAL'),
    ('60708	', 'GUARDERÍA'), ('60801	', 'CULTURAL'),
    ('60802	', 'RELIGIOSA'), ('60803	', 'LABORAL'),
    ('60804	', 'POLÍTICA'), ('60805	', 'ASISTENCIA SOCIAL'),
    ('60806	', 'COMERCIAL'), ('60807	', 'PROFESIONAL'),
    ('70101	', 'SIN CONSTRUIR'), ('70201	', 'EN CONSTRUCCIÓN'),
    ('70301	', 'CONSTRUCCIÓN PARCIAL'),
    ('70401	', 'CON CONSTRUCCIÓN DE TERCEROS'),
    ('70402	', 'TERRENO CONSTRUCCIÓN PARCIAL'),
    ('80101	', 'CON CONSTRUCCIÓN'), ('90101	', 'CASA HABITACIÓN'),
    ('90201	', 'EDIFICIO'), ('90202	', 'QUINTA'),
    ('90301	', 'COMERCIO'), ('100101', '	EDIFICIO'),
    ('100102', '	QUINTA'), ('100103', '	CALLEJON'),
    ('100104', '	CORRALON'), ('100105', '	SOLAR'),
    ('100106', '	CASA HABITACION'), ('100201', '	CENTRO COMERCIAL'),
    ('100202', '	GALERIA'), ('100203', '	OFICINA'),
    ('100204', '	OTRO NO ESPECIFICADO'), ('100205', '	MERCADO'),
    ('100301', '	INDUSTRIA'), ('100401', '	RESIDENCIAL'),
    ('100402', '	COMERCIAL'), ('100403', '	INDUSTRIAL '),)
PREDIO_CATASTRAL_EN = (
    ('GALERIA', '(01) GALERIA'), ('MERCADO', '(02) MERCADO'),
    ('CAMPO FERIAL', '(03) CAMPO FERIAL'),
    ('CENTRO COMERCIAL', '(04) CENTRO COMERCIAL'), ('QUINTA', '(05) QUINTA'),
    ('CALLEJON', '(06) CALLEJON'),
    ('PREDIO INDEPENDIENTE', '(07) PREDIO INDEPENDIENTE'),
    ('SOLAR', '(08) SOLAR'), ('CORRALON', '(09) CORRALON'),
    ('AZOTEA', '(10) AZOTEA'), ('AIRES', '(11) AIRES'),
    ('PREDIO EN EDIFICIO', '(12) PREDIO EN EDIFICIO'),)
EVALUACION_PREDIO_CATASTRAL = (
    ('CATASTRAL OMISO', '(01) PREDIO CATASTRAL OMISO'),
    ('CATASTRAL SUBVALUADO', '(02) PREDIO CATASTRAL SUBVALUADO'),
    ('CATASTRAL SOBREVALUADO', '(03) PREDIO CATASTRAL SOBREVALUADO'),
    ('CATASTRAL CONFORME', '(04) PREDIO CATASTRAL CONFORME'),)
T_CONDICION_DECLARANTE = (('TITULAR CATASTRAL', '(01) TITULAR CATASTRAL'),
                          ('REPRESENTANTE LEGAL', '(02) REPRESENTANTE LEGAL'),
                          ('ARRENDATARIO', '(03) ARRENDATARIO'),
                          ('FAMILIAR', '(04) FAMILIAR'),
                          ('VECINO', '(05) VECINO'),
                          ('POSEEDOR', '(06) POSEEDOR'),
                          ('ENCARGADO', '(07) ENCARGADO'),)
T_MANTENIMIENTO_F_INDIVIDUAL = (
    ('SER PREDIO CATASTRAL NUEVO', '(01) SER PREDIO CATASTRAL NUEVO'),
    ('VARIACION EN LA CONSTRUCCION', '(02) VARIACION EN LA CONSTRUCCION'),
    ('CAMBIO DEL TITULAR CATASTRAL', '(03) CAMBIO DEL TITULAR CATASTRAL'),
    ('CAMBIO DE USO', '(04) CAMBIO DE USO'),)
T_SANEAMIENTO = (('SOLO AGUA', 'SOLO AGUA'), ('SOLO DESAGUE', 'SOLO DESAGUE'),
                 ('AGUA Y DESAGUE', 'AGUA Y DESAGUE'),)
T_MEP = (
    ('CONCRETO', 'CONCRETO'), ('LADRILLO', 'LADRILLO'), ('ADOBE', 'ADOBE '),
    ('QUINCHA', 'QUINCHA'), ('MADERA', 'MADERA'),

)

T_ECS = (
    ('MUY BUENO', 'MUY BUENO'), ('BUENO', 'BUENO'), ('REGULAR', 'REGULAR'),
    ('MALO', 'MALO'),)
T_ECC = (('TERMINADO', 'TERMINADO'), ('EN CONSTRUCCION', 'CONSTRUCCION'),
         ('INCONCLUSA', 'INCONCLUSA'), ('EN RUINAS', 'RUINAS'),)
T_VALO_UNIT_EDIF = (
    ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
    ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'),)

T_UCA = (('RETIRO MUNICIPAL', 'RETIRO MUNICIPAL'),
         ('JARDIN DE AISLAMIENTO', 'JARDIN DE AISLAMIENTO'),
         ('VIA PUBLICA', 'VIA PUBLICA'),
         ('LOTE COLINDANTE', 'LOTE COLINDANTE'),
         ('ALTURA NO REGLAMENTARIA', 'ALTURA NO REGLAMENTARIA'),
         ('PARQUE', 'PARQUE'), ('BIEN COMUN', 'BIEN COMUN'),
         ('ZONA DE RIESGO', 'ZONA DE RIESGO'),)

T_DOCCUMENTO_ADJUNTO = (('CONFORMIDAD DE OBRA', '(01) CONFORMIDAD DE OBRA'), (
'LICENCIA DE CONSTRUCCION', '(02) LICENCIA DE CONSTRUCCION'), (
                        'DECLARATORIA DE FABRICA',
                        '(03) DECLARATORIA DE FABRICA'), (
                        'ULTIMA DECLARACION JURADA AUTOAVALUO',
                        '(04) ULTIMA DECLARACION JURADA AUTOAVALUO'), (
                        'RESOLUCION DE EXONERACION',
                        '(05) RESOLUCION DE EXONERACION'),
                        ('PODERES', '(06) PODERES'), (
                        'DOCUMENTO DE TRANSFERENCIA',
                        '(07) DOCUMENTO DE TRANSFERENCIA'), (
                        'CONSTANCIA DE POSESION',
                        '(08) CONSTANCIA DE POSESION'),
                        ('PARTIDA DE DEFUNCION', '(09) PARTIDA DE DEFUNCION'),
                        (
                        'CERTIFICADO CATASTRAL', '(10) CERTIFICADO CATASTRAL'),
                        ('HOJA INFORMATIVA CATASTRAL',
                         '(11) HOJA INFORMATIVA CATASTRAL'), (
                        'PARTIDA DE NACIMIENTO', '(12) PARTIDA DE NACIMIENTO'),
                        ('TITULO', '(13) TITULO'),
                        ('COMPRA - VENTA', '(14) COMPRA - VENTA'), (
                        'AUTORIZACION DE FUNCIONAMIENTO',
                        '(15) AUTORIZACION DE FUNCIONAMIENTO'),)

T_PARTIDA = (('TOMO', '(01) TOMO'), ('FICHA', '(02) FICHA'),
             ('PARTIDA ELECTRONICA', '(03) PARTIDA ELECTRONICA'),
             ('CODIGO DE PREDIO', '(04) CODIGO DE PREDIO'),)
T_CODIGO_DECLARACION_FABRICA = (('FABRICA INSCRITA', '(01) FABRICA INSCRITA'),
                                ('FABRICA NO INSCRITA',
                                 '(02) FABRICA NO INSCRITA'),)

"""
 ============== data for table ========
"""

Tipo_ClasificacionEdificacionn = (
    ('0100  ', 'CASA HABITACION'), ('0200 ', 'TIENDA / DEPOSITO / ALMACEN'),
    ('0300  ', 'PREDIO EN EDIFICIO'), ('0401 ', 'CLINICA'),
    ('0410', 'CEMENTERIO'), ('0411', 'SUB ESTACION'),
    ('0412', 'BANCO FINANCIERA'), ('0413', 'TERMINAL DE TRANSPORTE'),
    ('0414', 'MERCADO'), ('0415', 'CLUB SOCIAL'),
    ('0416', 'CLUB DE ESPARCIMIENTO'), ('0417', 'PLAYA DE ESTACIONAMIENTO'),
    ('0402 ', 'HOSPITAL'), ('0403 ', 'CINE / TEATRO'), ('0404 ', 'INDUSTRIA'),
    ('0405 ', 'TALLER'), ('0406 ', 'IGLESIA / TEMPLO'),
    ('0407 ', 'CENTRO DE ENSEÃANZA'), ('0408 ', 'SERVICIO DE COMIDA'),
    ('0409 ', 'PARQUE'), ('0500  ', 'TERRENO SIN CONSTRUIR'),
    ('999', '(419) -OTRO-'),)

Tipo_TipoObraComplementaria = (("01", 'TANQUE ELEVADO                   ',
                                'CONCRETO                         ', 'M3'), (
                               "02", 'TANQUE ELEVADO                   ',
                               'LADRILLO                         ', 'M3'), (
                               "03", 'TANQUE ELEVADO                   ',
                               'ASBESTO / PLASTICO / FIBRA DE VIDRIO              ',
                               'M3'), (
                               "04", 'TANQUE PARA COMBUSTIBLE          ',
                               'CONCRETO                         ', 'GALONES'),
                               ("05", 'CISTERNA                         ',
                                'CONCRETO                         ', 'M3'), (
                               "06", 'PISCINA                          ',
                               'CONCRETO  ARMADO CON MAYOLICA    ', 'M3'), (
                               "07", 'PISCINA                          ',
                               'LADRILLO KING KONG CON PINTURA   ', 'M3'), (
                               "08", 'ESPEJO DE AGUA                   ',
                               'CONCRETO                         ', 'M3'), (
                               "09",
                               'POZO TUBULAR HASTA 100 M. DE PROFUNDIDAD          ',
                               '                                 ', 'UNIDAD'),
                               ("10",
                                'POZO TUBULAR HASTA 150 M. DE PROFUNDIDAD          ',
                                '                                 ', 'UNIDAD'),
                               ("11",
                                'POZO TUBULAR HASTA 200 M. DE PROFUNDIDAD          ',
                                '                                 ', 'UNIDAD'),
                               ("12", 'TRIBUNA                          ',
                                'CONCRETO                         ', 'M2'), (
                               "13", 'RAMPA                            ',
                               'CONCRETO                         ', 'M2'), (
                               "14", 'PAVIMENTO                        ',
                               'CONCRETO                         ', 'M2'), (
                               "15", 'PAVIMENTO                        ',
                               'ASFALTO                          ', 'M2'), (
                               "16", 'AREA LIBRE CON PISO DE MARMOL    ',
                               'MARMOL                           ', 'M2'), (
                               "17", 'AREA LIBRE CON PISO DE CERAMICA  ',
                               'CERAMICO                         ', 'M2'), (
                               "18", 'AREA LIBRE CON PISO DE LOSETA    ',
                               'LOSETA                           ', 'M2'), (
                               "19",
                               'AREA LIBRE CON PISO DE CEMENTO PULIDO             ',
                               'CEMENTO                          ', 'M2'), (
                               "20", 'AREA LIBRE CON PISO DE LAJA      ',
                               'LAJA                             ', 'M2'), (
                               "21", 'CERCO O MURO PERIMETRICO         ',
                               'PIEDRA                           ', 'ML'), (
                               "22", 'CERCO O MURO PERIMETRICO         ',
                               'LADRILLO                         ', 'ML'), (
                               "23", 'CERCO O MURO PERIMETRICO         ',
                               'ALUMINIO                         ', 'ML'), (
                               "24", 'CERCO O MURO PERIMETRICO         ',
                               'FIERRO                           ', 'ML'), (
                               "25", 'CERCO O MURO PERIMETRICO         ',
                               'MADERA                           ', 'ML'), (
                               "26", 'MURO DE CONTENCIÓN               ',
                               'CONCRETO                         ', 'M2'), (
                               "27", 'SARDINEL                         ',
                               'CONCRETO                         ', 'M2'), (
                               "28", 'PARAPETO                         ',
                               'LADRILLO                         ', 'ML'), (
                               "29", 'CAMPO DEPORTIVO                  ',
                               'GRASS                            ', 'M2'), (
                               "30", 'CANCHA DEPORTIVA                 ',
                               'ARCILLA                          ', 'M2'), (
                               "31", 'LOSA DEPORTIVA                   ',
                               'CONCRETO                         ', 'M2'), (
                               "32", 'CANCHA DE FRONTON                ',
                               'CONCRETO                         ', 'M2'), (
                               "33", 'CANCHA DE SQUASH                 ',
                               'CONCRETO                         ', 'M2'), (
                               "34", 'GRUTA                            ',
                               'CONCRETO                         ', 'M2'), (
                               "35", 'PILETA                           ',
                               'CONCRETO                         ', 'M3'), (
                               "36", 'PERGOLA                          ',
                               'CONCRETO                         ', 'M2'), (
                               "37", 'TORRE PARA ANTENA                ',
                               'METALICO                         ', 'ML'), (
                               "38", 'TORRE PARA ANTENA                ',
                               'TUBULAR METALICO                 ', 'ML'), (
                               "39", 'PORTONES                         ',
                               'MADERA                           ', 'M2'), (
                               "40", 'PUERTAS                          ',
                               'MADERA                           ', 'M2'), (
                               "41", 'TANQUE SEPTICO                   ',
                               'CONCRETO                         ', 'M3'), (
                               "42", 'ESTACIONAMIENTO                  ',
                               'CONCRETO                         ', 'M2'), (
                               "43", 'TORRES  DE VIGILANCIA            ',
                               '                                 ', 'UNIDAD'),
                               ("44", 'POSTES                           ',
                                'CONCRETO                         ', 'UNIDAD'),
                               ("45", 'BASES  DE SOPORTE  DE MAQUINAS   ',
                                'CONCRETO                         ', 'UNIDAD'),
                               ("46", 'POZOS SUMIDEROS                  ',
                                'CONCRETO                         ', 'M3'), (
                               "47", 'PATIO DE MANIOBRAS               ',
                               'CONCRETO  / ASFALTO              ', 'M2'), (
                               "48", 'SUPERFICIE DE RODADURA           ',
                               'CONCRETO  / ASFALTO              ', 'M2'), (
                               "49", 'VEREDA                           ',
                               'CONCRETO  / ASFALTO              ', 'M2'), (
                               "50", 'HORNOS                           ',
                               'CONCRETO  / LADRILLO REFRACTARIO ', 'M3'), (
                               "51", 'CHIMENEAS                        ',
                               'CONCRETO  / LADRILLO REFRACTARIO ', 'M3'), (
                               "52", 'INCINERADORES                    ',
                               'CONCRETO  / LADRILLO REFRACTARIO ', 'M3'), (
                               "53", 'BOVEDAS                          ',
                               'CONCRETO                         ', 'M3'), (
                               "54", 'BALANZAS INDUSTRIALES            ',
                               'CONCRETO                         ', 'M3'),)
Tipo_TipoInterior = (
    ('01', 'DEPARTAMENTO'), ('02', 'CASA / CHALET'), ('03', 'FICINA'),
    ('04', 'ESTACIONAMIENTO'), ('05', 'DEPOSITO'), ('06', 'TENDAL'),
    ('07', 'TIENDA'), ('08', 'PUESTO'), ('09', 'STAND'), ('999', '-OTRO-'),)

notarias_list = (('ALCA CHUCHON  FILEMON         ',
                  '                   AYACUCHO', '               AYACUCHO',
                  'CANGALLO', 'CANGALLO', 'JR. TARAPACÁ S/N', '-----------',
                  'tula_27_06@hotmail.com'), (
                 'ALMONACID CISNEROS  MARIO MARCIAL', 'AYACUCHO', 'AYACUCHO',
                 'HUAMANGA', 'AYACUCHO', 'JR. AREQUIPA N° 162',
                 '(066) 31-3990', 'ana_yasir23@hotmail.com'), (
                 'ALVIZ MONTAÑEZ  REYNALDO', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CUSCO', 'CUSCO', 'CALLE SAN ANDRÉS N° 282', '(084) 23-3312',
                 'notariaalviz@hotmail.com'), (
                 'AMAO RODAS  LADISLAO', 'AYACUCHO', 'AYACUCHO', 'HUANTA',
                 'HUANTA', 'JR. CORDOVA N° 156 (PARQUE CENTRAL)',
                 '(066) 32-1167', 'amaorodas@hotmail.com'), (
                 'AVENDAÑO GARCIA  NESTOR FRANCISCO', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'CUSCO', 'CUSCO', 'CALLE AYACUCHO N° 200',
                 '(084) 22-5194', 'nag.notarioabogado@gmail.com.pe'), (
                 'BELTRÁN PACHECO  FIDEL ORESTES', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'LA CONVENCIÓN', 'SANTA ANA',
                 'PROLONGACIÓN AV. GENERAL GAMARRA S/N FRENTE A LA UNIVERSIDAD ANDINA - QUILLABAMBA',
                 '084-613379', 'notariabeltran@hotmail.com'), (
                 'BETALLELUZ BETALLELUZ  SAMY IBETT', 'AYACUCHO', 'AYACUCHO',
                 'HUANTA', 'HUANTA', 'JR. MILLER N° 114', '(066) 32-2534',
                 'notariabetalleluz@hotmail.com'), (
                 'BUSTAMANTE ARAGON  JORGE OSWALDO', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'CUSCO', 'CUSCO',
                 'CAL. PAMPA DEL CASTILLO N° 460 (459)',
                 '(084) 25-8072 / (084)23-1665',
                 'notariabustamante@hotmail.com'), (
                 'CENTELLAS MACHACA  OLGER', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'QUISPICANCHI', 'URCOS', 'JR. MARIANO MELGAR NRO. 113',
                 '(084) 30-7259', 'ollgercentellas@hotmail.com'), (
                     'CHILLCCE JAYO  MIGUEL ANGEL', 'AYACUCHO', 'AYACUCHO',
                     'HUANTA', 'HUANTA', 'AV. SAN MARTIN N° 220',
                     '(066) 40-2986', 'miguelchillcce@hotmail.com'), (
                 'CUBA CASTRO  ALFREDO', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'LA CONVENCIÓN', 'SANTA ANA', 'JR. LIBERTAD N° 611',
                 '(084) 28-1077', 'alfcubacastro@hotmail.com'), (
                 'DE LOS RIOS GUZMAN DE CARCAUSTO  BLANCA MARIA',
                 'CUSCO Y MADRE DE DIOS', 'CUSCO', 'CUSCO', 'SANTIAGO',
                 'AV. GRAU N° 949B', '(084) 25-3441',
                 'notariadelosrios_guzman@hotmail.com'), (
                 'DELGADO ESCOBEDO   MARTHA BEATRIZ ALEXANDRA',
                 'CUSCO Y MADRE DE DIOS', 'CUSCO', 'CUSCO', 'SAN JERONIMO',
                 'MZA. L LOTE. 23-B URB. VERSALLES', '(084) 27-1717',
                 'marthadenot@hotmail.com'), (
                 'FIGUEROA CAMACHO  EDIE', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CALCA', 'PISAC', 'AV. AMAZONAS N° 101 - PISAC',
                 '(084) 20-3288', 'notariafigueroa@hotmail.com'), (
                 'GALDO SOTOMAYOR  MARIA EUGENIA', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'QUISPICANCHI', 'URCOS',
                 'JR. BELAUNDE TERRY N° 176 - PLAZA DE ARMAS DE  URCOS',
                 '(084) 30-7088 / (084) 50-9689', 'notariagaldos@hotmail.com'),
                 ('GAONA CHACÓN  OSWALDO RUFFO', 'CUSCO Y MADRE DE DIOS',
                  'CUSCO', 'ESPINAR', 'ESPINAR',
                  'CAL. TEATRO N° 207 - ESPINAR', '(084) 30-1358',
                  'ogaona@notariagaona.com'), (
                 'GAONA CISNEROS  RUFFO HERMOGENES', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'CUSCO', 'CUSCO', 'SAN ANDRES N° 238',
                 '(084) 22-4937/ (084)23-6923', 'maria.ganoa@mariaganoa.com'),
                 ('GARCÍA MEDINA  LOURDES MADELEINE', 'CUSCO Y MADRE DE DIOS',
                  'MADRE DE DIOS', 'TAMBOPATA', 'TAMBOPATA',
                  'JR. PUNO N° 716 PUERTO MALDONADO', '(082) 50-2258',
                  'notarialourdesga@hotmail.com'), (
                 'GIRON ARANA  CESAR ODON', 'AYACUCHO', 'AYACUCHO', 'HUANTA',
                 'HUANTA', 'JR. GERVASIO SANTILLANA N° 202',
                 '(066) 32-2198 / (066) 32-2215', 'notariogiron@terra.com'), (
                 'HINOSTROZA AUCASIME  JOSE', 'AYACUCHO', 'AYACUCHO',
                 'HUAMANGA', 'AYACUCHO', 'JR. BELLIDO N° 609', '(066) 32-7407',
                 'jhinostroza10@hotmail.com'), (
                 'HOLGADO NOA DE CACERES  LISBETH', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'CUSCO', 'SANTIAGO',
                 'MZA. B-3 LOTE. A - URB. BANCOPATA', '(084) 26-0615',
                 'lisbeth.holgado@hotmail.com'), (
                 'HUANCA CAYLLAHUA  TORIBIO MARCIAL', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'ANTA', 'ANTA',
                 'JR. JAQUIJAHUANA MZA. C-6 LOTE. 10 INT. 201 CENTRO POBLADO IZCUCHACA',
                 '(084) 20-3677', 'huanca1236@hotmail.com'), (
                 'JORDAN GAMARRA  YORKA INES', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'ANTA', 'ANTA', 'JR. JAQUIJAHUANA N° 513- IZCUCHACA',
                 '(084) 43-4012', 'notariajordangamarra@hotmail.com'), (
                 'LIRA APAZA  LUIS ALBERTO', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CUSCO', 'SAN SEBASTIAN',
                 'PROLG. AV LA CULTURA MZA. O-12-B (ENTRE EL PARADERO CAMIONERO Y PARADERO SANTA ROSA)',
                 '(084) 27-6890', 'luis_lira@hotmail.com'), (
                 'MACHACA  CALLE  SEVERO', 'AYACUCHO', 'AYACUCHO', 'LA MAR',
                 'AYNA', 'AV. 28 DE JULIO N°  49', '(066)31-2015',
                 'severomachaca@hotmail.com'), (
                 'MACHACA CALLE  GUDELIA', 'AYACUCHO', 'AYACUCHO', 'HUAMANGA',
                 'AYACUCHO', 'AV. GARCILASO DE LA VEGA N° 241',
                 '(066) 31-1359', 'notariamachacacalle@hotmail.com'), (
                 'MAMANI ASLLA  ANACLETO', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CHUMBIVILCAS', 'SANTO TOMAS', 'CAL. SIGLO XX N° 511',
                 '(084) 830421', '-'), (
                 'MEDINA DELGADO  VÍCTOR ELÍAS', 'AYACUCHO', 'AYACUCHO',
                 'HUAMANGA', 'JESUS NAZARENO', 'JR. CIRO ALEGRIA N° 341',
                 '(066) 32-7081', 'notariovictormedina@hotmail.com'), (
                 'MENDOZA AZPARRENT  DALMACIO DARÍO', 'AYACUCHO', 'AYACUCHO',
                 'HUAMANGA', 'AYACUCHO', 'JR. CUSCO N° 260', '(066) 31-4130',
                 'mazparrent260@hotmail.com'), (
                 'MUÑIZ ESCOBAR  ABEL', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'LA CONVENCIÓN', 'SANTA ANA', 'JR. ESPINAR N° 353',
                 '(084) 28-1134', 'abelmuñiz@terra.com.pe'), (
                 'NEGRÓN PERALTA  RODZANA', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CUSCO', 'SAN SEBASTIAN', 'PROL. AV DE LA CULTURA N° 1108',
                 '(084) 27-3351', 'negronperalta@no.com pe'), (
                 'OCAMPO DELAHAZA  LUCILA ANTONIETA', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'CUSCO', 'CUSCO',
                 'AV. EL SOL N° 616  INTERIOR 5  PASAJE GRACE',
                 '(084) 22-8711', 'ocampodelahaza@hotmail.com'), (
                 'OCHOA ALVAREZ  GUIDO EDUARDO', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'URUBAMBA', 'URUBAMBA', 'CAL. COMERCIO N° 211',
                 '(084) 20-1078', '-'), (
                 'OLAGUIBEL OLIVERA   GIL ABAD', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'URUBAMBA', 'URUBAMBA', 'JR. YUPANQUI N° 115',
                 '(084) 20-1670 / (084) 80-0790', 'abperuado1@hotmail.com'), (
                 'OLIVERA UMERES  JOHN', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CHUMBIVILCAS', 'SANTO TOMAS',
                 'CALLE PROGRESO N° 100-A SANTO TOMAS', '-----------',
                 'notariaolivera@hotmail.com'), (
                 'ORE GAMBOA  CARLOS PELAYO', 'AYACUCHO', 'AYACUCHO',
                 'HUAMANGA', 'SAN JUAN BAUTISTA', 'AV. SAN LORENZO N° 490',
                 '(066) 32-7081', 'notariaoregamboa@gmail.com'), (
                 'OROS CARRASCO  RODOLFO', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CUSCO', 'WANCHAQ', 'AV. HUASCAR N° 219B', '(084) 23-5388',
                 'notaria.oroscarrasco@gmail.com'), (
                 'OSORIO ALVARADO  HONORATO ZENON', 'AYACUCHO', 'AYACUCHO',
                 'HUANTA', 'SIVIA', 'AV. HUANTA N° 138', '(066) 79-2948',
                 'notariasivia@hotmail.com'), (
                 'PACHECO MERCADO  ORLANDO', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CUSCO', 'CUSCO', 'AV. GRAU N° 438', '(084) 23-7891',
                 'notaria_pacheco@hotmail.com'), (
                 'PALOMINO MANTILLA  LUIS FERNANDO', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'PARURO', 'PARURO', 'PLAZA. PLAZA DE ARMAS S/N',
                 '(084) 27-3433', 'notariapalominomantillalf@hotmail.com'), (
                 'PANTIGOSO HERRERA  JUAN MANUEL', 'CUSCO Y MADRE DE DIOS',
                 'MADRE DE DIOS', 'TAMBOPATA', 'TAMBOPATA',
                 'AV. LEON VELARDE N° 727', '(082) 57-4064 / (082) 57-1445',
                 '-'), ('POZO UGARTE   ABEL SALUSTIO', 'CUSCO Y MADRE DE DIOS',
                        'CUSCO', 'LA CONVENCIÓN', 'QUELLOUNO',
                        'JR. QUILLABAMBA N° 205 PLAZA DE ARMAS', '-----------',
                        'abelpozougarte@hotmail.com'), (
                 'PRADO CALDERON  JOSE LUIS', 'AYACUCHO', 'AYACUCHO',
                 'HUAMANGA', 'SAN JUAN BAUTISTA', 'AV. RAMON CASTILLA N° 184',
                 '(066) 32-6646', 'notaprado@hotmail.com'), (
                 'REMON BUITRON  ALIPIO', 'AYACUCHO', 'AYACUCHO', 'HUAMANGA',
                 'AYACUCHO', 'JR. SAN MARTIN N° 452', '(066) 31-3056',
                 '----------'), (
                 'RODRÍGUEZ GIL  CESAR LADISLAO', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'ACOMAYO', 'ACOMAYO', 'JR. SUCRE N° 100',
                 '(084) 83-0075', 'crodriguez@notarios.org.pe'), (
                 'RUEDA ALVAREZ  JOSÉ FERNANDO', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'PAUCARTAMBO', 'PAUCARTAMBO',
                 'CAL. MARCAVALLE N° 204 - URB. PAUCARTAMBO', '-----------',
                 'jruedaalvarez@yahoo.es'), (
                 'RíOS PICKMANN   GAVIN ALFREDO', 'CUSCO Y MADRE DE DIOS',
                 'MADRE DE DIOS', 'TAMBOPATA', 'TAMBOPATA',
                 'AV. LEON VELARDE N° 765 - TAMBOPATA', '(082) 57-1116',
                 'notarioriospickmann@yahoo.com'), (
                 'SALAZAR PUENTE DE LA VEGA  MERCEDES',
                 'CUSCO Y MADRE DE DIOS', 'CUSCO', 'CUSCO', 'WANCHAQ',
                 'AV. HUAYNA CCAPAC N° 113 INT. A',
                 '(084) 22-1039 / (084) 22-8597',
                 'mechispv@gmail.com / mersal63@hotmail.com'), (
                 'SANCHEZ GAMARRA DE ORDOÑEZ   MERY ALINDA',
                 'CUSCO Y MADRE DE DIOS', 'CUSCO', 'CALCA', 'CALCA',
                 'CAL. CORDOVA N° 146 - CALCA', '(084) 20-2321',
                 'mery.a.sanchez@gmail.com'), (
                 'SARAVIA PALOMINO  WILLIAM LIOV', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'CALCA', 'CALCA', 'JR. BOLIVAR N° 741 - CALCA',
                 '(084) 70-3729', 'liovs@hotmail.com'), (
                 'SOMOCURCIO ALARCÓN  CARLOS AUGUSTO', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'CUSCO', 'CUSCO', 'CALLE BELEN N° 307 - CUSCO',
                 '(084) 24-2224', 'ca.somocurcio@terra.com.pe'), (
                 'TERRAZAS GONZALES  DUNIA VICTORIA', 'CUSCO Y MADRE DE DIOS',
                 'CUSCO', 'ESPINAR', 'ESPINAR', 'JIRÓN ARICA N° 119 ESPINAR',
                 '(084) 77-9960', 'terrazasg@hotmail.com'), (
                 'VENERO TAPIA  MARCO YVAN', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'CANCHIS', 'MARANGANI',
                 'AV. SAN MARTIN N° 826 - FRENTE DE INSTITUTO EDUCA',
                 '(084) 79-6009', 'nelly.yv@gmail.com'), (
                 'VILLANUEVA SANCHEZ  NESTOR DIONICIO',
                 'CUSCO Y MADRE DE DIOS', 'CUSCO', 'CANCHIS', 'SICUANI',
                 'JR. TACNA N° 145', '(084) 35-1013',
                 'nestornotario@hotmail.com'), (
                 'VILLANUEVA SANCHEZ  URIEL', 'CUSCO Y MADRE DE DIOS', 'CUSCO',
                 'ESPINAR', 'ESPINAR', 'CAL. TACNA N° 104', '(084) 30-1218',
                 'uriel_villanueva@hotmail.com'),

)
T_CONDICION_CONDUCTOR = (('TITULAR CATASTRAL', 'TITULAR CATASTRAL'),
                         ('ARRENDATARIO', 'ARRENDATARIO'),
                         ('CESION EN USO', 'CESION EN USO'),)
T_MANTENIMIENTO_F_ECONOMICA = (
    ('PREDIO CATASTRAL NUEVO', 'POR SER PREDIO CATASTRAL NUEVO'),
    ('VARIACION EN AREA DE USO', 'POR TENER VARIACION EN AREA DE USO'),
    ('CAMBIO DE CONDUCTOR', 'POR CAMBIO DE CONDUCTOR'),
    ('CAMBIO DE GIRO', 'POR CAMBIO DE GIRO'),)
T_DOCUMENTO_PRESENTADO_ECONOMICA = (
    ('LICENCIA DE FUNCIONAMIENTO', 'LICENCIA DE FUNCIONAMIENTO'),
    ('LICENCIA DE ANUNCIOS', 'LICENCIA DE ANUNCIOS'), (
    'LICENCIA DE FUNCIONAMIENTO Y ANUNCIOS',
    'LICENCIA DE FUNCIONAMIENTO Y ANUNCIOS'),)
t_anuncio = (
    ('011', 'AVISO ECOLOGICO VARIABLE'), ('012', 'AVISO ECOLOGICO LUMINOSO'),
    ('013', 'AVISO ECOLOGICO DE PROYECCION'),
    ('014', 'AVISO ECOLOGICO ILUMINADO'), ('021', 'CARTEL VARIABLE'),
    ('022', 'CARTEL LUMINOSO'), ('023', 'CARTEL DE PROYECCION'),
    ('024', 'CARTEL ILUMINADO'), ('031', 'CARTELERA VARIABLE'),
    ('032', 'CARTELERA LUMINOSO'), ('033', 'CARTELERA DE PROYECCION'),
    ('034', 'CARTELERA ILUMINADO'), ('041', 'GLOBO AEROSTATICO VARIABLE'),
    ('042', 'GLOBO AEROSTATICO LUMINOSO'),
    ('043', 'GLOBO AEROSTATICO DE PROYECCION'),
    ('044', 'GLOBO AEROSTATICO ILUMINADO'), ('051', 'LETRERO VARIABLE'),
    ('052', 'LETRERO LUMINOSO'), ('053', 'LETRERO DE PROYECCION'),
    ('054', 'LETRERO ILUMINADO'), ('061', 'LETRAS RECORTADAS VARIABLE'),
    ('062', 'LETRAS RECORTADAS LUMINOSO'),
    ('063', 'LETRAS RECORTADAS DE PROYECCION'),
    ('064', 'LETRAS RECORTADAS ILUMINADO'), ('071', 'MARQUESINA VARIABLE'),
    ('072', 'MARQUESINA LUMINOSO'), ('073', 'MARQUESINA DE PROYECCION'),
    ('074', 'MARQUESINA ILUMINADO'), ('081', 'PANEL SIMPLE VARIABLE'),
    ('082', 'PANEL SIMPLE LUMINOSO'), ('083', 'PANEL SIMPLE DE PROYECCION'),
    ('084', 'PANEL SIMPLE ILUMINADO'), ('091', 'PANEL MONUMENTAL VARIABLE'),
    ('092', 'PANEL MONUMENTAL LUMINOSO'),
    ('093', 'PANEL MONUMENTAL DE PROYECCION'),
    ('094', 'PANEL MONUMENTAL ILUMINADO'), ('101', 'PROYECCIONES VARIABLE'),
    ('102', 'PROYECCIONES LUMINOSO'), ('103', 'PROYECCIONES DE PROYECCION'),
    ('104', 'PROYECCIONES ILUMINADO'),
    ('111', 'ROTULOS EN VEHICULOS VARIABLE'),
    ('112', 'ROTULOS EN VEHICULOS LUMINOSO'),
    ('113', 'ROTULOS EN VEHICULOS DE PROYECCION'),
    ('114', 'ROTULOS EN VEHICULOS ILUMINADO'), ('121', 'TOLDOS VARIABLE'),
    ('122', 'TOLDOS LUMINOSO'), ('123', 'TOLDOS DE PROYECCION'),
    ('124', 'TOLDOS ILUMINADO'), ('131', 'AVISO ESCULTORIO VARIABLE'),
    ('132', 'AVISO ESCULTORIO LUMINOSO'),
    ('133', 'AVISO ESCULTORIO DE PROYECCION'),
    ('134', 'AVISO ESCULTORIO ILUMINADO'))
t_actividad_economica = (
    ('11101', 'MATANZA DE GANADO Y PREPARACIÓN Y CONSERVACIÓN DE CARNE '),
    ('11102', 'FABRICACIÓN DE PRODUCTOS LACTEOS '),
    ('11103', 'ENVASADOS Y CONSERVACIÓN DE FRUTAS Y LEGUMBRES '),
    ('11104', 'ELABORACIÓN DE PESCADO '),
    ('11105', 'FABRICACIÓN DE ACEITE Y GRASAS VEGETALES Y ANIMALES '),
    ('11106', 'PRODUCTOS DE MOLINERÍA '),
    ('11107', 'FABRICACIÓN DE PRODUCTOS DE PANADERÍA '),
    ('11108', 'FÁBRICAS Y REFINERIAS DE AZUCAR '),
    ('11109', 'FABRICACIÓN DE CACAO '),
    ('11110', 'ELABORACIÓN DE PRODUCTOS ALIMENTICIOS DIVERSOS '),
    ('11111', 'ELABORACIÓN DE ALIMENTOS PREPARADOS PARA ANIMALES '),
    ('11201', 'DESTILACIÓN '), ('11202', 'INDUSTRIAS VINÍCOLAS '),
    ('11203', 'BEBIDAS MALTEADAS Y MALTAS '),
    ('11204', 'INDUSTRIAS DE BEBIDAS NO ALCOHÓLICAS Y AGUAS GASEOSAS '),
    ('11301', 'INDUSTRIA DEL TABACO '), ('12101', 'HILADO '),
    ('12102', 'ARTÍCULOS CONFECCIONADOS DE MATERIALES TEXTILES '),
    ('12103', 'FÁBRICA DE TEJIDOS DE PUNTO '),
    ('12104', 'FABRICACIÓN DE TAPICES Y ALFOMBRAS '), ('12105', 'CORDELERÍA '),
    ('12106', 'FABRICACIÓN DE TEXTILES N.E.P. '),
    ('12201', 'FABRICACIÓN DE PRENDAS DE VESTIR EXCEPTO CALZADO '),
    ('12301', 'CURTIDURÍAS Y TALLERES DE ACABADO '),
    ('12302', 'INDUSTRIA DE LA PREPARACIÓN Y TEÑIDO DE PIELES '),
    ('12303', 'FABRICACIÓN DE ARTÍCULOS DE CUERO Y SUCEDÁNEOS DE CUERO '), (
    '12401',
    'FABRICACIÓN DE CALZADO EXCEPTO EL DE CAUCHO VULCANIZADO O MOLDEADO DE PLÁSTICO '),
    ('13101', 'ASERRADEROS '), ('13102',
                                'FABRICACIÓN DE ENVASES DE MADERA Y DE CAÑA Y ARTÍCULOS MENUDOS DE CAÑA '),
    ('13103', 'FABRICACIÓN DE PRODUCTOS DE MADERA Y CORCHO '),
    ('13201', 'FABRICACIÓN DE MUEBLES Y ACCESORIOS '),
    ('14101', 'FABRICACIÓN DE PULPA DE MADERA '),
    ('14102', 'FABRICACIÓN DE ENVASES Y CAJAS DE PAPEL Y DE CARTÓN '),
    ('14103', 'FABRICACIÓN DE ARTÍCULOS DE PULPA '), ('14201', 'IMPRENTAS '), (
    '15101',
    'FABRICACIÓN DE SUSTANCIAS QUÍMICAS INDUSTRIALES BÁSICAS EXCEPTO ABONOS '),
    ('15102', 'FABRICACIÓN DE ABONOS Y PLAGUICIDAS '),
    ('15103', 'FABRICACIÓN DE RESINAS SINTÉTICAS '),
    ('15201', 'FABRICACIÓN DE PINTURAS '),
    ('15202', 'FABRICACIÓN DE PRODUCTOS FARMACÉUTICOS Y MEDICAMENTOS '),
    ('15203', 'FABRICACIÓN DE JABONES Y PREPARADOS DE LIMPIEZA '),
    ('15204', 'FABRICACIÓN DE PRODUCTOS QUÍMICOS '),
    ('15301', 'REFINERIAS DE PETROLEO '), ('15302',
                                           'FABRICACIÓN DE PRODUCTOS DIVERSOS DERIVADOSDEL PETRÓLEO Y DEL CARBÓN '),
    ('15401', 'INDUSTRIAS DE LLANTAS Y CÁMARAS '),
    ('15402', 'FABRICACIÓN DE PRODUCTOS DE CAUCHO '),
    ('15403', 'FABRICACIÓN DE PRODUCTOS PLÁSTICOS '),
    ('16101', 'FABRICACIÓN DE OBJETOS DE BARRO '),
    ('16201', 'FABRICACIÓN DE VIDRIO Y PRODUCTOS DE VIDRIO '),
    ('16301', 'FABRICACIÓN DE OTROS PRODUCTOS DE ARCILLA PARA CONSTRUCCIÓN '),
    ('16302', 'FABRICACIÓN DE CEMENTO '),
    ('17101', 'INDUSTRIAS BÁSICAS DE HIERRO Y ACERO '),
    ('17201', 'INDUSTRIAS BÁSICAS DE METALES NO FERROSOS '),
    ('18101', 'FABRICACIÓN DE CUCHILLERÍA '),
    ('18102', 'FABRICACIÓN DE MUEBLES Y ACCESORIOS PRINCIPALES METÁLICOS '),
    ('18103', 'FABRICACIÓN DE PRODUCTOS METÁLICOS ESTRUCTURALES '),
    ('18104', 'FABRICACIÓN DE PRODUCTOS METÁLICOS '),
    ('18201', 'CONSTRUCCIÓN DE MOTORES Y TURBINAS '),
    ('18202', 'CONSTRUCCIÓN DE MAQUINARIAS Y EQUIPO PARA LA AGRICULTURA '), (
    '18203',
    'CONSTRUCCIÓN DE MAQUINARIAS PARA TRABAJAR LOS METALES Y LA MADERA '), (
    '18204',
    'CONSTRUCCIÓN DE MAQUINARIA Y EQUIPOS ESPECIALES PARA LAS INDUSTRIAS '),
    ('18205', 'CONSTRUCCIÓN DE MAQUINARIAS DE OFICINA '),
    ('18206', 'CONSTRUCCIÓN DE MAQUINARIA Y EQUIPO N.E.P. '),
    ('18301', 'CONSTRUCCIÓN DE MAQUINAS Y APARATOS INDUSTRIALES ELÉCTRICOS '),
    ('18302', 'CONSTRUCCIÓN DE EQUIPOS Y APARATOS DE RADIO '), ('18303',
                                                                'CONSTRUCCIÓN DE APARATOS Y ACCESORIOS ELÉCTRICOS DE USO DOMÉSTICO '),
    ('18304', 'CONSTRUCCIÓN DE APARATOS Y SUMINISTROS ELÉCTRICOS '),
    ('18401', 'CONSTRUCCIONES NAVALES Y REPARACIÓN DE BARCOS '),
    ('18402', 'CONSTRUCCIÓN DE EQUIPO FERROVIARIO '),
    ('18403', 'FABRICACIÓN DE VEHÍCULOS AUTOMÓVILES '),
    ('18404', 'FABRICACIÓN DE MOTOCICLETAS Y BICICLETAS '),
    ('18405', 'FABRICACIÓN DE AERONAVES '),
    ('18406', 'CONSTRUCCIÓN DE MATERIAL DE TRANSPORTE N.E.P. '),
    ('18501', 'FABRICACIÓN DE EQUIPO PROFESIONAL Y CIENTÍFICO '), (
    '18502', 'FABRICACIÓN DE APARATOS FOTOGRÁFICOS É INSTRUMENTOS DE ÓPTICA '),
    ('18503', 'FABRICACIÓN DE RELOJES '),
    ('19101', 'FABRICACIÓN DE JOYAS Y ARTÍCULOS CONEXOS '),
    ('19201', 'FABRICACIÓN DE INSTRUMENTOS DE MÚSICA '),
    ('19301', 'FABRICACIÓN DE ARTÍCULOS DE DEPORTE Y ATLETÍSMO '),
    ('19401', 'INDUSTRIAS MANUFACTURERAS N.E.P. '),
    ('20101', 'LUZ Y FUERZA ELÉCTRICA '),
    ('20102', 'PRODUCCIÓN Y DISTRIBUCIÓN DE GAS '),
    ('20103', 'SUMINISTRO DE VAPOR Y AGUA CALIENTE '),
    ('20201', 'OBRAS HIDRÁULICAS Y SUMINISTRO DE AGUA '),
    ('21101', 'CONSTRUCCION '), ('31101', 'CAFÉ EN GRANO '),
    ('31102', 'CEREALES '), ('31103', 'ESPECIERÍAS '), ('31104', 'FRUTERIAS '),
    ('31105', 'VERDULERÍA '), ('31106', 'MENESTRAS '),
    ('31107', 'TUBERCULOS '), ('31108', 'ACEITUNAS '), ('31109', 'CACAO '), (
    '31199',
    'OTROS PRODUCTOS AGRÍCOLAS COMESTIBLES NO CLASIFICADOS EN OTRA PARTE '),
    ('31201', 'ALGODÓN '), ('31202', 'FLORERIA '), ('31203', 'FORRAJES '),
    ('31204', 'SEMILLAS Y PLANTAS '), ('31205', 'TABACO EN RAMA '),
    ('31206', 'COCA '), ('31207', 'YERBA SECA PARA DIFERENTES USOS '), (
    '31209',
    'OTROS PRODUCTOS AGRÍCOLAS NO UTILIZADOS PARA EL CONSUMO NO CLASIFICADOS EN OTRA PARTE '),
    ('31301', 'PRODUCTOS DE LA CASA '), ('31302', 'PESES ORNAMENTALES '),
    ('31303', 'ANIMALES DE CARGA '), ('31304', 'COCHINILLA '),
    ('31305', 'ANIMALES DOMESTICOS '), ('31399',
                                        'OTROS ANIMALES NO UTILIZADOS EN LA ALIMENTACIÓN Y NO CLASIFICADOS EN OTRA PARTE '),
    ('31401', 'AVICOLAS '), ('31402', 'CARNICERIA '),
    ('31403', 'GANADO EN PIE '), ('31404', 'PESCADERIAS Y AFINES '),
    ('31405', 'ANIMALES PEQUEÑOS '), ('31499',
                                      'OTROS ANIMALES VIVOS Y PRODUCTOS PECUARIOS UTILIZADOS EN LA ALIMENTACIÓN Y NO CLASIFICADOS EN LA OTRA PARTE '),
    ('32101', 'PLANTAS MEDICINALES '), ('32102', 'TRONCOS PARA ASERRADEROS '),
    ('32103', 'COMERCIO DE MINERALES Y METALES '), ('32199',
                                                    'OTROS PRODUCTOS EN ESTADO NATURAL NO CLASIFICADOS EN OTRA PARTE '),
    ('32201', 'CAUCHO '), ('32202',
                           'PRODUCTOS PROVENIENTES DEL CULTIVO Y/O EXPLOTACIÓN DE OTRAS ESPECIES VEGETALES: GERMEN DE TRIGO '),
    ('32299', 'OTROS PRODUCTOS DERIVADOS NO INDUSTRIALIZADOS '),
    ('33101', 'CAFÉ DE TOSTADURIA '), ('33102', 'CONFITERIA '),
    ('33103', 'EMBUTIDOS '), ('33104', 'HELADERIAS '),
    ('33105', 'LECHERIA Y CREMERIA '), ('33106', 'PANADERIA Y PASTELERIA '),
    ('33107', 'TIENDA DE ABARROTES '),
    ('33109', 'OTROS PRODUCTOS ALIMENTICIOS NO CLASIFICADOS EN OTRA PARTE '),
    ('33110', 'MINIMARKET '), ('33201', 'NUTRIMENTOS '), ('33299',
                                                          'OTROS PRODUCTOS ALIMENTICIOS PREPARADOS PARA ANIMALES NO CLASIFICADOS EN OTRA PARTE '),
    ('33301', 'LICORERIAS '), ('33302', 'CIGARRERIA '),
    ('33303', 'BEBIDAS REFRESCANTES '),
    ('33399', 'OTROS ARTÍCULOS CONEXOS NO CLASIFICADOS EN OTRA PARTE '),
    ('33401', 'ARTICULOS DE TOCADOR E HIGIENE PERSONAL '),
    ('33402', 'FARMACIA '), ('33403', 'PRODUCTOS VETERINARIOS '),
    ('33499', 'OTROS PRODUCTOS FARMACÉUTICOS NO CLASIFICADOS EN OTRA PARTE '),
    ('33501', 'GAS PROPANO '), ('33502', 'GRIFO '), ('33503', 'CARBONERIA '),
    ('33504', 'LUBRICANTES '), ('33505', 'RON DE QUEMAR '),
    ('33599', 'OTROS COMBUSTIBLES '), ('34101', 'MERCERIA '),
    ('34102', 'ZAPATERIAS '), ('34103', 'PELETERIAS '), ('34104', 'BAZAR '),
    ('34105', 'SOMBRERERIA (SOMBREROS) '), ('34106', 'TELAS Y TEJIDOS '),
    ('34107', 'TRAJES DE BODA Y COMPROMISOS EN GENERAL Y ACCESORIOS '),
    ('34108', 'ARTICULOS PARA EL ARREGLO PERSONAL '),
    ('34199', 'OTRAS TELAS Y TEJIDOS '), ('34201', 'APARATOS DOMESTICOS '),
    ('34202', 'ALFOMBRAS '), ('34203', 'COLCHONERÍA '),
    ('34204', 'MUEBLERIA (MUEBLES PARA EL HOGAR) '), ('34205', 'LENCERIA '),
    ('34206', 'LOCERIA Y CRISTALERIA '), ('34207', 'UTENSILIOS DE COCINA '),
    ('34208', 'ARTÍCULOS PARA EL ARREGLO DEL HOGAR Y COMPLEMENTARIOS '),
    ('34299', 'OTROS ARTÍCULOS PARA EL HOGAR NO CLASIFICADOS EN OTRA PARTE '),
    ('34301', 'LIBRERÍA Y/O ARTICULOS DE OFICINA '),
    ('34302', 'REVISTAS Y PERIODICOS '), ('34303', 'TARJETAS '),
    ('34399', 'OTROS LIBROS '), ('34401', 'ARTICULOS ARTESANALES '),
    ('34402', 'ANTIGUEDADES '), ('34403', 'PLATERIA '),
    ('34404', 'CASA DE REGALOS '), ('34405', 'ARTICULOS RELIGIOSOS '),
    ('34406', 'DISFRACES Y ARTICULOS PARA FIESTAS '),
    ('34407', 'JOYERIA Y RELOJERIA '), ('34408', 'CUADROS Y ESCULTURAS '),
    ('34409', 'BRONCERIA '), ('34410', 'ARTICULOS DE FILATELIA '),
    ('34411', 'LAMPARAS '), ('34412', 'ARTICULOS DE FANTASIA '),
    ('34413', 'ARTICULOS DE PIROTECNIA '),
    ('34499', 'OTROS ARTÍCULOS Y DE LUJO NO CLASIFICADOS EN OTRA PARTE '),
    ('34501', 'AUTOMOVILES '), ('34502', 'BICICLETAS Y SIMILARES '),
    ('34503', 'MOTOCICLETAS Y MOTONETAS '), ('34599',
                                             'OTROS AUTOMÓVILES Y OTROS MEDIOS DE TRANSPORTE Y TRACCIÓN PERSONAL NO CLASIFICADOS EN OTRA PARTE '),
    ('34601', 'INMUEBLES '),
    ('34699', 'OTROS BIENES RAICES NO CLASIFICADOS EN OTRA PARTE '),
    ('34702', 'ARMERIA '), ('34703', 'ARTICULOS DEPORTIVOS '),
    ('34704', 'CASA DE DISCOS '),
    ('34705', 'EQUIPOS FOTOGRAFICOS Y DE PROYECCION '),
    ('34706', 'INSTRUMENTOS MUSICALES '), ('34707', 'JUGUETERIA '),
    ('34708', 'MALETERIA '), ('34709', 'CASA DE REMATES '),
    ('34710', 'OBJETOS DE CUERO PARA ANIMALES DE TRACCIÓN '),
    ('34711', 'OBJETOS DE CUERO PARA TRANSPORTE DE ARTÍCULOS PERSONALES '),
    ('34712', 'ARTÍCULOS DOMÉSTICOS DE PLÁSTICO Y ACRÍLICO '),
    ('34713', 'HOJALATERIA '), ('34799',
                                'OTROS ARTÍCULOS DIVERSOS DE USO DURADERO NO CLASIFICADOS EN OTRA PARTE '),
    ('35101', 'FERTILIZANTES Y PESTICIDAS '),
    ('35199', 'OTROS FERTILIZANTES '), ('35201', 'CUERO '),
    ('35202', 'CHATARRA '),
    ('35203', 'PRODUCTOS QUIMICOS INDUSTRIALES ESENCIALES '),
    ('35204', 'PAPEL Y CARBON '), ('35205', 'ALCOHOL HIDRATADO '),
    ('35206', 'LEVADURAS Y ESENCIAS '), ('35207', 'LANA '),
    ('35208', 'INSUMOS PARA LA INDUSTRIA DEL CALZADO '),
    ('35209', 'MARROQUINES '), ('35299',
                                'OTROS INSUMOS MANUFACTURADOS PARA LA INDUSTRIA DE TRANSFORMACIÓN NO CLASIFICADOS EN OTRA PARTE '),
    ('35301', 'FERRETERIA '), ('35302', 'CEMENTO '),
    ('35303', 'FIERRO Y ACERO EN VARILLAS '), ('35304', 'LADRILLOS '),
    ('35305', 'MADERAS '), ('35306', 'MARMOLERIA '), ('35307', 'PINTURAS '),
    ('35308', 'SANITARIOS '), ('35309', 'VIDRIERIA '),
    ('35310', 'PRODUCTOS DE CANTERAS '),
    ('35311', 'INSUMOS PARA CARPINTERÍA METÁLICA '), ('35399',
                                                      'OTROS INSUMOS MANUFACTURADOS USADOS PREFERENTEMENTE PARA LA CONSTRUCCIÓN NO CLASIFICADOS EN OTRA PARTE '),
    ('35401', 'REPUESTOS DE APARATOS DOMESTICOS '),
    ('35402', 'REPUESTOS DE VEHICULOS AUTOMOTORES '),
    ('35403', 'REPUESTOS DE MOTOS Y BICICLETAS '),
    ('35404', 'REPUESTOS DE MAQUINARIA EN GENERAL '),
    ('35405', 'OTROS REPUESTOS Y ACCESORIOS NO CLASIFICADOS EN OTRA PARTE '),
    ('36101', 'EQUIPOS DE SEGURIDAD E HIGIENE '),
    ('36102', 'EQUIPOS PARA OFICINA '), ('36103', 'MUEBLES PARA OFICINA '),
    ('36104', 'MAQUINARIAS '), ('36105', 'MAQUINARIAS '),
    ('36106', 'MAQUINARIAS '), ('36107', 'MAQUINARIAS '),
    ('36199', 'OTRAS MAQUINARIAS '), ('36201', 'PARA COMERCIO '),
    ('36202', 'PARA INGENIERIA '), ('36203', 'PARA MEDICINA '),
    ('36204', 'PARA SERVICIOS '), ('36205', 'OTROS APARATOS DE MEDICIÓN '),
    ('36301', 'CAMIONES '), ('36302', 'CARGADORES '),
    ('36303', 'VEHICULOS DE TRANSPORTE ACUATICO '),
    ('36399', 'OTROS VEHÍCULOS NO CLASIFICADOS EN OTRA PARTE '),
    ('37101', 'TIENDAS DE DEPARTAMENTOS '), ('37102', 'CAJAS '),
    ('37103', 'BOLSAS '), ('37104', 'BOTELLAS '), ('37105', 'HIELO '),
    ('37106', 'CHATARRA '),
    ('37199', 'OTROS BIENES NO IDENTIFICADOS EN LOS GRUPOS ANTERIORES '),
    ('41101', 'BAR '), ('41102', 'CAFÉ '), ('41103', 'CEVICHERÍA '),
    ('41104', 'CHIFA '), ('41105', 'DULCERIA '), ('41106', 'HELADERIA '),
    ('41107', 'JUGUERIA '), ('41108', 'PARRILLADA '), ('41109', 'PICANTERIA '),
    ('41110', 'POLLERIA '), ('41111', 'RECREO '), ('41112', 'RESTAURANTE '),
    ('41113', 'PIZZERIA '), ('41114', 'FUENTE DE SODA '),
    ('41115', 'SANDWICHERÍA '), ('41116', 'SNACK BAR '),
    ('41117', 'COMIDA AL PASO '), ('41199',
                                   'OTROS SERVICIOS DE ALIMENTACIÓN Y BEBIDAS NO CLASIFICADOS EN OTRA PARTE '),
    ('41201', 'ALQUILER DE TRAJES '), ('41202', 'LAVANDERIA Y TINTORERIA '),
    ('41203', 'LUSTRADO DE CALZADO '), ('41204', 'REPARACION DE CALZADO '),
    ('41205', 'TALLER DE SOMBRERIA '), ('41206', 'SASTRERÍA '),
    ('41207', 'TALLER DE MODAS '), ('41208', 'BORDADURIA '),
    ('41209', 'REMALLADORA DE MEDIAS '),
    ('41210', 'TALLER DE ESTAMPADOS Y PINTURAS DE TELAS '),
    ('41299', 'OTROS SERVICIOS DE VESTIMENTA NO CLASIFICADAS EN OTRA PARTE '),
    ('41301', 'ALQUILER DE INMUEBLES '), ('41302', 'CENTROS VACACIONALES '),
    ('41303', 'HOSTAL '), ('41304', 'HOSTAL RESIDENCIAL '),
    ('41305', 'HOTEL '), ('41306', 'HOTEL RESIDENCIAL '),
    ('41307', 'MOTELES '), ('41308', 'PENSION '),
    ('41309', 'MANTENIMIENTO Y LIMPIEZA DE INMUEBLES '), ('41310',
                                                          'OTROS SERVICIOS DE VIVIENDA Y ALOJAMIENTO NO CLASIFICADOS EN OTRA PARTE '),
    ('41401', 'BAÑOS PUBLICOS '), ('41402', 'PEDICURIA Y/O MANICURIA '),
    ('41403', 'PELUQUERIA '), ('41404', 'SALONES DE BELLEZA Y PEINADOS '),
    ('41405', 'BAÑOS SAUNA O BAÑOS TURCOS '), ('41406', 'GIMNASIO '), ('41499',
                                                                       'OTROS SERVICIOS DE HIGIENE Y ESTÉTICA PERSONAL NO CLASIFICADOS EN OTRA PARTE '),
    ('41501', 'FUNERARIAS '),
    ('41599', 'OTROS SERVICIOS PERSONALES NO CLASIFICADOS EN OTRA PARTE '),
    ('42101', 'MECANOGRAFIADO '),
    ('42102', 'FOTOCOPIA DE DOCUMENTOS Y/O ENMICADOS '),
    ('42103', 'FRAGMENTACION Y/O EMBAZADO '), ('42104', 'ROTULACION '),
    ('42105', 'FUMIGACION '), ('42106', 'AGENCIAS DE PUBLICACION '),
    ('42107', 'PROCESAMIENTO ELECTRONICO DE DATOS '),
    ('42108', 'ESTUDIO FOTOGRAFICO '), ('42109', 'DECORACIONES '),
    ('42110', 'INSTALACIONES INDUSTRIALES Y COMERCIALES '),
    ('42111', 'GALVANOPLASTIA '), ('42112', 'CERRAJERIA '),
    ('42113', 'TORNERIA '),
    ('42114', 'SERVICIOS TECNICOS DE ASESORIA E INVESTIGACION DE MERCADOS '),
    ('42115', 'SERVICIOS GRAFICOS '),
    ('42199', 'OTROS SERVICIOS TÉCNICOS NO CLASIFICADOS EN OTRA PARTE '),
    ('43101', 'ALINEAMIENTO DE DIRECCIÓN Y/O BALANCEO DE RUEDAS '),
    ('43102', 'FACTORIA '), ('43103', 'LAVADO Y ENGRASE DE VEHÍCULOS '),
    ('43104', 'RECTIFICACION DE MOTORES '),
    ('43105', 'TALLER DE REPARACIONES ELECTRICAS DE VEHICULOS AUTOMOTORES '),
    ('43106', 'TALLER DE MECANICA AUTOMOTRIZ '),
    ('43107', 'TALLER DE REPARACIÓN DE BICICLETAS Y/O MOTOCICLETAS '),
    ('43108', 'CARROCERIAS '), ('43109', 'TALLER DE PLANCHADO Y PINTURA '),
    ('43110', 'VULCANIZADORA Y/O REENCAUCHADORA '),
    ('43111', 'TALLER DE BATERIAS '),
    ('43112', 'REPARACION DE EMBARCACIONES PESQUERAS '),
    ('43113', 'INSTALACIÓN DE TUBOS DE ESCAPE Y AFINES '), ('43199',
                                                            'OTROS SERVICIOS DE MECÁNICA AUTOMOTRIZ Y AFINES NO CLASIFICADOS EN OTRA PARTE '),
    ('43201', 'TALLER DE SOLDADURA '),
    ('43202', 'TALLER DE REPARACION DE MAQUINARIA EN GENERAL '),
    ('43203', 'INSTALACIONES ELECTRICAS Y/O ELECTRONICAS '), ('43204',
                                                              'OTROS SERVICIOS DE MECÁNICA EN GENERAL Y ELECTRICIDAD NO CLASIFICADOS EN OTRA PARTE '),
    ('43301', 'TALLER DE REPARACION DE APARATOS DOMESTICOS ELECTRICOS '),
    ('43302', 'TALLER DE REPARACION DE APARATOS DE RADIO Y TELEVISION '),
    ('43303', 'TALLER DE REPARACION DE APARATOS DOMESTICOS MECANICOS '),
    ('43304', 'CARPINTERIA METALICA '), ('43306', 'TAPICERIA '),
    ('43307', 'GASFITERIA '), ('43308', 'REPARACIÓN DE CATRES Y SIMILARES '), (
    '43399',
    'REPARACIÓN DE OTROS APARATOS DOMÉSTICOS NO ESPECIFICADOS EN OTRA PARTE '),
    ('43401', 'TALLER DE MECANICA DE PRECISION '),
    ('43402', 'TALLER DE RELOJES '),
    ('43403', 'TALLER DE REPARACIONES DE JOYAS '), ('43499',
                                                    'OTROS SERVICIOS DE MECÁNICA FINA NO CLASIFICADOS EN OTRA PARTE '),
    ('44101', 'TRANSPORTE FERROVIARIO '), ('44102', 'TRANSPORTE URBANO '),
    ('44103', 'OTROS SERVICIOS TERRESTRES DE TRANSPORTE DE PASAJEROS '),
    ('44104', 'TRANSPORTE DE CARGA POR CARRETERA '),
    ('44105', 'TRANSPORTE POR OLEODUCTOS O GASEODUCTOS '),
    ('44106', 'SERVICIOS RELACIONADOS CON EL TRANSPORTE TERRESTRE '),
    ('44107', 'SILOS '), ('44199',
                          'OTROS SERVICIOS DE TRANSPORTE TERRESTRE NO ESPECIFICADOS EN OTRA PARTE '),
    ('44201', 'TRANSPORTE OCEANICO O DE CABOTAJE '),
    ('44202', 'TRANSPORTE POR VIAS DE NAVEGACION INTERIOR '),
    ('44203', 'ESTIBADORES '),
    ('44204', 'SERVICIOS RELACIONADOS CON EL TRANSPORTE DE AGUA '), ('44299',
                                                                     'OTROS SERVICIOS DE TRANSPORTE AÉREO NO CLASIFICADOS EN OTRA PARTE '),
    ('44301', 'EMPRESAS DE TRANSPORTE AEREO '),
    ('44302', 'SERVICIOS RELACIONADOS CON EL TRANSPORTE AEREO '),
    ('44399', 'OTROS SERVICIOS DE TRANSPORTE AÉREO '),
    ('44401', 'SERVICIOS RELACIONADOS CON EL TRANSPORTE '),
    ('44402', 'DEPÓSITO Y ALMACENAMIENTO '),
    ('44499', 'OTROS SERVICIOS CONEXOS NO CLASIFICADOS EN OTRA PARTE '),
    ('44501', 'COMUNICACIONES '),
    ('44502', 'OTROS SERVICIOS CONEXOS NO CLASIFICADOS EN OTRA PARTE '),
    ('45101', 'BANCO '), ('45102', 'AGENCIA BANCARIA '),
    ('45103', 'CAJA DE AHORRO '), ('45104', 'MUTUAL '),
    ('45105', 'COOPERATIVA DE CREDITO '), ('45106', 'CASA DE PRÉSTAMOS '),
    ('45199', 'OTRAS INSTITUCIONES MONETARIAS NO CLASIFICADAS EN OTRA PARTE '),
    ('45201', 'FINANCIERAS '), ('45202', 'BOLSA DE VALORES '),
    ('45203', 'AGENCIAS CAMBIARIAS '),
    ('45204', 'COMPAÑÍA DE PATENTES Y LICENCIAS '),
    ('45205', 'SERVICIOS FINANCIEROS '), ('45299',
                                          'OTROS SERVICIOS DE ESTABLECIMIENTOS FINANCIEROS NO CLASIFICADOS EN OTRA PARTE '),
    ('45301', 'SEGUROS '),
    ('45399', 'OTROS SERVICIOS DE SEGUROS NO CLASIFICADOS EN OTRA PARTE '),
    ('45401', 'SERVICIOS JURIDICOS '), ('45402', 'SERVICIOS DE CONTABILIDAD '),
    ('45403', 'SERVICIOS DE ELABORACION DE DATOS Y DE TABULACION '),
    ('45404', 'SERVICIOS TECNICOS Y ARQUITECTÓNICOS '),
    ('45405', 'SERVICIOS DE PUBLICIDAD '), ('45406', 'AGENCIA COMISIONISTA '),
    ('45407', 'COBRANZAS Y/O MENSAJES '), ('45408', 'AGENCIA DE EMPLEOS '),
    ('45409', 'AGENCIAS DE TRÁMITES '),
    ('45499', 'SERVICIOS PRESTADOS A LAS EMPRESAS '),
    ('45501', 'ALQUILER Y ARRENDAMIENTO DE MAQUINARIA Y EQUIPO '), ('45599',
                                                                    'OTROS SERVICIOS DE ALQUILER Y ARRENDAMIENTO DE MAQUINARIA Y EQUIPO NO CLASIFICADOS EN OTRA PARTE '),
    ('46101', 'SERVICIOS DE SANEAMIENTO Y SIMILARES '), ('46102',
                                                         'OTROS SERVICIOS DE SANEAMIENTO Y SIMILARES NO CLASIFICADOS EN OTRA PARTE '),
    ('46201',
     'SERVICIOS MÉDICOS Y ODONTOLÓGICOS Y OTROS SERVICIOS DE SANIDAD '),
    ('46203', 'ASOCIACIONES COMERCIALES '), ('46299',
                                             'OTROS SERVICIOS SOCIALES Y COMUNALES NO CLASIFICADOS EN OTRA PARTE '),
    ('46301', 'PRODUCCION DE PELICULAS CINEMATOGRAFICAS '),
    ('46302', 'DISTRIBUCION Y EXHIBICION DE PELICULAS CINEMATOGRAFICAS '),
    ('46303', 'EMISION DE RADIO Y TELEVISION '),
    ('46304', 'PRODUCTORES TEATRALES Y SERVICIOS DE ESPARCIMIENTO '),
    ('46305', 'AUTORES '), ('46306', 'BIBLIOTECAS '),
    ('46307', 'SERVICIOS DE DIVERSION Y ESPARCIMIENTO '),
    ('46308', 'ALQUILER DE APARATOS É INSTRUMENTOS MUSICALES '),
    ('46309', 'CENTROS DE COMPETENCIAS Y/O APUESTAS '),
    ('46310', 'CENTROS NOCTURNOS '), ('46311', 'CABARET '),
    ('46312', 'DISCOTECA '), ('46313', 'BOITE '), ('46314', 'COLISEOS '),
    ('46315', 'SALON DE JUEGOS '), ('46316', 'SERVICIOS PARA FIESTAS '),
    ('46317', 'CAFÉ-TEATROS '), ('46318', 'PEÑA CRIOLLA '),
    ('46319', 'CASAS DE CITAS '), ('46320', 'PROSTIBULOS '),
    ('46322', 'ALQUILER DE VIDEOS (V.H.S.) '),
    ('46323', 'VIDEOS JUEGOS (NINTENDO) '), ('46324', 'VIDEO PUB '),
    ('46327', 'PUB '), ('46400', 'EDUCACION '),
    ('46330', 'TALLER ARTES PLÁSTICAS '),
    ('46399', 'OTROS SERVICIOS DE DIVERSIÓN      '),)
T_USO_BIENES_COM = (
    ('EDIFICIO', '(100101) EDIFICIO'), ('QUINTA', '(100102) QUINTA'),
    ('CALLEJÓN', '(100103) CALLEJÓN'), ('CORRALÓN', '(100104) CORRALÓN'),
    ('SOLAR', '(100105) SOLAR'),
    ('CASA HABITACIÓN', '(100106) CASA HABITACIÓN'),
    ('CENTRO COMERCIAL', '(100201) CENTRO COMERCIAL'),
    ('GALERÍA', '(100202) GALERÍA'), ('OFICINA', '(100203) OFICINA'),
    ('OTRO NO ESPECIFICADO', '(100204) OTRO NO ESPECIFICADO'),
    ('MERCADO', '(100205) MERCADO'), ('INDUSTRIA', '(100301) INDUSTRIA'),
    ('RESIDENCIAL', '(100401) RESIDENCIAL'),
    ('COMERCIAL', '(100402) COMERCIAL'), ('NDUSTRIAL', '(100403) NDUSTRIAL'),)
T_MANTENIMIENTO_F_BIENES_COMUNES = (
    ('VARIACION DE UNIDADES', 'POR VARIACION DE UNIDADES'),
    ('VARIACION EN LA CONSTRUCCION', 'POR VARIACION EN LA CONSTRUCCION'),
    ('VARIACION DE PORCENTAJE', 'POR VARIACION DE PORCENTAJE'),
    ('CAMBIO DE USO', 'POR CAMBIO DE USO'),)
T_CATEGORIA_INMUEBLE = (('PATRIMONIO MUNDIAL', '(01) PATRIMONIO MUNDIAL'), (
'ZONA ARQUIOLÓGICA MONUMENTAL', '(02) ZONA ARQUIOLÓGICA MONUMENTAL'),
                        ('SITIO ARQUIOLÓGICO', '(03) SITIO ARQUIOLÓGICO'), (
                        'ZONA DE RESERVA ARQUIOLÓGICA',
                        '(04) ZONA DE RESERVA ARQUIOLÓGICA'), (
                        'ELEMENTO ARQUIOLÓGICO AISLADO',
                        '(05) ELEMENTO ARQUIOLÓGICO AISLADO'), (
                        'PAISAJE CULTURAL ARQUIOLÓGICO',
                        '(06) PAISAJE CULTURAL ARQUIOLÓGICO'),)
T_UNIDAD_MEDIDA = (('M2', 'M2'), ('HAS', 'HAS'),)
T_FILIACION_CRONOLOGICA = (('PRECERÁMICO', '(01) PRECERÁMICO'),
                           ('PERIODO INICIAL', '(02) PERIODO INICIAL'),
                           ('HORIZONTE TEMPRANO', '(03) HORIZONTE TEMPRANO'),
                           ('INTERMEDIO TEMPRANO', '(04) INTERMEDIO TEMPRANO'),
                           ('HORIZONTE MEDIO', '(05) HORIZONTE MEDIO'),
                           ('INTERMEDIO TARDÍO', '(06) INTERMEDIO TARDÍO'),
                           ('HORIZONTE TARDÍO', '(07) HORIZONTE TARDÍO'),
                           ('VARIOS PERIODOS', '(08) VARIOS PERIODOS'),
                           ('INDETERMINADO', '(09) INDETERMINADO'),)
t_TipoArquitectura = (
    'MONTÍCULO', 'PLATAFORMAS', 'PIRÁMIDE', 'COMPLEJO PIRAMIDAL',
    'ESTRUCTURA AISLADA', 'ALDEA', 'CIUDADELA', 'SITIO AMURALLADO',
    'ESTRUCTURA FUNERARIA', 'CEMENTERIO', 'ÁREAS DE ACTIVIDAD', 'PARAVIENTO',
    'ABRIGOS Y CUEVAS', 'PETROGLIFOS', 'TERRAZAS HABITACIONALES',
    'SISTEMA HIDRÁULICO', 'SISTEMA DE CAMINOS', 'SISTEMA AGRÍCOLA',
    'GEOGLIFOS', 'PINTURAS RUPESTRES',)
t_TipoMaterialConstruido = (
    'Piedra sin trabajo', 'Piedra Canteada', 'Piedra Labrada',
    'Adobe hecho a mano', 'Adobe hecho en molde', 'Tapial', 'Quincha',)
t_TipoAfectacionesNaturales = (
    'Lluvia', 'Vegetación', 'Inundaciones', 'Erosión', 'Huaycos', 'Eólico',
    'Animales', 'Fenómenos Atmosféricos')
t_TipoAfectacionesAntropicas = (
    'Huaqueo', 'Invasiones', 'Grafittis', 'Agricultura', 'Actividades Mineras',
    'Vías de Acceso', 'Trabajos Públicos', 'turismo no controlado', 'pastoreo',
    'basura',)

t_TipoIntervencionConservacion = (
    'RestauradoSeñalizado', 'Anastilosis', 'Conservación', 'Consolidación',
    'Cerco Perimétrico', 'Museo de Sitio', 'Puesta en Valor',)
T_PRESENCIA_NORMAL = (('MAP', 'MONUMENTO ARQUEOLOGICO PREHISPANO'),
                      ('MHCR', 'MONUMENTO HISTORICO COLONIAL/REPUBLICANO'),)
T_ARQUITECTURA = (('CIVIL PÚBLICA', '(01) CIVIL PÚBLICA'),
                  ('CIVIL DOMÉSTICA', '(02) CIVIL DOMÉSTICA'),
                  ('RELIGIOSA', '(03) RELIGIOSA'), ('MILITAR', '(04) MILITAR'),
                  ('INDUSTRIAL', '(05) INDUSTRIAL'),
                  ('FUNERARIA', '(06) FUNERARIA'),)
T_ANIO_CONSTRUCCION = (('AÑO', 'AÑO'), ('SIGLO', 'SIGLO'),)
t_ElementosArquitectonicosMonumento = (
    'Portada', 'Balcones', 'Pilastras', 'Molduras', 'Cornisas', 'Ventanas',
    'Balaustra', 'Rejas',)
T_FILIACION_ESTILISTICA = (
    ('GÓTICO', '(01) GÓTICO'), ('MUDÉJAR', '(02) MUDÉJAR'),
    ('PLATERESCO', '(03) PLATERESCO'), ('RENACENTISTA', '(04) RENACENTISTA'),
    ('MANIERISTABARROCO', '(05) MANIERISTABARROCO'), ('ROCOCO', '(06) ROCOCO'),
    ('NEOCLÁSICO', '(07) NEOCLÁSICO'),
    ('NEORENACENTISTA', '(08) NEORENACENTISTA'),
    ('ACADEMICISTA', '(09) ACADEMICISTA'),
    ('ART NOUVEAU', '(010) ART NOUVEAU'), ('NEOCOLONIAL', '(011) NEOCOLONIAL'),
    ('NEOPERUANO', '(012) NEOPERUANO'), ('INDIGENISTA', '(013) INDIGENISTA'),
    ('ART-DECO', '(014) ART-DECO'),)
T_ESTADO_ELEMENTO_ESTRUCTURAL = (
    ('BUENO', 'BUENO'), ('REGULAR', 'REGULAR'), ('MALO', 'MALO'),)
T_INTERVENCION_INMUEBLE = (
    ('AMPLIACIÓN', '(01) AMPLIACIÓN'), ('ANASTILOSIS', '(02) ANASTILOSIS'),
    ('CONSERVACIÓN', '(03) CONSERVACIÓN'),
    ('CONSOLIDACIÓN', '(04) CONSOLIDACIÓN'),
    ('CONSTRUCCIÓN', '(05) CONSTRUCCIÓN'), ('DEMOLICIÓN', '(06) DEMOLICIÓN'), (
    'RENOVACIÓN/REVITALIZACIÓN URBANA',
    '(07) RENOVACIÓN/REVITALIZACIÓN URBANA'),
    ('PROTECCIÓN', '(08) PROTECCIÓN'),
    ('PUESTA EN VALOR', '(09) PUESTA EN VALOR'),
    ('REFACCIÓN', '(010) REFACCIÓN'), ('REMODELACIÓN', '(011) REMODELACIÓN'),
    ('OBRA NUEVA', '(012) OBRA NUEVA'),
    ('RESTAURACIÓN', '(013) RESTAURACIÓN'),)
T_USO_RURAL = (('TERRENO DE CULTIVO', '(01) TERRENO DE CULTIVO'),
               ('TERRENO DESNUDO', '(02) TERRENO DESNUDO'),
               ('COBERTURA ARBÓREA', '(03) COBERTURA ARBÓREA'),
               ('PASTOS NATURALES', '(04) PASTOS NATURALES'),
               ('USO NO AGRÍCOLA', '(05) USO NO AGRÍCOLA'),
               ('TURÍSTICO / RECREACIONAL', '(06) TURÍSTICO / RECREACIONAL'),
               ('ERIAZO', '(07) ERIAZO'),)
T_CLASIFICACION_USO_ACTUAL = (
    ('AGRÍCOLA', '(01) AGRÍCOLA'), ('GANADERA', '(02) GANADERA'),
    ('AVÍCOLAFORESTAL', '(03) AVÍCOLAFORESTAL'),
    ('AGRO-INDUSTRIAL', '(04) AGRO-INDUSTRIAL'),)
T_CONSTRUCCION_INSTALACION = (
    ('DEPÓSITO', '(01) DEPÓSITO'), ('RANCHERÍA', '(02) RANCHERÍA'),
    ('ESTABLO', '(03) ESTABLO'), ('CORRAL', '(04) CORRAL'),
    ('SILO', '(05) SILO'), ('GALPON DE AVES', '(06) GALPON DE AVES'),
    ('INVERNADERO', '(07) INVERNADERO'), ('POZO', '(08) POZO'),
    ('TANQUE ELEVADO', '(09) TANQUE ELEVADO'),
    ('RESERVORIO', '(10) RESERVORIO'),
    ('CANAL REVESTIDO', '(11) CANAL REVESTIDO'),)
T_RIEGO = (
    ('GRAVEDAD', 'RIEGO POR GRAVEDAD'), ('TECNIFICADO', 'RIEGO TECNIFICADO'),
    ('SECANO', 'SECANO'),)
T_DOCUMENTO_ACREDITA_RURAL = (('PROPIEDAD', (
    ('TITULO DE PROPIEDAD.', '(01) TITULO DE PROPIEDAD.'), (
    'CONTRATO DE OTORGAMIENTO DE TERRENOS RÚSTICOS.',
    '(02) CONTRATO DE OTORGAMIENTO DE TERRENOS RÚSTICOS.'), (
    'ESCRITURA PUBLICA DE COMPRA VENTA',
    '(03) ESCRITURA PUBLICA DE COMPRA VENTA, CELEBRADA ANTE NOTARIO-TESTIMONIO PÚBLICO.'),
    ('RESOLUCIÓN DE ADJUDICACIÓN.', '(04) RESOLUCIÓN DE ADJUDICACIÓN.'), (
    'CONTRATO OTORGADO DE ACUERDO A LA LEY NO 15037.',
    '(05) CONTRATO OTORGADO DE ACUERDO A LA LEY NO 15037.'), (
    'CONTRATO DE OTORGAMIENTO DE TERRENOS ERIAZOS ',
    '(06) CONTRATO DE OTORGAMIENTO DE TERRENOS ERIAZOS CON FINES DE IRRIGACIÓN Y OTROS USOS.'),
    ('ESCRITURA PUBLICA DE INDEPENDIZACIÓN ',
     '(07) ESCRITURA PUBLICA DE INDEPENDIZACIÓN OTORGADA POR LA  COOPERATIVA AGRARIA DE TRABAJADORES.'),
    ('TÍTULO SUPLETORIO CON RESOLUCIÓN JUDICIAL CONSENTIDA.',
     '(08) TÍTULO SUPLETORIO CON RESOLUCIÓN JUDICIAL CONSENTIDA.'), (
    'PRESCRIPCIÓN ADQUISITIVA DE DOMINIO CON RESOLUCIÓN JUDICIAL CONSENTIDA.',
    '(09) PRESCRIPCIÓN ADQUISITIVA DE DOMINIO CON RESOLUCIÓN JUDICIAL CONSENTIDA.'),
    ('MINUTA DE COMPRA VENTA.', '(10) MINUTA DE COMPRA VENTA.'), (
    'ANTICIPO DE HERENCIA MEDIANTE ESCRITURA PÚBLICA O MINUTA',
    '(11) ANTICIPO DE HERENCIA MEDIANTE ESCRITURA PÚBLICA O MINUTA, ACOMPAÑADA CON EL FORMULARIO REGISTRAL.'),
    ('DECLARATORIA DE HEREDEROS',
     '(12) DECLARATORIA DE HEREDEROS, CON RESOLUCIÓN JUDICIAL CONSENTIDA.'), (
    'DIVISIÓN Y PARTICIÓN DE PREDIOS PRIVADOS POR ESCRITURA PÚBLICA.',
    '(13) DIVISIÓN Y PARTICIÓN DE PREDIOS PRIVADOS POR ESCRITURA PÚBLICA.'),
    ('RESOLUCIÓN DE INAFECTACIÓN.', '(14) RESOLUCIÓN DE INAFECTACIÓN.'),)), (
                              'POSESIÓN', ((
                                           'DECLARACIÓN ESCRITA DE TODOS LOS COLINDANTES Y/O SEIS VECINOS.',
                                           '(01) DECLARACIÓN ESCRITA DE TODOS LOS COLINDANTES Y/O SEIS VECINOS.'),
                                           (
                                               'DECLARACIÓN ESCRITA DE COMITÉS, FONDOS U ORGANIZACIONES REPRESENTATIVAS DE LOS PRODUCTORES AGRARIOS DE LA ZONA.',
                                               '(02)  DECLARACIÓN ESCRITA DE COMITÉS, FONDOS U ORGANIZACIONES REPRESENTATIVAS DE LOS PRODUCTORES AGRARIOS DE LA ZONA.'),
                                           (
                                           'DECLARACIÓN ESCRITA DE LA JUNTA DE USUARIOS O COMISIONES DE REGANTES DEL RESPECTIVO DISTRITO DE RIEGO.',
                                           '(03) DECLARACIÓN ESCRITA DE LA JUNTA DE USUARIOS O COMISIONES DE REGANTES DEL RESPECTIVO DISTRITO DE RIEGO.'),
                                           (
                                               'CONSTANCIA DE POSESIÓN OTORGADA POR LA AGENCIA AGRARIA RESPECTIVA PARA LA INSCRIPCIÓN DEL DERECHO DE POSESIÓN AL AMPARO DEL D.L. NO 667.',
                                               '(04)  CONSTANCIA DE POSESIÓN OTORGADA POR LA AGENCIA AGRARIA RESPECTIVA PARA LA INSCRIPCIÓN DEL DERECHO DE POSESIÓN AL AMPARO DEL D.L. NO 667, EXPEDIDA DENTRO DE LOS 6 MESES ANTERIORES A LA SOLICITUD DE INSCRIPCIÓN EN EL REGISTRO.'),
                                           (
                                           'DOCUMENTOS QUE ACREDITEN PRÉSTAMOS O ADELANTOS DE PRÉSTAMOS POR CRÉDITO AGRARIO.',
                                           '(05) DOCUMENTOS QUE ACREDITEN PRÉSTAMOS O ADELANTOS DE PRÉSTAMOS POR CRÉDITO AGRARIO, OTORGADOS POR INSTITUCIONES BANCARIAS A FAVOR DEL POSEEDOR.'),
                                           (
                                           'DECLARACIÓN JURADA DEL PAGO DEL IMPUESTO PREDIAL, CORRESPONDIENTE A LOS AÑOS DE POSESIÓN DEL PREDIO.',
                                           '(06)  DECLARACIÓN JURADA DEL PAGO DEL IMPUESTO PREDIAL, CORRESPONDIENTE A LOS AÑOS DE POSESIÓN DEL PREDIO. LAS DECLARACIONES JURADAS QUE HAYAN SIDO FORMULADAS EN VÍAS DE REGULARIZACIÓN SOLO TIENEN MÉRITO PARA ACREDITAR POSESIÓN RESPECTO DE LA FECHA QUE HAN SIDO PRESENTADOS.'),
                                           (
                                           'RECIBOS DE PAGOS REALIZADOS POR EL POSEEDOR, POR CONCEPTO DE USO DE AGUA, CON FINES AGRARIOS.',
                                           '(07)  RECIBOS DE PAGOS REALIZADOS POR EL POSEEDOR, POR CONCEPTO DE USO DE AGUA, CON FINES AGRARIOS.'),
                                           (
                                           'DOCUMENTO PÚBLICO O PRIVADO CON FIRMAS LEGALIZADAS POR NOTARIO PÚBLICO O JUEZ DE PAZ .',
                                           '(08)  DOCUMENTO PÚBLICO O PRIVADO CON FIRMAS LEGALIZADAS POR NOTARIO PÚBLICO O JUEZ DE PAZ .'),
                                           (
                                           'CONTRATO DE COMPRA VENTA DE LA PRODUCCIÓN AGRARIA, PECUARIA O FORESTAL.',
                                           '(09)  CONTRATO DE COMPRA VENTA DE LA PRODUCCIÓN AGRARIA, PECUARIA O FORESTAL, CELEBRADO CON EMPRESAS DEL ESTADO.'),
                                           (
                                           'CONSTANCIA DE REGISTRO DEL POSEEDOR, EN EL RESPECTIVO PADRÓN DE REGANTES',
                                           '(10)  CONSTANCIA DE REGISTRO DEL POSEEDOR, EN EL RESPECTIVO PADRÓN DE REGANTES, EXPEDIDA DENTRO DE LOS 6 MESES ANTERIORES AL LLENADO DE LA FICHA.'),
                                           (
                                           'INSPECCIÓN JUDICIAL DE TIERRAS EN PROCESO DE PRUEBA ANTICIPADA.',
                                           '(11) INSPECCIÓN JUDICIAL DE TIERRAS EN PROCESO DE PRUEBA ANTICIPADA, CON EL OBJETO DE VERIFICAR LA POSESIÓN DEL PREDIO.'),
                                           (
                                           'CERTIFICADO DE INSCRIPCIÓN DE MARCAS Y SEÑALES DE GANADO, EXPEDIDO A NOMBRE DEL POSEEDOR.',
                                           '(12) CERTIFICADO DE INSCRIPCIÓN DE MARCAS Y SEÑALES DE GANADO, EXPEDIDO A NOMBRE DEL POSEEDOR.'),
                                           (
                                           'CERTIFICADO DE INSCRIPCIÓN DEL POSEEDOR DEL PREDIO EN EL PADRÓN DE PRESTATARIOS DE FONDOS ROTATORIOS.',
                                           '(13) CERTIFICADO DE INSCRIPCIÓN DEL POSEEDOR DEL PREDIO EN EL PADRÓN DE PRESTATARIOS DE FONDOS ROTATORIOS.'),
                                           (
                                               'CERTIFICADO EXPEDIDO A NOMBRE DEL POSEEDOR DEL PREDIO DE HABER SIDO EMPADRONADO POR EL INSTITUTO NACIONAL DE ESTADÍSTICA E INFORMÁTICA.',
                                               '(14) CERTIFICADO EXPEDIDO A NOMBRE DEL POSEEDOR DEL PREDIO DE HABER SIDO EMPADRONADO POR EL INSTITUTO NACIONAL DE ESTADÍSTICA E INFORMÁTICA.'),
                                           (
                                               'CERTIFICADO EXPEDIDO A NOMBRE DEL POSEEDOR DEL PREDIO DE TENER ADEUDOS PENDIENTES DE PAGO POR CONTRATOS DE CRÉDITOS AGRÍCOLAS CON FONDEAGRO O EL MINAG.',
                                               '(15) CERTIFICADO EXPEDIDO A NOMBRE DEL POSEEDOR DEL PREDIO DE TENER ADEUDOS PENDIENTES DE PAGO POR CONTRATOS DE CRÉDITOS AGRÍCOLAS CON FONDEAGRO O EL MINAG.'),
                                           (
                                           'CERTIFICADO EN EL QUE CONSTE QUE EL POSEEDOR FUE PRESTATARIO DEL BANCO AGRARIO',
                                           '(16) CERTIFICADO EN EL QUE CONSTE QUE EL POSEEDOR FUE PRESTATARIO DEL BANCO AGRARIO'),
                                           (
                                               'CERTIFICADO EN QUE CONSTE QUE EL PREDIO ESTUVO INSCRITO A NOMBRE DEL POSEEDOR EN EL PADRÓN CATASTRAL DE LA EX DIRECCIÓN GENERAL DE REFORMA AGRARIA Y ASENTAMIENTO RURAL.',
                                               '(17) CERTIFICADO EN QUE CONSTE QUE EL PREDIO ESTUVO INSCRITO A NOMBRE DEL POSEEDOR EN EL PADRÓN CATASTRAL DE LA EX DIRECCIÓN GENERAL DE REFORMA AGRARIA Y ASENTAMIENTO RURAL.'),))

)
T_SEXO = (("VARON", 'VARON'), ("MUJER", 'MUJER'),)
T_TELEFONO = (('TELEFONO', 'TELEFONO'), ('CELULAR', 'CELULAR'))
T_OPERADOR_TELEFONO = (
('AMERICATEL', 'AMERICATEL'), ('BITEL', 'BITEL'), ('CLARO', 'CLARO'),
('ENTEL', 'ENTEL'), ('MOVISTAR', 'MOVISTAR'), ('OTRO', 'OTRO'))
T_SELECTOR_PERSONA = (('TITULAR', 'EXISTE CATASTRAL TITULAR'),
                      ('DESCONOCIDO', 'TITULAR CATASTRAL DESCONOCIDO'),
                      ('COTITULARIDAD', 'TITULAR CATASTRAL EN CO TITULARIDAD'),
                      ('LITIGIO', 'PROPIEDAD EN LITIGIO'),
                      ('FALLECIDO', 'TITULAR CATASTRAL FALLECIDO'),)
