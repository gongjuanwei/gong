elif check_digit(count) == 0:
print('数量必须是大于0的整数！')
elif is_f(price) == '':
print('价格必须是大于0的整数/小数！')
else:
all[good] = {'price': float(price), 'count': int(count)}
print('商品添加成功！')