import json
FILENAME = "product.json"

def op_file(file_name=FILENAME,content=None):
    with open(file_name,'a+',encoding="utf-8") as f:
        f.seek(0)
        if content:
            f.truncate()
            json.dump(content,f)
            # f.write(json.dumps(content,ensure_ascii=False,indent=4))
        else:
            content = f.read()
            if content: #这一步是为了判断空文件的
                return json.loads(content)
            return {}



def is_count(s):
    s = str(s)
    if s.isdigit() and int(s)>0:
        return True

def is_price(s):
    s = str(s)
    if s.count('.') == 1:
        left,right = s.split('.') #[1,1]#-s.2
        if left.isdigit() and right.isdigit():#0.0
            return float(s) > 0
    return is_count(s)





def add():
    for i in range(3):
        name = input("name:").strip()
        price = input("price:").strip()
        count = input("count:").strip()
        if not name or not price or not count:
            print("name/price/count不能为空")
        elif not is_price(price):
            print("价格不合法，必须是大于0的整数/小数")
        elif not is_count(count):
            print("数量不合法，必须是大于0的整数")
        else:
            products = op_file()
            if name in products:
                print("商品已经存在")
            else:
                products[name] = {"price":float(price),"count":int(count)}
                op_file(content=products)
                print("添加成功")
                break

def update():
    for i in range(3):
        name = input("name:").strip()
        price = input("price:").strip()
        count = input("count:").strip()
        if not name or not price or not count:
            print("name/price/count不能为空")
        elif not is_price(price):
            print("价格不合法，必须是大于0的整数/小数")
        elif not is_count(count):
            print("数量不合法，必须是大于0的整数")
        else:
            products = op_file()
            if name in products:
                products[name] = {"price": float(price), "count": int(count)}
                op_file(content=products)
                print("修改成功")
                break
            else:
                print("商品不存在，无法修改")



def show():
    for i in range(3):
        name = input("name:").strip()
        if not name:
            print("name/price/count不能为空")
        else:
            products = op_file()
            if name in products:
                print(products[name])
                break
            elif name == "all":
                print(products)
                break
            else:
                print("商品不存在")


def delete():
    for i in range(3):
        name = input("name:").strip()
        if not name:
            print("name不能为空")
        else:
            products = op_file()
            if name in products:
                products.pop(name)
                op_file(content=products)
                print("删除成功！")
                break
            else:
                print("商品不存在")


def start():
    while True:
        choice = input("请输入你的选择：1、查询商品 2新增产品 3修改商品 4、删除商品 5、退出:").strip()
        if choice == "1":
            show()
        elif choice == "2":
            add()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            break
        else:
            print("输入错误！")

def start_new():
    func_map = {"1":show,"2":add,"3":update,"4":delete,"5":quit}
    while True:
        choice = input("请输入你的选择：1、查询商品 2新增产品 3修改商品 4、删除商品 5、退出:").strip()
        if choice in func_map:
            func_map[choice]()
        else:
            print("输入选项不合法")



start_new()

