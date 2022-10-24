from django.contrib import admin
from .models import Categoria, Contato


class ConatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria', 'mostrar')

    list_display_links = ('nome', 'sobrenome', 'telefone')

    #list_filter = ('nome', 'sobrenome', 'data_criacao')

    list_per_page = 20

    search_fields = ('nome', 'data_criacao')

    list_editable = ('mostrar',)


admin.site.register(Categoria)

admin.site.register(Contato, ConatoAdmin)
