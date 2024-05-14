from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', default='asia/jakarta', blank=True, null=True)
    id_note = models.AutoField(primary_key=True)
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kategori = models.ManyToManyField('Kategori')
    def __str__(self):
        return self.judul

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.kategori
    
