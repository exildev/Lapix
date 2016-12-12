#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    registro = models.CharField(max_length=200, verbose_name="Registro Dane")
    direccion = models.TextField(max_length=400, verbose_name="Dirección")
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Configuracion(models.Model):
    BOOL_CHOICES7 = ((2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'),
                     (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'))
    BOOL_CHOICES2 = ((1, 'Primera'), (2, 'Segunda'), (3, 'Tercera'), (4, 'Cuarta'), (5, 'Quinta'), (6, 'Sexta'),
                     (7, 'Septima'), (8, 'Octava'), (9, 'Novena'), (10,
                                                                    'Decima'), (11, 'Decima Primera'),
                     (12, 'Decima segunda'))
    BOOL_CHOICES1 = ((1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'),
                     (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'))

    BOOL_CHOICES3 = (
        (0, '00'), (1, '01'), (2, '02'), (3, '03'), (4, '04'), (5,
                                                                '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'),
        (10, '10'),
        (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15,
                                                         '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'),
        (20, '20'),
        (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25,
                                                         '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'),
        (30, '30'),
        (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35,
                                                         '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'),
        (40, '40'),
        (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45,
                                                         '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'),
        (50, '50'),
        (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'))

    BOOL_CHOICES4 = ((0, 'am'), (1, 'pm'))
    sede = models.ForeignKey(Sede, verbose_name='*Sede')
    BOOL_CHOICES5 = ((1, 'Diurna'), (2, 'Tarde'), (3, 'Nocturna'))
    jornada = models.IntegerField("*Jornada", choices=BOOL_CHOICES5, default=1)
    horaIni = models.IntegerField(
        "*Horas de inicio de clase", choices=BOOL_CHOICES1, default=7)
    miniIni = models.IntegerField(
        "*Minutos de inicio de clase", choices=BOOL_CHOICES3, default=0)
    nothora = models.IntegerField(
        "*Notacion de la hora ", choices=BOOL_CHOICES4, default=0)
    desIni = models.IntegerField(
        "*Inicio descanso al finalizar la hora", choices=BOOL_CHOICES2, default=4)
    horaDia = models.IntegerField("*Valor hora academica en minutos")
    cantidaHora = models.IntegerField("*Cantidad de Horas al día")
    minutos_descanso = models.IntegerField("*Cantidad minutos descanso")
    ano = models.IntegerField(choices=BOOL_CHOICES7)
    hora_ini_sec_1 = models.CharField(max_length=200)
    hora_fin_sec_1 = models.CharField(max_length=200)
    hora_ini_sec_2 = models.CharField(max_length=200)
    hora_fin_sec_2 = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % convertirJornada(self.jornada)
    # end def
# end class


class Descanso(models.Model):
    jornada = models.ForeignKey(Configuracion)
    inicio = models.IntegerField()
    minutos = models.IntegerField()

    def __unicode__(self):
        return '%s' % convertirJornada(self.jornada.jornada)
    # end def
# end class


class ConfiguracionPeriodo(models.Model):
    cantidad = models.IntegerField("Cantidad de Periodos Academicos")
    inicio = models.DateField("Inicio del Periodo Academico")
    fin = models.DateField("Fin del Periodo Academico")

    def __unicode__(self):
        return "Configuracion Periodo Academico"
    # end def
# end class


class Salon(models.Model):
    cantidad = models.IntegerField("Numero de estudiantes por salon")

    def __unicode__(self):
        return "Configuracion de cupos en salon"
    # end def
# end class

# Borrar despues


class MaxMinGrado(models.Model):
    cantidad = models.IntegerField("Numero de grado minimo")
    cantidad2 = models.IntegerField("Numero de grado maximo")

    def __unicode__(self):
        return "Configuracion de grado inicial y final"
    # end def
# end class


class FechaPeriodo(models.Model):
    inicio = models.DateField("* Inicio de periodos ")
    fin = models.DateField("* Fin de periodos ")

    def __unicode__(self):
        return '%s - %s' % (self.inicio, self.fin)
    # end def
# end class


class Periodo(models.Model):
    configuracion = models.ForeignKey(ConfiguracionPeriodo)
    nombreP = models.IntegerField("Nombre")
    inicio = models.DateField(null=True, blank=False)
    fin = models.DateField(null=True, blank=False)
    porcentaje = models.FloatField("Porcenaje")

    def __unicode__(self):
        nombre = "Periodo %d" % (self.nombreP)
        return nombre
    # emd def
# end class


def convertirJornada(n):
    if n == 1:
        return "Diurna"
    elif n == 2:
        return "Vespertina"
    else:
        return "Nocturna"
    # end if
# end def
