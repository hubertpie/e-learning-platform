# Generated by Django 3.1.4 on 2020-12-16 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20201214_0523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='overView',
            new_name='overview',
        ),
    ]
