from django.db import models

# Create your models here.

class PpompuData(models.Model):
    site_name = models.CharField(max_length=10)
    link = models.CharField(max_length=200)
    comment = models.IntegerField()
    post_num = models.IntegerField()
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.site_name + '_' + self.title

class CategoryData(models.Model):
    name = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    img = models.IntegerField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.category + '_' + self.name

class KeywordData(models.Model):
    token = models.CharField(max_length=200)
    keyword = models.CharField(max_length=20)
    bulletinName = models.CharField(max_length=10)

    def __str__(self):
        return self.bulletinName+ "_"+ self.keyword + '_' + self.token
