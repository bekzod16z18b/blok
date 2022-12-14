from django.contrib import admin

# Register your models here.
from .models import lugat

class LugadAdmin(admin.ModelAdmin):
    list_display = ['sotix','maslahat','mahsulot_turi','xarajat','hosildorlik','daromad','sof_foyda','rentabellik']
admin.site.register(lugat,LugadAdmin)