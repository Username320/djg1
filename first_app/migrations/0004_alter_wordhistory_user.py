# Generated by Django 5.1.3 on 2024-12-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_wordhistory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordhistory',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
