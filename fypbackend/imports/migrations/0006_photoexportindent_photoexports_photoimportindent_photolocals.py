# Generated by Django 3.0.5 on 2021-09-19 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0005_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoLocals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='locals/%Y/%m/%d')),
                ('locals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imports.Locals')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoImportIndent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='import_indents/%Y/%m/%d')),
                ('import_indents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imports.ImportIndent')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoExports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='exports/%Y/%m/%d')),
                ('exports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imports.Exports')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoExportIndent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='export_indents/%Y/%m/%d')),
                ('exports', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imports.ExportIndent')),
            ],
        ),
    ]