from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from . import models
from rest_framework.response import Response
class NoteList(generics.ListCreateAPIView):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['get', 'post']

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']

class NoteCreate(generics.CreateAPIView):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['post']

class NoteUpdate(generics.UpdateAPIView):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['put', 'patch']

class NoteDelete(generics.DestroyAPIView):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['delete']

class KategoriList(generics.ListCreateAPIView):
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['get', 'post']

class KategoriDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']   

class KategoriCreate(generics.CreateAPIView):
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['post']

class KategoriUpdate(generics.UpdateAPIView):
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['put', 'patch']

class KategoriDelete(generics.DestroyAPIView):
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['delete']

# class NoteByCategoryList(generics.ListAPIView):
#     serializer_class = serializers.NoteSerializer
#     def get_queryset(self):
#         category_pk = self.kwargs['pk']
#         queryset = models.Note.objects.filter(kategori__id_kategori=category_pk)
#         return queryset
#     def get(self, request, pk, format=None):
#         queryset = self.get_queryset(pk)
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)


class NoteByCategoryList(generics.ListAPIView):
    serializer_class = serializers.NoteSerializer
    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = models.Note.objects.filter(kategori__id_kategori=category_pk)
        return queryset

    def get(self, request, pk, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

