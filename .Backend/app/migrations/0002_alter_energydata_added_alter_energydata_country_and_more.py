# Generated by Django 4.2.5 on 2023-09-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energydata',
            name='added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='end_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='impact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='insight',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='likelihood',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='pestle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='relevance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='sector',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='start_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='energydata',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
