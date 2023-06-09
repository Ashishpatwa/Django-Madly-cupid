# Generated by Django 4.1.3 on 2022-12-02 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=True, max_length=1)),
                ('profilepic', models.ImageField(default=True, upload_to='images')),
                ('status', models.TextField(default=True)),
                ('City', models.CharField(default=True, max_length=30)),
                ('Lives', models.CharField(default=True, max_length=10)),
                ('Interested', models.CharField(default=True, max_length=20)),
                ('Relationship', models.CharField(default=True, max_length=20)),
                ('Looking', models.CharField(default=True, max_length=10)),
                ('Height', models.IntegerField(default=True)),
                ('Education', models.CharField(default=True, max_length=20)),
                ('Favoutite_music', models.CharField(default=True, max_length=30)),
                ('Favoutite_movie', models.CharField(default=True, max_length=30)),
                ('Favoutite_Books', models.CharField(default=True, max_length=30)),
                ('Favoutite_TV_shows', models.CharField(default=True, max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
