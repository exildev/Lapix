from django.contrib import admin
from exileui.admin import exileui
from curriculo import models
# Register your models here.


class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'canhora', 'eliminado']
    search_fields = ('nombre',)
    filter_horizontal = ('profesores', )
# end class


exileui.register(models.Area, AreaAdmin)
