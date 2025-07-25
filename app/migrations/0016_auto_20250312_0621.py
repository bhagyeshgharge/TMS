# Generated by Django 3.2 on 2025-03-12 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=3, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='Country',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Days',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='EndDate',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='package',
            name='Image',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Image2',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Image3',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Image4',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Night',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Place',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='StartDate',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='package',
            name='State',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Total_Person',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='package',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='package',
            name='Month',
            field=models.ManyToManyField(to='app.Month'),
        ),
    ]
