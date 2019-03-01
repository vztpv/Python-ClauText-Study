# 4-1 Problem1, Problem2

def is_odd(n):
    return n & 1 == 1

def mean(*args):
    result = 0.0
    for x in args:
        result += x
    result /= len(args)
    return result

print(is_odd(3), end=" ")
print(is_odd(4))

print(mean(1, 2, 3, 4, 5))