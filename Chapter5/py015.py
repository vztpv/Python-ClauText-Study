# 5-4 Problem

result = 0

try:
    [1, 2, 3][3] # here
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError: # here
    result += 4
finally: # here
    result += 8

print(result)

