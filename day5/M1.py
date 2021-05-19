# a=1
# def test():
#     print("wo shi m1 test 函数")
# print("这是M1")
#
# for i in range(10):
#     print(i)
def op_file():
    print('op_file')
def op_mysql():
    print('op_mysql')
def op_redis():
    print('op_redis')

print(__name__)
if __name__=='__main__':
    op_file
    op_mysql()
    op_redis()