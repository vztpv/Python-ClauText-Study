# 5-6 Problmes

import sys
sum = 0
for i, x in enumerate(sys.argv):
    if i > 0:
        sum += int(x)
print(sum)


import os
os.chdir("c:\\")
x = os.popen("dir")
print(x.read())
x.close()

import glob
print(glob.glob("c:/*.py"))

import time

print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))

import random
x = list(range(1,46))
random.shuffle(x)
for nth, i in enumerate(x):
    if nth >= 6:
        break
    print(i, end= " ")
print("")