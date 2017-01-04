#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from configuracion.models import Sede
# Create your models here.


class GradoEntrante(models.Model):
    nombre = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Estudiante(User):
    BOOL_CHOICES = ((True, 'Hombre'), (False, 'Mujer'))
    fecha = models.DateField("* Fecha de Nacimiento")
    sexo = models.BooleanField(
        "* Sexo", choices=BOOL_CHOICES, blank=False, default=True)
    identificacion = models.CharField(
        "* Identificación", max_length=200, unique=True)
    telefono = models.IntegerField("* Telefono")
    direccion = models.CharField("* Dirección", max_length=400)
    status = models.BooleanField(default=True)
    grado = models.ForeignKey(GradoEntrante, verbose_name="*Curso de ingreso")
    # con null=True, blank=True podremos guardar un producto sin image
    imagen = models.ImageField(
        upload_to='MultimediaData/estudiante', null=True, blank=True)
    codigo_Estudiante = models.CharField(
        "Codigo de Estudiante", max_length=200, unique=True, null=True, blank=True)
    colegio_Anterior = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
    # end class

    def save(self, *args, **kwargs):
        self.nombre = self.first_name.title()
        self.apellidos = self.last_name.title()
        super(Estudiante, self).save(*args, **kwargs)
    # end def

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    def clean(self):
        if self.imagen:
            if self.imagen.size > 5 * 1024 * 1024:
                raise ValidationError("La imagen no puede exceder los 5MB")
            # end if
        # end if
    # end def

    def thumbnail(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>' % (self.imagen, self.imagen)
    # end def

    thumbnail.allow_tags = True
# end class


class Profesor(User):
    BOOL_CHOICES = ((True, 'Hombre'), (False, 'Mujer'))
    fecha = models.DateField("* Fecha de Nacimiento")
    sexo = models.BooleanField(
        "* Sexo", choices=BOOL_CHOICES, blank=False, default=True)
    identificacion = models.CharField(
        "* Identificación", max_length=200, unique=True)
    telefono = models.IntegerField("* Telefono")
    direccion = models.CharField("* Dirección", max_length=400)
    status = models.BooleanField(default=True)
    imagen = models.ImageField(
        upload_to='MultimediaData/estudiante', null=True, blank=True)
    hoja_vida = models.FileField(
        "Hoja de Vida", upload_to='MultimediaData/hoja_vida', null=True, blank=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    def clean(self):
        if self.imagen:
            if self.imagen.size > 5 * 1024 * 1024:
                raise ValidationError("La imagen no puede exceder los 5MB")
            # end if
        # end if
        if self.hoja_vida:
            if self.hoja_vida.size > 5 * 1024 * 1024:
                raise ValidationError(
                    "La hoja de vida no puede exceder los 5MB")
            # end if
        # end def
    # end def

    def thumbnail(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>' % (self.imagen, self.imagen)
    # end def

    thumbnail.allow_tags = True
# end class


class Acudiente(User):
    BOOL_CHOICES = ((True, 'Hombre'), (False, 'Mujer'))
    fecha = models.DateField("* Fecha de Nacimiento")
    sexo = models.BooleanField(
        "* Sexo", choices=BOOL_CHOICES, blank=False, default=True)
    identificacion = models.CharField(
        "* Identificación", max_length=200, unique=True)
    telefono = models.IntegerField("* Telefono")
    direccion = models.CharField("* Dirección", max_length=400)
    status = models.BooleanField(default=True)
    estudiantes = models.ManyToManyField(Estudiante)
    imagen = models.ImageField(upload_to='MultimediaData/acudiente', null=True,
                               blank=True)

    class Meta:
        verbose_name = "Acudiente"
        verbose_name_plural = "Acudientes"
    # end class

    def clean(self):
        if self.imagen:
            if self.imagen.size > 5 * 1024 * 1024:
                raise ValidationError("La imagen no puede exceder los 5MB")
            # end if
        # end if

    def thumbnail(self):
        return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>' % (self.imagen, self.imagen)
    # end def

    thumbnail.allow_tags = True
# end class


class AsiganacionSede(models.Model):
    profesor = models.ForeignKey(Profesor)
    sede = models.ManyToManyField(Sede)
    anio = models.IntegerField('Año')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Asignación de sede"
        verbose_name_plural = "Asignaciones de sede"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.profesor.nombre, self.profesor.apellidos)
    # end def

# end class
