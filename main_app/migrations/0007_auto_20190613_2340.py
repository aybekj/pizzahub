# Generated by Django 2.2 on 2019-06-13 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_pizza_descriprions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='Descriprions',
            new_name='descriprions',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='ingredients',
        ),
    ]