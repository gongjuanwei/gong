import os
f1 = open("user.txt",encoding='utf-8')
f2 = open("user.txt.bak","w",encoding="utf-8")
for line in f1:
    new_line = line.replace("周","周杰伦")
    f2.write(new_line)
f1.close()
f2.close()
os.remove("user.txt")
os.rename("user.txt.bak","user.txt")

elif check_digit(count) == 0:
print('数量必须是大于0的整数！')
elif is_f(price) == '':
print('价格必须是大于0的整数/小数！')
else:
all[good] = {'price': float(price), 'count': int(count)}
print('商品添加成功！')
write_file_comtent(all)