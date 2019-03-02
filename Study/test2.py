# Study 2

x = int(input('number'))
if x & 1 == 0:
    print('even')
else:
    print('odd')


x = input('number')
# need chking size?
x = x[0:2]
x = int(x) + 1900
print(x)
old = 2019 - x + 1
print(old)
if old >= 65:
    print(old)


num = 13
if num % 2 == 0 or num % 3 == 0:
    print('true')
else:
    print('false') 


point = 99
if point >= 80:
    print("good")
elif point >= 60:
    print("do best")
elif point < 60:
    print("re")


i = 5
while i < 10:
    print(i << 1)
    i += 1


x = int(input("x "))
y = int(input("y "))

print(abs(x-y))

z = int(input("z "))

_max = max(x, y)
_max = max(_max, z)
_min = min(x, y)
_min = min(_min, z)
_middle = x + y + z - _max - _min
print(_max * _min - _middle)

# sort
if x > y:
    x,y = y,x
if y > z:
    y,z = z,y
if x > y:
    x,y = y,x
print(z * x - y)


x = int(input("x : "))
y = int(input("y: "))

_min = min(x, y)
_max = max(x, y)

i = _min
while i <= _max:
    if i % 5 != 0:
        i += 1
        continue
    print(i)
    i += 1


x = int(input('number - prime test : '))

import math
def is_prime(x):
    i = 2
    if x <= 1:
        return
    elif x == 2: 
        print('prime')
    else:
        limit = math.sqrt(x) + 1
        isPrime = True
        while i < limit:
            if x % i == 0:
                print("because", i, "it is not prime")
                isPrime = False
                break
            i += 1 
            # cf 2 is even, ( 3 5 7 ~ are odd )
        if isPrime:
            print("prime")
for i in range(1, 100):
    print(i, end=' ') 
    is_prime(i)
    print("")


str = input("number - sum : ")
sum = 0
for x in str:
    sum += ord(x) - ord('0')
print(sum)

def is_digit(x):
    return ord(x) >= ord('0') and ord(x) <= ord('9')
def is_dot(x):
    return x == '.'

state = 0
chk = True
str = input("str - is number? : ")
for i in range(0, len(str)):
    x = str[i]
    if state == 0 and ( x == '+' or x =='-' ):
        state = 1
        i += 1
    elif state == 0 and is_digit(x):
        state = 1
    elif state == 0:
        chk = False
        print('False')
        break
    elif state == 1 and is_digit(x):
        state = 2
        i += 1 # state = 1
    elif state == 1:
        chk = False
        print('False')
        break
    elif state == 2 and is_digit(x):
        i += 1
    elif state == 2 and is_dot(x):
        state = 3
        i += 1
    elif state == 2:
        chk = False
        print('False')
        break
    elif state == 3 and is_digit(x):
        i += 1
        state = 3
    else:
        chk = False
        print('False')
        break

if chk:
    print('True')

i = -10
t = 0
while t < 11:
    print('*' * ( abs( 11 - abs(i) )))
    t += 1
    i += 2
   