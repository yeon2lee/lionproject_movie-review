# Generated by Django 3.2.5 on 2021-07-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(default='제목없음', max_length=100)),
                ('movie_title', models.CharField(default='제목없음', max_length=100)),
                ('author', models.CharField(default='글쓴이없음', max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='review/')),
            ],
        ),
    ]
