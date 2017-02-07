# -*- coding: utf-8 -*-
from django import forms
import models
import datetime
from horario import models as horario


class SedeForm(forms.ModelForm):
    class Meta:
        model = models.Sede
        fields = ['nombre', 'registro', 'direccion',]
        exclude = ['estado',]
    # end class
# end class

class JornadaForm(forms.ModelForm):
    class Meta:
        model = models.Configuracion
        fields = ['sede', 'jornada', 'horaIni', 'miniIni', 'nothora', 'desIni', 'horaDia', 'cantidaHora', 'minutos_descanso',]
        exclude = ['estado', 'hora_ini_sec_1', 'hora_fin_sec_1', 'hora_ini_sec_2', 'hora_fin_sec_2', 'ano',]
    # end class

    def clean(self):
        data = super(JornadaForm, self).clean()
        if data.get('desIni') and data.get('cantidaHora') and data.get('sede'):
            if data.get('desIni') >= data.get('cantidaHora'):
                self.add_error('cantidaHora', 'El descanso no puede iniciar al finalizar las horas academicas.')
            # end if
            if isinstance(data.get('nothora'), int) and isinstance(data.get('horaDia'), int) and  isinstance(data.get('horaIni'), int) and isinstance(data.get('cantidaHora'), int) and  isinstance(data.get('minutos_descanso'), int) and isinstance(data.get('miniIni'), int):
                h = models.Configuracion.objects.filter(ano=datetime.datetime.now().year,sede__nombre__exact=data.get('sede'))
                if self.instance.id :
                    print 'existe',len(h)
                    h = h.exclude(id=self.instance.id)
                    print 'existe',len(h)
                # end if
                if h :
                    newadd = intervaloHora(data.get('horaIni'),data.get('miniIni'),data.get('cantidaHora'),data.get('horaDia'),data.get('minutos_descanso'),data.get('nothora'))
                    estado, mensaje = validarIntervaloJornada(newadd, h)
                    if estado :
                        self.add_error('sede', mensaje)
                    # end if
                # end if
        # end if
    # end def

    def save(self, commit=True):
        jornada = super(JornadaForm, self).save(commit)
        horas1 = jornada.horaIni + (jornada.desIni * jornada.horaDia / 60) # calculo del transcurso en horas desde el inicio
        minutos1 = jornada.miniIni + ((jornada.desIni * jornada.horaDia) % 60) # minutos restantes
        if minutos1 >= 60:
            horas1 = horas1 + minutos1 / 60
            minutos1 = minutos1 % 60
        #end if
        #representacion de la hora de la primera asignacion
        jornada.hora_ini_sec_1 = '%d:%s %s' % (jornada.horaIni, rellenoMinuto(jornada.miniIni),
        formatoHorra(jornada.nothora,jornada.horaIni))#primera asignacion de el horario de inicio clase hora
        jornada.hora_fin_sec_1 = '%d:%s %s' % (
        calcularFormatoHora(horas1), rellenoMinuto(minutos1), formatoHorra(jornada.nothora, horas1))
        #Calculamos el tiemmpo con el transcurso de tiempo del descanzo
        minutos11 = minutos1 + jornada.minutos_descanso
        if minutos11 / 60 >= 1:
            horas1 = horas1 + minutos11 / 60
            minutos1 = minutos11 % 60
        else:
            minutos1 = minutos11
        #end if
        jornada.hora_ini_sec_2 = '%d:%s %s' % (calcularFormatoHora(horas1), rellenoMinuto(minutos1), formatoHorra(jornada.nothora, horas1))
        hora2 = horas1 + (jornada.cantidaHora - jornada.desIni) * jornada.horaDia / 60
        minutos2 = minutos1 + (jornada.cantidaHora - jornada.desIni) * jornada.horaDia % 60
        if minutos2 / 60 >= 1:
            hora2 = hora2 + minutos2 / 60
            minutos2 = minutos2 % 60
        #end if
        jornada.hora_fin_sec_2 = '%d:%s %s' % (calcularFormatoHora(hora2), rellenoMinuto(minutos2), formatoHorra(jornada.nothora, hora2))
        jornada.save()
        return jornada
    # end def
