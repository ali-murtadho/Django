from django.db import models
from django.contrib.auth.models import User
import pickle
# Create your models here.

VARIETAS_CHOICES = (
    ('Pandan_Wangi', 'Pandan_Wangi'),
    ('Ciheran', 'Ciheran'),
    ('Mi_Kongga', 'Mi_Kongga'),
    ('IR64', 'IR64'),
    ('Beras_Merah', 'Beras_Merah'),
    ('Beras_Hitam', 'Beras_Hitam') 
    )

WARNA_CHOICES = (
    ('Merah', 'Merah'),
    ('Putih', 'Putih'),
    ('Hitam', 'Hitam'),
    ('Coklat', 'Coklat'),
    )

RASA_CHOICES = (
    ('Pulen', 'Pulen'),
    ('Sangat_Pulen', 'Sangat_Pulen'),
    )

TEKNIK_CHOICES = (
    ('SRI', 'SRI'),
    ('Jajar_Legowo', 'Jajar_Legowo'),
    )

MUSIM__CHOICES = (
    ('Hujan', 'Hujan'),
    ('Kemarau', 'Kemarau'),
    )

PENYAKIT_CHOICES = (
    ('Burung', 'Burung'),
    ('Penggerek_Batang', 'Penggerek_Batang'),
    ('Wereng_Coklat', 'Wereng_Coklat'),
    ('Wereng_Hijau', 'Wereng_Hijau'),
    ('Tikus', 'Tikus'),
    )

GRADE_MUTU_CHOICES = (
    ('Grade_A', 'Grade_A'),
    ('Grade_B', 'Grade_B'),
    ('Grade_C', 'Grade_C'),
    ('Grade_D', 'Grade_D'),
    )
    

class padi(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    varietas = models.CharField(max_length=100, choices=VARIETAS_CHOICES)
    warna = models.CharField(max_length=100, choices=WARNA_CHOICES)
    rasa = models.CharField(max_length=100, choices=RASA_CHOICES)
    teknik = models.CharField(max_length=100, choices=TEKNIK_CHOICES)
    musim = models.CharField(max_length=100, choices=MUSIM__CHOICES)
    penyakit = models.CharField(max_length=100, choices=PENYAKIT_CHOICES)
    ph = models.FloatField()
    b = models.FloatField()
    grade_mutu = models.CharField(max_length=100, choices=GRADE_MUTU_CHOICES, null=True)

    # def save(self, *args, **kwargs):
    #     ml_models = pickle.load(open('pickle/model-no-smote-no-scaler.pkl', 'rb'))
    #     self.prediction = ml_models.predict([[self.varietas, self.warna, self.rasa, self.teknik, self.musim, self.penyakit, self.ph, self.b]])
    #     return super().save(*args, **kwargs)
    
    class Meta:
        order_with_respect_to = 'user'
    
    def __str__(self):
        if self.user is not None:
            return f"{self.user.username} - {self.varietas}"