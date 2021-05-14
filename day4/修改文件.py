import os
f1 = open("user.txt",encoding='utf-8')
f2 = open("user.txt.bak","w",encoding="utf-8")
for line in f1:
    new_line = line.replace("周","周杰伦")
    f2.write(new_line)
f1.close()
f2.close()
os.remove("user.txt")
os.rename("user.txt.bak","user.txt")

