# Generated by Django 3.2.7 on 2021-10-29 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JigyasaApp', '0004_alter_feedbackstaffs_feedback_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
