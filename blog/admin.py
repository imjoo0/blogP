from django.contrib import admin
from .models import Category

# Register your models here.
# 관리자 페이지 : admin / 1234
# Admin 페이지를 통해서, Category 모델에 ‘영화’, ‘드라마’, ‘예능’ 이라는 카테고리를 각각 생성

# Register your models here.
admin.site.register(Category) # 이 코드가 나의 category를 Admin에 추가 해 줍니다