# Author guomin
prduct_list=[
    ('iPhone',5800),
    ('mac Pro',9800),
    ('Bike',800),
    ('Watch',1200),
    ('Coffee',31),
]
shop_list=[]
salary=input("Input your salary:")
if salary.isdigit():
    salary=int(salary)
    while True :
        for index,item in enumerate(prduct_list):
            print(index,item)
        user_choice=input("请选择要购买的商品")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(prduct_list) and user_choice >=0:
                p_item=prduct_list[user_choice]
                if p_item[1]<=salary: #买得起
                    shop_list.append(p_item)
                    salary-=p_item[1]
                    print("add %s into shopping cart,your current is \033[31;1m%s \033[0m"%(p_item,salary) )
                else:
                    print("\033[41;1m你的余额只剩[%s]了\033[0m"%salary)
            else:
                print("商品不存在")
        elif user_choice=='q':
            for p in shop_list:
                print(p)
            print("你当前金额",salary)
            exit()
        else:
            print("输错了")