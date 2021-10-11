from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from ownapp.models import Papers

class TestPaperListViews(TestCase):
    def setUp(self):
        self.list_url = reverse('paper')
        self.client = Client()


    def test_paperlist_api(self):
        user = User.objects.create(username='foo')
        Papers.objects.create(
            Creator=user,
            PaperName="For PO Bank Preparation",
            DateOfCreating="2021-09-24",
            saved_file="mani.txt"
        )
        paper = Papers.objects.all().count()
        response = self.client.get(self.list_url)

        self.assertEquals(paper, 1)
        self.assertEquals(response.status_code, 403)



    def test_paper_page(self):
        response = self.client.get('/Paper')

        self.assertEquals(response.status_code, 403)

class TestPaperDetailViews(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='admin')
        self.project1 = Papers.objects.create(
            Creator=user,
            PaperId=5,
            PaperName="For Clerk Bank Preparation",
            DateOfCreating="2021-09-23",
            saved_file="manikanta.txt"
        )
        self.detail_url = reverse('paperdetail', args=[self.project1.PaperId])


    def test_paperdetail_api(self):
        paper = Papers.objects.all().count()
        response = self.client.get(self.detail_url)

        #self.assertEquals(paper, 1)
        self.assertEquals(response.status_code, 200)



    def test_paper1_page(self):
        response = self.client.get('/Paper/5/')

        self.assertEquals(response.status_code, 200)
