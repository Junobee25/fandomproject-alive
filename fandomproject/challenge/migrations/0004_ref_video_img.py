# Generated by Django 4.2.2 on 2023-06-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_remove_score_title_remove_score_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ref_video',
            name='img',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
