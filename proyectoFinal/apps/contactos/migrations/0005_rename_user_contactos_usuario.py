# Generated by Django 4.2.3 on 2023-07-25 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0004_alter_contactos_asunto_alter_contactos_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactos',
            old_name='user',
            new_name='usuario',
        ),
    ]
