# Generated by Django 3.0.7 on 2020-12-05 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('United', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='budget',
            field=models.IntegerField(default=1000),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_booked', models.IntegerField()),
                ('booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mytickets', to=settings.AUTH_USER_MODEL)),
                ('reservations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved', to='United.Event')),
            ],
        ),
    ]
