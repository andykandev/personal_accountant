# Generated by Django 4.1.4 on 2022-12-18 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_token_expense'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='note',
            new_name='token',
        ),
        migrations.RemoveField(
            model_name='token',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='token',
            name='time',
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
