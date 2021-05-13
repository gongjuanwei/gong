# 定义一个变量，最好用大写字母，表示它是一个常量，不会改变
product_111 = 'product111.json'
import json


# 定义一个公共函数，获取文件内容并转换成字典，共后面三个调用
def read_goods():
    with open(product_111, encoding='utf-8') as f:  # 读取文件
        contend = f.read()  # 读取文件
        if len(contend) > 0:  # 判断文件不为空
            # if contend:#这两种写法都可以，因为非空即真
            rf = json.loads(contend)  # json转化成字典
        else:
            rf = {}  # 否则返回一个空字典，说明文件里没东西
        return rf


# 增加和删除都是写文件，定义一个函数，供他们俩使用
def write_file_comtent(dic):
    with open(product_file, 'w', encoding='utf-8') as f:
        json.dump(dic, f, indent=4, ensure_ascii=False)  # 空四格，中文要显示


# 判断是否为int类型和是否>0,供增加商品使用
def check_digit(st: str):  # 告诉他传过来的是str类型
    if st.isdigit():  # 判断是否为整数
        st = int(st)
        if st > 0:  # 再判断是否大于0
            return st
        else:
            return 0
    else:
        return 0


# 增加商品
def add_good():
    good = input('请输入商品名称：').strip()
    count = input('请输入商品数量：').strip()
    price = input('请输入商品价格：').strip()

    all = read_goods()  # 获取全部内容
    if good == '':
        print('商品名称不能为空')
    elif good in all:
        print('商品已经存在')

    elif check_digit(count) == 0:
        print('商品数量为大于0的整数')
    elif check_digit(price) == 0:
        print('商品价格为大于0的整数')

    else:
        all[good] = {'price': int(price), 'count': int(count)}  # 将商品加入到字典中，添加一个key和他的值
        write_file_comtent(all)  # 调用函数，写入文件中


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

    if d_good in all:
        all.pop(d_good)
        print('已将商品 %s 成功删除' % d_good)
        write_file_comtent(all)  # 调用函数，将字典写入文件中


choice = input('请选择您的操作：\n1、添加商品\n2、删除商品\n3、查看商品')
if choice == '':
    add_good()
elif choice == '':
    del_good()
elif choice == '':
    show_good()
else:
    print('输入有误')