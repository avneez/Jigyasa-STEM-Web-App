# Generated by Django 3.2.7 on 2021-11-06 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JigyasaApp', '0005_alter_leavereportstudent_leave_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_total_marks', models.FloatField(default=0)),
                ('subject_scored_marks', models.FloatField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JigyasaApp.students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JigyasaApp.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleMeeting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JigyasaApp.staffs')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JigyasaApp.subjects')),
            ],
        ),
    ]
