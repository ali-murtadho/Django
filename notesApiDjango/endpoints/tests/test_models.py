from django.test import TestCase
from models import Note, Category


class TestNoteModel(TestCase):
    def test_create_note(self):
        title = 'Test Title'
        content = 'Test Content'
        category = Category.objects.create(name='Test Category')
        note = Note.objects.create(title=title, content=content, category=category)
        self.assertEqual(note.title, title)
        self.assertEqual(note.content, content)
        self.assertEqual(note.category, category)

class TestCategoryModel(TestCase):
    def test_create_category(self):
        name = 'Test Category'
        category = Category.objects.create(name=name)
        self.assertEqual(category.name, name)
