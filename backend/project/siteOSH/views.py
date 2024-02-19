from django.shortcuts import render
from django.http import JsonResponse
from .models import ImageInfo, DocumentsInfo, VideInfo
from datetime import datetime
from django.db.models import Model


def getDataFromModel(model: Model) -> list:
    objects = model.objects.all().order_by('-datePublished').values()

    objectsList = []

    for object in objects:
        objectsList.append(
            {
                "id": object["id"],
                "title": object["title"],
                "file": "https://sparlex.ru/media/" + object["file"],
                "datePublished": object["datePublished"].strftime("%d.%m.%Y") 
            }
        )

    return objectsList


def allDocuments(request):
    return JsonResponse({
        "documents": getDataFromModel(DocumentsInfo)
    })


def allImages(request):
    return JsonResponse({
        "images": getDataFromModel(ImageInfo)
    })


def allVideos(request):
    return JsonResponse({
        "videos": getDataFromModel(VideInfo)
    })