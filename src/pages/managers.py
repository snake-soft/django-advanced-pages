from django.db import models


class PageManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('flatpage')
        return qs
