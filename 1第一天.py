count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i*100 + j*10 + k)
                count += 1
print("共有{}个互不相同且无重复数字的三位数".format(count))

x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
z = int(input("请输入第三个整数："))
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print("从小到大排序结果：", x, y, z)


fibonacci = [0, 1]
for i in range(2, 20):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("斐波那契数列的前20项：", fibonacci)

for i in range(1, 10):
    for j in range(1, i):
        print("{}*{}={}".format(i, j, i*j), end="\t")
    print("\n")
