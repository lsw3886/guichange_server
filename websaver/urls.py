"""websaver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from parsed_data import views

router = routers.DefaultRouter()
router.register(r'ppompers', views.PpompuViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'keywords', views.KeywordViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-v1/', include('rest_framework.urls', namespace='rest_framewor_category')),
    url(r'^keyword/(?P<token>.*)/(?P<keyword>.*)/(?P<bulletinName>.*)/$', views.AddKeyword, name ="AddKeyword"),
    url(r'^Rkeyword/(?P<token>.*)/(?P<keyword>.*)/(?P<bulletinName>.*)/$', views.RemoveKeyword, name ="RemoveKeyword"),

#    url(r'^callback$', view=views.DisplayCategory, name='callback'),

]
