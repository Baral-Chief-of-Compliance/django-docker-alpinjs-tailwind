from django.contrib import admin
from siteOSH.models import ImageInfo, VideInfo, DocumentsInfo
from django import forms


class ImageInfoClassForm(forms.ModelForm):
    class Meta:
        model = ImageInfo
        fields = '__all__'


class ImageInfoClassAdmin(admin.ModelAdmin):
    list_display = ("title", "datePublished")
    list_filter = ("datePublished",)
    search_fields = ("title",)
    form = ImageInfoClassForm
    save_on_top = True
    save_as = True


class DocumentsInfoClassForm(forms.ModelForm):
    class Meta:
        model = DocumentsInfo
        fields = '__all__'


class DocumentsInfoClassAdmin(admin.ModelAdmin):
    list_display = ("title", "datePublished")
    list_filter = ("datePublished",)
    search_fields = ("title",)
    form = DocumentsInfoClassForm
    save_on_top = True
    save_as = True


class VideInfoClassForm(forms.ModelForm):
    class Meta:
        model = VideInfo
        fields = '__all__'


class VideInfoClassAdmin(admin.ModelAdmin):
    list_display = ("title", "datePublished")
    list_filter = ("datePublished",)
    search_fields = ("title",)
    form = VideInfoClassForm
    save_on_top = True
    save_as = True


admin.site.register(ImageInfo, ImageInfoClassAdmin)
admin.site.register(DocumentsInfo, DocumentsInfoClassAdmin)
admin.site.register(VideInfo, VideInfoClassAdmin)

