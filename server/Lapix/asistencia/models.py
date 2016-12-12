from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from binary import ByteAField

# Create your models here.


class Validable(models.Model):
    user = models.ForeignKey(User)
    activo = models.BooleanField(default=False)
    identificador = models.CharField(max_length=45, null=True, default=None)
    class_name = models.CharField(max_length=45, null=True, default=None)

    class Meta:
        verbose_name = "Validable"
        verbose_name_plural = "Validables"
    # end cladd

    def __unicode__(self):
        return unicode(self.activo)
    # end def
# end class


class Excusa(models.Model):
    horario = models.DateField()
    descripcion = models.TextField()
    archivo = models.FileField(null=True, default=None, blank=True)
    validable = models.ForeignKey(Validable)
# end class


class Template(models.Model):
    template = ByteAField()
    validable = models.OneToOneField(Validable)

    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"
    # end class

    def __unicode__(self):
        return unicode(self.validable)
    # end def
# end class


class Asistencia(models.Model):
    validable = models.ForeignKey(Validable)
    fecha = models.DateTimeField(auto_now_add=True)
    horario = models.ForeignKey('horario.Horario', null=True, default=None)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
    # end class

    def __unicode__(self):
        return unicode(self.fecha)
    # end def
# end class
