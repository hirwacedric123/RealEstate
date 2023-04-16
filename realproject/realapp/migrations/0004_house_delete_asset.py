# Generated by Django 4.1.7 on 2023-04-14 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0003_asset_use'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('use', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('rooms', models.IntegerField(null=True)),
                ('baths', models.IntegerField(null=True)),
                ('price', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
    ]
