from django.test import TestCase
from ownapp.models import Papers
from django.contrib.auth.models import User

class TestPaper(TestCase):
    def test_paper_creation(self):
        user = User.objects.create(username='foo')
        paper = Papers.objects.create(
            Creator=user,
            PaperName="For PO Bank Preparation",
            DateOfCreating="2021-09-24",
            saved_file="mani.txt"
        )
        self.assertEquals(str(paper), 'For PO Bank Preparation 2021-09-24 mani.txt')
        self.assertEquals(Papers.objects.all().count(), 1)
