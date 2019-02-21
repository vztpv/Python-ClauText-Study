# 2- 8 problme 1, problem2

a = [1,2,3]
b=[1,2,3]
print(a is b) # False


a = [1,2,3]
print(id(a))
a = a + [4,5]
print(id(a))

a = [1,2,3]
print(id(a))
a.extend([4,5])
print(id(a))

a = [1,2,3]
print(id(a))
a += [4,5]
print(id(a))
