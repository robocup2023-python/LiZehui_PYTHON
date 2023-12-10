string = input("请输入一行字符：")
letters = 0
spaces = 0
digits = 0
others = 0

for char in string:
    if char.isalpha():
        letters += 1
    elif char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1

print("英文字母个数：", letters)
print("空格个数：", spaces)
print("数字个数：", digits)
print("其他字符个数：", others)


a = input("请输入一个数字：")
n = int(input("请输入相加的个数："))

s = 0
num = 0
for i in range(n):
    num = num * 10 + int(a)
    s += num

print("相加的结果为：", s)


height = 100
distance = height
for i in range(1, 10):
    height /= 2
    distance += height * 2

print("第10次落地时，共经过{}米".format(distance))
print("第10次反弹{}米".format(height))


for num in range(100, 1000):
    digit1 = num // 100
    digit2 = (num // 10) % 10
    digit3 = num % 10

    if num == digit1 ** 3 + digit2 ** 3 + digit3 ** 3:
        print(num)


import math

prime_numbers = []
for num in range(101, 201):
    is_prime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("101-200之间的素数：", prime_numbers)
