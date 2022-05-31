from django.db import models

# Create your models here.
# 글 제목, 글 카테고리, 글 내용>이 들어갈 수 있는 Article 이라는 모델
# <카테고리 이름, 설명>이 들어갈 수 있는 Category 라는 모델을 만들어보
# Article 모델의 글 카테고리에는, Category 모델에 존재하는 카테고리만 들어갈 수 있도록 만들어보세요. (힌트: Foreign Key)
# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "Categories"

    name = models.CharField(max_length=20, null=False)
    desc = models.CharField(max_length=256, null=False)

class Article(models.Model):
    class Meta:
        db_table = "Articles"

    title = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    entertain = models.CharField(max_length=256, default='')
