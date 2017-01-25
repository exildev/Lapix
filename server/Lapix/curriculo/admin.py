from django.contrib import admin

# Register your models here.


class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'canhora']
    search_fields = ('nombre',)
    filter_horizontal = ('profesores', )
# end class
