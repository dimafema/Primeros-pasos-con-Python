# Generated by Django 4.2.13 on 2024-06-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0010_alter_vacaciones_dias_totales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacaciones',
            name='dias_totales',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]