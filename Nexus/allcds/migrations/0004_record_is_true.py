# Generated by Django 4.2.5 on 2023-09-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcds', '0003_record_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='is_true',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
