# Generated by Django 2.1.5 on 2019-02-13 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('responsable', models.CharField(blank=True, max_length=100)),
                ('creacion', models.DateField(blank=True)),
            ],
        ),
    ]
