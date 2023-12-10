'''
第七天
Author：李泽辉
2221313156
'''
import random
import re

#第一题
path=r'C:\Users\LZH\Desktop\test.txt'
db = open(path, 'wb')
for i in range(0,10):
    for j in range(0,3):
        db.write(bytes((str)(random.random()), encoding='utf-8'))
        db.write(bytes(',', encoding='utf-8'))
    db.write(bytes('\n', encoding='utf-8'))
db.close()

db =open(path,'r')
data=db.read()
data=re.split(',|\n',data)

import random

data = [[random.randint(0, 100) for _ in range(3)] for _ in range(10)]
second_column = [row[1] for row in data]
print("第二列数据:", second_column)
max_value = max(second_column)
print("最大值:", max_value)
min_value = min(second_column)
print("最小值:", min_value)
average_value = sum(second_column) / len(second_column)
print("平均值:", average_value)
sorted_column = sorted(second_column)
if len(sorted_column) % 2 == 0:
    median_value = (sorted_column[len(sorted_column) // 2 - 1] + sorted_column[len(sorted_column) // 2]) / 2
else:
    median_value = sorted_column[len(sorted_column) // 2]
print("中位数:", median_value)


#第二题
file = open("test.txt", "r+")
file.seek(0)
file.write("python")
file.seek(0, 2)
file.write("python")
file.close()


#第三题
file1 = open("test.txt", "r")
file2 = open("copy_test.txt", "r")
line_number = 1
different_lines = []
for line1, line2 in zip(file1, file2):
    if line1 != line2:
        different_lines.append(line_number)
    line_number += 1
print("不同行的编号:", different_lines)
file1.close()
file2.close()
