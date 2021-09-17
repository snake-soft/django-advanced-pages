# Generated by Django 3.1.6 on 2021-06-09 17:39

from django.db import migrations, models
import django.db.models.deletion
from django.core.management import call_command


def create_initial_pages(apps, schema):
    Site = apps.get_model('sites', 'Site')
    Site.objects.get_or_create(id=1, defaults={'domain': 'localhost:8000', 'name': 'New Site'})
    call_command('loaddata', 'initial_pages.json', app_label='pages')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveSmallIntegerField(choices=[(0, 'Undefined'), (1, 'Company'), (2, 'Legal')], default=0, verbose_name='Category')),
                ('priority', models.SmallIntegerField(default=0, verbose_name='Priority')),
                ('flatpage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='flatpages.flatpage')),
            ],
            options={
                'verbose_name': 'Categorized page',
                'verbose_name_plural': 'Categorized pages',
                'ordering': ['-priority'],
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='page_attachments/', verbose_name='File')),
                ('flatpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='flatpages.flatpage')),
            ],
            options={
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
        ),
        migrations.RunPython(create_initial_pages, migrations.RunPython.noop)
    ]
