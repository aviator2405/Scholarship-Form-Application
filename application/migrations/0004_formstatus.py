# Generated by Django 5.0.6 on 2024-08-15 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_rename_ifcs_appbaninfo_ifsc'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Requested', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=10)),
                ('message', models.CharField(default='NA', max_length=100)),
                ('username', models.ForeignKey(default='Requested', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
