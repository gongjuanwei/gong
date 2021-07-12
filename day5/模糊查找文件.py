import os
def search_file(path,keyword):
    for cur_path,dirs,files in os.walk(path):
        for file_name in files:
            if keyword in file_name:#根据关键字在不在里面；if file_name.endswith(keyword):#根据以什么结尾
            # if file_name.endswith(keyword):#根据以什么结尾
                abs_path =os.path.join(cur_path,file_name)#吧当前目录与file_name拼接一下得到绝对路径
                print("查找到%s,绝对路径是 %s" %(file_name,abs_path))

search_file("e:","mp4")
# search_file("/","mp4")