# Generated by Django 4.2.5 on 2023-10-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_staff_notification"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff_notification",
            name="status",
            field=models.IntegerField(default=0, null=True),
        ),
    ]