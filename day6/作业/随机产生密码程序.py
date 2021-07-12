import random,string

def create_password(num,filename="passwords.txt"): #10
    all_password = set()
    while num !=len(all_password):
        length = random.randint(8, 15)
        s2 = random.sample(string.digits+string.ascii_letters,length)
        if set(s2) & set(string.ascii_uppercase) and set(s2) & set(string.ascii_lowercase) and set(s2) & \
            set(string.digits):
            password = ''.join(s2) + '\n'
            all_password.add(password)

    with open(filename,'w') as f:
        f.writelines(all_password)
    print("密码生成完成")


def create_password2(num,filename="passwords.txt"):  # 10
    all_password = set()
    while num != len(all_password):
        length = random.randint(8, 15)
        s1 = random.choice(string.ascii_lowercase)  + random.choice(string.ascii_uppercase) \
        + random.choice(string.digits)
        s2 = random.sample(string.ascii_letters+string.digits,length-3)
        s2.append(s1) #['s','c','5','A','2','sfd']
        random.shuffle(s2)
        password = ''.join(s2) + '\n'
        all_password.add(password)

    with open(filename, 'w') as f:
        f.writelines(all_password)
    print("密码生成完成")


if __name__ == '__main__':
    create_password(100)
    # create_password2(100,'password2.txt')