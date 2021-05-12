import json
import pprint
# 1、新增
#                 输入 商品名称、价格、数量
#                 商品不存在才可以添加
#                 价格必须是大于0的整数/小数
#                 数量必须是大于0的整数

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
    elif not is_positive_float(price):
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


def show_product():
    with open('product.json', 'a+', encoding='utf-8') as f:
        f.seek(0)
        if os.path.getsize('product.json'):
            product = json.load(f)
            return product
        else:
            print('暂无商品，请先添加商品')


if __name__ == '__main__':
    T = True
    while T:
        choice = input('请输入您的选择：A or a-添加商品，D or d-删除商品，S or s-查看商品，T or t-退出程序').strip()
        if choice not in ('A','D','S','T','a','s','d','t'):
            continue
        elif choice == 'A' or choice == 'a':
            add_product()
        elif choice == 'D' or choice == 'd':
            del_product()
        elif choice == 'S' or choice == 's':
            products = show_product()
            if products:
                print(products)
        elif choice == 'T' or choice == 't':
            T = False
