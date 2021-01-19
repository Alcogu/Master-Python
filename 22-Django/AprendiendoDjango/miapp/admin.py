from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at' )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#Configurar titulo del panel

admin.site.site_header = "Panel de Control Django"
admin.site.site_title = "Panel de Control Django"
admin.site.index_title = "Panel de gestión"