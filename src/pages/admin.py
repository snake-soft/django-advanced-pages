from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from .models import Page, Attachment


class PageInLine(admin.TabularInline):
    model = Page
    list_display=['has_attachments']


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 0


class FlatPageAdmin(admin.ModelAdmin):
    inlines = [PageInLine, AttachmentInline]
    fields = [
        'title',
        'url',
        'content',
        'template_name',
        'registration_required',
    ]
    list_display = (
        'title',
        'url',
        'registration_required',
        'page',
    )


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
