#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from curriculo import models as curriculo
from hojadevida import models as hoja
from configuracion import models as conf
from datetime import date
# Create your models here.


class Horario(models.Model):
    dia = models.IntegerField()
    ini = models.IntegerField()
    fin = models.IntegerField()
    horas = models.IntegerField()
    anio = models.IntegerField("Año", default=date.today().year)
    materia = models.ForeignKey(curriculo.Materia, verbose_name="Materia")
    profesor = models.ForeignKey(hoja.Profesor, verbose_name="Profesor")
    curso = models.ForeignKey(curriculo.Curso, verbose_name="Curso")
    jornada = models.ForeignKey(conf.Configuracion)

    def __unicode__(self):
        return u"Curso %s, Materia %s, Profesor %s %s" % (self.curso.nombre, self.materia.nombre, self.profesor.first_name, self.profesor.last_name)
    # end def
# end class
