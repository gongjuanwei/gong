product_file = 'product.json'
import json
# 定义一个公共函数，获取文件内容并转换成字典，共后面三个调用
def read_goods():
    with open(product_file, encoding='utf-8') as f:  # 读取文件
        contend = f.read()  # 读取文件
        if len(contend) > 0:  # 判断文件不为空
            rf = json.loads(contend)
        else:
            rf = {}  # 否则返回一个空字典，说明文件里没东西
        return rf

# 增加和删除都是写文件，定义一个函数，供他们俩使用
def  write_file_comtent(dic):
    with open (product_file,'w',encoding='utf-8') as f :
        json.dump(dic,f,indent=4,ensure_ascii=False)#空四格，中文要显示

#判断商品
def check_digit(st:str): #告诉他传过来的是str类型
    if st.isdigit():# 判断是否为整数
        st=int(st)
        if st>0:# 再判断是否大于0
            return st
        else:
            return 0
    else:
        return 0

#判断价格
def is_f(s):
    s = str(s)
    if s.count('.') == 1:# 判断小数点个数
        left,right = s.split('.')# 按照小数点进行分割
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left.count('-')==1 \
                and left[1:].isdigit() and right.isdigit():
            return True
    return False



# 增加商品
def add_good():
    good = input('请输入商品名称：').strip()
    count = input('请输入商品数量：').strip()
    price = input('请输入商品价格：').strip()
    all = read_goods()  # 获取全部内容
    if good == '':
        print('商品名称不能为空！')
    elif good in all:
        print('商品已经存在！')
    elif check_digit(count) == 0:
        print('数量必须是大于0的整数！')
    elif is_f(price) == '':
        print('价格必须是大于0的整数/小数！')
    else:
        all[good] = {'price': float(price), 'count': int(count)}
        print('商品添加成功！')
        write_file_comtent(all)



# 查看商品
def show_good():
    s_good = input('请输入要查看的商品名称').strip()
    all = read_goods()
    if s_good == 'all':
        print(all)
    elif s_good not in all:
        print('商品不存在')
    else:
        print(all.get(s_good))
# 删除商品
def del_good():
    d_good = input('请输入要删除的商品名称：').strip()
    all = read_goods()
    if d_good in all:
        all.pop(d_good)
        print('已将商品 %s 成功删除' % d_good)
        write_file_comtent(all)  # 调用函数，将字典写入文件中

#修改商品
# def modify_good():
#     produt_name=input("请输入你想修改的商品：")
#     all = read_goods()
#     if produt_name in all:
#         count = input("请输入修改商品的数量：")
#         price = input("请输入修改商品的价格:")
#         try:
#             if float(count) >= 0:
#                 value = {}
#                 value["count"] = count
#                 value["price"] = price
#                 all[produt_name]=value
#                 print('商品修改成功')
#                 write_file_comtent(all)  # 调用函数，写入文件中
#             else:
#                 print("请输入正数")
#         except ValueError as e:
#             print("请输入实数！", e)
#     else:
#         print("修改的商品不存在，请重新输入：")

def modify_good():
    good=input("请输入你想修改的商品：")
    all = read_goods()
    if good in all:
        count = input("请输入修改商品的数量：")
        price = input("请输入修改商品的价格:")

  elif s_good not in all:
       print('商品不存在')






if __name__ == '__main__':
    T = True
    while T:
        choice = input("请输入你的选择：\n1查询商品\n2新增产品\n3修改商品新\n4删除商品\n5退出 ")
        if choice not in ('1','2','3','4','5'):
            continue
        elif choice == '2' :
            add_good()
        elif choice == '4' :
            del_good()
        elif choice =='3':
            modify_good()
        elif choice == '1' :
            products = show_good()
            if products:
                print(products)
        elif choice == '5' :
            T = False




