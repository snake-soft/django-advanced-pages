from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
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
        'sites',
    ]
    list_display = (
        'title',
        'url',
        'registration_required',
        'page',
        'get_sites',
    )
    list_filter = (
        'sites',
        'registration_required',
    )
    filter_horizontal = ('sites',)

    @admin.display(description=_('Sites'))
    def get_sites(self, obj):
        return mark_safe(
            '<br>'.join([f'{x.name} ({x.domain})' for x in obj.sites.all()]))


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
