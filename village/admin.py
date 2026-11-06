
from django.contrib import admin
from .models import (
    CarouselImage,
    GalleryImage,
    VillageNews,
    HistorySection,
    VillagePlace,
)


# Admin panel branding
admin.site.site_header = "Noolukunta Village Administration"
admin.site.site_title = "Noolukunta Admin"
admin.site.index_title = "Manage Village Website Content"


# Homepage carousel images
@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("caption",)
    list_filter = ("is_active",)
    search_fields = ("caption",)
    ordering = ("order", "id")


# Village gallery
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("title",)
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order", "id")


# Village news and events
@admin.register(VillageNews)
class VillageNewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "event_date",
        "is_active",
    )
    list_filter = ("category", "is_active", "event_date")
    search_fields = ("title", "description")
    list_editable = ("is_active",)
    ordering = ("-created_at",)


# Village history
@admin.register(HistorySection)
class HistorySectionAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    list_display_links = ("title",)
    list_filter = ("is_active",)
    search_fields = ("title", "content")
    ordering = ("order", "id")


# Village directory
@admin.register(VillagePlace)
class VillagePlaceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "contact_number",
        "is_active",
        "order",
    )
    list_filter = ("category", "is_active")
    search_fields = (
        "name",
        "description",
        "address",
        "contact_number",
    )
    list_editable = ("is_active", "order")
    ordering = ("order", "name")
