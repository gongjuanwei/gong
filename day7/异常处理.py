l = [1,2,3]
d  = {"name":"11"}
import traceback
try:
    name = d["name"]
    # l[4]
# except KeyError as e:
#     print(e)
#     print("出现异常了")
# except IndexError as e:
#     print("出现下标不存在的异常了")
except Exception as e:
    traceback.print_exc()
    msg = traceback.format_exc()
    print(msg)
else:
    print("没有出现异常")
finally:
    print("不管你出不出异常他都会走")
