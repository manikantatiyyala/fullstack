from django.conf.urls import url
from ownapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path





urlpatterns =[
    url(r'^Paper$', views.PaperList.as_view(), name="paper"),
    path('Paper/<int:pk>/', views.PaperDetail.as_view(), name="paperdetail"),

    url(r'^paper$', views.PaperApi),
    url(r'^paper/([0-9]+)$', views.PaperApi),
    url(r'^paper/SaveFile', views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
