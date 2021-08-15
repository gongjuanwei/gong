import threading
import time,random
def create_data(url):
    t = random.randint(1,5)
    print("t..",t)
    time.sleep(t)
    print("url",url)

start_time = time.time()

#第一种主线程等待子线程的方式
# threads = []
# for i in range(5):
#     t = threading.Thread(target=create_data,args=(i,))
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()

#第二种 通过判断当前线程数的方式
for i in range(5):
    t = threading.Thread(target=create_data,args=(i,))
    t.start()

while threading.activeCount() !=1:
    pass

end_time = time.time()

print('执行时间',end_time - start_time)

print(threading.activeCount()) #当前的线程数