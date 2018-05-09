# Author guomin
from django.db import models
#
class UserGroup(models.Model):
    uid=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=32,unique=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
#
class UserInfo(models.Model):
    #id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    gender=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now =True,null=True)
    #created_at updated_at更新生效的条件是save
    #   usertype=models.ForeignKey(UserType)
    # user_chose=(
    #     (1,'超级用户'),
    #     (2,'五星用户'),
    #     (3,'普通用户'),
    # )
    # userType=models.IntegerField(choices=user_chose,default=1)
    # 数据库中userType会是整型 ，在Django_admin中下拉选择
    user_group=models.ForeignKey("UserGroup",to_field="uid",on_delete=models.CASCADE,default=1)