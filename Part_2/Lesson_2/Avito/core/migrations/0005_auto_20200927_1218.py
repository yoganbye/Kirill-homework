# Generated by Django 3.1.1 on 2020-09-27 08:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20200926_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_edit',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 27, 8, 18, 58, 144477, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=700)),
                ('date_publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('in_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ad')),
            ],
        ),
    ]