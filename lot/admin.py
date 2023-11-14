from django.contrib import admin

from .models import Lot, LotSection, LotComment


class LotAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(Lot, LotAdmin)
admin.site.register(LotSection)
admin.site.register(LotComment)
