import json
import pprint
flie_name ='product.json'
f= open('product.json', encoding='utf-8')
product_info =json.load(f)

#判断价格
def is_f(jiage):
    s = str(s)
    if s.count('.') == 1:
        left,right = s.split('.')
        if left.isdigit() and right.isdigit():
            return True
        elif left.startswith('-') and left.count('-')==1 \
                and left[1:].isdigit() and right.isdigit():
            return True
    return False

#判断，商品名称，是否存在
def name(mc):
    names={}
    for i in porduct_info:
        name.apend(c)
        if show_name in names:
            return True
        return False

# 1、新增
#                 输入：商品名称、价格、数量
#                 商品不存在才可以添加
#                 价格必须是大于0的整数/小数
#                 数量必须是大于0的整数
def insert_product(mc):
    if name(mc):
        print('商品已存在，不能添加')
    else:
        add={}
        jg =input('请输入商品价格:')
        sl =input('请输入商品数量:')
        if not sl.strip() or not jg.strip():
            print('输入不能为空')










