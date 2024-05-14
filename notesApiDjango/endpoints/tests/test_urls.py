from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(url, '/api/register/')

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(url, '/api/login/')

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(url, '/api/logout/')

    def test_notes_url(self):
        url = reverse('notes')
        self.assertEqual(url, '/api/notes/')

    def test_notes_detail_url(self):
        url = reverse('notes-detail', args=[1])
        self.assertEqual(url, '/api/notes/1/')

    def test_notes_create_url(self):
        url = reverse('notes-create')
        self.assertEqual(url, '/api/notes/create/')

    def test_notes_update_url(self):
        url = reverse('notes-update', args=[1])
        self.assertEqual(url, '/api/notes/1/update/')

    def test_notes_delete_url(self):
        url = reverse('notes-delete', args=[1])
        self.assertEqual(url, '/api/notes/1/delete/')

    def test_categories_url(self):
        url = reverse('categories')
        self.assertEqual(url, '/api/categories/')

    def test_categories_detail_url(self):
        url = reverse('categories-detail', args=[1])
        self.assertEqual(url, '/api/categories/1/')

    def test_categories_create_url(self):
        url = reverse('categories-create')
        self.assertEqual(url, '/api/categories/create/')

    def test_categories_update_url(self):
        url = reverse('categories-update', args=[1])
        self.assertEqual(url, '/api/categories/1/update/')

    def test_categories_delete_url(self):
        url = reverse('categories-delete', args=[1])
        self.assertEqual(url, '/api/categories/1/delete/')

    def test_category_notes_url(self):
        url = reverse('category-notes', args=[1])
        self.assertEqual(url, '/api/categories/1/notes/')




