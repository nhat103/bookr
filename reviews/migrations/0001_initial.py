# Generated by Django 4.1 on 2022-09-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of publisher', max_length=50)),
                ('website', models.URLField(help_text="the publisher's website")),
                ('email', models.EmailField(help_text="the publisher's email", max_length=254)),
            ],
        ),
    ]