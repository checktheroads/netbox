# Generated by Django 3.0.6 on 2020-07-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0044_jobresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='configcontext',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
