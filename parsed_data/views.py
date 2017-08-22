from django.shortcuts import render
from parsed_data.models import PpompuData
from parsed_data.models import CategoryData
from parsed_data.models import KeywordData

from rest_framework import viewsets
from parsed_data.serializers import PpompuSerializer
from parsed_data.serializers import KeywordSerializer

from parsed_data.serializers import CategorySerializer
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.

class PpompuViewSet(viewsets.ModelViewSet):
    queryset = PpompuData.objects.all().order_by('post_num')
    serializer_class = PpompuSerializer

    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryData.objects.all()
    serializer_class = CategorySerializer
    

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = KeywordData.objects.all()
    serializer_class = KeywordSerializer
    

def AddKeyword(request, token, keyword, bulletinName):
#    SomeModel_json = serializers.serialize("json", PpompuData.objects.filter(post_num__gt=t))
#    data = {"ppompu": SomeModel_json}    
    KeywordData( token = token, keyword = keyword, bulletinName = bulletinName).save()
    
    data = {"token" : token, "keyword" : keyword, "bulletinName" : bulletinName}

    return HttpResponse("")

def RemoveKeyword(request, token, keyword, bulletinName):

    return HttpResponse("")
