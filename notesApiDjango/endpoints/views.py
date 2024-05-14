from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.is_active = False  # Atur pengguna menjadi tidak aktif hingga diverifikasi
        user.save()
        # Di sini Anda dapat menambahkan logika untuk mengirim email verifikasi atau pesan lain kepada pengguna
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class LoginView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = models.Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
    
class LogoutView(generics.DestroyAPIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NoteList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['get', 'post']

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']

class NoteCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['post']


class NoteUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['put', 'patch']

class NoteDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    http_method_names = ['delete']

class KategoriList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['get', 'post']

class KategoriDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']   

class KategoriCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['post']

class KategoriUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['put', 'patch']

class KategoriDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.KategoriSerializer
    queryset = models.Kategori.objects.all()
    http_method_names = ['delete']

class NoteByCategoryList(generics.ListAPIView):
    serializer_class = serializers.NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = models.Note.objects.filter(kategori__id_kategori=category_pk)
        return queryset

    def get(self, request, pk, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

