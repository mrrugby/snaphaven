# Generated by Django 3.1.5 on 2021-06-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoStudio', '0003_queries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queries',
            name='User_Discription',
            field=models.TextField(max_length=500),
        ),
    ]