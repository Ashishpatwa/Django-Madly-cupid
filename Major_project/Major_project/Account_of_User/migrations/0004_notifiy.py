# Generated by Django 4.1.3 on 2023-05-10 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account_of_User', '0003_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifiy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('visited', 'visited'), ('like', 'like'), ('frndrequest', 'frndrequest')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notireceiver', to='Account_of_User.friend')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notisender', to='Account_of_User.friend')),
            ],
        ),
    ]