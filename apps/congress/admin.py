from django.contrib import admin

from apps.congress.models import Edition, Company, Speaker


class EditionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['company']
    search_fields = ['first_name', 'last_name']


admin.site.register(Edition, EditionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Speaker, SpeakerAdmin)