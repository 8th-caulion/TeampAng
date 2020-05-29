from django.db import models
from django.conf import settings
import jsonfield

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 현 계정의 사용자를 가져올 수 있음.
    nickname = models.CharField(max_length=64)
    profile_photo = models.ImageField(blank=True)
    json_time_table = jsonfield.JSONField()

class Login(models.Model):
    username =models.TextField()
    password=models.TextField() 
    # 비밀번호의 경우 숫자랑 문자 섞어서 쓰는데 이런건 어떻게 처리하지?
    # 그리고 login이랑 signup models.py안 필요한가?

class SignUp(models.Model):
    username=models.TextField()
    password=models.TextField()