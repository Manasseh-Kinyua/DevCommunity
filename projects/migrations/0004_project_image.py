# Generated by Django 4.2.1 on 2023-05-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_review_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
