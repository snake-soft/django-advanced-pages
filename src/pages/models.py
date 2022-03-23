from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.flatpages.models import FlatPage
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .managers import PageManager


class Attachment(models.Model):
    flatpage = models.ForeignKey(
        FlatPage,
        related_name='attachments',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=250,
    )
    file = models.FileField(
        _('File'),
        upload_to='page_attachments/'
    )

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')


class Category(models.IntegerChoices):
    """
    COMPANY -> Used in footer middle
    LEGAL -> Used in footer right
    """
    UNDEFINED = 0, _('Undefined')
    COMPANY = 1, _('Company')
    LEGAL = 2, _('Legal')


class Page(models.Model):
    """ This is passed to the template context to build menu and urls """
    flatpage = models.OneToOneField(
        FlatPage,
        related_name='page',
        on_delete=models.CASCADE,
    )
    category = models.PositiveSmallIntegerField(
        _('Category'),
        choices=Category.choices,
        default=Category.UNDEFINED,
    )
    priority = models.SmallIntegerField(
        _('Priority'),
        default=0,
    )
    objects = PageManager()

    @property
    def title(self):
        return self.flatpage.title

    @property
    def category_name(self):
        return Category(self.category).label

    def get_absolute_url(self):
        return self.flatpage.get_absolute_url()

    def __str__(self):
        return f'{self.category_name}: {self.flatpage}'

    class Meta:
        ordering = ['category', 'priority']
        verbose_name = _('Categorized page')
        verbose_name_plural = _('Categorized pages')


@receiver(pre_save, sender=FlatPage)
def flatpage_pre_save(sender, instance, **kwargs):
    if not instance.url.startswith('/'):
        instance.url = '/' + instance.url
    if not instance.url.endswith('/'):
        instance.url += '/'
