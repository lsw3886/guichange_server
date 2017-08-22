from parsed_data.models import PpompuData
from rest_framework import serializers
from parsed_data.models import CategoryData
from parsed_data.models import KeywordData


class PpompuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PpompuData
        fields = ('site_name', 'link', 'comment', 'post_num', 'title', 'date')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryData
        fields = ("name", "category", "img","password")

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordData
        fields =("token", "keyword", "bulletinName")
