from django.contrib import admin

# Register your models here.

from .models import PpompuData
from .models import CategoryData
from .models import KeywordData

admin.site.register(PpompuData)
admin.site.register(CategoryData)
admin.site.register(KeywordData)
