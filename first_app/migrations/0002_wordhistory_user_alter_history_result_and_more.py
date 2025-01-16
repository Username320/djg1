# Generated by Django 5.1.3 on 2024-12-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordhistory',
            name='user',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='history',
            name='result',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wordhistory',
            name='numCount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wordhistory',
            name='wordCount',
            field=models.IntegerField(),
        ),
    ]
