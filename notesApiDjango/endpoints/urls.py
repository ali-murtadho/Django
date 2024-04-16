from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='notes'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='notes-detail'),
    path('notes/create/', views.NoteCreate.as_view(), name='notes-create'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='notes-delete'),
    
    path('categories/', views.KategoriList.as_view(), name='categories'),
    path('categories/<int:pk>/', views.KategoriDetail.as_view(), name='categories-detail'),
    path('categories/create/', views.KategoriCreate.as_view(), name='categories-create'),
    path('categories/<int:pk>/update/', views.KategoriUpdate.as_view(), name='categories-update'),
    path('categories/<int:pk>/delete/', views.KategoriDelete.as_view(), name='categories-delete'),
    path('categories/<int:pk>/notes/', views.NoteByCategoryList.as_view(), name='category-notes'),
]