# end class

# Validar intervalos de tiempo de las jornadas
def validarIntervaloJornada(newadd, h):
    for ant in h :
        oldadd = intervaloHora(ant.horaIni,ant.miniIni,ant.cantidaHora,ant.horaDia,ant.minutos_descanso,ant.nothora)
        if (obtencionValor(oldadd[0],oldadd[1]) < obtencionValor(newadd[0],newadd[1]) and obtencionValor(oldadd[2],oldadd[3]) > obtencionValor(newadd[0],newadd[1])) or (obtencionValor(oldadd[0],oldadd[1]) < obtencionValor(newadd[2],newadd[3]) and obtencionValor(oldadd[2],oldadd[3]) > obtencionValor(newadd[2],newadd[3])):
            return True, 'La seleccion de horario se encuentra en el intervalo de la jornada %s.'%(models.convertirJornada(ant.jornada))
        #end if
        if (obtencionValor(oldadd[0],oldadd[1]) > obtencionValor(newadd[0],newadd[1]) and obtencionValor(oldadd[0],oldadd[1]) < obtencionValor(newadd[2],newadd[3])) and (obtencionValor(oldadd[2],oldadd[3]) > obtencionValor(newadd[0],newadd[1]) and obtencionValor(oldadd[2],oldadd[3]) < obtencionValor(newadd[2],newadd[3])):
            return True, 'La seleccion de horario contiene a la jornada %s.'%(models.convertirJornada(ant.jornada))
        #end if
    #end for
    return False, None
# end def


## LOS VIEWS PARA AGREGAR ##

def intervaloHora(hi,mi,ch,vm,des,nt):
	mf = ch * vm + des + mi
	if nt == 1  and hi != 12:
		hi+=12
	#end if
	hf = hi + mf/60
	mf = mf % 60
	return [hi,mi,hf,mf]
#end def

def obtencionValor(a,b):
	return a + float(b)/60.0
#end def

def calcularFormatoHora(horaactual):# esta funcion se encarga de dar el formato no militar
	if horaactual > 12:
		return horaactual - 12
	else:
		return horaactual
		#end if
#end def

#Funciones
def formatoHorra(par1, actual):#funcion para asignar el formato hora
	if par1 == 0:
		if actual < 12:
			return 'am'
		else:
			return 'pm'
			#end if
	else:
		if actual < 12:
			return 'pm'
		else:
			return 'am'
			#end if
#end def

def rellenoMinuto(num):#esta funcion se encarga de completar
	if num == 0:
		return '00'
	else:
		return '%d' % num
	#end if
#end def

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


class ConfiguracionPeriodoForm(forms.ModelForm):
    class Meta:
        model = models.ConfiguracionPeriodo
        fields = ['cantidad', 'inicio', 'fin']
        exclude = ['estado']
    # end class

    def clean(self):
        configuracion = models.ConfiguracionPeriodo.objects.filter(inicio__year=datetime.datetime.now().year)
        if configuracion:
            self.add_error('inicio', 'Existe configuración para este año.')
        # end class
        data = super(ConfiguracionPeriodoForm, self).clean()
        if data.get('cantidad'):
            if data.get('cantidad') < 0 :
                self.add_error('cantidad', 'Debe por lo menos existir un periodo.')
            # end def
        # end def
        print data.get('inicio'), data.get('fin')
        inicio = data.get('inicio')
        fin = data.get('fin')
        if inicio and fin:
            if inicio > fin:
                self.add_error('fin', 'La fecha de fin debe ser mayor a la de inicio.')
            # end def
        # end if
    # end def
# end class
