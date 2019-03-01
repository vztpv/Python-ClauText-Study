# 5-5 Problems

print(all([1, 2, abs(-3)-3]))
print(chr(ord('a')) == 'a')

x = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda val: val > 0, x)))

x = hex(234)
print(int(x, 16))

x = [1, 2, 3, 4]
print(list(map(lambda a: a * 3, x)))

x = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(x) + min(x))

x = 17 / 3
print(round(x, 4))