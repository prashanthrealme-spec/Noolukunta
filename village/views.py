
from django.shortcuts import render

from .models import (
    CarouselImage,
    GalleryImage,
    VillageNews,
    HistorySection,
    VillagePlace,
)


def home(request):
    slides = CarouselImage.objects.filter(
        is_active=True
    ).order_by("order", "id")

    gallery_images = GalleryImage.objects.filter(
        is_active=True
    ).order_by("order", "id")

    news_items = VillageNews.objects.filter(
        is_active=True
    ).order_by("-created_at")[:6]

    context = {
        "slides": slides,
        "gallery_images": gallery_images,
        "news_items": news_items,
    }

    return render(request, "village/home.html", context)


def history(request):
    sections = HistorySection.objects.filter(
        is_active=True
    ).order_by("order", "id")

    return render(
        request,
        "village/history.html",
        {"sections": sections},
    )


def directory(request):
    places = VillagePlace.objects.filter(
        is_active=True
    ).order_by("order", "name")

    return render(
        request,
        "village/directory.html",
        {"places": places},
    )
