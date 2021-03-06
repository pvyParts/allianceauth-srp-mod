# Generated by Django 2.2.9 on 2020-04-11 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('esi', '0005_remove_token_length_limit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SrpPaymentToken',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='srp_character', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esi.Token')),
            ],
        ),
    ]
