# f =open('user.txt','r+',encoding='utf-8')
# with open("user.txt",encoding='utf-8') as f:#打开一个文件
# f.read()
with open("user.txt", encoding='utf-8') as f, open("user.txt2","w",encoding='utf-8') as f2:#打开两个文件
#修改文件
   for line in f:
       new_line=line.replace("周杰伦","周")
       f2.write(new_line)

