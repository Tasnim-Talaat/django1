# Generated by Django 4.0.5 on 2022-06-19 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('nid', models.DecimalField(decimal_places=0, max_digits=14)),
                ('courses', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Trainee.course')),
            ],
        ),
    ]