from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

class ImageInfo(models.Model):
    title = models.CharField("Название информативного изобрежения", max_length=350)
    file = models.ImageField("Информативное изображение", upload_to='imagesInfo/')
    datePublished = models.DateField("дата публикации информативного изображения", default=date.today)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("image-info-detail", kwargs={"id": self.id})
    

    class Meta:
        verbose_name = "Информативное изображение"
        verbose_name_plural = "Информативные изображения"



class DocumentsInfo(models.Model):
    title = models.CharField("Название документа", max_length=350)
    file = models.FileField(upload_to="documentsInfo/")
    datePublished = models.DateField("дата публикации документа", default=date.today)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("documents-info-detail", kwargs={"id": self.id})
    

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class VideInfo(models.Model):
    title = models.CharField("Название видеоролика", max_length=350)
    file = models.FileField(upload_to="videoInfo/")
    datePublished = models.DateField("дата публикации видеоролика", default=date.today)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("video-info-detail", kwargs={"id": self.id})
    

    class Meta:
        verbose_name = "Видеоролик"
        verbose_name_plural = "ВИдеоролиики"
