# Generated by Django 2.2 on 2019-06-13 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20190613_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='descriprions',
            new_name='descriptions',
        ),
    ]
