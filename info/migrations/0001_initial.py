# Generated by Django 3.1.1 on 2020-09-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieuDe', models.CharField(max_length=100)),
                ('noiDung', models.TextField()),
                ('anhNen', models.TextField()),
            ],
        ),
    ]
