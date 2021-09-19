from django.test import TestCase
from django.core.files import File
from django.contrib.flatpages.models import FlatPage
from pages.models import Page, Category, Attachment

class TestPageModel(TestCase):
    fixtures = ['initial_pages']

    def setUp(self):
        self.flatpage = FlatPage.objects.create()
        self.page = Page.objects.create(
            flatpage=self.flatpage,
            category=Category.COMPANY,
            priority=10,
        )
    
    def test_str(self):
        self.assertIn(str(self.page.category_name), str(self.page))
        #breakpoint()

    def test_url(self):
        self.assertEqual(
            self.page.get_absolute_url(),
            self.flatpage.get_absolute_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.page.title,
            self.flatpage.title,
        )

class TestAttachmentModel(TestCase):
    def setUp(self):
        self.flatpage = FlatPage.objects.create()
        self.file = File(file=b"", name='test.pdf')
        self.attachment = Attachment(
            file=self.file,
            title='testtitle',
            flatpage=self.flatpage,
        )


    def test_str(self):
        self.assertEqual(str(self.attachment), self.file.name)
