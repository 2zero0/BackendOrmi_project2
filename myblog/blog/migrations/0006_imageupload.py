# Generated by Django 4.2.3 on 2023-07-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_content2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_image', models.ImageField(null=True, upload_to='upload_img/')),
            ],
        ),
    ]
