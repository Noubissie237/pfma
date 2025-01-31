# Generated by Django 4.2.6 on 2024-02-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_documents_hand_in_hand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images_Mediatheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='staticfiles/images')),
            ],
            options={
                'verbose_name': 'Images_Mediatheque',
                'verbose_name_plural': 'Images_Mediatheque',
                'db_table': 'Images_Mediatheque',
            },
        ),
    ]
