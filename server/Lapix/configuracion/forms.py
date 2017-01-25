# -*- coding: utf-8 -*-
from django import forms
import models


class ColegioForm(forms.ModelForm):
    class Meta:
        model = models.Colegio
        fields = ['nit', 'registro', 'nombre', 'tipo', 'jornada', 'year']
    # end class

    def clean(self):
        data = super(ColegioForm, self).clean()
        if not data.get('year'):
            colegio = models.Colegio.objects.filter(year=data.get('year'))
            if colegio:
                self.add_error('year', 'Existe una configuracion para este año')
            # end if
        # end if
    # end def
# end class


class ColegioFormEdit(forms.ModelForm):
    class Meta:
        model = models.Colegio
        fields = ['nit', 'registro', 'nombre', 'tipo', 'jornada', 'year']
    # end class
# end class
