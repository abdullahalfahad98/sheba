# Generated by Django 5.0 on 2024-02-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='event_images/')),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('event_date', models.DateField()),
            ],
        ),
    ]