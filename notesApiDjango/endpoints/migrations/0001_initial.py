# Generated by Django 3.2.23 on 2024-04-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('kategori', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id_note', models.AutoField(primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=255)),
                ('isi', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kategori', models.ManyToManyField(to='endpoints.Kategori')),
            ],
        ),
    ]
