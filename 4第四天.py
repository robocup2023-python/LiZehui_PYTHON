my_list = [1, 2, 3, 4, 5]
output = ",".join(str(x) for x in my_list)
print(output)


sorted_list = [1, 3, 5, 7, 9] 
num = int(input("请输入一个数: "))
if num > sorted_list[-1]:
    sorted_list.append(num)
else:
    for i in range(len(sorted_list)):
        if num < sorted_list[i]:
            sorted_list.insert(i, num)
            break

print(sorted_list)


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = []

for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[i])):
        sum = matrix1[i][j] + matrix2[i][j]
        row.append(sum)
    result.append(row)

print(result)



n = int(input("请输入整数个数: "))
m = int(input("请输入向后移动的位置: "))

my_list = []
for i in range(n):
    num = int(input("请输入第{}个整数: ".format(i+1)))
    my_list.append(num)

for i in range(m):
    num = my_list.pop()
    my_list.insert(0, num)

print(my_list)





my_tuple = (1, 2, 3)
my_tuple[0] = 4 




my_list = [1, 2, 3, 4, 5]
for num in my_list:
    if num % 2 != 0:
        my_list.remove(num)
print(my_list)
my_list = [1, 2, 3, 4, 5]
new_list = [num for num in my_list if num % 2 == 0]
print(new_list)

