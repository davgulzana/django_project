# Generated by Django 3.0.3 on 2020-02-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0002_auto_20200220_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(blank=True, null=True, verbose_name='Published date'),
        ),
    ]
