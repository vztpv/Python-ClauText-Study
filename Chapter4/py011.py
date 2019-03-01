# 4 - 2 Problem 1, 2, 3, 4

input1 = int(input("first number"))
input2 = int(input("second number"))

total = input1 + input2
print("sum is {}".format(total))


str = input("numbers")
numbers = str.split(',')

print(numbers)
sum = 0
for x in numbers:
    sum += int(x)
print(sum)


print("you", "need", "python")


num = int(input("number "))
for i in range(1,10):
    print(num * i, end=' ')