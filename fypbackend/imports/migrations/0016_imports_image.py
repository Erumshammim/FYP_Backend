# Generated by Django 3.0.5 on 2021-07-18 15:13

from django.db import migrations, models
import imports.models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0015_auto_20210718_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='imports',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=imports.models.upload_to),
        ),
    ]
