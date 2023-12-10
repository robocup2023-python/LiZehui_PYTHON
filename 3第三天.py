# 第一题：猴子吃桃
peaches = 1
for day in range(9, 0, -1):
    peaches = (peaches + 1) * 2
print("第一天共摘了{}个桃子".format(peaches))

# 第二题：求和
for i in range(1, 6):
    print(" " * (5-i) + "*" * (2*i-1))
for i in range(4, 0, -1):
    print(" " * (5-i) + "*" * (2*i-1))

# 第三题：数字位数
num = int(input("请输入一个正整数："))
digits = len(str(num))
print("位数：", digits)
print("逆序打印：", str(num)[::-1])

# 第四题：回文数
def is_palindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    else:
        return False

num = int(input("请输入一个正整数: "))
if is_palindrome(num):
    print(num, "是回文数")
else:
    print(num, "不是回文数")


year = int(input("请输入一个年份: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "是闰年")
else:
    print(year, "不是闰年")

year = int(input("请输入年份: "))
month = int(input("请输入月份: "))
day = int(input("请输入日期: "))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29

day_count = sum(days_in_month[:month-1]) + day

print("这一天是这一年的第", day_count, "天")


