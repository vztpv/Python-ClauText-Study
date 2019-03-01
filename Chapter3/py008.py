# problem 3-2, Problem 1, Problem2, Problem3

sum = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        sum += 3
    i = i + 1
print('{}'.format(sum))

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

mean = 0
i = 0
while i < len(A):
    point = A[i]
    mean += point
    i += 1
mean /= len(A)

print('{}'.format(mean))

i = 0
while i < 4:
    print('*' * (i+1))
    i += 1
