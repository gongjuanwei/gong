from day5.time模块 import str_to_timestamp,timestamp_to_str
import os
# 1、写一个清理日志程序
# 1、使用造日志的脚本造出来数据
# 2、删除logs目录下，三天前的日志文件或者为空的日志文件，如果当天的日志文件为空，不删除
def clean_log(path,day=3):
    step = 60 * 60 * 24 * day
    if os.path.isdir(path):#目录是否存在，或者传入路径是不是一个文件夹
        for cur_path,dirs,files in os.walk(path):
            os.chdir(cur_path)
            for file in files:
                # file =os.path.join(cur_path,file)
                if file.endswith(".log"):
                    file_date = file.split('_')[-1].split('.')[0]
                    file_date_timestamp = str_to_timestamp(file_date,"%Y-%m-%d")
                    if str_to_timestamp() - file_date_timestamp > step:
                        os.remove(file)
                    elif os.path.getsize(file) == 0 and file_date!=timestamp_to_str(format="%Y-%m-%d"):
                        os.remove(file)
        print("清理完成！")
    else:
        print("请输入一个正确路径！")

if __name__ =='__main__':
    clean_log("logs")
