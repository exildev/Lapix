#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from exileui.widgets import DatePickerWidget
import models


class ProfesorForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['fecha'].widget = DatePickerWidget(
            attrs={'class': 'date'},
            format="%m/%d/%Y")
        self.fields['fecha'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d')
        self.fields['telefono'].widget = forms.NumberInput()
        self.fields['identificacion'].widget = forms.NumberInput()
    # end def

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', False)
        if fecha:
            if fecha.year < 1900:
                raise forms.ValidationError(
                    "El año debe ser mayor a 1900"
                )
            # end if
            return fecha
        # end if
        raise forms.ValidationError(
            "Este campo es requerido"
        )
    # end def

    class Meta:
        model = models.Profesor
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'direccion', 'telefono', 'fecha', 'imagen', 'hoja_vida']
    # end class

    def save(self, commit=True):
        usuario = super(ProfesorForm, self).save(commit)
        usuario.is_staff = False
        usuario.save()
        return usuario
    # end def
# end class


class EditProfesor(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditProfesor, self).__init__(*args, **kwargs)
        self.fields['fecha'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d')
    # end def

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', False)
        if fecha:
            if fecha.year < 1900:
                raise forms.ValidationError(
                    "El año debe ser mayor a 1900"
                )
            # end if
            return fecha
        # end if
        raise forms.ValidationError(
            "Este campo es requerido"
        )
    # end def

    class Meta:
        model = models.Profesor
        fields = ['first_name', 'last_name', 'identificacion', 'direccion', 'email', 'telefono', 'fecha', 'status', 'email', 'email', 'status', 'eliminado']
        widgets = {
            "fecha_nacimiento": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y"),
            "identificacion": forms.NumberInput(),
            "telefono": forms.NumberInput()
        }
    # end class
# end clas


class EstudianteForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['fecha'].widget = DatePickerWidget(
            attrs={'class': 'date'},
            format="%m/%d/%Y")
        self.fields['fecha'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d')
        self.fields['telefono'].widget = forms.NumberInput()
        self.fields['identificacion'].widget = forms.NumberInput()
    # end def

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', False)
        if fecha:
            if fecha.year < 1900:
                raise forms.ValidationError(
                    "El año debe ser mayor a 1900"
                )
            # end if
            return fecha
        # end if
        raise forms.ValidationError(
            "Este campo es requerido"
        )
    # end def

    class Meta:
        model = models.Estudiante
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'direccion', 'telefono', 'fecha', 'grado', 'imagen', 'codigo_Estudiante', 'colegio_Anterior']
    # end class

    def save(self, commit=True):
        usuario = super(EstudianteForm, self).save(commit)
        usuario.is_staff = False
        usuario.save()
        return usuario
    # end def
# end class


class EdirEstudiante(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EdirEstudiante, self).__init__(*args, **kwargs)
        self.fields['fecha'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d')
    # end def

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', False)
        if fecha:
            if fecha.year < 1900:
                raise forms.ValidationError(
                    "El año debe ser mayor a 1900"
                )
            # end if
            return fecha
        # end if
        raise forms.ValidationError(
            "Este campo es requerido"
        )
    # end def

    class Meta:
        model = models.Estudiante
        fields = ['first_name', 'last_name', 'identificacion', 'direccion', 'email', 'telefono', 'fecha', 'grado', 'imagen', 'codigo_Estudiante', 'colegio_Anterior', 'eliminado']
        widgets = {
            "fecha_nacimiento": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y"),
            "identificacion": forms.NumberInput(),
            "telefono": forms.NumberInput()
        }
    # end class
# end clas


class AcudienteForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AcudienteForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['fecha'].widget = DatePickerWidget(
            attrs={'class': 'date'},
            format="%m/%d/%Y")
        self.fields['fecha'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d')
        self.fields['telefono'].widget = forms.NumberInput()
        self.fields['identificacion'].widget = forms.NumberInput()
    # end def

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', False)
        if fecha:
            if fecha.year < 1900:
                raise forms.ValidationError(
                    "El año debe ser mayor a 1900"
                )
            # end if
            return fecha
        # end if
        raise forms.ValidationError(
            "Este campo es requerido"
        )
    # end def

    class Meta:
        model = models.Acudiente
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'direccion', 'telefono', 'fecha', 'estudiantes', 'imagen']
    # end class

    def save(self, commit=True):
        usuario = super(AcudienteForm, self).save(commit)
        usuario.is_staff = False
        usuario.save()
        return usuario
    # end def
# end class


class EditAcudiente(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditAcudiente, self).__init__(*args, **kwargs)
        self.fields['fecha'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '')
    # end def

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', False)
        if fecha:
            if fecha.year < 1900:
                raise forms.ValidationError(
                    "El año debe ser mayor a 1900"
                )
            # end if
            return fecha
        # end if
        raise forms.ValidationError(
            "Este campo es requerido"
        )
    # end def

    class Meta:
        model = models.Acudiente
        fields = ['first_name', 'last_name', 'identificacion', 'direccion', 'telefono', 'fecha', 'estudiantes', 'imagen', 'eliminado']
        widgets = {
            "fecha_nacimiento": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y"),
            "identificacion": forms.NumberInput(),
            "telefono": forms.NumberInput()
        }
    # end class
# end clas


class AsignacionSedeForm(forms.ModelForm):

    class Meta:
        model = models.AsignacionSede
        exclude = ()
    # end class
# end class
