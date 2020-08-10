# Generated by Django 3.1 on 2020-08-08 10:15

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.CharField(max_length=250)),
                ('guid', models.IntegerField(default=0)),
                ('pubDate', models.CharField(max_length=100)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feeds.category')),
            ],
        ),
    ]