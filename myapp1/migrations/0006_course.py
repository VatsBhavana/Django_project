# Generated by Django 5.1.5 on 2025-02-07 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_duration', models.CharField(max_length=60)),
                ('fees', models.CharField(max_length=16)),
                ('course_discription', models.TextField()),
                ('course_lecture_flow', models.FileField(upload_to='media/lecture_flow/')),
                ('course_handbook', models.FileField(upload_to='media/handbook/')),
                ('course_interview_question', models.FileField(upload_to='media/interviewpreperation/')),
                ('course_assignment', models.FileField(upload_to='media/assignment/')),
                ('course_tutor_name', models.CharField(max_length=60)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
