from django.contrib import admin
from . import models
from django.contrib.auth.models import User
# Register your models here.
@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id_note', 'judul', 'isi', 'created_at', 'updated_at')

@admin.register(models.Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id_kategori', 'kategori', 'created_at', 'updated_at')
