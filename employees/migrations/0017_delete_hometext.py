# Generated by Django 4.0.8 on 2024-07-29 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_rename_lang_code_hometext_en_lang_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeText',
        ),
    ]