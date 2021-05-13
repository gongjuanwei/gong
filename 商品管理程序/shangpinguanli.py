import json
import pprint
import os

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


def add_product():
    with open('product.json', 'a+', encoding='utf-8') as f:   #以a+模式打开文件，如果存在判断是否有商品
        f.seek(0)    #文件指针放到最前面以便读取文件
        if os.path.getsize('product.json'): #有商品读出商品，放到字典里
            product = json.load(f)
        else:
            product = {}
    name = input('请输入要添加的商品名称：').strip()
    price = input('请输入商品价格：').strip()
    count = input('请输入商品数量：').strip()
    if name in product:
        print('您添加的商品已经存在')
    elif not is_f(price):
        print('您添加的商品价格不是大于0的数字')
    elif not count.isdigit() or int(count) == 0:
        print('您添加的商品数量不是大于0的整数')
    else:
        product.setdefault(name, {'price': eval(price), 'count': eval(count)})
    with open('product.json', 'w', encoding='utf-8') as f:  #以清空原文件的写模式写入完整的字典数据
        json.dump(product, f, ensure_ascii=False, indent=4)



def del_product():
    with open('product.json', 'a+', encoding='utf-8') as f:
        f.seek(0)
        if os.path.getsize('product.json'):
            product = json.load(f)
        else:
            print("暂无商品，您需要先去添加商品")
            return       #文件不存在结束函数
    name = input('请输入要删除的商品名称：').strip()
    if name not in product:
        print('您输入的商品不存在！')
    else:
        product.pop(name)
    with open('product.json', 'w', encoding='utf-8') as f:
        if product:
            json.dump(product, f, ensure_ascii=False, indent=4)
        else:
            f.truncate()     #删除了所以商品后，product是空字典，继续写入会写入{},需要直接清空字典




def chaxun_product():
    with open('product.json', 'a+', encoding='utf-8') as f:
        f.seek(0)
        if os.path.getsize('product.json'):
            product = json.load(all)
            return product
        else:
            print('暂无商品，请先添加商品')


if __name__ == '__main__':
    T = True
    while T:
        choice = input("请输入你的选择：\n1查询商品\n2新增产品\n3修改商品新\n4删除商品\n5退出 ")
        if choice not in ('1','2','3','4','5'):
            continue
        elif choice == '2' :
            add_product()
        elif choice == '4' :
            del_product()
        elif choice == '1' :
            products = chaxun_product()
            if products:
                print(products)
        elif choice == '5' :
            T = False
