from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ownapp.models import Papers
from .permissions import IsAuthorOrReadOnly # new

from ownapp.serializers import PaperSerializer

from django.core.files.storage import default_storage
from rest_framework import generics, permissions


# Create your views here.
class PaperList(generics.ListCreateAPIView):
    queryset = Papers.objects.all()
    serializer_class = PaperSerializer

class PaperDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Papers.objects.all()
    serializer_class = PaperSerializer


@csrf_exempt
def PaperApi(request,id=0):
    if request.method=='GET':
        papers = Papers.objects.all()
        papers_serializer=PaperSerializer(papers,many=True)
        return JsonResponse(papers_serializer.data,safe=False)
    elif request.method=='POST':
        paper_data=JSONParser().parse(request)
        papers_serializer=PaperSerializer(data=paper_data)
        if papers_serializer.is_valid():
            papers_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        paper_data=JSONParser().parse(request)
        paper=Papers.objects.get(PaperId=paper_data['PaperId'])
        papers_serializer=PaperSerializer(paper,data=paper_data)
        if papers_serializer.is_valid():
            papers_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        paper=Papers.objects.get(PaperId=id)
        paper.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES.get('file')
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
