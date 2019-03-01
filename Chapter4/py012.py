# 4-3 Problems
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # added
f2 =open("test.txt", 'r')
print(f2.read())
f2.close()

str = input("input ")
f1 = open("test.txt", 'a')
f1.write('\n')
f1.write(str)
f1.close()
f2 =open("test.txt", 'r')
print(f2.read())
f2.close()

f1 = open("test.txt", 'r')
lines = f1.read()
lines = lines.split('\n')
lines.reverse()
print(lines)
f1.close()
f1 = open("test.txt", 'w')
i = 0
while i < len(lines):
    f1.write(lines[i])
    if i < len(lines)-1:
        f1.write('\n')
    i += 1
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

f1 = open("test.txt", 'w')
f1.write('Life is too shrot\nyou need java')
f1.close()
f2 = open("test.txt", 'r')
str = f2.read()
f2.close()
str = str.replace('java', 'python')
f1 = open("test.txt", 'w')
f1.write(str)
f1.close()


sum = 0
mean = 0.0
num = 0
f1 = open("sample.txt", 'r')
values = f1.readlines()
f1.close()
print(values)
for value in values:
    value = value.rstrip()
    sum += int(value)
    num += 1
mean = sum / num
f2 = open("result.txt", 'w')
f2.write('{} {}'.format(sum, mean))
f2.close()

