# Generated by Django 4.2.1 on 2023-05-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_news_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='writer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]