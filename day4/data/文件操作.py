# r：只读不能写，文件不存在会报错
# w：能写不能读，文件不存会创建，文件已存在会清空文件里面内容
# a：追加写不能读，文件不存在会创建，不会清空原来的文件，只会在末尾添加
# r或者r+: 读写模式:读取文件不存在会报错，他的文件指针是在最前面的
# w或者w+：写读模式:会创建文件，会清空文件里面内容
# a或者a+：追加模式：读，就要移动文件指针seek（0）；即使移动指针写，也只会追加到最后面
#rb    wb    ab
#rb+   wb+   ab+

#r+: 读写模式
# f =open('user.txt','r+',encoding='utf-8')
# f.read()#读
# f.write("你好啊")#写
# f.close()

#w+：写读模式
# f =open('user.txt','w+',encoding='utf-8')
# f.write("w+")#只能写字符串
# f.seek(0)#指针移到前面
# print(f.read())#读
# f.close()
#write完，文件没有写进文件
f =open('user.txt', 'w+', encoding='utf-8')
f.write("w+")#只能写字符串
f.flush()#刷新一下缓冲，立马写入磁盘
print(f.tell())#告诉你现在文件指针的位置
f.close()





# f =open('user.txt','a+',encoding='utf-8')
# f.seek(0)
# # print(f.read())#读
# f.write("指针移到最前面，也是在后面追加")
# f.close()


#读大文件
# f = open('access.log',encoding='utf-8')
# for line in f:#直接循环文件对象，循环的时候就是文件里面的每一行
#     print(line)
# f.close()


