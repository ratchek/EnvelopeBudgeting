# Generated by Django 5.0.2 on 2024-03-04 20:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_fill_notes_alter_transaction_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="envelope",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="envelopes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
