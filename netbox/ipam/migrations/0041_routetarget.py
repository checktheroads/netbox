# Generated by Django 3.1 on 2020-09-24 15:19

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0010_custom_field_data'),
        ('extras', '0052_customfield_cleanup'),
        ('ipam', '0040_service_drop_port'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=21, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='route_targets', to='tenancy.tenant')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='vrf',
            name='export_targets',
            field=models.ManyToManyField(blank=True, related_name='exporting_vrfs', to='ipam.RouteTarget'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='import_targets',
            field=models.ManyToManyField(blank=True, related_name='importing_vrfs', to='ipam.RouteTarget'),
        ),
    ]
