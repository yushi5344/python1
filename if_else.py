# Author guomin
import getpass
# username=input("username:")
# password=getpass.getpass("password:")
# _username='maguomin'
# _password="123456"
# if username==_username and password==_password:
#     print('welcome user {name}'.format(name=username))
# else:
#     print('密码错误')
# print(username,password)
age_of_me=32
while True:
    guess_age=int(input("guess age:"))
    if guess_age==age_of_me:
        print('猜中了')
        break
    elif guess_age>age_of_me:
        print('猜大了')
    else:
        print('猜小了')