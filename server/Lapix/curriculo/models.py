#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from hojadevida import models as hoja
from configuracion import models as conf
from datetime import date

# Create your models here.


class Area(models.Model):
    nombre = models.CharField(max_length=20, unique=True)  # nombre del area
    # cantidad de horas asignadas para una area
    canhora = models.IntegerField("Cantidad de Horas")
    profesores = models.ManyToManyField(hoja.Profesor)

    class Meta:
        ordering = ['nombre']
    # endclass

    def __unicode__(self):
        return u"%s" % (self.nombre_area)
    # end def

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.title()
        super(Area, self).save(*args, **kwargs)
    # end def
# end class


class Materia(models.Model):
    area = models.ForeignKey(Area)
    nombre = models.CharField(max_length=20, unique=True)  # nombre del materia

    class Meta:
        ordering = ['nombre']
    # endclass

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.title()
        super(Materia, self).save(*args, **kwargs)
    # end def
# end class


class Grado(models.Model):
    nombre = models.CharField(max_length=10, unique=True)  # nombre del grado
    valor = models.IntegerField(default=0)

    class Meta:
        ordering = ['nombre']
    # endclass

    def clean(self):
        if int(self.nombre) < 0 or self.nombre == "":
            raise ValidationError(
                "El nombre del grado no puede ser un numero negativo")
        # end if
    # end def

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    jornada = models.ForeignKey(conf.Configuracion)
    director = models.ForeignKey(hoja.Profesor, verbose_name="Director de Grupo")
    grado = models.ForeignKey(Grado)
    anio = models.IntegerField("Año", default=date.today().year)

    class Meta:
        ordering = ['nombre']
        unique_together = (('nombre', 'grado', 'jornada',
                            'director', 'anio'), ('nombre', 'grado', 'jornada', 'anio'))
    # endclass

    def __unicode__(self):
        return u"%s-%s" % (self.grado.nombre, self.nombre)
    # end def

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Curso, self).save(*args, **kwargs)
    # end def

# end class


# esta clase es la que enlaza a el grado con las asignaturas a dictar en el
class Asignacion(models.Model):
    grado = models.ForeignKey(Grado)
    materia = models.ForeignKey(Materia)
    horas_asignadas = models.IntegerField("Horas Asignadas")
    anio = models.IntegerField("Año", default=date.today().year)
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ['anio']
        unique_together = ('grado', 'materia', 'anio')
    # end class

    def clean_materia(self):
        if self.materia:
            unique = Asignacion.objects.filter(
                grado=self.grado, materia=self.materia, ano=date.today().year).first()
            if unique:
                raise ValidationError(
                    "Ya existe una asignacion con la misma materia en el mismo grado")
            # end if
            return self.materia
        # end if
        raise ValidationError("Este campo es requerido")
    # end def

    def __unicode__(self):
        return u"Materia %s al grado %s Año %d" % (self.materia.nombre, self.grado.nombre, self.anio)
    # end defz
# end class
