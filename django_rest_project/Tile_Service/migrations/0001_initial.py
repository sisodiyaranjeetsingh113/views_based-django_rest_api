# Generated by Django 3.2.10 on 2021-12-12 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Status_Service', '0001_initial'),
        ('Task_Service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_date', models.DateField(blank=True, null=True)),
                ('status', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Status_Service.status')),
                ('task', models.ManyToManyField(to='Task_Service.Task')),
            ],
        ),
    ]
