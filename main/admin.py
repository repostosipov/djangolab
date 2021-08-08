from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
# models:
from django.contrib.flatpages.models import FlatPage
from .models import Ads, Category, Seller, Tag
# forms:
from django.contrib.flatpages.admin import FlatpageForm


class FlatpageForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = FlatPage
        fields = '__all__'


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['user', 'ads_count']
