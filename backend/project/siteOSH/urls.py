from django.urls import path

from . import views


urlpatterns = [
    path("documents/", views.allDocuments, name="documents"),
    path("videos/", views.allVideos, name="videos"),
    path("images/", views.allImages, name="images")
]