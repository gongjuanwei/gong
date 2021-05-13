# 1、新增
#                 输入 商品名称、价格、数量
#                 商品不存在才可以添加
#                 价格必须是大于0的整数/小数
#                 数量必须是大于0的整数
import json
import pprint
def is_f(s):
    s = str(s)
    if s.count('.') == 1:
        left,right = s.split('.')
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left.count('-')==1 \
                and left[1:].isdigit() and right.isdigit():
            return True
    return False


def insert_product():
    with open('product.json', 'a+', encoding='utf-8') as f:   #以a+模式打开文件，如果存在判断是否有商品
        f.seek(0)    #文件指针放到最前面以便读取文件
        if os.path.getsize('product.json'): #有商品读出商品，放到字典里
            product = json.load(f)
        else:
            product = {}

    def insert_product():
        for open('product.json', 'a+', encoding='utf-8') as f:  # 以a+模式打开文件，如果存在判断是否有商品
            f.seek(0)  # 文件指针放到最前面以便读取文件
            if os.path.getsize('product.json'):  # 有商品读出商品，放到字典里
                product = json.load(f)
            else:
                product = {}

while True:
    ips = {}
    f = open('product.json', 'a+', encoding='utf-8')
    f.seek(0)
    for line in f:
        line = line.strip()
        if line:
            ip = line.split()
            if ip in ips:
                ips[[] =
            else:
                ips[ip] = 1



    #
    # name = input('请输入要添加的商品名称：').strip()
    # price = input('请输入商品价格：').strip()
    # count = input('请输入商品数量：').strip()
    # if name in product:
    #     print('您添加的商品已经存在')
    # elif not is_f(price):
    #     print('您添加的商品价格不是大于0的数字')
    # elif not count.isdigit() or int(count) == 0:
    #     print('您添加的商品数量不是大于0的整数')
    # else:
    #     product.setdefault(name, {'price': eval(price), 'count': eval(count)})
    # with open('product.json', 'w', encoding='utf-8') as f:  #以清空原文件的写模式写入完整的字典数据
    #     json.dump(product, f, ensure_ascii=False, indent=4)