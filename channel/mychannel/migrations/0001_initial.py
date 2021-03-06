# Generated by Django 3.1 on 2020-08-13 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=11)),
                ('chat_with_us', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('video_call', models.URLField(blank=True, max_length=50)),
                ('feedback', models.CharField(blank=True, max_length=50)),
                ('inquiry', models.CharField(blank=True, max_length=50)),
                ('voip_call', models.CharField(blank=True, max_length=50)),
                ('i_buy_your_goods', models.CharField(blank=True, max_length=50)),
                ('instagram_follow', models.CharField(blank=True, max_length=100)),
                ('facebook_follow', models.CharField(blank=True, max_length=100)),
                ('linkedin_follow', models.CharField(blank=True, max_length=100)),
                ('twitter_follow', models.CharField(blank=True, max_length=100)),
                ('website', models.CharField(blank=True, max_length=50)),
                ('youtube_subscribe', models.CharField(blank=True, max_length=100)),
                ('provide_rating', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
