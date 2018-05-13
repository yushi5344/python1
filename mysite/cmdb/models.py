# Author guomin
from django.db import models
#
#UserGroup如果想访问userinfo表 可以使用userinfo_set
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

#用户权限表
class Auth(models.Model):
    name=models.CharField(max_length=43)


#用户权限中间表
class UserToAuth(models.Model):
    a=models.ForeignKey(to='Auth',to_field='id',on_delete=models.CASCADE,default=1)
    u=models.ForeignKey(to='UserInfo',to_field='id',on_delete=models.CASCADE,default=1)
    #这是自定义关系表


#自动创建关系表  比如用户角色表
class Role(models.Model):
    role_name=models.CharField(max_length=40)
    au=models.ManyToManyField('UserInfo')
    #无法直接操作第三章表  cmdb_role_au
    #可以间接方法操作
    #obj=Role.objects.get(id=1)
    #obj.au.add(2) 意味着在cmdb_role_au 中增加一条 role_id=1 userinfo_id=2
    #obj.au.add(*[1,2,3,4])意味着增加4条 分别是1-1,1-2,1-3,1-4
    #或者  obj.au.add(1,2,3,4)
    #obj.au.remove(2)删除role_id=1且user_ifo_id=2
    #obj.r.clear()清除所有role_id=1的
    #obj.au.set()修改