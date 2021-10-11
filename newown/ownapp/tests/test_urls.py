from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ownapp.models import Papers
from ownapp.views import PaperList, PaperDetail
from django.contrib.auth.models import User



class TestUrls(SimpleTestCase):
    databases = '__all__'

    def test_detailist_url_resolves(self):
        user = User.objects.create(username='admin')
        self.project1 = Papers.objects.create(
            Creator=user,
            PaperId=5,
            PaperName="For Clerk Bank Preparation",
            DateOfCreating="2021-09-23",
            saved_file="manikanta.txt"
        )
        self.detail_url = reverse('paperdetail', args=[self.project1.PaperId])
        url = self.detail_url
        self.assertEquals(resolve(url).func.view_class, PaperDetail)



    def test_paperlist_url_resolves(self):
        url = reverse('paper')
        self.assertEquals(resolve(url).func.view_class, PaperList)


