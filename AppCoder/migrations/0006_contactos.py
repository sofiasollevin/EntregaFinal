# Generated by Django 4.1 on 2022-09-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_jugadoresselecciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=30)),
                ('contactotelefonico', models.IntegerField()),
                ('mensaje', models.CharField(max_length=1000000)),
            ],
        ),
    ]
