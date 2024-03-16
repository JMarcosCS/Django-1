from django.contrib import admin

from .models import Produto, Client

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco','estoque')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome','email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Client, ClientAdmin)
