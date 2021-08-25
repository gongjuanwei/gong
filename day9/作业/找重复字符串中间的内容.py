
from collections import defaultdict

def find_str(string:str):
    # str_index={}#用一个字典存数据{s：[3,6]f:[9,12]}
    #先找到相同的元素的下标
    str_index_map=defaultdict(list)#q取元素对应的下标 {s：[3,6]f:[9,12]}
    [str_index_map[s].append(index)for index,s in enumerate(string) if string .count(s)>1]
    # print(s)
    # print(str_index_map)
    count =1
    for index_list in str_index_map.values():
        for index in range(len(index_list)-1):#处理重复次数大于2的
            start_index=index_list[index]#开始的下标
            end_index=index_list[index+1]#结束的下标
            target_str=string[start_index:end_index+1]#通过开始和结束的下标
            target_str_len=len(target_str)-2
        # 在找出相同元素中间的元素
        # start_index,end_index=index_list
        # target_str =string[start_index:end_index+1]
        # target_str_len =len(target_str)-2
        print("%s.%s %s" %(index,target_str,target_str_len))
        count+=1

    # for index,s in enumerate(string):#enumerate:可以拿到下标和元素
    #     if string.count(s)>1:
    #             str_index_map[s].append(index)
    #     print(str_index_map)


if __name__=='__main__':

    s='abcsdgdsf1s23f'
    find_str(s)