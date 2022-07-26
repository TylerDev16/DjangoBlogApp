# Generated by Django 4.0.6 on 2022-07-19 17:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_publish_alter_post_slug_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 19, 17, 56, 33, 590915, tzinfo=utc)),
        ),
    ]
