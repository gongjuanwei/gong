import random


def ssq(num):
    all = set()
    red_range = [str(i).zfill(2) for i in range(1,34)]
    blue_range = [str(i).zfill(2) for i in range(1,17)]
    while len(all) != num:
        red = random.sample(red_range,6)
        blue = random.choice(blue_range)
        red = ' '.join(red)
        result = "红色球: %s 蓝色球: %s " % (red,blue)
        all.add(result)

    return all

def main():
    num = input("num:").strip()
    if num.isdigit():
        all_ball = ssq(int(num))
        for ball in all_ball:
            print(ball)
    else:
        print("请输入正确的数量")

if __name__ == '__main__':
    main()