# 3-3  Problem1, Problem2, Problem3

sum = 0
for i in range(1, 101):
    sum += i
print('{}'.format(sum))


A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
mean = 0.0
for point in A:
    mean += point
mean /= len(A)
print('{}'.format(mean))


numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
