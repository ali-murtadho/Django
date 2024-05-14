# Generated by Django 3.2.23 on 2024-05-03 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='padi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('varietas', models.CharField(choices=[('Pandan_Wangi', 'Pandan_Wangi'), ('Ciheran', 'Ciheran'), ('Mi_Kongga', 'Mi_Kongga'), ('IR64', 'IR64'), ('Beras_Merah', 'Beras_Merah'), ('Beras_Hitam', 'Beras_Hitam')], max_length=100)),
                ('warna', models.CharField(choices=[('Merah', 'Merah'), ('Putih', 'Putih'), ('Hitam', 'Hitam'), ('Coklat', 'Coklat')], max_length=100)),
                ('rasa', models.CharField(choices=[('Pulen', 'Pulen'), ('Sangat_Pulen', 'Sangat_Pulen')], max_length=100)),
                ('teknik', models.CharField(choices=[('SRI', 'SRI'), ('Jajar_Legowo', 'Jajar_Legowo')], max_length=100)),
                ('musim', models.CharField(choices=[('Hujan', 'Hujan'), ('Kemarau', 'Kemarau')], max_length=100)),
                ('penyakit', models.CharField(choices=[('Burung', 'Burung'), ('Penggerek_Batang', 'Penggerek_Batang'), ('Wereng_Coklat', 'Wereng_Coklat'), ('Wereng_Hijau', 'Wereng_Hijau'), ('Tikus', 'Tikus')], max_length=100)),
                ('ph', models.FloatField()),
                ('b', models.FloatField()),
                ('grade_mutu', models.CharField(choices=[('Grade_A', 'Grade_A'), ('Grade_B', 'Grade_B'), ('Grade_C', 'Grade_C'), ('Grade_D', 'Grade_D')], max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]