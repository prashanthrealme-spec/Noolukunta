
from django.db import models
class CarouselImage(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="carousel/")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Homepage Carousel Image"
        verbose_name_plural = "Homepage Carousel Images"

    def __str__(self):
        return self.caption

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="village-gallery/")
    description = models.CharField(max_length=250, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Village Gallery Image"
        verbose_name_plural = "Village Gallery Images"

    def __str__(self):
        return self.title

class VillageNews(models.Model):
    CATEGORY_CHOICES = [
        ("NEWS", "Village News"),
        ("FESTIVAL", "Festivals"),
        ("EVENT", "Village Events"),
        ("ANNOUNCEMENT", "Announcements"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="NEWS",
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to="village-news/",
        blank=True,
        null=True,
    )
    event_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Village News / Announcement"
        verbose_name_plural = "Village News & Announcements"

    def __str__(self):
        return self.title

class HistorySection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to="village-history/",
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Village History Section"
        verbose_name_plural = "Village History Sections"

    def __str__(self):
        return self.title

class VillagePlace(models.Model):
    CATEGORY_CHOICES = [
        ("TEMPLE", "Temple"),
        ("SCHOOL", "School"),
        ("HEALTH", "Health Service"),
        ("GOVERNMENT", "Government Office"),
        ("WATER", "Water & Public Facility"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="OTHER",
    )
    description = models.TextField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    map_link = models.URLField(blank=True)
    image = models.ImageField(
        upload_to="village-places/",
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Village Place"
        verbose_name_plural = "Village Directory"

    def __str__(self):
        return self.name
