import time
from day8.homework.监控错误次数大于5次 import clear_error_user

while True:
    if time.strftime("%H:%M") == "00:10":
        clear_error_user()
    time.sleep(60)