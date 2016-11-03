from django.contrib import admin

from apps.congress.models import Edition, Company, Speaker, Tag, Track, ActivityFormat, Activity


class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class EditionAdmin(admin.ModelAdmin):
    list_display = ["start", "end", "name", "description"]
    search_fields = ["name", "description"]


class TrackAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "description"]


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    list_filter = ["company"]
    search_fields = ["first_name", "last_name"]


class ActivityFormatAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]


class ActivityAdmin(admin.ModelAdmin):
    filter_horizontal = ["tags", "speakers", "companies"]
    list_display = ["id", "title", "start", "end", "format", "track"]
    list_filter = ["format", "tags", "edition", "track"]
    search_fields = ["title", "description", "tags", "format", "speakers", "companies"]


admin.site.register(Tag, TagAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(ActivityFormat, ActivityFormatAdmin)
admin.site.register(Activity, ActivityAdmin)
