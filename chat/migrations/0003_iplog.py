# Generated by Django 5.1.4 on 2024-12-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
