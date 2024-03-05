from django.contrib import admin

from .models import Produto, Cliente # importando do models para visualizar na interface do admin

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

admin.site.register(Produto, ProdutoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    
admin.site.register(Cliente, ClienteAdmin)