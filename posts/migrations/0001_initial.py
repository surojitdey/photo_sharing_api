# Generated by Django 3.1.7 on 2021-03-11 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('media_file', models.ImageField(upload_to=posts.models.user_directory_path)),
                ('likes', models.IntegerField(default=0, verbose_name='likes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_id', to='posts.post')),
            ],
        ),
    ]