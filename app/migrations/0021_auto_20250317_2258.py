# Generated by Django 3.2 on 2025-03-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20250317_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image2',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='image3',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='image4',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
