# Generated by Django 3.0.8 on 2021-04-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default='not Defiend', max_length=150),
            preserve_default=False,
        ),
    ]
