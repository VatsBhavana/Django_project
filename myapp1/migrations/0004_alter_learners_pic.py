# Generated by Django 5.1.5 on 2025-01-31 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_adminuser_pic_learners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learners',
            name='pic',
            field=models.FileField(default='media/boy_default.png', upload_to='media/images/'),
        ),
    ]
