# Generated by Django 3.0.5 on 2021-05-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0009_auto_20210505_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exports',
            name='paymentTerm',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='Cash', max_length=4),
        ),
        migrations.AlterField(
            model_name='exports',
            name='status',
            field=models.CharField(choices=[('Signed', 'Signed'), ('Unsigned', 'Unsigned'), ('Pending', 'Pending')], default='Signed', max_length=9),
        ),
    ]
